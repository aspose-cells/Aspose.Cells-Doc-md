---
title: Reading and Writing Query Table of Worksheet with Node.js via C++
linktitle: Reading and Writing Query Table of Worksheet
type: docs
weight: 40
url: /nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells provides Worksheet.QueryTables collection which returns the object of type QueryTable by index. It has the following two properties

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

These are both Boolean values. You can view them in Microsoft Excel via Data > Connections > Properties.

{{% /alert %}}

## Reading and Writing Query Table of Worksheet

The following sample code reads the first QueryTable of the first worksheet and then prints both of the QueryTable properties. Then it sets the QueryTable.preserveFormatting to true.

You can download the source Excel file used in this code and the output Excel file generated by the code from the following links.

- [Source Excel File](5115533.xlsx)
- [Output Excel File](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### Console Output

Here is the console output of the above sample code

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Retrieve query table result range

Aspose.Cells provides option to read the address i.e. result range of cells for a query table. Following code demonstrates this feature by reading the address of result range for a query table. Sample file can be downloaded [here](72417290.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
