---
title: Create Open-High-Low-Close(OHLC) Stock Chart with Golang via C++
description: Learn how to create an open-high-low-close stock chart using Aspose.Cells for C++. Our guide will demonstrate how to plot stock market data, including the open, high, low, and close prices, onto a chart for better analysis and visualization.
keywords: Aspose.Cells for C++, Open-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 182
url: /go-cpp/create-open-high-low-close-stock-chart/
---

## **Possible Usage Scenarios**
The Open-High-Low-Close (OHLC) chart uses five columns of data, in order: category, open, high, low, and close. The range of prices in each category is again indicated by a vertical line, while the range between open and close is given by a wider floating bar; if the price increases in the category (close is higher than open), the bar is filled with one color, while if the price decreases, the bar is filled with another. This type of chart is often called a candlestick chart.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Visibility improvements in the chart**
We often use colors rather than black and white to indicate increasing and decreasing prices. In the first set of candlesticks below, red shows increasing and green decreasing prices.

![todo:image_alt_text](sample2.png)

## **Sample Code**
The following sample code loads the [sample Excel file](Open-High-Low-Close.xlsx) and generates the [output Excel file](out.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-CreateOpenHighLowCloseChart.go" >}}