---  
title: 使用 C++ 通过 Node.js 管理图片  
linktitle: 管理图片  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/managing-pictures/  
description: 学习如何使用Aspose.Cells for Node.js via C++在电子表格中添加和定位图片。  
---  

Aspose.Cells允许开发人员在运行时向电子表格添加图片。此外，可以在运行时控制这些图片的定位，更多细节将在接下来的章节中讨论。

本文说明了如何添加图片以及如何插入显示某些单元格内容的图片。

## **添加图片**

向电子表格中添加图片非常简单。只需几行代码：  
只需调用[**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-)方法（封装在[**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)对象中）即可。[**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-)方法接受以下参数：

- **左上角行索引**，左上角行的索引。
- **左上角列索引**，左上角列的索引。
- **图像文件名**，图像文件的名称，包括完整路径。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

## **定位图片**

使用Aspose.Cells控制图片定位有两种可能的方法：

- 比例定位：定义相对于行高和列宽的位置。
- 绝对定位：定义图像插入页面的确切位置，例如距离单元格边缘左侧40像素，下面20像素。

### **比例定位**

开发者可以使用[**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--)和[**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--)属性通过[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)对象将图片按比例定位到行高和列宽。通过传递其图片索引，您可以从[**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)集合中获取[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)对象。此示例在F6单元格放置一张图片。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

### **绝对定位**

开发者也可以使用[**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--)和[**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--)属性通过[**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)对象绝对定位图片。此示例在F6单元格放置一张图片，距离左侧60像素，距离顶部10像素。

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

## **基于单元格引用插入图片**

Aspose.Cells允许您在图像形状中显示工作表单元格的内容。您可以将图片链接到包含您要显示数据的单元格。由于单元格或单元格范围与图形对象链接，因此您对该单元格或单元格范围中的数据所做的更改将自动显示在图形对象中。

通过调用[**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)方法（封装在[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)对象中）并指定[**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--)属性的单元格范围，将图片添加到工作表。

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

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **高级主题**
- [使用单元格文本添加条件图标集](/cells/zh/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [从网址插入链接图片](/cells/zh/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [基于单元格引用插入图片](/cells/zh/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [从URL中加载Web图像到Excel工作表](/cells/zh/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

