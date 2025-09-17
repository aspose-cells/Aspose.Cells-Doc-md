##Create Dynamic Charts
Learn how to create dynamic charts in Aspose.Cells for Python via .NET. Our guide will show you how to dynamically update chart data, series, and formatting based on your requirements, allowing you to present changing data visually in your worksheets.
Dynamic (or interactive) charts have the ability to change when you change the scope of data. In other words, the dynamic charts can automatically reflect changes when the data source is changed. In order to trigger the change in the data source, one can use the filtering option of Excel Tables or use a control such as ComboBox or Dropdown list.
This article demonstrates the usage of Aspose.Cells for Python via .NET APIs to create dynamic charts using both of the aforementioned approaches.
## **Using Excel Tables**
Excel tables are referred to as ListObjects in Aspose.Cells' perspective, therefore, we will use the term "ListObject" instead of "Table" for clarity. Please read in detail on how to [create ListObjects](https://docs.aspose.com/cells/python-net/create-and-format-table/) with Aspose.Cells for Python via .NET API.
ListObjects provides the in-built functionality to sort & filter the data upon user interaction. Both sorting & filtering options are provided through the drop-down lists which are automatically added to the header row of the . Due to these features (sorting & filtering), the [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) seems to be the perfect candidate to serve as the data source to a dynamic chart because when sorting or filtering is changed, the representation of data in the chart will be changed to reflect the current state of the .
In order to keep the demonstration simple to understand, we will create the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) from scratch and move forward step by step as outlined below.
1. Create an empty [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Access the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) of the first [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) in the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Insert some data to the cells.
1. Create [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) based on the inserted data.
1. Create [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) based on the data range of [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject).
1. Save the result on the disc.
## **Using Dynamic Formulas**
In case you do not wish to use the [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) as a data source to the dynamic chart, the other option is to use Excel functions (or formulas) to create a dynamic range of data, and a control (such as ComboBox) to trigger the change in data. In this scenario, we will use the VLOOKUP function to fetch the appropriate values based on the selection of ComboBox. When selection is changed, the VLOOKUP function will refresh the cell value. If a range of cells is using the VLOOKUP function, the whole range can be refreshed upon user interaction, therefore it can be used as a source to the dynamic chart.
In order to keep the demonstration simple to understand, we will create the Workbook from scratch and move forward step by step as outlined below.
1. Create an empty [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Access the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) of the first [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) in the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Insert some data to the cells by creating a Named Range. This data will serve as a series to the dynamic chart.
1. Create [**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) based on the Named Range created in the previous step.
1. Insert some more data to the cells that will serve as a source to the VLOOKUP function.
1. Insert VLOOKUP function (with appropriate parameters) to a range of cells. This will range will serve as a source to the dynamic chart.
1. Create [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) based on the range created in the previous step.
1. Save the result on the disc.
