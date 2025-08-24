---
title: Set Data Source for the Chart with Golang via C++
linktitle: Data Source
type: docs
weight: 10
url: /go-cpp/data-formatting-in-charts/
description: Learn about the various data sources supported by Aspose.Cells for C++. Our guide will walk you through the different types of data sources available and show you how to connect and retrieve data from them to populate your worksheets.
keywords: Aspose.Cells for C++, charting, data formatting, labels, colors, fonts, appearance, usability.
---

In our previous topics, we have already provided many examples to demonstrate how you can set a data source for your chart. In this topic, we are going to provide more details about the types of data that can be set for a chart.

## **Setting Chart Data**

There are two types of data to deal with while working on charts using Aspose.Cells as follows:

- Chart data.
- Category data.

### **Chart Data**

Chart data is the data that we use as a data source to build our charts. We can add a range of the cells (containing chart data) by calling the [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) object's [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) method.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-DataSource.go" >}}
### **Category Data**

Category data is used for the labeling of chart data and can be added to [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) by using its [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/) property. A complete example is given below to demonstrate the use of chart and category data. After executing the above example code, a column chart will be added to the worksheet as shown below.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-DataSource-1.go" >}}
## **Advance Topics**
- [Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range](/cells/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Create Dynamic Charts](/cells/cpp/create-dynamic-charts/)
- [Easy way for Chart Setup using Chart.SetChartDataRange method](/cells/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Find Type of X and Y Values of Points in Chart Series](/cells/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)