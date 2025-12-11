---
title: Create Dynamic Charts
description: Learn how to create dynamic charts in Aspise.Cells for .NET. Our guide will show you how to dynamically update chart data, series, and formatting based on your requirements, allowing you to present changing data visually in your worksheets.
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /net/create-dynamic-charts/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Dynamic (or interactive) charts have the ability to change when you change the scope of data. In other words, dynamic charts can automatically reflect changes when the data source is changed. To trigger the change in the data source, you can use the filtering option of Excel tables or a control such as a ComboBox or dropdown list.

This article demonstrates the usage of Aspose.Cells for .NET APIs to create dynamic charts using both of the aforementioned approaches.

{{% /alert %}}

## **Using Excel Tables**

{{% alert color="primary" %}}

Excel tables are referred to as ListObjects from Aspose.Cells' perspective; therefore, we will use the term "ListObject" instead of "Table" for clarity. Please read in detail on how to [create ListObjects](/cells/net/create-and-format-table/) with Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects provide built‑in functionality to sort and filter the data upon user interaction. Both sorting and filtering options are provided through the drop‑down lists that are automatically added to the header row of the [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject). Due to these features (sorting and filtering), the [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) seems to be the perfect candidate to serve as the data source for a dynamic chart because when sorting or filtering is changed, the representation of data in the chart will be changed to reflect the current state of the [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

To keep the demonstration simple to understand, we will create the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) from scratch and move forward step by step as outlined below.

1. Create an empty [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
2. Access the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) of the first [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) in the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
3. Insert some data into the cells.
4. Create a [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) based on the inserted data.
5. Create a [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) based on the data range of the [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
6. Save the result to disk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Using Dynamic Formulas**

If you do not wish to use the [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) as a data source for the dynamic chart, another option is to use Excel functions (or formulas) to create a dynamic range of data, along with a control (such as a ComboBox) to trigger the change in data. In this scenario, we will use the VLOOKUP function to fetch the appropriate values based on the selection of the ComboBox. When the selection is changed, the VLOOKUP function will refresh the cell value. If a range of cells is using the VLOOKUP function, the whole range can be refreshed upon user interaction; therefore, it can be used as a source for the dynamic chart.

To keep the demonstration simple to understand, we will create the Workbook from scratch and move forward step by step as outlined below.

1. Create an empty [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
2. Access the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) of the first [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) in the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
3. Insert some data into the cells by creating a named range. This data will serve as a series for the dynamic chart.
4. Create a [**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) based on the named range created in the previous step.
5. Insert some more data into the cells that will serve as a source for the VLOOKUP function.
6. Insert the VLOOKUP function (with appropriate parameters) into a range of cells. This range will serve as a source for the dynamic chart.
7. Create a [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) based on the range created in the previous step.
8. Save the result to disk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
