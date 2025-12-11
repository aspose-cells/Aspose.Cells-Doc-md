---  
title: Freeze First Column(s) of Excel Worksheet with Node.js via C++  
linktitle: Freeze Columns  
type: docs  
weight: 190  
url: /nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: Learn how to freeze left columns of Excel worksheets programmatically using Aspose.Cells for Node.js via C++.  
keywords: Freeze left columns, Freeze first columns, Lock the column(s)  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Introduction**  

In this article, we will learn how to freeze the left column(s). When you have a huge amount of data in a row, you may be unable to see the left columns while scrolling horizontally across the worksheet. You can freeze and lock the first column(s) so that you can see the frozen portion even when the rest of the data is scrolled. This makes it easy to see headers in the left columns.  

## **Freeze Columns In Excel**  

**![Freeze left column(s) in Excel](freeze-columns.png)**  

1. If you want to freeze left column(s), first select the column to the right of the column(s) that need to be frozen.  
2. Click **View > Freeze Panes**.  
3. In the drop‑down menu, click **Freeze First Column**.  
4. When you scroll horizontally, the first column remains in view.  

**![Frozen column](frozen-columns.png)**  

As you can see, the first column is frozen, and it stays locked on the left side of the view when you scroll horizontally.  

Freeze columns let you view long data without the hassle of keeping track of the first column.  

## **Freeze Columns with Aspose.Cells for Node.js via C++**  
It’s simple to freeze the first column(s) with Aspose.Cells for Node.js via C++.  
Please use the **[Worksheet.freezePanes(number, number, number, number)](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)** method to freeze column(s) at the selected position.  
1. Construct a **Workbook** to open an existing file or create a new workbook.  
2. Freeze the first column with the **Worksheet.freezePanes()** method.  
3. Save the file.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freeze panes at the second column (B1)
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Save the file
workbook.save("frozen.xlsx");
```  

Attached is a [sample source Excel file](Freeze.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
