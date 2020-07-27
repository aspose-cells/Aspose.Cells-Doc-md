+++
title = "Create Dynamic Charts" 
description = "" 
weight = 20521 
+++

Aspose.Cells for .NET : Create Dynamic Charts  

# Aspose.Cells for .NET : Create Dynamic Charts


Dynamic (or interactive) charts have the ability to change when you change the scope of data. In other words, the dynamic charts can automatically reflect changes when the data source is changed. In order to trigger the change in the data source, one can use the filtering option of Excel Tables or use a control such as ComboBox or Dropdown list.

This article demonstrates the usage of Aspose.Cells for .NET APIs to create dynamic charts using both of the aforementioned approaches.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Using Excel Tables](#CreateDynamicCharts-UsingExcelTables)
*   2 [Using Dynamic Formulas](#CreateDynamicCharts-UsingDynamicFormulas)
{{< /panel >}}
 

 

## Using Excel Tables

Excel tables are referred to as ListObjects in Aspose.Cells' perspective, therefore, we will use the term "ListObject" instead of "Table" for clarity. Please read in detail on how to [create ListObjects](http://www.aspose.com/docs/display/cellsnet/Creating+a+List+Object) with Aspose.Cells for .NET API.

ListObjects provides the in-built functionality to sort & filter the data upon user interaction. Both sorting & filtering options are provided through the drop-down lists which are automatically added to the header row of the [ListObject](https://apireference.aspose.com/net/cells/aspose.cells.tables/listobject). Due to these features (sorting & filtering), the [ListObject](https://apireference.aspose.com/net/cells/aspose.cells.tables/listobject) seems to be the perfect candidate to serve as the data source to a dynamic chart because when sorting or filtering is changed, the representation of data in the chart will be changed to reflect the current state of the [ListObject](https://apireference.aspose.com/net/cells/aspose.cells.tables/listobject).

In order to keep the demonstration simple to understand, we will create the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) from scratch and move forward step by step as outlined below.

1.  Create an empty [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook).
2.  Access the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) of the first [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) in the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook).
3.  Insert some data to the cells.
4.  Create [ListObject](https://apireference.aspose.com/net/cells/aspose.cells.tables/listobject) based on the inserted data.
5.  Create [Chart](https://apireference.aspose.com/net/cells/aspose.cells.charts/chart) based on the data range of [ListObject](https://apireference.aspose.com/net/cells/aspose.cells.tables/listobject).
6.  Save the result on the disc.

## Using Dynamic Formulas

In case you do not wish to use the [ListObject](https://apireference.aspose.com/net/cells/aspose.cells.tables/listobject) as a data source to the dynamic chart, the other option is to use Excel functions (or formulas) to create a dynamic range of data, and a control (such as ComboBox) to trigger the change in data. In this scenario, we will use the VLOOKUP function to fetch the appropriate values based on the selection of ComboBox. When selection is changed, the VLOOKUP function will refresh the cell value. If a range of cells is using the VLOOKUP function, the whole range can be refreshed upon user interaction, therefore it can be used as a source to the dynamic chart.

In order to keep the demonstration simple to understand, we will create the `Workbook` from scratch and move forward step by step as outlined below.

1.  Create an empty [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook).
2.  Access the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) of the first [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) in the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook).
3.  Insert some data to the cells by creating a Named Range. This data will serve as a series to the dynamic chart.
4.  Create [ComboBox](https://apireference.aspose.com/net/cells/aspose.cells.drawing/combobox) based on the Named Range created in the previous step.
5.  Insert some more data to the cells that will serve as a source to the VLOOKUP function.
6.  Insert VLOOKUP function (with appropriate parameters) to a range of cells. This will range will serve as a source to the dynamic chart.
7.  Create [Chart](https://apireference.aspose.com/net/cells/aspose.cells.charts/chart) based on the range created in the previous step.
8.  Save the result on the disc.

