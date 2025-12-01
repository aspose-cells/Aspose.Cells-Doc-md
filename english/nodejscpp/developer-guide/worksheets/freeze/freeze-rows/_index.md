---
title: Freeze Top Row(s) of Excel Worksheet with Node.js via C++
linktitle: Freeze Rows
type: docs
weight: 190
url: /nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: In this article, you will learn how to freeze top rows of Excel Worksheets programmatically using Node.js Library with C++ API.
keywords: Freeze top rows, Freeze top row Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to freeze top row(s). When you have a huge amount of data under a common heading you are unable to see the heading when scrolled down the worksheet. You can freeze top row(s) so that you can see that frozen portion even when the rest of the data is being scrolled. You can easily see headers in the top rows.

## **Freeze Rows In Excel**

**![Freeze top row(s) in Excel](Freeze-Rows.png)**

1. If you want to freeze top row(s), then first select the row under the row that needs to be frozen.
2. Click View > Freeze Panes.
3. On the drop-down menu, click Freeze Top Row.
4. If you scroll down, the first row is always in the top view.

**![Frozen row](Frozen-Row.png)**

As you can see, the 1st Row is frozen; the first row always stays at the top of the view when you scroll down.

Freeze Rows let you view your large data without keeping track of the Row label.

## **Freeze Rows with Aspose.Cells for Node.js via C++**
It's simple to freeze row(s) with Aspose.Cells for Node.js via C++. 
Please use the [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) method to freeze row(s) at the selected row.
1. Construct Workbook to open the file or create an empty file.
2. Freeze the first row with Worksheet.freezePanes() method.
3. Save the file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

Attached [sample source Excel file](../Freeze.xlsx).
{{< app/cells/assistant language="nodejs-cpp" >}}
