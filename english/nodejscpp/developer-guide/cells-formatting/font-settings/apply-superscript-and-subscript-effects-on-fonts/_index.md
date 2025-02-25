---
title: Apply Superscript and Subscript Effects on Fonts with Node.js via C++
linktitle: Apply Superscript and Subscript Effects on Fonts
type: docs
weight: 80
url: /nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/
description: The Node.js code to apply superscript and subscript effects to text in Excel using Aspose.Cells for Node.js via C++.
keywords: excel superscript node.js via c++, excel subscript node.js via c++, excel superscript and subscript node.js via c++, insert subscript and superscript in excel node.js via c++, add subscript and superscript in excel node.js via c++, add superscript and subscript excel node.js via c++, add superscript excel node.js via c++, add subscript excel node.js via c++
---

{{% alert color="primary" %}}

Aspose.Cells provides the functionality to apply superscript (text above the baseline) and subscript (text below the baseline) effects to text.

{{% /alert %}}

## **Working with Superscript and Subscript**

Apply the superscript effect by setting the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/font) object's [**isSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#isSuperscript) property to **true**. To apply subscript, set the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/font) object's [**isSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#isSubscript) property to **true**.

The following code examples show how to apply super and subscript to text.

### Node.js code to Apply Superscript effect on text

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello");

// Setting the font Superscript
const style = cell.getStyle();
style.getFont().setIsSuperscript(true);
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "Superscript.out.xls"), AsposeCells.SaveFormat.Auto);
```

### Node.js code to Apply Subscript effect on text

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require('fs');
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello");

// Setting the font Subscript
const style = cell.getStyle();
style.getFont().setIsSubscript(true);
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "Subscript.out.xls"), AsposeCells.SaveFormat.Auto);
```
