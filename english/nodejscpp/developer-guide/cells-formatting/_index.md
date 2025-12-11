---  
title: Format cells with Node.js via C++  
description: Learn how to format and style cells in Aspose.Cells for Node.js via C++, including number formatting, date formatting, font styles, and other cell style options. Our guide will help you create attractive and professional‑looking spreadsheets.  
keywords: Aspose.Cells for Node.js via C++, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.  
linktitle: Format cells  
type: docs  
weight: 120  
url: /nodejs-cpp/cells-formatting/  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Introduction**  

{{% alert color="primary" %}}  

Aspose.Cells provides the [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) and [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) methods of the [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) class, used to get/set the formatting style of a cell. Aspose.Cells also provides a [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) class.  

{{% /alert %}}  

## **How to Format Cells using GetStyle and SetStyle Methods**  

Apply different kinds of formatting styles **to** cells to set background or foreground colors, borders, fonts, horizontal and vertical alignments, indentation level, text direction, rotation angle, and much more.  

### **How to Use the GetStyle and SetStyle Methods**  

If developers need to apply different formatting styles to different cells, then it's better to get the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) of the cell using the [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) method, specify the style attributes, and then apply the formatting using the [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) method. An example is given below to demonstrate this approach to apply various formatting **to** a cell.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```  

### **How to Use a Style Object to Format Different Cells**  

If developers need to apply the same formatting style to different cells, they can use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object. Please follow the steps below to use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object:  

1. Add a **Style** object by calling the [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--) method of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class.  
2. Access the newly added **Style** object.  
3. Set the desired properties/attributes of the **Style** object to apply the required formatting settings.  
4. Assign the configured **Style** object to the desired cells.  

This approach can greatly improve the efficiency of your applications and save memory too.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```  

### **How to Use Microsoft Excel 2007 Predefined Styles**  

If you need to apply predefined styles for Microsoft Excel 2007, use the Aspose.Cells API. The example below demonstrates how to apply a predefined style to a cell.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value into A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```  



## **How to Format Selected Characters in a Cell**  

Dealing with Font Settings explains how to format text in cells, but it only explains how to format all of the cell content. What if you want to format only selected characters?  

Aspose.Cells supports this feature too. This topic explains how to use it effectively.  

### **How to Format Selected Characters**  

Aspose.Cells provides a class, **Workbook**, that represents a Microsoft Excel file. The **Workbook** class contains the **getWorksheets()** collection that allows access to each worksheet in an Excel file. A worksheet is represented by the **Worksheet** class. The **Worksheet** class provides a **getCells()** collection. Each item in the **getCells()** collection represents an object of the **Cell** class.  

The **Cell** class provides the **characters(number, number)** method that takes the following parameters to select a range of characters inside a cell:  

- **Start Index** – the index of the character where the selection starts.  
- **Number of Characters** – the number of characters to select.  

The **characters(number, number)** method returns an instance of the **FontSetting** class that allows developers to format the characters in the same way as they would a cell, as shown below. In the output file, the word *Visit* will be formatted with the default font, while *Aspose!* is bold and blue.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```  

{{% alert color="primary" %}}  

If you are interested in formatting a portion of rich text in a cell, consider using the **Cell.getCharacters()** and **Cell.setCharacters(FontSetting[])** methods. The **Cell.getCharacters()** method is used to access the portions of the text, after which amendments can be made using the **Cell.setCharacters(FontSetting[])** method, whereas the **get** method returns an array of **FontSetting** objects that can be manipulated to set various properties such as font name, font color, boldness, etc., and the **set** method can be used to apply the changes.  

{{% /alert %}}  

## **How to Format Rows and Columns**  

Sometimes, developers need to apply the same formatting **to** rows or columns. Applying formatting on cells one by one often takes longer and is not an efficient solution.  
To address this issue, Aspose.Cells provides a simple, fast way discussed in detail in this article.  

### **Formatting Rows & Columns**  

Aspose.Cells provides a class, **Workbook**, that represents a Microsoft Excel file. The **Workbook** class contains a **getWorksheets()** collection that allows access to each worksheet in the Excel file. A worksheet is represented by the **Worksheet** class. The **Worksheet** class provides a **getCells()** collection. The **getCells()** collection provides a **getRows()** collection.  

### **How to Format a Row**  

Each item in the **getRows()** collection represents a **Row** object. The **Row** object offers the **applyStyle(Style, StyleFlag)** method used to set the row's formatting. To apply the same formatting to a row, use the **Style** object. The steps below show how to use it.  

1. Add a **Style** object to the **Workbook** class by calling its **createStyle()** method.  
2. Set the **Style** object's properties to apply formatting settings.  
3. Turn the relevant attributes **ON** for the **StyleFlag** object.  
4. Assign the configured **Style** object to the **Row** object.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```  

### **How to Format a Column**  

The **getCells()** collection also provides a **getColumns()** collection. Each item in the **getColumns()** collection represents a **Column** object. Similar to a **Row** object, the **Column** object also offers the **applyStyle(Style, StyleFlag)** method for formatting a column.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```  

## **Advanced topics**  
- [Alignment Settings](/cells/nodejs-cpp/cells-alignment-settings/)  
- [Border Settings](/cells/nodejs-cpp/cells-border-settings/)  
- [Set Conditional Formats of Excel and ODS files.](/cells/nodejs-cpp/conditional-formatting/)  
- [Excel Themes and Colors](/cells/nodejs-cpp/excel-themes-and-colors/)  
- [Fill Settings](/cells/nodejs-cpp/cells-fill-settings/)  
- [Font Settings](/cells/nodejs-cpp/cells-font-settings/)  
- [Format Worksheet Cells in a Workbook](/cells/nodejs-cpp/format-worksheet-cells-in-a-workbook/)  
- [Implement 1904 Date System](/cells/nodejs-cpp/implement-1904-date-system/)  
- [Merging and Unmerging Cells](/cells/nodejs-cpp/merging-and-unmerging-cells/)  
- [Number Settings](/cells/nodejs-cpp/cells-number-settings/)  
- [Get and Set Style for cells](/cells/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
