---
title: Creating and Customizing Charts
type: docs
weight: 10
url: /cpp/creating-and-customizing-charts/
---

## **Possible Usage Scenarios**

A chart is a visual display of information. Aspose.Cells allows developers to visualize information in charts just as Microsoft Excel does. Presenting information in charts is always helpful to decision-makers for making quick and timely decisions. It's easier to quickly see comparisons, patterns, and trends in data with charts rather than raw numbers. Creating charts at runtime, based on the data in a spreadsheet, is one of Aspose.Cells' useful feature. Aspose.Cells supports creating both Standard and Customized charts. Below, we will show a few examples with sample files on how to create some common MS-Excel chart types using Aspose.Cells API.

## **Pyramid Chart**

When the example code is executed, a pyramid chart is added to the worksheet. Please see the [output Excel file](66519068.xlsx) of the following sample code.

{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Charts-CreatingAndCustomizingCharts_PyramidChart.cpp" >}}

## **Line Chart**

In the above example, simply changing the [**ChartType**](https://apireference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70) to [**ChartType_Line**](https://apireference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70ad12ff1561ab1424a0c3095b6dc07ac25) creates a line chart. The complete source is provided below. when the code is executed, a line chart is added to the worksheet. Please see the [output Excel file](66519069.xlsx) of the following sample code.

{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Charts-CreatingAndCustomizingCharts_LineChart.cpp" >}}

## **Bubble Chart**

In order to create a bubble chart, the [**ChartType**](https://apireference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70) has to be set to [**ChartType_Bubble**](https://apireference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70a5efa533b454f9415e4497dbb2ab28b3d) and few extra properties such as [**SetBubbleSizes**](https://apireference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a00cf890ba7ab419d31a522ab52b02e9d) & [**SetXValues**](https://apireference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a788ff4aa51dbf9bed5327298af93a6db) need to be set accordingly. Upon executing the following code, a bubble chart is added to the worksheet. Please see the [output Excel file](66519070.xlsx) of the following sample code.

{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Charts-CreatingAndCustomizingCharts_BubbleChart.cpp" >}}

## **Creating Custom Charts**

So far, when we've discussed charts, we've looked at standard charts that have their own standard formatting settings. We only define the data source, set a few properties and the chart is created with its default format settings. But Aspose.Cells APIs also supports creating custom charts that allow developers to create charts with their own format settings. Developers can create custom charts at run-time using Aspose.Cells.

A chart is composed of a data series. When creating a custom chart, developers have the freedom to use different types of charts for different data series.

The example code below demonstrates how to create custom charts. In this example, we are going to use a column chart for the first data series and a line chart for the second series. The result is that we add a column chart, combined with a line chart, to the worksheet. Please see the [output Excel file](66519071.xlsx) of the following sample code.

{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Charts-CreatingAndCustomizingCharts_CustomChart.cpp" >}}
