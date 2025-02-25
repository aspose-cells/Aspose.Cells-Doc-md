---
title: Modify an Existing Style with Node.js via C++
linktitle: Modify an Existing Style
description: Aspose.Cells is a Node.js library for working with spreadsheet files that allows users to modify existing cell styles. This article will introduce how to modify an existing cell style with the Aspose.Cells library so that users can change the appearance of the cells as they need.
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /nodejs-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

To apply the same formatting options to cells, create a new formatting style object. A formatting style object is a combination of formatting characteristics, such as font, font size, indentation, number, border, patterns etc., named and stored as a set. When applied, all of the formatting in that style are applied.

You can also use an existing style, save it with the workbook and use to format information with the same attributes.

When cells aren't explicitly formatted, the **Normal** style (the workbook's default style) is applied. Microsoft Excel predefines several styles in addition to the Normal style including Comma, Currency, and Percent.

Aspose.Cells allows modifying any of these styles or any other style that you define with your desired attributes.

{{% /alert %}}

## **Using Microsoft Excel**

To update a style in Microsoft Excel 97-2003:

1. On the **Format** menu, click **Style**.
1. Select the style you want to modify from the **Style name** list.
1. Click **Modify**.
1. Select the style options that you want using the tabs in the Format Cells dialog.
1. Click **OK**.
1. Under **Style includes**, specify the style features you want.
1. Click **OK** to save the style and apply it to the selected range.

## **Using Aspose.Cells for Node.js via C++**

The following examples demonstrate how to use [**Style.update**](https://reference.aspose.com/cells/nodejs-cpp/style/#update) method.

### **Creating and Modifying a Style**

This example creates a [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object, applies it to a range of cells, and modifies the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object. The modifications are automatically applied to the cell and the range the style was applied to.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Create a new style object.
const style = workbook.createStyle();

// Set the number format.
style.setNumber(14);

// Set the font color to red color.
style.getFont().setColor(AsposeCells.Color.Red);

// Name the style.
style.setName("Date1");

// Get the first worksheet cells.
const cells = workbook.getWorksheets().get(0).getCells();

// Specify the style (described above) to A1 cell.
cells.get("A1").setStyle(style);

// Create a range (B1:D1).
const range = cells.createRange("B1", "D1");

// Initialize styleflag object.
const flag = new AsposeCells.StyleFlag();

// Set all formatting attributes on.
flag.setAll(true);

// Apply the style (described above) to the range.
range.applyStyle(style, flag);

// Modify the style (described above) and change the font color from red to black.
style.getFont().setColor(AsposeCells.Color.Black);

// Done! Since the named style (described above) has been set to a cell and range, 
// The change would be reflected(new modification is implemented) to cell(A1) and 
// Range (B1:D1).
style.update();

// Save the excel file. 
workbook.save(path.join(dataDir, "book_styles.out.xls"));
```

### **Modifying an Existing Style**

This example uses a simple template Excel file in which a style called Percent has already been applied to a range. The example:

1. gets the style,
1. creates a style object and
1. modifies the style formatting.

The modifications are automatically applied to the range the style was applied to.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");

// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);

// We get the Percent style and create a style object.
const style = workbook.getNamedStyle("Percent");

// Change the number format to "0.00%".
style.setNumber(11);

// Set the font color.
style.getFont().setColor(AsposeCells.Color.Red);

// Update the style. so, the style of range "A1:C8" will be changed too.
style.update();

// Save the excel file.	
workbook.save(path.join(dataDir, "book2.out.xlsx"));
```
