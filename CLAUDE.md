# CLAUDE.md

## What This Project Does

Converts Markdown documents into a multi-page website using Tufte CSS styling. The main content is a guide on Refer-A-Friend (RAF) programs for fintech/consumer businesses.

**Live site:** https://boazsobrado.com/how-to-refer-a-friend/
**Repository:** https://github.com/sobradob/how-to-refer-a-friend

## Quick Commands

```bash
# Generate multi-page site (outputs to docs/ for GitHub Pages)
python3 md_to_multipage.py refer_a_friend.md docs/

# Generate single-page HTML (legacy)
python3 md_to_tufte.py refer_a_friend.md -o refer_a_friend_output.html

# Minify CSS (from tufte-css/)
cleancss -o tufte.min.css tufte.css
```

## Project Structure

```
raf/
├── refer_a_friend.md          # Main content (markdown source)
├── md_to_multipage.py         # Multi-page site generator
├── md_to_tufte.py             # Single-page converter (legacy)
├── docs/                      # Generated site (GitHub Pages source)
│   ├── index.html             # Introduction + TOC
│   ├── understanding-referrals.html
│   ├── design-principles.html
│   ├── operations.html
│   ├── referrals-and-affiliates.html
│   ├── when-to-reach-out.html
│   ├── unincentivised-referrals.html
│   ├── tufte-css/             # CSS + fonts
│   └── img/                   # Images
├── tufte-css/                 # Tufte CSS framework (source)
│   ├── tufte.css
│   └── nav.css                # Navigation styles
├── img/                       # Source images
├── TUFTE_MARKDOWN_SYNTAX.md   # Custom markdown syntax reference
└── SCRIPT_EMBEDDING_GUIDE.md  # How to embed scripts/iframes
```

## Site Structure

The site is split into 7 chapters:

| Chapter | File | Nav Label |
|---------|------|-----------|
| Introduction | `index.html` | Intro |
| Understanding Referrals | `understanding-referrals.html` | I. Understanding |
| Design Principles | `design-principles.html` | II. Design |
| Operations | `operations.html` | III. Operations |
| Referrals And Affiliates | `referrals-and-affiliates.html` | IV. Affiliates |
| When to Reach out (CRM) | `when-to-reach-out.html` | V. CRM |
| Unincentivised Referrals | `unincentivised-referrals.html` | VI. Unincentivised |

## Multi-Page Converter (md_to_multipage.py)

### Key Configuration

**Chapter short names** (in `CHAPTER_SHORT_NAMES` dict):
```python
CHAPTER_SHORT_NAMES = {
    'introduction': 'Intro',
    'understanding-referrals': 'I. Understanding',
    'design-principles': 'II. Design',
    ...
}
```

**Slug overrides** (in `generate_slug()` function):
```python
slug_overrides = {
    'Introduction': 'introduction',
    'Understanding Referrals': 'understanding-referrals',
    ...
}
```

### How It Works

1. Parses markdown, splits on H2 headings into chapters
2. Skips "Table of Contents" section
3. Generates persistent navigation bar for all pages
4. Introduction chapter becomes `index.html`
5. All other chapters get their own `{slug}.html` file
6. Copies `tufte-css/` and `img/` to output directory
7. Wraps content in `<section>` elements for proper Tufte styling

### Adding a New Chapter

1. Add `## Chapter Title` in `refer_a_friend.md`
2. Add slug override in `generate_slug()` if needed
3. Add short name in `CHAPTER_SHORT_NAMES`
4. Run `python3 md_to_multipage.py refer_a_friend.md docs/`

## Tufte Markdown Syntax

The converter supports custom syntax beyond standard markdown:

- **Sidenotes**: `[^sn: sidenote text]`
- **Margin notes**: `[^mn: margin note text]`
- **New thought**: `<span class="newthought">Opening phrase</span>`
- **Epigraphs**: Use `<div class="epigraph">` with blockquote
- **Full-width figures**: `{fullwidth}` marker

See `TUFTE_MARKDOWN_SYNTAX.md` for complete reference.

## Navigation Design

- Sticky header with site title
- Chapter links with current page highlighted (bold)
- Mobile: CSS-only hamburger menu
- Dark mode support via `prefers-color-scheme`
- PDF download link (placeholder)

## Deployment

The site is deployed via GitHub Pages from the `docs/` folder.

```bash
# After making changes:
python3 md_to_multipage.py refer_a_friend.md docs/
git add -A
git commit -m "Update content"
git push
```

GitHub Pages will automatically rebuild within a few minutes.

## HTML Structure

Each page follows this structure:

```html
<body>
  <nav class="site-nav">
    <div class="nav-container">
      <a href="index.html" class="site-title">How To Refer A Friend</a>
      <a href="refer_a_friend.pdf" class="pdf-link">[PDF]</a>
      <input type="checkbox" id="nav-toggle" class="nav-toggle">
      <label for="nav-toggle" class="nav-toggle-label"></label>
      <ul class="chapter-nav">
        <li><a href="index.html" class="current">Intro</a></li>
        <li><a href="understanding-referrals.html">I. Understanding</a></li>
        ...
      </ul>
    </div>
  </nav>
  <article>
    <h1>Chapter Title</h1>
    <section>
      <h3>Subsection</h3>
      <p>Content with sidenotes...</p>
    </section>
  </article>
</body>
```

## Testing

1. Run `python3 md_to_multipage.py refer_a_friend.md docs/`
2. Open `docs/index.html` in browser
3. Test:
   - Navigation links work
   - Current page is highlighted
   - Mobile hamburger menu works
   - Sidenotes toggle on mobile
   - No horizontal scrollbar
