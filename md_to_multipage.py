#!/usr/bin/env python3
"""
Multi-Page Markdown to Tufte CSS HTML Converter

Converts a single Markdown file into multiple HTML pages with persistent navigation.
Each H2 section becomes its own page.

Usage: python3 md_to_multipage.py input.md output_dir/
"""

import sys
import re
import subprocess
import tempfile
import os
import shutil
from urllib.parse import urlparse, parse_qs

# Import functions from the single-page converter
from md_to_tufte import (
    process_tufte_annotations,
    convert_youtube_links,
    process_markdown_links,
    extract_metadata_from_markdown,
    process_script_embeds,
    extract_youtube_id
)


# Short names for navigation (Roman numeral + abbreviated title)
CHAPTER_SHORT_NAMES = {
    'introduction': 'Intro',
    'understanding-referrals': 'I. Understanding',
    'design-principles': 'II. Design',
    'operations': 'III. Operations',
    'referrals-and-affiliates': 'IV. Affiliates',
    'when-to-reach-out': 'V. CRM',
    'unincentivised-referrals': 'VI. Unincentivised',
}


def generate_slug(title):
    """Convert a chapter title to a URL-friendly slug."""
    # Special cases for cleaner slugs
    slug_overrides = {
        'Introduction': 'introduction',
        'Understanding Referrals': 'understanding-referrals',
        'Design Principles of Referrals Schemes': 'design-principles',
        'Operations': 'operations',
        'Referrals And Affiliates': 'referrals-and-affiliates',
        'When to Reach out (CRM)': 'when-to-reach-out',
        'Customer Stickiness': 'customer-stickiness',
        'Unincentivised Referrals: You Are Already Acquiring Users Through Referrals': 'unincentivised-referrals',
    }

    if title in slug_overrides:
        return slug_overrides[title]

    # Generic slug generation
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)  # Remove special chars
    slug = re.sub(r'\s+', '-', slug)  # Replace spaces with hyphens
    slug = re.sub(r'-+', '-', slug)  # Collapse multiple hyphens
    slug = slug.strip('-')
    return slug


def parse_chapters(markdown_content):
    """
    Split markdown into chapters based on H2 headings.

    Returns list of dicts: {title, slug, content, subsections, is_empty}
    Skips 'Table of Contents' section.
    """
    # Normalize non-breaking spaces to regular spaces
    markdown_content = markdown_content.replace('\xa0', ' ')

    # Split on H2 headings, keeping the heading (## followed by space or non-breaking space)
    pattern = r'^(##[ \xa0].+)$'
    parts = re.split(pattern, markdown_content, flags=re.MULTILINE)

    chapters = []
    current_title = None
    current_content = []

    # First part (before any H2) is intro/metadata - skip it
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue

        if part.startswith('## '):
            # Save previous chapter if exists
            if current_title:
                content = '\n'.join(current_content).strip()
                # Skip empty chapters and Table of Contents
                if current_title.lower() != 'table of contents':
                    slug = generate_slug(current_title)
                    # Check if chapter has meaningful content (more than just whitespace)
                    is_empty = len(re.sub(r'\s+', '', content)) < 50
                    chapters.append({
                        'title': current_title,
                        'slug': slug,
                        'content': content,
                        'is_empty': is_empty,
                    })

            # Start new chapter
            current_title = part[3:].strip()  # Remove '## '
            current_content = []
        else:
            current_content.append(part)

    # Don't forget the last chapter
    if current_title and current_title.lower() != 'table of contents':
        content = '\n'.join(current_content).strip()
        slug = generate_slug(current_title)
        is_empty = len(re.sub(r'\s+', '', content)) < 50
        chapters.append({
            'title': current_title,
            'slug': slug,
            'content': content,
            'is_empty': is_empty,
        })

    # Filter out empty chapters
    chapters = [ch for ch in chapters if not ch['is_empty']]

    return chapters


