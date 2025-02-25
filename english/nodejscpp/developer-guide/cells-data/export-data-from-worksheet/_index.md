---
title: Export Data from Worksheet in Node.js via C++
linktitle: Export Data from Worksheet
type: docs
weight: 180
url: /nodejs-cpp/export-data-from-worksheet/
description: This article explains how to export or import data from a worksheet into a DataTable using Node.js.
keywords: Node.js Export Data from Worksheet, Node.js Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non-Strongly Typed Data, Node.js Export Range with flag to skip column name, Node.js How to Export Range with Header.
---

## Overview

This article explains how to export your Worksheet data to DataTable using Node.js. It covers the following topics:

_Format_: **Excel**
- [Node.js Excel to DataTable](#nodejs-excel-to-datatable)
- [Node.js Convert Excel to DataTable](#nodejs-convert-excel-to-datatable)
- [Node.js Import Excel to DataTable](#nodejs-import-excel-to-datatable)
- [Node.js Export to DataTable from Excel](#nodejs-export-to-datatable-from-excel)

_Format_: **XLS**
- [Node.js XLS to DataTable](#nodejs-xls-to-datatable)
- [Node.js Convert XLS to DataTable](#nodejs-convert-xls-to-datatable)
- [Node.js Import XLS to DataTable](#nodejs-import-xls-to-datatable)
- [Node.js Export to DataTable from XLS](#nodejs-export-to-datatable-from-xls)

_Format_: **XLSX**
- [Node.js XLSX to DataTable](#nodejs-xlsx-to-datatable)
- [Node.js Convert XLSX to DataTable](#nodejs-convert-xlsx-to-datatable)
- [Node.js Import XLSX to DataTable](#nodejs-import-xlsx-to-datatable)
- [Node.js Export to DataTable from XLSX](#nodejs-export-to-datatable-from-xlsx)

_Format_: **ODS**
- [Node.js ODS to DataTable](#nodejs-ods-to-datatable)
- [Node.js Convert ODS to DataTable](#nodejs-convert-ods-to-datatable)
- [Node.js Import ODS to DataTable](#nodejs-import-ods-to-datatable)
- [Node.js Export to DataTable from ODS](#nodejs-export-to-datatable-from-ods)

## **How to Export Excel Data Using Node.js**

{{% alert color="primary" %}}

This article discusses some data export techniques that developers have access to through Aspose.Cells.

{{% /alert %}}

## **How to Export Data from Worksheet**

Aspose.Cells not only facilitates its users to import data to worksheets from external data sources but also allows them to export their worksheet data to a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8). As we know that [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) is a part of ADO.NET and is used to hold data. Once the data is stored in a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8), it can be used in any way according to the requirements of users. Developers can also store this data (stored in [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)) directly to a database if they wish. So, we can see that it becomes easier for the developers to manipulate worksheet data if it is exported to a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **How to Export Data to DataTable Using Aspose.Cells**

Developers can easily export their worksheet data to a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) object by calling either [**exportDataTable**](https://reference.aspose.com/cells/nodejs-cpp/cells/#exportDataTable-number-number-number-number-boolean-) or [**exportDataTableAsString**](https://reference.aspose.com/cells/nodejs-cpp/cells/#exportDataTableAsString-number-number-number-number-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class. Both methods are used in different scenarios, which are discussed below in more detail.

## **Columns Containing Strongly Typed Data**

We know that a spreadsheet stores data as a sequence of rows and columns. If all values in the columns of a worksheet are strongly typed (that means all values in a column must have the same data type) then we can export the worksheet content by calling the [**exportDataTable**](https://reference.aspose.com/cells/nodejs-cpp/cells/#exportDataTable-number-number-number-number-boolean-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class. [**exportDataTable**](https://reference.aspose.com/cells/nodejs-cpp/cells/#exportDataTable-number-number-number-number-boolean-) method takes the following parameters to export worksheet data as [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) object:

- **Row number**, the row number of the first cell data will be exported from.
- **Column number**, the column number of the first cell the data will be exported from.
- **Number of rows**, the number of rows to export.
- **Number of columns**, the number of columns to export.
- **Export column names**, a Boolean property that indicates whether the data in the first row of the worksheet should be exported as column names of the [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) or not.

_Steps: Exporting Data to DataTable_

- <a name="nodejs-excel-to-datatable" id="nodejs-excel-to-datatable"><strong><em>Steps:</em> Excel to DataTable in Node.js</strong></a>
  - <a name="nodejs-xls-to-datatable" id="nodejs-xls-to-datatable"><strong><em>Steps:</em> XLS to DataTable in Node.js</strong></a>
  - <a name="nodejs-xlsx-to-datatable" id="nodejs-xlsx-to-datatable"><strong><em>Steps:</em> XLSX to DataTable in Node.js</strong></a>
  - <a name="nodejs-ods-to-datatable" id="nodejs-ods-to-datatable"><strong><em>Steps:</em> ODS to DataTable in Node.js</strong></a>
- <a name="nodejs-convert-excel-to-datatable" id="nodejs-convert-excel-to-datatable"><strong><em>Steps:</em> Convert Excel to DataTable in Node.js</strong></a>
  - <a name="nodejs-convert-xls-to-datatable" id="nodejs-convert-xls-to-datatable"><strong><em>Steps:</em> Convert XLS to DataTable in Node.js</strong></a>
  - <a name="nodejs-convert-xlsx-to-datatable" id="nodejs-convert-xlsx-to-datatable"><strong><em>Steps:</em> Convert XLSX to DataTable in Node.js</strong></a>
  - <a name="nodejs-convert-ods-to-datatable" id="nodejs-convert-ods-to-datatable"><strong><em>Steps:</em> Convert ODS to DataTable in Node.js</strong></a>
- <a name="nodejs-import-excel-to-datatable" id="nodejs-import-excel-to-datatable"><strong><em>Steps:</em> Import Excel to DataTable in Node.js</strong></a>
  - <a name="nodejs-import-xls-to-datatable" id="nodejs-import-xls-to-datatable"><strong><em>Steps:</em> Import XLS to DataTable in Node.js</strong></a>
  - <a name="nodejs-import-xlsx-to-datatable" id="nodejs-import-xlsx-to-datatable"><strong><em>Steps:</em> Import XLSX to DataTable in Node.js</strong></a>
  - <a name="nodejs-import-ods-to-datatable" id="nodejs-import-ods-to-datatable"><strong><em>Steps:</em> Import ODS to DataTable in Node.js</strong></a>
- <a name="nodejs-export-to-datatable-from-excel" id="nodejs-export-to-datatable-from-excel"><strong><em>Steps:</em> Export to DataTable from Excel in Node.js</strong></a>
  - <a name="nodejs-export-to-datatable-from-xls" id="nodejs-export-to-datatable-from-xls"><strong><em>Steps:</em> Export to DataTable from XLS in Node.js</strong></a>
  - <a name="nodejs-export-to-datatable-from-xlsx" id="nodejs-export-to-datatable-from-xlsx"><strong><em>Steps:</em> Export to DataTable from XLSX in Node.js</strong></a>
  - <a name="nodejs-export-to-datatable-from-ods" id="nodejs-export-to-datatable-from-ods"><strong><em>Steps:</em> Export to DataTable from ODS in Node.js</strong></a>

_Code Steps:_

1. Load your Excel file in [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) object.
   - [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) object can load Excel file formats e.g. XLS, XLSX, XLSM, ODS etc.
2. Access the first [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) in the Excel file.
3. Choose your export area e.g. 7 rows and 2 columns starting from 1st cell of **DataTable**.
4. Use [exportDataTable](https://reference.aspose.com/cells/nodejs-cpp/cells/exportdatatable/#number-number-number-number-boolean-) method to export the data into DataTable.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Exporting the contents of 7 rows and 2 columns starting from 1st cell to DataTable
const dataTable = worksheet.getCells().exportArray(0, 0, 11, 2);

// Iterating through the DataTable rows and columns to log the values
dataTable.forEach(row => {
    row.forEach(value => {
        process.stdout.write(value + "    ");
    });
    console.log();
});
```

## **Columns Containing Non-Strongly Typed Data**

If all values in the columns of a worksheet are not strongly typed (that means the values in a column may have different data types) then we can export the worksheet content by calling the [**exportDataTableAsString**](https://reference.aspose.com/cells/nodejs-cpp/cells/#exportDataTableAsString-number-number-number-number-) method of the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) class. [**exportDataTableAsString**](https://reference.aspose.com/cells/nodejs-cpp/cells/#exportDataTableAsString-number-number-number-number-) method takes the same set of parameters as that of the [**exportDataTable**](https://reference.aspose.com/cells/nodejs-cpp/cells/#exportDataTable-number-number-number-number-boolean-) method to export worksheet data as a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) object.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Exporting the contents of 7 rows and 2 columns starting from 1st cell to DataTable
const dataTable = worksheet.getCells().exportArray(0, 0, 11, 2);

// Iterating through the data table and printing the values
dataTable.forEach(row => {
    row.forEach(value => {
        process.stdout.write(value + "            ");
    });
    console.log();
});
```

## **How to Export Range with Header**

Data from a range can be exported to a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) where a flag is available to skip the header row in the exported data. Following code exports a range of data to a [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) with an argument [**ExportTableOptions**](https://reference.aspose.com/cells/nodejs-cpp/exporttableoptions) which contains [**ExportColumnName**](https://reference.aspose.com/cells/nodejs-cpp/exporttableoptions/#exportColumnName) flag. It is set to **true** if header information is there, hence it will not be included in data and set to **false** if no header is there and all rows are to be considered as data.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = RunExamples.getSourceDirectory();

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Names.xlsx"));

// Instantiating a WorkbookDesigner object
const designer = new AsposeCells.WorkbookDesigner(workbook);

// Accessing the range having name "Names"
const range = designer.getWorkbook().getWorksheets().getRangeByName("Names");

// Instantiating the ExportTableOptions object
const options = new AsposeCells.ExportTableOptions();

// Setting the ExportColumnName flag to true shows that first line is header and not part of data
options.setExportColumnName(true);

// Exporting data with the selected information
const dataTable = range.exportDataTable(options);
```

## **Advance topics**
- [Export Excel Data to DataTable without any Formatting](/cells/nodejs-cpp/export-excel-data-to-datatable-without-any-formatting/)
- [Export HTML String Value of the Cells to the DataTable](/cells/nodejs-cpp/export-html-string-value-of-the-cells-to-the-datatable/)
- [Export Visible Rows Data from Worksheet](/cells/nodejs-cpp/export-visible-rows-data-from-worksheet/)
- [Ignore Hidden Columns while Exporting Worksheet Data to Data Table](/cells/nodejs-cpp/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Rename duplicate columns automatically while exporting worksheet data](/cells/nodejs-cpp/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
