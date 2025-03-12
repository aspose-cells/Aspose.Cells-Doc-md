---  
title: Managing Pictures with Node.js via C++  
linktitle: Managing Pictures  
type: docs  
weight: 10  
url: /nodejs-cpp/managing-pictures/  
description: Learn how to add and position pictures in spreadsheets using Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells allows developers to add pictures to spreadsheets at runtime. Moreover, the positioning of these pictures can be controlled at runtime, which is discussed in more detail in the coming sections.

This article explains how to add pictures and how to insert an image that shows the content of certain cells.

## **Adding Pictures**

Adding pictures to a spreadsheet is very easy. It only takes a few lines of code:  
Simply call the [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) method of the [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) object). The [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) method takes the following parameters:

- **Upper left row index**, the index of the upper left row.
- **Upper left column index**, the index of the upper left column.
- **Image file name**, the name of the image file, complete with path.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Positioning Pictures**

There are two possible ways to control the positioning of pictures using Aspose.Cells:

- Proportional positioning: define a position proportional to the row height and width.
- Absolute positioning: define the exact position on the page where the image will be inserted, for example, 40 pixels to the left and 20 pixels below the edge of the cell.

### **Proportional Positioning**

Developers can position the pictures proportional to row height and column width using the [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--) and [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--) properties of the [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/nodejs-cpp/drawing/picture) object. A [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/drawing/picture) object can be obtained from the [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) collection by passing its picture index. This example places an image in the F6 cell.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Absolute Positioning**

Developers can also position the pictures absolutely by using the [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--) and [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--) properties of the [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/drawing/picture) object. This example places an image in cell F6, 60 pixels from the left and 10 pixels from the top of the cell.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Inserting a Picture Based on Cell Reference**

Aspose.Cells lets you display the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell, or cell range, is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object.

Add a picture to the worksheet by calling the [**AddPicture**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-string-string-) method of the [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) object). Specify the cell range by using the [**Formula**](https://reference.aspose.com/cells/nodejs-cpp/drawing/picture/properties/formula) attribute of the [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/drawing/picture) object.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getPictures().addPicture(0, 3, 10, 6, null);

// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Advance topics**
- [Add Conditional Icons Set with the Cell Text](/cells/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Insert a Linked Picture from Web Address](/cells/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [Insert a Picture Based on Cell Reference](/cells/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Load a Web Image from a URL into an Excel Worksheet](/cells/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

