---
title: Search and Replace Data in a Range with Node.js via C++
linktitle: Search and Replace Data in a Range
type: docs
weight: 170
url: /nodejs-cpp/search-and-replace-data-in-a-range/
description: This article shows how to search and replace data in a range in Excel using Node.js via C++ code.
keywords: node.js search and replace data in excel, node.js search data in excel, node.js search and replace data in a range, node.js search data in a range, node.js searching data in a range, node.js searching data in range, node.js searching data in excel, node.js search data in range, search and replace data in excel with node.js, search and replace data in a range with node.js, search and replace data in range with node.js
---

{{% alert color="primary" %}}

Sometimes you need to search for and replace specific data in a range ignoring any cell values outside the desired range. Aspose.Cells for Node.js via C++ allows you to limit a search to a specific range. This article explains how.

{{% /alert %}}

Aspose.Cells for Node.js via C++ provides the [**FindOptions.setRange()**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/methods/setRange) method for specifying a range when searching for data. Below code sample searches and replaces data in a range.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Specify the range where you want to search
// Here the range is E3:H6
const area = AsposeCells.CellArea.createCellArea("E9", "H15");

// Specify Find options
const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);
opts.setRange(area);

let cell = null;

do {
    // Search the cell with value search within range
    cell = worksheet.getCells().find("search", cell, opts);

    // If no such cell found, then break the loop
    if (cell === null) {
        break;
    }

    // Replace the cell with value replace
    cell.putValue("replace");

} while (true);

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
