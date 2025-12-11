---
title: How to add/insert TextBox to Worksheet with Node.js via C++
linktitle: Add Text Box to Worksheet
type: docs
weight: 10
url: /nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: How to add/insert TextBox to Worksheet in Aspose.Cells for Node.js via C++.
keywords: add/insert Text Box TextBox Worksheet Excel Aspose Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Add Text Box to Worksheet in Excel

In the Excel program (version 07 and above), there are two places where you can insert text boxes. One is in **Insert → Shapes**, and the other is on the right side of the top menu of the **Insert** tab.

### Method one:

![1](1.png)

### Method two:

![2](2.png)

## How to create

You can create text boxes with horizontal or vertical text.

- Select the corresponding option (horizontal or vertical).  
- Left‑click on the page.  
- Hold down the left mouse button and drag to the desired size.  
- Release the left mouse button.

Now you get a text box.

## Add Text Box to Worksheet in Aspose.Cells for Node.js via C++

When you need to bulk‑insert TextBox objects into a worksheet, the manual insertion method is clearly impractical. If this bothers you, this document will help. **Aspose.Cells** provides an API that makes bulk inserts easy in your code.

The following sample code creates a text box.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access the first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

You will get a file similar to the [result file](result.xlsx). In the file, you will see the following:

![](52449.png)

{{< app/cells/assistant language="nodejs-cpp" >}}
