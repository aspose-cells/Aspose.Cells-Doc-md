---  
title: Font Settings with Node.js via C++  
linktitle: Font Settings  
description: Aspose.Cells is a Node.js library for working with spreadsheet files. It supports setting the font settings of cells, allowing users to customize the font style and properties of cells. This article will introduce how to use the Aspose.Cells library to set cell font settings.  
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties, Node.js via C++  
type: docs  
weight: 30  
url: /nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
The look and feel of a text can be controlled by changing font settings. The font settings may include the name, style, size, color and other effects of the fonts. Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.  
{{% /alert %}}  

## **Configuring Font Settings**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.  

Aspose.Cells provides the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class' [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle) and [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle) methods which are used to get and set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) class provides properties for configuring font settings.  

### **Setting Font Name**  

Developers can apply any font to text inside a cell by using the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#font) object's [name](https://reference.aspose.com/cells/nodejs-cpp/font/#name) property.  

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
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();

// Setting the font name to "Times New Roman"
style.getFont().setName("Times New Roman");

// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```  

### **Setting Font Style to Bold**  

Developers can make text bold by setting the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#font) object's [**isBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#isBold) property to **true**.   

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();

// Setting the font weight to bold
style.getFont().setIsBold(true);

// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save("out.xlsx");
```  

### **Setting Font Size**  

Set the font size with the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#font) object's [**size**](https://reference.aspose.com/cells/nodejs-cpp/font/#size) property.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();

// Setting the font size to 14
style.getFont().setSize(14);

// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save("out.xlsx");
```  

### **Setting Font Color**  

Use the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#font) object's [**color**](https://reference.aspose.com/cells/nodejs-cpp/font/#color) property to set the font color. Select any color from the Color enumeration (part of Node.js) and assign it to the [**color**](https://reference.aspose.com/cells/nodejs-cpp/font/#color) property.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();

// Setting the font color to blue
style.getFont().setColor(AsposeCells.Color.Blue);

// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save("out.xlsx");
```  

### **Setting Font Underline Type**  

Use the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#font) object's [**underline**](https://reference.aspose.com/cells/nodejs-cpp/font/#underline) property to underline text. Aspose.Cells offers various pre-defined font underline types in the [**fontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype) enumeration.  

|**Font Underline Types**|**Description**|  
| :- | :- |  
|Accounting|A single accounting underline|  
|Double|Double underline|  
|DoubleAccounting|Double accounting underline|  
|None|No underline|  
|Single|A single underline|  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputPath = path.join(dataDir, "out.xlsx");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)){
    require("fs").mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();

// Setting the font to be underlined
style.getFont().setUnderline(AsposeCells.FontUnderlineType.Single);

// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(outputPath);
```  

### **Setting Strikeout Effect**  

Apply strikeout by setting the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#font) object's [**isStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#isStrikeout) property to **true**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();

// Setting the strike out effect on the font
style.getFont().setIsStrikeout(true);

// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "out.xlsx"));
```  

### **Setting Subscript Effect**  

Apply subscript by setting the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#font) object's [**isSubScript**](https://reference.aspose.com/cells/nodejs-cpp/font/#isSubScript) property to **true**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();

// Setting subscript effect
style.getFont().setIsSubscript(true);

// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "out.xlsx"));
```  

### **Setting Superscript Effect on Font**  

Developers can apply the superscript effect on the font by setting the [**isSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#isSuperscript) property of the [**Style.Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#font) object to **true**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Obtaining the style of the cell
const style = cell.getStyle();

// Setting superscript effect
style.getFont().setIsSuperscript(true);

// Applying the style to the cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "out.xlsx"));
```  

## **Advance topics**  
- [Apply Superscript and Subscript Effects on Fonts](/cells/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Get a List of Fonts used in a Spreadsheet or Workbook](/cells/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  

  