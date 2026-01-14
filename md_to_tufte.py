#!/usr/bin/env python3
"""
Markdown to Tufte CSS HTML Converter

This script converts Markdown files to HTML with Tufte CSS styling.
It provides a starting point that can then be manually refined.

Usage: python3 md_to_tufte.py input.md output.html
"""

import sys
import re
import subprocess
import tempfile
import os
from urllib.parse import urlparse, parse_qs

def convert_markdown_to_tufte_html(input_file, output_file):
    """Convert Markdown to Tufte-styled HTML"""
    
    # Read and preprocess the markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.read()
    
    # Extract metadata (title, subtitle) before processing
    title, subtitle, cleaned_markdown = extract_metadata_from_markdown(markdown_content)
    
    # Clean up any non-breaking spaces and other unicode issues
    cleaned_markdown = cleaned_markdown.replace('\u00a0', ' ')  # Replace non-breaking spaces
    cleaned_markdown = re.sub(r'^(#{1,6})\s*([^\n]+)', r'\1 \2', cleaned_markdown, flags=re.MULTILINE)  # Fix header spacing
    
    # Process script embeds first and get placeholders
    processed_result = process_script_embeds(cleaned_markdown)
    if isinstance(processed_result, tuple):
        cleaned_markdown, script_placeholders = processed_result
    else:
        cleaned_markdown = processed_result
        script_placeholders = {}
    
    # Process Tufte annotations before pandoc conversion
    processed_markdown = process_tufte_annotations(cleaned_markdown)
    
    # Write processed markdown to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_md:
        temp_md.write(processed_markdown)
        temp_md_path = temp_md.name
    
    # Convert processed markdown to basic HTML using pandoc
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as temp_file:
        temp_html = temp_file.name
    
    try:
        subprocess.run(['pandoc', temp_md_path, '-o', temp_html], check=True)
        
        # Debug: print the processed markdown to see what went wrong
        if 'debug' in globals():
            with open(temp_md_path, 'r') as f:
                print("DEBUG - Processed markdown:")
                print(f.read()[:500] + "...")
                print("=" * 50)
        
        # Read the basic HTML
        with open(temp_html, 'r') as f:
            html_content = f.read()
        
        # Create Tufte-styled HTML
        tufte_html = create_tufte_structure(html_content, input_file, title, subtitle)
        
        # Restore script placeholders
        if 'script_placeholders' in locals():
            for placeholder, script_content in script_placeholders.items():
                tufte_html = tufte_html.replace(placeholder, script_content)
        
        # Write the final HTML
        with open(output_file, 'w') as f:
            f.write(tufte_html)
            
        print(f"Converted {input_file} to {output_file}")
        print("✅ Processed sidenotes and margin notes from markdown")
        print("✅ Converted YouTube links to iframes")
        print("Manual editing recommended to add:")
        print("- newthought spans for section openings")
        print("- Additional styling refinements")
        
    finally:
        # Clean up temp files
        if os.path.exists(temp_html):
            os.unlink(temp_html)
        if os.path.exists(temp_md_path):
            os.unlink(temp_md_path)

def extract_youtube_id(url):
    """Extract YouTube video ID from various YouTube URL formats"""
    parsed_url = urlparse(url)
    
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query).get('v', [None])[0]
        elif parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
    elif parsed_url.hostname in ['youtu.be']:
        return parsed_url.path[1:]
    
    return None

def convert_youtube_links(content):
    """Convert YouTube links to Tufte CSS iframe elements"""
    # Pattern to match YouTube URLs in paragraphs (handles HTML-escaped ampersands)
    youtube_pattern = r'<p>(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[\w\-&=?]*(?:(?:&amp;|&)t=\d+s?)?)</p>'
    
    def replace_youtube(match):
        url = match.group(1)
        # Unescape HTML entities
        url = url.replace('&amp;', '&')
        video_id = extract_youtube_id(url)
        
        if video_id:
            # Extract timestamp if present
            timestamp_match = re.search(r'[&?]t=(\d+)s?', url)
            start_param = f"?start={timestamp_match.group(1)}" if timestamp_match else ""
            
            embed_url = f"https://www.youtube.com/embed/{video_id}{start_param}"
            
            return f'''<figure class="iframe-wrapper">
          <iframe width="400" height="240" src="{embed_url}" frameborder="0" allowfullscreen></iframe>
        </figure>'''
        
        return match.group(0)  # Return original if we can't parse
    
    return re.sub(youtube_pattern, replace_youtube, content)