def generate_nav_html(chapters, current_slug=None, include_pdf=True):
    """
    Generate the persistent top navigation bar HTML.

    Args:
        chapters: List of chapter dicts
        current_slug: Slug of current page (for highlighting)
        include_pdf: Whether to include PDF download link
    """
    # Build chapter links
    chapter_links = []
    for ch in chapters:
        slug = ch['slug']
        short_name = CHAPTER_SHORT_NAMES.get(slug, ch['title'][:15])

        # Introduction links to index.html, others to their slug.html
        href = 'index.html' if slug == 'introduction' else f'{slug}.html'

        # Mark current page as active
        css_class = ' class="current"' if slug == current_slug else ''

        chapter_links.append(f'<li><a href="{href}"{css_class}>{short_name}</a></li>')

    pdf_link = '<a href="refer_a_friend.pdf" class="pdf-link">[PDF]</a>' if include_pdf else ''

    nav_html = f'''<nav class="site-nav">
    <div class="nav-container">
        <a href="index.html" class="site-title">How To Refer A Friend</a>
        {pdf_link}
        <input type="checkbox" id="nav-toggle" class="nav-toggle">
        <label for="nav-toggle" class="nav-toggle-label"></label>
        <ul class="chapter-nav">
            {chr(10).join('            ' + link for link in chapter_links)}
        </ul>
    </div>
</nav>'''

    return nav_html


def generate_chapter_toc(chapters, start_index=1):
    """
    Generate the table of contents listing remaining chapters.
    Used on the index page after the first chapter content.
    Skips Introduction (which is the index page itself).
    """
    if start_index >= len(chapters):
        return ''

    toc_items = []
    roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

    # Counter for roman numerals (skips Introduction)
    numeral_idx = 0
    for ch in chapters[start_index:]:
        # Skip Introduction (it's the index page)
        if ch['slug'] == 'introduction':
            continue

        numeral = roman_numerals[numeral_idx] if numeral_idx < len(roman_numerals) else str(numeral_idx + 1)
        href = f'{ch["slug"]}.html'
        toc_items.append(f'<li><a href="{href}">{numeral}. {ch["title"]}</a></li>')
        numeral_idx += 1

    toc_html = f'''<section class="chapter-toc">
        <h2>Continue Reading</h2>
        <ol>
            {chr(10).join('            ' + item for item in toc_items)}
        </ol>
    </section>'''

    return toc_html


def convert_chapter_markdown_to_html(markdown_content):
    """Convert chapter markdown to HTML using pandoc."""
    # Clean up whitespace
    markdown_content = markdown_content.replace('\u00a0', ' ')
    markdown_content = re.sub(r'^(#{1,6})\s*([^\n]+)', r'\1 \2', markdown_content, flags=re.MULTILINE)

    # Process script embeds
    processed_result = process_script_embeds(markdown_content)
    if isinstance(processed_result, tuple):
        markdown_content, script_placeholders = processed_result
    else:
        markdown_content = processed_result
        script_placeholders = {}

    # Process Tufte annotations
    processed_markdown = process_tufte_annotations(markdown_content)

    # Write to temp file and convert with pandoc
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_md:
        temp_md.write(processed_markdown)
        temp_md_path = temp_md.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as temp_html:
        temp_html_path = temp_html.name

    try:
        subprocess.run(['pandoc', temp_md_path, '-o', temp_html_path], check=True)

        with open(temp_html_path, 'r') as f:
            html_content = f.read()

        # Convert YouTube links
        html_content = convert_youtube_links(html_content)

        # Restore script placeholders
        for placeholder, script_content in script_placeholders.items():
            html_content = html_content.replace(placeholder, script_content)

        return html_content

    finally:
        if os.path.exists(temp_md_path):
            os.unlink(temp_md_path)
        if os.path.exists(temp_html_path):
            os.unlink(temp_html_path)


