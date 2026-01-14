# CLAUDE.md

## What This Project Does

Converts Markdown documents into elegant HTML using Tufte CSS styling. The main content is a guide on Refer-A-Friend (RAF) programs for fintech/consumer businesses.

## Quick Commands

```bash
# Convert markdown to Tufte HTML
python md_to_tufte.py refer_a_friend.md -o refer_a_friend_output.html

# Minify CSS (from tufte-css/)
cleancss -o tufte.min.css tufte.css
```

## Key Files

| File | Purpose |
|------|---------|
| `md_to_tufte.py` | Markdown → Tufte HTML converter script |
| `refer_a_friend.md` | Main content document |
| `TUFTE_MARKDOWN_SYNTAX.md` | Custom markdown syntax reference |
| `SCRIPT_EMBEDDING_GUIDE.md` | How to embed scripts/iframes |
| `tufte-css/tufte.css` | Tufte CSS framework |
| `tufte-css/index.html` | CSS demo/reference page |

## Tufte Markdown Syntax

The converter supports custom syntax beyond standard markdown:

- **Sidenotes**: `{>> sidenote text <<}` or `{sn: sidenote text}`
- **Margin notes**: `{mn: margin note text}`
- **New thought**: `{nt: Opening phrase}` for small-caps paragraph starts
- **Epigraphs**: Blockquotes with `-- Author, Source` attribution
- **Full-width figures**: `{fullwidth}` marker

See `TUFTE_MARKDOWN_SYNTAX.md` for complete reference.

## HTML Structure

When editing output HTML or the converter:

```html
<article>
  <h1>Title</h1>
  <p class="subtitle">Subtitle</p>
  <section>
    <h2>Section</h2>
    <p><span class="newthought">Opening phrase</span> continues...</p>
    <label for="sn-1" class="margin-toggle sidenote-number"></label>
    <input type="checkbox" id="sn-1" class="margin-toggle"/>
    <span class="sidenote">Sidenote content</span>
  </section>
</article>
```

## Testing

Open output HTML files in a browser. Test responsive behavior at various widths—sidenotes collapse into toggleable notes on mobile.
