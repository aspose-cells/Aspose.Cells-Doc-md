---
title: Create Open-High-Low-Close(OHLC) Stock Chart
type: docs
weight: 182
url: /net/create-open-high-low-close-stock-chart/
---

## **Possible Usage Scenarios**
The Open-High-Low-Close (OHLC) chart uses five columns of data, in order: category, open, high, low, and close. The range of prices in each category is again indicated by a vertical line, while the range between open and close is given by a wider floating bar; if the price increases in the category (close is higher than open), the bar is filled with one color, while if the price decreases, the bar is filled with another. This type of chart is often called a candlestick chart.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Visibility improvements in the chart**
We often use colors rather than black and white to indicate increasing and decreasing prices.  In the first set of candlesticks below, red shows increasing nad green decreasing prices.

![todo:image_alt_text](sample2.png)
## **Sample Code**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}