def process_script_embeds(content):
    """Process custom script embed syntax and preserve raw script tags"""
    
    # First, protect existing script tags by converting them to placeholders
    script_counter = 0
    script_placeholders = {}
    
    def protect_script(match):
        nonlocal script_counter
        placeholder = f"__SCRIPT_PLACEHOLDER_{script_counter}__"
        script_placeholders[placeholder] = match.group(0)
        script_counter += 1
        return placeholder
    
    # Protect existing <script> tags
    content = re.sub(r'<script[^>]*>.*?</script>', protect_script, content, flags=re.DOTALL)
    
    # Process custom Google Trends syntax
    trends_pattern = r'\[!trends:([^\]]+)\]'
    
    def replace_trends(match):
        nonlocal script_counter
        params_str = match.group(1)
        params = {}
        
        # Parse parameters (keyword:value,keyword2:value2)
        for param in params_str.split(','):
            if ':' in param:
                key, value = param.split(':', 1)
                params[key.strip()] = value.strip()
        
        keyword = params.get('keyword', 'Zilch')
        geo = params.get('geo', 'GB')
        time_range = params.get('time', '2021-01-01 2021-12-31')
        
        widget_id = f"trends-{keyword}-{geo}".replace(' ', '-').lower()
        
        # Create a properly formatted Google Trends embed
        embed_html = f'''__SCRIPT_PLACEHOLDER_{script_counter}__'''
        script_placeholders[embed_html] = f'''<figure class="fullwidth">
  <div class="trends-embed-container" style="width: 100%; height: 400px; margin: 1em 0;">
    <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/3829_RC01/embed_loader.js"></script>
    <script type="text/javascript">
      trends.embed.renderExploreWidget("TIMESERIES", {{"comparisonItem":[{{"keyword":"{keyword}","geo":"{geo}","time":"{time_range}"}}],"category":0,"property":""}}, {{"exploreQuery":"date={time_range.replace(' ', '%20')}&geo={geo}&q={keyword}&hl=en","guestPath":"https://trends.google.com:443/trends/embed/"}});
    </script>
  </div>
  <figcaption>Google Trends data for "{keyword}" in {geo}</figcaption>
</figure>'''
        
        script_counter += 1
        return embed_html
    
    content = re.sub(trends_pattern, replace_trends, content)
    
    # Store placeholders for later restoration
    content = (content, script_placeholders)
    return content

def process_tufte_annotations(content):
    """
    Process custom Tufte annotations before pandoc conversion
    
    Syntax:
    - Sidenotes: text[^sn: This is a sidenote]
    - Margin notes: text[^mn: This is a margin note]  
    - Sidenotes with images: text[^sn: Caption text ![alt](image.jpg)]
    - Margin notes with images: text[^mn: Caption text ![alt](image.jpg)]
    """
    sidenote_counter = 1
    
    def replace_sidenote(match):
        nonlocal sidenote_counter
        note_content = match.group(1)
        note_id = f"sn-{sidenote_counter}"
        
        # Check if there's an image in the note
        img_match = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', note_content)
        if img_match:
            alt_text = img_match.group(1)
            img_src = img_match.group(2)
            # Replace image markdown with HTML, keep any surrounding text
            note_content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', 
                                f'<img src="{img_src}" alt="{alt_text}"/>', note_content)
        
        # Process markdown links in sidenote content
        note_content = process_markdown_links(note_content)
        
        result = f'<label for="{note_id}" class="margin-toggle sidenote-number"></label><input type="checkbox" id="{note_id}" class="margin-toggle"/><span class="sidenote">{note_content}</span>'
        sidenote_counter += 1
        return result
    
    def replace_marginnote(match):
        note_content = match.group(1)
        mn_pattern = r'\[\^mn:'
        note_id = f"mn-{len(re.findall(mn_pattern, content))}"
        
        # Check if there's an image in the note
        img_match = re.search(r'!\[([^\]]*)\]\(([^)]+)\)', note_content)
        if img_match:
            alt_text = img_match.group(1)
            img_src = img_match.group(2)
            # Replace image markdown with HTML, keep any surrounding text
            note_content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', 
                                f'<img src="{img_src}" alt="{alt_text}"/>', note_content)
        
        # Process markdown links in margin note content
        note_content = process_markdown_links(note_content)
        
        return f'<label for="{note_id}" class="margin-toggle">&#8853;</label><input type="checkbox" id="{note_id}" class="margin-toggle"/><span class="marginnote">{note_content}</span>'
    
    # Process annotations with proper bracket handling
    def find_matching_bracket(text, start_pos):
        """Find the matching closing bracket, handling nested brackets"""
        bracket_count = 1
        pos = start_pos + 1
        
        while pos < len(text) and bracket_count > 0:
            if text[pos] == '[':
                bracket_count += 1
            elif text[pos] == ']':
                bracket_count -= 1
            pos += 1
        
        return pos - 1 if bracket_count == 0 else -1
    
    # Process sidenotes
    sn_pattern = r'\[\^sn:\s*'
    pos = 0
    while True:
        match = re.search(sn_pattern, content[pos:])
        if not match:
            break
        
        start = pos + match.start()
        content_start = pos + match.end()
        end = find_matching_bracket(content, start)
        
        if end != -1:
            note_content = content[content_start:end]
            replacement = replace_sidenote(type('Match', (), {'group': lambda x: note_content}))
            content = content[:start] + replacement + content[end+1:]
            pos = start + len(replacement)
        else:
            pos = content_start
    
    # Process margin notes
    mn_pattern = r'\[\^mn:\s*'
    pos = 0
    while True:
        match = re.search(mn_pattern, content[pos:])
        if not match:
            break
        
        start = pos + match.start()
        content_start = pos + match.end()
        end = find_matching_bracket(content, start)
        
        if end != -1:
            note_content = content[content_start:end]
            replacement = replace_marginnote(type('Match', (), {'group': lambda x: note_content}))
            content = content[:start] + replacement + content[end+1:]
            pos = start + len(replacement)
        else:
            pos = content_start
    
    return content

