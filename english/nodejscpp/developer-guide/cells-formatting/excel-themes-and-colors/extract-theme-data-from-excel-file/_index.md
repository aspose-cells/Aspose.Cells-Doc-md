---  
title: Extract Theme Data from Excel File with Node.js via C++  
linktitle: Extract Theme Data from Excel File  
description: Learn how to extract theme data from Excel files using Aspose.Cells for Node.js via C++. Obtain style and formatting information effectively.  
keywords: Aspose.Cells, Excel File, Theme Data, Style, Format, Node.js via C++  
type: docs  
weight: 120  
url: /nodejs-cpp/extract-theme-data-from-excel-file/  
---  
  
{{% alert color="primary" %}}  
  
Aspose.Cells allows the users to extract Theme related data from Excel file. For example, you can extract Theme Name applied to workbook and Theme Color applied to cell or borders of the cell, etc.  
  
You can apply Theme to your workbook using Microsoft Excel via Page Layout > Themes command.  
  
{{% /alert %}}  
  
## JavaScript code to extract theme data from Excel file  
  
The following sample code extracts the Theme name applied to the source workbook and then it extracts the Theme color applied to cell A1 and the Theme color applied to the bottom border of the cell.  
  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Extract theme name applied to this workbook
console.log(workbook.getTheme());

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const cell = worksheet.getCells().get("A1");

// Get the style object
const style = cell.getStyle();

if (style.getForegroundThemeColor() != null) {
    // Extract theme color applied to this cell if theme has foreground theme color defined
    console.log(style.getForegroundThemeColor().getColorType());
} else {
    console.log("Theme has not foreground color defined.");
}

// Extract theme color applied to the bottom border of the cell if theme has border color defined
const bot = style.getBorders().getBorder(AsposeCells.BorderType.BottomBorder);
if (bot.getThemeColor() != null) {
    console.log(bot.getThemeColor().getColorType());
} else {
    console.log("Theme has not Border color defined.");
}
```  
