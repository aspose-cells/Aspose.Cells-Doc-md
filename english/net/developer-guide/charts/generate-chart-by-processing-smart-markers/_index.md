---
title: Generate Chart by Processing Smart Markers
description: Learn how to generate charts with smart markers using Aspose.Cells for .NET. Our guide will show you how to process smart markers and their properties to enhance the appearance and usability of your charts.
keywords: Aspose.Cells for .NET, chart generation, smart markers, appearance, usability, processing.
type: docs
weight: 2100
url: /net/generate-chart-by-processing-smart-markers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells APIs provide the [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) class to work with Smart Markers where the formatting & formulas are placed in the designer spreadsheets and then processed with [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) class to fill up the data according to specified Smart Markers. It is also possible to create Excel charts by processing Smart Markers, which will require the following steps.

- Creation of designer spreadsheet
- Processing designer spreadsheet against the specified data source
- Creation of chart based on populated data

{{% /alert %}}

## Creation of Designer Spreadsheet

A designer spreadsheet is a simple Excel file created with Microsoft Excel application or Aspose.Cells APIs containing the visual formatting, formulas and smart markers, where the contents can be populated at runtime.

For the sake of simplicity, we will create the designer spreadsheet using the Aspose.Cells for .NET API and later process it against a dynamically created data source for demonstration purposes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Processing Designer Spreadsheet

In order to process the designer spreadsheet, one must have a data source that corresponds to the Smart Markers used in the designer spreadsheet. For instance, we have created a Smart Marker entry as &=Sales.Year, that represents the Year column in the DataTable Sales. In case a corresponding column isn't available in the data source, the Aspose.Cells APIs will skip the processing for that particular Smart Marker, and as a result, the data for the particular Smart Marker will not be populated.

In order to demonstrate this use case, we will create the data source from scratch and process it against the designer spreadsheet created in the previous step. However, in a real-time scenario, data could already be available for further processing so you can skip the creation of data source if data is already available.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

The processing of Smart Markers is quite simple as demonstrated by the following code snippet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

The above code snippet uses the existing instance of the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class created in the first step. If you already have the designer spreadsheet file on disk or memory, you can create an instance of [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class by loading the existing designer spreadsheet.

{{% /alert %}}

## Creation of Chart

Once the data is in place, all we need to do is to create a chart based on the data source. In order to keep the example simple, we will use the [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange) method so that we do not have to configure the chart further.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
