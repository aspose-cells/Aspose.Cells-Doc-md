---
title: Find if the Worksheet is Dialog Sheet with Node.js via C++
linktitle: Find if the Worksheet is Dialog Sheet
type: docs
weight: 90
url: /nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: This article provides instructions and sample code for determining programmatically whether an Excel worksheet is a Dialog Sheet using Aspose.Cells for Node.js via C++.
keywords: find excel worksheet dialog type Node.js via C++, worksheet dialog Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

A Dialog Sheet is an old format of sheet that contains a dialog box. Such a sheet could be inserted by an older version of Microsoft Excel, e.g., 2003, as shown in this screenshot. It can also be inserted with VBA in newer versions, e.g., Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

You can find if the sheet is a dialog sheet or another type of sheet using the [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) property provided by Aspose.Cells for Node.js via C++. If it returns the enumeration value [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), then it means you are dealing with a dialog sheet.

## **Find if the Worksheet is Dialog Sheet**

The following sample code loads the sample Excel file (64716820.xlsx) that contains a dialog sheet. It checks the [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) property, compares it with [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), and then prints a message. Please see the console output of the sample code below for more details.

## **Sample Code**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
    console.log("Worksheet is a Dialog Sheet.");
}
```

## **Console Output**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