def build_anchor_map(chapters):
    """
    Build a map of all H3 anchor IDs to their containing chapter.
    Used for rewriting internal links.
    """
    anchor_map = {}

    for ch in chapters:
        slug = ch['slug']
        # Find all H3 headings and extract their would-be anchor IDs
        h3_pattern = r'^### (.+)$'
        for match in re.finditer(h3_pattern, ch['content'], re.MULTILINE):
            heading = match.group(1).strip()
            # Generate anchor ID (pandoc style: lowercase, hyphens for spaces)
            anchor_id = heading.lower()
            anchor_id = re.sub(r'[^a-z0-9\s-]', '', anchor_id)
            anchor_id = re.sub(r'\s+', '-', anchor_id)
            anchor_id = re.sub(r'-+', '-', anchor_id).strip('-')
            anchor_map[anchor_id] = slug

    return anchor_map


def rewrite_internal_links(html_content, anchor_map, current_slug):
    """
    Rewrite internal anchor links to point to the correct chapter file.
    """
    def replace_link(match):
        anchor = match.group(1)
        if anchor in anchor_map:
            target_slug = anchor_map[anchor]
            if target_slug == current_slug:
                # Same page, keep as anchor
                return f'href="#{anchor}"'
            else:
                # Different page, add filename
                href = 'index.html' if target_slug == 'introduction' else f'{target_slug}.html'
                return f'href="{href}#{anchor}"'
        return match.group(0)

    return re.sub(r'href="#([^"]+)"', replace_link, html_content)


def rewrite_image_paths(html_content, source_dir):
    """
    Rewrite absolute image paths to relative paths.
    """
    # Pattern to match src attributes with absolute paths
    def replace_img_src(match):
        src = match.group(1)
        # If it's an absolute path containing the source directory
        if source_dir in src:
            # Extract just the relative path from img/
            if '/img/' in src:
                relative = 'img/' + src.split('/img/')[-1]
                return f'src="{relative}"'
        # If it's already a URL or relative, leave it alone
        return match.group(0)

    return re.sub(r'src="([^"]+)"', replace_img_src, html_content)


def generate_page_html(title, subtitle, nav_html, body_content, chapter_title=None, css_path='tufte-css'):
    """Generate the full HTML page."""

    # Use chapter title as page title if provided
    page_title = chapter_title if chapter_title else title

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <title>{page_title} - {title}</title>
    <link rel="stylesheet" href="{css_path}/tufte.css"/>
    <link rel="stylesheet" href="{css_path}/nav.css"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    {nav_html}
    <article>
        {body_content}
    </article>
