---
title: Convert Excel to CSV, TSV and Txt with Node.js via C++
linktitle: Save as CSV, TSV and Txt
type: docs
weight: 40
url: /nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Learn how to convert Excel files to CSV, TSV, and TXT formats using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to convert Excel, ODS, JSON, and other format files to CSV, TSV, and TXT.

{{% /alert %}}

## **Saving Workbook to Text or CSV Format**

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default, both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into text format. Load the source workbook, which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS, and so on) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#separator-string-) is a comma, so do not specify a separator if saving to CSV format.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Saving Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **Advance topics**
- [Keep Separators for Blank Rows while exporting spreadsheets to CSV format](/cells/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format](/cells/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