def extract_metadata_from_markdown(markdown_content):
    """Extract title and subtitle from markdown content"""
    lines = markdown_content.split('\n')
    title = None
    subtitle = None
    
    # Look for title (first # line)
    for line in lines:
        if line.strip().startswith('# '):
            title = line.strip()[2:].strip()
            break
    
    # Look for subtitle on line after title (format: subtitle: Your Subtitle)
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('subtitle:'):
            subtitle = line.strip()[9:].strip()  # Remove 'subtitle:' prefix
            # Remove this line from content for processing
            lines.pop(i)
            break
        # Alternative: look for italic text right after title
        elif title and i > 0 and lines[i-1].strip().startswith('# ') and line.strip().startswith('*') and line.strip().endswith('*'):
            subtitle = line.strip()[1:-1]  # Remove asterisks
            lines.pop(i)  # Remove from content
            break
    
    # Clean up empty lines at the beginning
    while lines and lines[0].strip() == '':
        lines.pop(0)
    
    # Process markdown links in subtitle if present
    if subtitle:
        subtitle = process_markdown_links(subtitle)
    
    return title, subtitle, '\n'.join(lines)

def process_markdown_links(text):
    """Convert markdown links to HTML links"""
    # Pattern for [text](url) or [!text](url)
    link_pattern = r'\[!?([^\]]+)\]\(([^)]+)\)'
    
    def replace_link(match):
        link_text = match.group(1)
        url = match.group(2)
        # Add https:// if no protocol specified and not an anchor link
        if not url.startswith(('http://', 'https://', '#', '/')):
            url = 'https://' + url
        return f'<a href="{url}">{link_text}</a>'
    
    return re.sub(link_pattern, replace_link, text)

def create_tufte_structure(html_content, input_file, title=None, subtitle=None):
    """Create the basic Tufte CSS structure"""
    
    # Extract title from HTML if not provided
    if not title:
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content)
        title = title_match.group(1) if title_match else "Document"
    
    # Clean up the HTML content - remove standalone h1 and wrap in sections
    content = html_content
    
    # Convert YouTube links to iframes before other processing
    content = convert_youtube_links(content)
    
    # Basic cleanup
    content = re.sub(r'<h1[^>]*>.*?</h1>', '', content)  # Remove first h1
    
    # Wrap h2 sections with proper indentation
    sections = re.split(r'(<h2[^>]*>.*?</h2>)', content)
    structured_content = ""
    in_section = False
    
    for i, section in enumerate(sections):
        if section.strip():
            if section.startswith('<h2'):
                # Close previous section if needed
                if in_section:
                    structured_content += "\n      </section>\n"
                # Start new section
                structured_content += f"\n      <section>\n        {section}\n"
                in_section = True
            else:
                # Add content with proper indentation
                if section.strip():
                    # Clean up and indent paragraphs properly
                    section_lines = section.strip().split('\n')
                    indented_lines = []
                    for line in section_lines:
                        if line.strip():
                            indented_lines.append(f"        {line.strip()}")
                    if indented_lines:
                        structured_content += '\n'.join(indented_lines) + '\n'
    
    # Close final section
    if in_section:
        structured_content += "      </section>"
    
    # Create subtitle element
    if not subtitle:
        subtitle = f"Generated from {os.path.basename(input_file)}"
    
    subtitle_html = f'<p class="subtitle">{subtitle}</p>' if subtitle else ''
    
    # Create the full HTML document
    tufte_template = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8"/>
    <title>{title}</title>
    <link rel="stylesheet" href="tufte-css/tufte.css"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>

  <body>
    <article>
      <h1>{title}</h1>
      {subtitle_html}
      {structured_content}
    </article>
  </body>
</html>'''
    
    return tufte_template

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 md_to_tufte.py input.md output.html")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} does not exist")
        sys.exit(1)
    
    convert_markdown_to_tufte_html(input_file, output_file)