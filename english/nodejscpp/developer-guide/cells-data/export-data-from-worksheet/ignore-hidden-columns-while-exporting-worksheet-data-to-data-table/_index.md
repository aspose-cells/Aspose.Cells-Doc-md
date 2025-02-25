---
title: Ignore Hidden Columns while Exporting Worksheet Data to Data Table with Node.js via C++
linktitle: Ignore Hidden Columns while Exporting Worksheet Data to Data Table
type: docs
weight: 330
url: /nodejs-cpp/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/
description: Learn how to ignore hidden columns while exporting worksheet data to a data table using Aspose.Cells for Node.js via C++.
keywords: Export Visible Columns Data to DataTable Node.js via C++, Export unhidden Columns Data to DataTable Node.js via C++, Export Columns Data to DataTable and Exclude hidden Columns Node.js via C++, Ignore Hidden Columns while Exporting Worksheet Data to Data Table Node.js via C++
---

{{% alert color="primary" %}}

Sometimes, you want to ignore hidden columns while exporting worksheet data to a data table. You can achieve it using Aspose.Cells for Node.js via C++ by setting the [**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/nodejs-cpp/exporttableoptions/#plotVisibleColumns-boolean-) to **true**. By default, its value is **false**, so you need to set it **true** to ignore the hidden columns.

{{% /alert %}}

The following sample code explains the usage of [**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/nodejs-cpp/exporttableoptions/#plotVisibleColumns-boolean-) property in ignoring the hidden columns while exporting the worksheet entire data to the data table.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(inputPath);

const worksheet = workbook.getWorksheets().get(0);

const opts = new AsposeCells.ExportTableOptions();
opts.setPlotVisibleColumns(true);

const totalRows = worksheet.getCells().getMaxRow() + 1;
const totalColumns = worksheet.getCells().getMaxColumn() + 1;

const dt = worksheet.getCells().exportDataTable(0, 0, totalRows, totalColumns, opts);
``` 
