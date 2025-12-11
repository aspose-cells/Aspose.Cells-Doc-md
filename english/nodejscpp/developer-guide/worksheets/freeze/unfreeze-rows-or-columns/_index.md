---
title: Unfreeze Rows or Columns with Node.js via C++
linktitle: Unfreeze panes
type: docs
weight: 190
url: /nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In this article, you will learn how to unfreeze rows, columns, or panes of Excel worksheets programmatically using the Node.js API with C++.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unfreeze window Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In this article, we will learn how to unfreeze rows, columns, and panes. If worksheets in the Excel files are frozen, you may want to unfreeze the worksheet or adjust frozen rows, columns, or panes.

## **In Excel**

1. Click **View** tab → **Freeze Panes** → **Unfreeze Panes**.

**![unfreeze panes in Excel](Unfreeze-Panes.png)**

## **Unfreeze Rows, Columns or Panes with Aspose.Cells for Node.js via C++**

It’s simple to unfreeze panes with Aspose.Cells for Node.js via C++. Please use the [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--) method to unfreeze panes.

1. Construct a workbook to open the frozen file.
2. Unfreeze panes with the `Worksheet.unFreezePanes()` method.
3. Save the file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Attached is the sample source Excel file (**Frozen.xlsx**).
{{< app/cells/assistant language="nodejs-cpp" >}}
