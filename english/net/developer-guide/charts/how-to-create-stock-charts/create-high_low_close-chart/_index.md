---
title: Create High-Low-Close(HLC) Stock Chart
description: Learn how to create a high-low-close stock chart using Aspose.Cells for .NET. Our step-by-step guide will demonstrate how to plot stock market data, including the high, low, and close prices, onto a chart for better analysis and visualization.
keywords: Aspose.Cells for .NET, High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 181
url: /net/create-high-low-close-stock-chart/
---

## **Possible Usage Scenarios**
The High-Low-Close (HLC) stock chart uses four columns of data. The first column is a category, usually a date but stock names can also be used. The next three columns in order are for high, low, and closing prices. The range of price for each category is indicated by a vertical line from low to high, and closing price is shown using a tickmark extending to the right of this line.

![todo:image_alt_text](sample.png)
## **Visibility improvements in the chart**
Sometimes, to make the chart look more intuitive, we can modify the appearance of the marker (close), or make it display on the secondary axis.

![todo:image_alt_text](sample2.png)
## **Sample Code**
The following sample code loads the [sample Excel file](High-Low-Close.xlsx) and generates the [output Excel file](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-high-low-close-stock-chart.cs" >}}
