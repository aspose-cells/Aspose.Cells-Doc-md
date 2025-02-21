---
title: Get Max Column Index in Row and Max Row Index in Column with Node.js via C++
type: docs
weight: 600
url: /nodejs-cpp/get-max-index-in-row-and-column/
description: Learn how to Get Max Column Index in Row and Max Row Index in Column through the Aspose.Cells for Node.js via C++ API.
keywords: Get Max Column Index in Row Node.js via C++, Get Max Row Index in Column Node.js via C++, Get Max Data Column Index in Row Node.js via C++, Get Max Data Row Index in Column Node.js via C++.
---

## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of rows and columns. Aspose.Cells for Node.js via C++ offers this feature. To obtain the maximum column index on a row, you can obtain the [Row.LastCell](https://reference.aspose.com/cells/nodejs-cpp/row/#lastCell-) and [Row.LastDataCell](https://reference.aspose.com/cells/nodejs-cpp/row/#lastDataCell-) properties, and then use the [Cell.Column](https://reference.aspose.com/cells/nodejs-cpp/cell/#column-) property to obtain the maximum column index and maximum data column index. But in order to obtain the maximum row index and maximum row data index on a column, you need to create a range on the column, then traverse the range to find the last cell, and finally obtain the [Cell.Row](https://reference.aspose.com/cells/nodejs-cpp/cell/#row-) attribute on the cell.

Aspose.Cells for Node.js via C++ provides the following properties and methods to help you achieve your goals.
- [**Row.LastCell**](https://reference.aspose.com/cells/nodejs-cpp/row/#lastCell-)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/nodejs-cpp/row/#lastDataCell-)
- [**Cell.Column**](https://reference.aspose.com/cells/nodejs-cpp/cell/#column-)
- [**Cell.Row**](https://reference.aspose.com/cells/nodejs-cpp/cell/#row-)

## **Get Max Column Index in Row and Max Row Index in Column using Aspose.Cells for Node.js via C++**
This example shows how to:

1. Load the [sample file](sample.xlsx).
1. Get the row that needs to get the maximum column index and maximum data column index.
1. Get [Cell.Column](https://reference.aspose.com/cells/nodejs-cpp/cell/#column-) attribute on the cell.
1. Create a range based on column.
1. Get iterator and traverse range.
1. Get [Cell.Row](https://reference.aspose.com/cells/nodejs-cpp/cell/#row-) attribute on the cell.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

const workbook = new AsposeCells.Workbook(dataDir + "sample.xlsx");
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

const row = cells.checkRow(1);
if (row != null) {
    //get Maximum column index of Row which contains data or style.
    console.log("Max column index in row: " + row.getLastCell().getColumn());

    //get Maximum column index of Row which contains data.
    console.log("Max data column index in row: " + row.getLastDataCell().getColumn());
}

// create the range of column B
const columnRange = cells.createRange(1, 1, true);

const colIter = columnRange.getEnumerator();
let maxRow = 0;
let maxDataRow = 0;
while (colIter.moveNext()) {
    const currCell = colIter.getCurrent();
    if (currCell.getStringValue() !== "") {
        maxDataRow = currCell.getRow();
    }
    if (currCell.getStringValue() !== "" || currCell.hasCustomStyle()) {
        maxRow = currCell.getRow();
    }
}
//Maximum row index of Column which contains data or style.
console.log("Max row index in Column: " + maxRow);

//Maximum row index of Column which contains data.
console.log("Max data row index in Column: " + maxDataRow);
```
