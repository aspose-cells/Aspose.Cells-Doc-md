---
title: Set Data source for the chart
description: Learn about the various data sources supported by Aspose.Cells for .NET. Our guide will walk you through the different types of data sources available and show you how to connect and retrieve data from them to populate your worksheets.
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: Data source
type: docs
weight: 10
url: /net/data-formatting-in-charts/
---

In our previous topics, we have already provided many examples to demonstrate that how can you set a data source for your chart but in this topic, we are going to provide more details about the types of data that can be set for a chart.

## **Setting Chart Data**

There are two types of data to deal with while working on charts using Aspose.Cells as follows:

- Chart data.
- Category data.

### **Chart Data**

Chart data is the data that we use as a data source to build our charts. We can add a range of the cells (containing chart data) by calling the [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) object's [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) method.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Category Data**

Category data is used for the labeling of chart data and can be added to [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) by using its [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata) property. A complete example is given below to demonstrate the use of chart and category data. After executing the above example code, a column chart will be added to the worksheet as shown below.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Advance topics**
- [Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range](/cells/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Create Dynamic Charts](/cells/net/create-dynamic-charts/)
- [Easy way for Chart Setup using Chart.SetChartDataRange method](/cells/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Find Type of X and Y Values of Points in Chart Series](/cells/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="csharp" >}}