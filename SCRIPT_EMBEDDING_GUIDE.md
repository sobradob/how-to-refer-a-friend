# Script Embedding Guide for Tufte CSS

## ✅ Recommended Approach: Direct HTML

For Google Trends and other complex scripts, use this pattern:

```html
<figure class="iframe-wrapper">
  <div id="trends-chart-1" style="width: 100%; height: 400px;"></div>
  <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/4116_RC01/embed_loader.js"></script>
  <script type="text/javascript">
    if (typeof trends !== 'undefined') {
      trends.embed.renderExploreWidget("TIMESERIES", 
        {"comparisonItem":[{"keyword":"zilch","geo":"GB","time":"2020-01-01 2021-12-18"}],"category":0,"property":""}, 
        {"exploreQuery":"date=2020-01-01%202021-12-18&geo=GB&q=zilch&hl=en-GB","guestPath":"https://trends.google.com:443/trends/embed/"}, 
        "trends-chart-1"
      );
    }
  </script>
</figure>
```

## Key Improvements:

1. **Target div**: Provides explicit container for the widget
2. **Unique ID**: Each chart gets its own container ID
3. **Safety check**: `if (typeof trends !== 'undefined')` prevents errors
4. **Proper sizing**: `width: 100%; height: 400px;` ensures visibility
5. **Tufte styling**: Uses `iframe-wrapper` class for responsive behavior

## Alternative: Simplified Embedding

For charts that support iframe embedding:

```html
<figure class="iframe-wrapper">
  <iframe src="https://trends.google.com/trends/embed/explore/TIMESERIES?req=%7B%22comparisonItem%22%3A%5B%7B%22keyword%22%3A%22zilch%22%2C%22geo%22%3A%22GB%22%2C%22time%22%3A%222020-01-01%202021-12-18%22%7D%5D%2C%22category%22%3A0%2C%22property%22%3A%22%22%7D&tz=0&eq=date%3D2020-01-01%25202021-12-18%26geo%3DGB%26q%3Dzilch" 
          width="100%" 
          height="400" 
          frameborder="0" 
          scrolling="no">
  </iframe>
</figure>
```

## Why These Work Better:

- **Explicit containers** prevent layout issues
- **Error handling** prevents JavaScript failures
- **Consistent sizing** ensures proper display
- **Tufte CSS integration** maintains elegant styling