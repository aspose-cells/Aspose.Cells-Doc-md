---
title: Using LightCells API
type: docs
weight: 80
url: /java/using-lightcells-api/
---

{{% alert color="primary" %}}

Sometimes you need to read and write large Microsoft Excel files with huge list of data or contents in the worksheet. The LightCells API is useful for creating huge Excel spreadsheets: with it, you need memory and get better performance and efficiency.

{{% /alert %}}

## **Event Driven Architecture**

Aspose.Cells provides the LightCells API, mainly designed to manipulate cell data one by one without building a complete data model block (using the Cell collection etc.) into memory. It works in an event-driven mode.

To save workbooks, provide the cell content cell by cell when saving, and the component saves it to the output file directly.

When reading template files, the component parses every cell and provides their value one by one.

In both procedures, one Cell object is processed and then discarded, the Workbook object does not hold the collection. In this mode, therefore, memory is saved when importing and exporting Microsoft Excel file that has a large data set which would otherwise use a lot of memory.

Even though the LightCells API processes the cells in the same way for XLSX and XLS files (it does not actually load all cells in memory but processes one cell and then discards it), it saves memory more effectively for XLSX files than XLS files because of the different data models and structures of the two formats.

However, **for XLS files**, to save more memory, developers can specify a temporary location for saving temporary data generated during the Save process. Commonly, **using LightCells API to save XLSX file may save 50% or more memory** than using the common way, **saving XLS may save about 20-40% memory**.

### **Writing Large Excel Files**

Aspose.Cells provides an interface, LightCellsDataProvider, that needs to be implemented in your program. The interface represents Data provider for saving large spreadsheet files in light-weight mode.

When saving a workbook by this mode, startSheet(int) is checked when saving every worksheet in the workbook. For one sheet, if startSheet(int) is true, then all the data and properties of rows and cells of this sheet to be saved is provided by this implementation. In the first place, nextRow() is called to get the next row index to be saved. If a valid row index is returned (the row index must be in ascending order for the rows to be saved), then a Row object representing this row is provided for implementation to set its properties by startRow(Row).

For one row, nextCell() is checked first. If a valid column index is returned (the column index must be in ascending order for all cells of one row to be saved), then a Cell object representing this cell is provided to set the data and properties by startCell(Cell). After the data of this cell is set, this cell is saved directly to the generated spreadsheet file and the next cell will be checked and processed.

The following example shows ho the LightCells API works.

The following program creates a huge file with 100,000 records in a worksheet, filled with data. We have added some hyperlinks, string values, numeric values and also formulas to certain cells in the worksheet. Moreover, we have formatted a range of cells as well.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **Reading Large Excel Files**

Aspose.Cells provide an interface, LightCellsDataHandler, that needs to be implemented in your program. The interface represents the data provider for reading large spreadsheet files in a light-weight mode.

When reading a workbook in this mode, startSheet() is checked when reading every worksheet in the workbook. For a sheet, if startSheet() returns true, then all the data and properties of the cells in the sheet's rows and columns is checked and processed. For every row, startRow() is called to check whether it needs to be processed. If a row needs to be processed, the row's properties are read first and developers can access its properties with processRow().

If the row's cells also need to be processed, then processRow() returns true and startCell() is called for every existing cell in the row to check whether it needs to be processed. If it does, processCell() is called.

The following sample code illustrates this process. The program reads a large file with millions of records. It takes a little time to read each sheet in the workbook. The sample code reads the file and retrieves the total number of cells, strings count and formulas count for each worksheet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

A class that implements LightCellsDataHandler interface

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
