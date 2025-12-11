---
title: Creating and Customizing Charts
type: docs
weight: 10
url: /cpp/creating-and-customizing-charts/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

A chart is a visual display of information. Aspose.Cells allows developers to visualize information in charts just as Microsoft Excel does. Presenting information in charts is always helpful to decision‑makers for making quick and timely decisions. It's easier to quickly see comparisons, patterns, and trends in data with charts rather than raw numbers. Creating charts at runtime, based on the data in a spreadsheet, is one of Aspose.Cells' useful features. Aspose.Cells supports creating both Standard and Customized charts. Below, we will show a few examples with sample files on how to create some common Microsoft Excel chart types using Aspose.Cells API.

## **Pyramid Chart**

When the example code is executed, a pyramid chart is added to the worksheet. Please see the [output Excel file](66519068.xlsx) of the following sample code.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **Line Chart**

In the above example, simply changing the [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) to **`ChartType::Line`** creates a line chart. The complete source is provided below. **When** the code is executed, a line chart is added to the worksheet. Please see the [output Excel file](66519069.xlsx) of the following sample code.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **Bubble Chart**

In order to create a bubble chart, the [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) has to be set to **`ChartType_Bubble`** and a few extra properties such as [**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) need to be set accordingly. Upon executing the following code, a bubble chart is added to the worksheet. Please see the [output Excel file](66519070.xlsx) of the following sample code.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **Creating Custom Charts**

So far, when we've discussed charts, we've looked at standard charts that have their own standard formatting settings. We only define the data source, set a few properties and the chart is created with its default format settings. But Aspose.Cells **API** also supports creating custom charts that allow developers to create charts with their own format settings. Developers can create custom charts at run‑time using Aspose.Cells.

A chart is composed of a data series. When creating a custom chart, developers have the freedom to use different types of charts for different data series.

The example code below demonstrates how to create custom charts. In this example, we are going to use a column chart for the first data series and a line chart for the second series. The result is that we add a column chart, combined with a line chart, to the worksheet. Please see the [output Excel file](66519071.xlsx) of the following sample code.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
