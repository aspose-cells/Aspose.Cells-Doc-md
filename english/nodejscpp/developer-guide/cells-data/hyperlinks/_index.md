---
title: Insert Hyperlinks into Excel or OpenOffice with Node.js via C++
linktitle: Managing Hyperlinks
type: docs
weight: 45
url: /nodejs-cpp/insert-hyperlinks-to-excel/
description: How to insert hyperlinks into Excel file with Aspose.Cells library without MS Excel using Node.js via C++.
keywords: Insert Hyperlinks into Excel Node.js via C++, Add or Insert Hyperlinks Node.js via C++, Add or Insert link to a URL Node.js via C++, Add or Insert a Link to a Cell Node.js via C++, Add a Link to an External File Node.js via C++
---

{{% alert color="primary" %}} 

A hyperlink is used to create a link between two entities. Everybody is familiar with the use of hyperlinks, especially on websites.
Using Aspose.Cells, developers can create different kinds of hyperlinks in Microsoft Excel files. This topic discusses what types of hyperlinks are supported by Aspose.Cells and how they can be used in our Excel files.

{{% /alert %}} 
## **Adding Hyperlinks**
Aspose.Cells allows developers to add hyperlinks to Excel files either using the API or designer spreadsheets (spreadsheets where hyperlinks are created manually and Aspose.Cells is used to import them into other spreadsheets).

Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides different methods for adding different hyperlinks to Excel files.
## **Adding Link to a URL**
The [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class contains a [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/hyperlinks) collection. Each item in the [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/hyperlinks) collection represents a [Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink). Add hyperlinks to URLs by calling the [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) collection's [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/methods/add/index) method. The [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/methods/add/index) method takes the following parameters:

- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the URL address.

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
let workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
let worksheet = workbook.getWorksheets().get(0);

// Adding a hyperlink to a URL at "A1" cell
worksheet.getHyperlinks().add("A1", 1, 1, "http://www.aspose.com");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}} 

In the above example, a hyperlink is added to a URL in an empty cell, **A1**. In such cases, if a cell is empty then the URL address is also added to that empty cell as its value. If the cell is not empty and a hyperlink is added, the value of the cell looks like plain text. To make it look like a hyperlink, apply the appropriate formatting settings on that cell.

{{% /alert %}} 
## **Adding a Link to a Cell in the Same File**
It is possible to add hyperlinks to cells in the same Excel file by calling the [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) collection's [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/methods/add/index) method. The [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/methods/add/index) method works for both internal and external hyperlinks. One version of the overloaded method takes the following parameters:

- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target cell.

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
let workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
workbook.getWorksheets().add();

// Obtaining the reference of the first (default) worksheet
let worksheet = workbook.getWorksheets().get(0);

// Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in
// The same Excel file
worksheet.getHyperlinks().add("B3", 1, 1, "Sheet2!B9");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```
## **Adding a Link to an External File**
It is possible to add hyperlinks to external Excel files by calling the [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection) collection's [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/methods/add/index) method. The [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/methods/add/index) method takes the following parameters:

- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target, external Excel file.

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

// Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
// The same Excel file
worksheet.getHyperlinks().add("A5", 1, 1, path.join(dataDir, "book1.xls"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Advance topics**
- [Add Image Hyperlinks](/cells/nodejs-cpp/add-image-hyperlinks/)
- [Detect Hyperlink Type](/cells/nodejs-cpp/detect-hyperlink-type/)
- [Editing Hyperlinks of Worksheet](/cells/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [Get Hyperlinks in Range](/cells/nodejs-cpp/get-hyperlinks-in-range/)