</body>
</html>'''

    return html


def generate_index_page(chapters, title, subtitle, nav_html, source_dir):
    """
    Generate the index page with Introduction content and TOC to remaining chapters.
    """
    # Find the Introduction chapter (should be first)
    intro_chapter = None
    for ch in chapters:
        if ch['slug'] == 'introduction':
            intro_chapter = ch
            break

    if not intro_chapter:
        intro_chapter = chapters[0]

    # Convert intro chapter content to HTML
    chapter_html = convert_chapter_markdown_to_html(intro_chapter['content'])

    # Rewrite image paths to relative
    chapter_html = rewrite_image_paths(chapter_html, source_dir)

    # Build subtitle HTML
    subtitle_html = f'<p class="subtitle">{subtitle}</p>' if subtitle else ''

    # Wrap content in sections (split on h2/h3)
    content_html = wrap_in_sections(chapter_html)

    # Generate TOC for all chapters except Introduction
    toc_html = generate_chapter_toc(chapters, start_index=0)

    # Don't show "Introduction" as H2 - it's redundant with the title
    body_content = f'''<h1>{title}</h1>
        {subtitle_html}
        {content_html}
        {toc_html}'''

    return generate_page_html(title, subtitle, nav_html, body_content, css_path='tufte-css')


def generate_chapter_page(chapter, chapters, title, nav_html, anchor_map, source_dir):
    """Generate an individual chapter page."""

    # Convert chapter content to HTML
    chapter_html = convert_chapter_markdown_to_html(chapter['content'])

    # Rewrite internal links
    chapter_html = rewrite_internal_links(chapter_html, anchor_map, chapter['slug'])

    # Rewrite image paths to relative
    chapter_html = rewrite_image_paths(chapter_html, source_dir)

    # Wrap content in sections
    content_html = wrap_in_sections(chapter_html)

    body_content = f'''<h1>{chapter['title']}</h1>
        {content_html}'''

    return generate_page_html(title, None, nav_html, body_content, chapter_title=chapter['title'], css_path='tufte-css')


def wrap_in_sections(html_content):
    """Wrap content in section elements for proper Tufte styling."""
    # Split on H3 headings
    parts = re.split(r'(<h3[^>]*>.*?</h3>)', html_content)

    result = []
    in_section = False

    for i, part in enumerate(parts):
        if not part.strip():
            continue

        if part.startswith('<h3'):
            if in_section:
                result.append('</section>')
            result.append('<section>')
            result.append(part)
            in_section = True
        else:
            # Wrap content before first H3 in a section too
            if not in_section and i == 0:
                result.append('<section>')
                in_section = True
            result.append(part)

    if in_section:
        result.append('</section>')

    return '\n'.join(result)


def copy_assets(source_dir, output_dir):
    """Copy CSS, fonts, and images to output directory."""
    # Copy tufte-css directory
    tufte_src = os.path.join(source_dir, 'tufte-css')
    tufte_dst = os.path.join(output_dir, 'tufte-css')

    if os.path.exists(tufte_dst):
        shutil.rmtree(tufte_dst)

    shutil.copytree(tufte_src, tufte_dst)
    print(f"  Copied tufte-css/ to {tufte_dst}")

    # Copy img directory if it exists
    img_src = os.path.join(source_dir, 'img')
    img_dst = os.path.join(output_dir, 'img')

    if os.path.exists(img_src):
        if os.path.exists(img_dst):
            shutil.rmtree(img_dst)
        shutil.copytree(img_src, img_dst)
        print(f"  Copied img/ to {img_dst}")


def main(input_file, output_dir):
    """Main conversion function."""

    # Read markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.read()

    # Extract metadata
    title, subtitle, cleaned_content = extract_metadata_from_markdown(markdown_content)
    if not title:
        title = "How To Refer A Friend"

    print(f"Converting {input_file} to multi-page site...")
    print(f"  Title: {title}")
    print(f"  Subtitle: {subtitle}")

    # Parse chapters
    chapters = parse_chapters(cleaned_content)
    print(f"  Found {len(chapters)} chapters:")
    for ch in chapters:
        print(f"    - {ch['title']} ({ch['slug']})")

    # Build anchor map for internal links
    anchor_map = build_anchor_map(chapters)

    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get source directory for asset copying
    source_dir = os.path.dirname(os.path.abspath(input_file))

    # Copy assets
    copy_assets(source_dir, output_dir)

    # Generate pages
    print("  Generating pages:")

    # Generate index page (Introduction content + TOC)
    nav_html = generate_nav_html(chapters, current_slug='introduction')
    index_html = generate_index_page(chapters, title, subtitle, nav_html, source_dir)
    index_path = os.path.join(output_dir, 'index.html')
    with open(index_path, 'w') as f:
        f.write(index_html)
    print(f"    - index.html (Introduction)")

    # Generate chapter pages (skip Introduction - it's the index page)
    for chapter in chapters:
        if chapter['slug'] == 'introduction':
            continue

        nav_html = generate_nav_html(chapters, current_slug=chapter['slug'])
        page_html = generate_chapter_page(chapter, chapters, title, nav_html, anchor_map, source_dir)

        page_path = os.path.join(output_dir, f"{chapter['slug']}.html")
        with open(page_path, 'w') as f:
            f.write(page_html)
        print(f"    - {chapter['slug']}.html")

    print(f"\nDone! Open {os.path.join(output_dir, 'index.html')} to view the site.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 md_to_multipage.py input.md output_dir/")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} does not exist")
        sys.exit(1)

    main(input_file, output_dir)
