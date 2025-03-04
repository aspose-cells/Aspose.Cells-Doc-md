---  
title: Get Icon Sets, Data Bars or Color Scales Objects used in Conditional Formatting with Node.js via C++  
linktitle: Get Icon Sets, Data Bars or Color Scales Objects used in Conditional Formatting  
description: Learn how to use Aspose.Cells for Node.js via C++ to retrieve icon sets, data bars, and color scale objects in conditional formatting from spreadsheet files.  
keywords: Aspose.Cells, Conditional Formatting, Icon Set, Data Bar, Color Scale, Spreadsheet, Node.js via C++  
type: docs  
weight: 10  
url: /nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/  
---  

{{% alert color="primary" %}}  

Sometimes, you need to retrieve icon sets that are used in the conditional formatting of a cell or a range of cells and you want to create an image file based on it. You might require to read the data bars or color scales used in the conditional formatting. Aspose.Cells supports this feature.

{{% /alert %}}  

The following code sample shows how to read icon sets that are used for conditional formatting. With Aspose.Cells' simple API, the icon set's image data is saved as an image.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the workbook
const sheet = workbook.getWorksheets().get(0);

// Get the A1 cell
const cell = sheet.getCells().get("A1");

// Get the conditional formatting result object
const cfr = cell.getConditionalFormattingResult();

if (cfr && !cfr.isNull()) {
// Get the icon set
const icon = cfr.getConditionalFormattingIcon();

if (icon && !icon.isNull()) {
// Create the image file based on the icon's image data
require("fs").writeFileSync(path.join(dataDir, "imgIcon.out.jpg"), icon.getImageData());
}
}
```  
  