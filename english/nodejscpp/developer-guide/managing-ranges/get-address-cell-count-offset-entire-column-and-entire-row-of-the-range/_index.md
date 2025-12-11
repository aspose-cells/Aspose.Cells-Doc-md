---
title: Get Address Cell Count Offset Entire Column and Entire Row of the Range with Node.js via C++
linktitle: Get Address Cell Count Offset Entire Column and Entire Row of the Range
type: docs
weight: 330
url: /nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells for Node.js via C++ provides the Range object which has various utility methods that facilitate the user in working with Excel ranges easily. This article illustrates the usage of the following methods or properties of the Range object.

- **Address**  
  Gets the address of the range.

- **Cell Count**  
  Gets the total cell count in the range.

- **Offset**  
  Gets the range by offset.

- **Entire Column**  
  Gets a Range object that represents the entire column (or columns) that contains the specified range.

- **Entire Row**  
  Gets a Range object that represents the entire row (or rows) that contains the specified range.

## **Get Address, Cell Count, Offset, Entire Column and Entire Row of the Range**
The following sample code explains the usage of the methods and properties as discussed above. Please see the console output of the code given below for reference.

## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Create range A1:B3.
console.log("Creating Range A1:B3\n");
let rng = ws.getCells().createRange("A1:B3");

// Print range address and cell count.
console.log("Range Address: " + rng.getAddress());
console.log("Range row Count: " + rng.getRowCount());
console.log("Range column Count: " + rng.getColumnCount());

// Formatting console output.
console.log("----------------------");
console.log("");

// Create range A1.
console.log("Creating Range A1\n");
rng = ws.getCells().createRange("A1");

// Print range offset, entire column and entire row.
console.log("Offset: " + rng.getOffset(2, 2).getAddress());
console.log("Entire Column: " + rng.getEntireColumn().getAddress());
console.log("Entire Row: " + rng.getEntireRow().getAddress());

// Formatting console output.
console.log("----------------------");
console.log("");
```

## **Console Output**
{{< highlight javascript >}}
Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
