---
title: Set Data source for the chart
description: Learn about the various data sources supported by Aspose.Cells for Python via .NET. Our guide will walk you through the different types of data sources available and show you how to connect and retrieve data from them to populate your worksheets.
keywords: Aspose.Cells for Python via .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: Data source
type: docs
weight: 10
url: /python-net/data-formatting-in-charts/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

In our previous topics, we have already provided many examples to demonstrate that how can you set a data source for your chart but in this topic, we are going to provide more details about the types of data that can be set for a chart.

## **Setting Chart Data**

There are two types of data to deal with while working on charts using Aspose.Cells for Python via .NET as follows:

- Chart data.
- Category data.

### **Chart Data**

Chart data is the data that we use as a data source to build our charts. We can add a range of the cells (containing chart data) by calling the [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) object's [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add) method.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **Category Data**

Category data is used for the labeling of chart data and can be added to [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) by using its [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data) property. A complete example is given below to demonstrate the use of chart and category data. After executing the above example code, a column chart will be added to the worksheet as shown below.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **Advance topics**
- [Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range](/cells/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Create Dynamic Charts](/cells/python-net/create-dynamic-charts/)
- [Easy way for Chart Setup using Chart.SetChartDataRange method](/cells/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Find Type of X and Y Values of Points in Chart Series](/cells/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="python-net" >}}
