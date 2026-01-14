# Tufte Markdown Syntax Guide

This enhanced conversion script supports custom markdown syntax for Tufte CSS elements.

## Titles and Subtitles

**Method 1 - Explicit subtitle:**
```markdown
# My Document Title
subtitle: My Custom Subtitle

## First Section
Content here...
```

**Method 2 - Italic subtitle:**
```markdown
# My Document Title  
*My Custom Subtitle*

## First Section
Content here...
```

**Result:** Creates proper Tufte CSS subtitle with `<p class="subtitle">` styling

## Sidenotes

Add numbered sidenotes that appear in the margin:

```markdown
This is regular text[^sn: This is a sidenote] with a sidenote.
```

**Result:** Creates a numbered sidenote with automatic numbering (1, 2, 3...)

## Margin Notes

Add unnumbered margin notes with a symbol (⊕):

```markdown  
This text has context[^mn: This is a margin note] in the margin.
```

**Result:** Creates a margin note with the ⊕ symbol instead of numbers

## Images in Sidenotes/Margin Notes

Include images within sidenotes or margin notes:

```markdown
PayPal's early growth[^sn: Logo ![PayPal Logo](logo.png) from their founding era] was remarkable.

Network effects matter[^mn: Diagram ![Network](network.jpg) showing connections] for platforms.
```

**Features:**
- ✅ Automatic image conversion to HTML `<img>` tags
- ✅ Alt text preservation 
- ✅ Proper nesting within sidenote/margin note spans
- ✅ Mixed text and images in same note

## YouTube Videos

Paste YouTube URLs directly in markdown:

```markdown
Here's a relevant video:

https://www.youtube.com/watch?v=vDwzmJpI4io&t=680s
```

**Result:** Converts to responsive Tufte CSS iframe with:
- ✅ Proper `iframe-wrapper` class
- ✅ Timestamp preservation (`&t=680s` → `?start=680`)
- ✅ Responsive sizing (400x240)

## Script Embeds

### Method 1: Direct HTML (Recommended)
Embed scripts directly in markdown (always works):

```markdown
<figure class="iframe-wrapper">
<script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/4116_RC01/embed_loader.js"></script>
<script type="text/javascript">
trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"zilch","geo":"GB","time":"2020-01-01 2021-12-18"}],"category":0,"property":""}, {"exploreQuery":"date=2020-01-01%202021-12-18&geo=GB&q=zilch&hl=en-GB","guestPath":"https://trends.google.com:443/trends/embed/"});
</script>
</figure>
```

### Method 2: Custom Syntax (Clean)
For Google Trends specifically:

```markdown
[!script:google-trends]
keyword: zilch
geo: GB
time: 2020-01-01 2021-12-18
[/script]
```

**Features:**
- ✅ Clean, readable syntax
- ✅ Auto-generates proper Google Trends embed code
- ✅ Proper Tufte CSS `iframe-wrapper` styling
- ✅ Works with all Google Trends parameters

## Complete Example

```markdown
# My Document
subtitle: A Comprehensive Guide

## Introduction

RAF programs are powerful[^sn: Can drive 30-50% of user acquisition] when done right.

Companies like PayPal[^mn: Logo ![PayPal](logo.png) shows their branding] used bonuses effectively.

Here's Elon discussing this:

https://www.youtube.com/watch?v=vDwzmJpI4io&t=680s

The key insight[^sn: $20 signup + $20 referral was their formula] was generous incentives.
```

## Usage

```bash
python3 md_to_tufte.py input.md output.html
```

**Processing Order:**
1. Parse custom Tufte annotations (`[^sn:]`, `[^mn:]`)
2. Convert to HTML with proper Tufte CSS classes
3. Process through pandoc for markdown → HTML
4. Convert YouTube links to iframes
5. Apply Tufte document structure

## Manual Refinements

After conversion, consider adding:
- `<span class="newthought">` for section openings
- Additional styling for blockquotes
- Custom figure elements for complex layouts