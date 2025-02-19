---
title: Find Cells with Specific Style using Node.js via C++
type: docs
weight: 190
url: /nodejs-cpp/find-cells-with-specific-style/
description: Learn how to find or search cells with a particular style applied through the Aspose.Cells for Node.js via C++ API.
keywords: Find cells with a particular style applied Node.js via C++, Search cells with a particular style applied Node.js via C++
---

{{% alert color="primary" %}}

Sometimes, you need to find cells with a particular style applied. You can use Aspose.Cells for Node.js via C++ to find all cells with a common style. Aspose.Cells provides the [**FindOptions.style**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#style) property which you can use to specify the style to search cells for.

{{% /alert %}}

The code in this example finds all cells that have the same style as that of cell A1. After the code has been executed, all the cells that have the same style as A1 contain the text "Found".

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TestBook.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Access the style of cell A1
const style = worksheet.getCells().get("A1").getStyle();

// Specify the style for searching
const options = new AsposeCells.FindOptions();
options.setStyle(style);

let nextCell = null;

do {
    // Find the cell that has a style of cell A1
    nextCell = worksheet.getCells().find(null, nextCell, options);
    if (nextCell === null) break;
    // Change the text of the cell
    nextCell.putValue("Found");

} while (true);

const outputPath = path.join(dataDir, "output.out.xlsx");
workbook.save(outputPath);
```
