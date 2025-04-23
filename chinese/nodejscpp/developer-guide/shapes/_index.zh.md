---  
title: 通过Node.js通过C++插入Excel文件的图片和形状  
linktitle: 形状  
type: docs  
weight: 140  
url: /zh/nodejs-cpp/insert-shapes/  
description: 使用Aspose.Cells for Node.js via C++管理Excel文件中的图片、OLE对象和形状。  
---  

{{% alert color="primary" %}}  
有时你需要在工作表中插入一些必要的形状。你可能需要在不同位置插入相同的形状，或者批量插入多个形状。  
不用担心！[Aspose.Cells](https://products.aspose.com/cells/)支持所有这些操作。  
{{% /alert %}}  

Excel中的形状主要分为以下几类：  
- **图片**  
- **Ole对象**  
- **线条**  
- **矩形**  
- **基本形状**  
- **方块箭头**  
- **方程式形状**  
- **流程图**  
- **星星和横幅**  
- **标注**  

本指南将从每个类别中选择一两个形状作为示例。通过这些例子，你将学习如何使用[Aspose.Cells](https://products.aspose.com/cells/)将指定形状插入到工作表中。  

## **使用Node.js在Excel工作表中添加图片**  

向电子表格中添加图片非常简单。只需几行代码：  
只需调用[**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-)方法（封装在[**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)对象中）即可。[**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-)方法接受以下参数：  

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

## **使用Node.js在Excel工作表中插入OLE对象**  

Aspose.Cells支持在工作表中添加、提取和操作OLE对象。因此，Aspose.Cells具有[**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection)类，用于向集合列表中添加新的OLE对象。另一个类，[**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject)，表示OLE对象。它具有一些重要成员：  

- [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--)属性指定图像（图标）的字节数组数据。图像将显示在工作表中，用于展示OLE对象。  
- [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--)属性指定对象的数据，形式为字节数组。当双击OLE对象图标时，将在相关程序中显示这些数据。  

下面的示例演示了如何将一个或多个OLE对象添加到工作表中。  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **使用Node.js在Excel工作表中插入线条**  

线条的形状属于**线条**类别。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入线条的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“最近使用的形状”或“线条”中选择线条  

![](line.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入线条。  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
此方法返回一个[LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape)对象。  
{{% /alert %}}  

以下示例展示了如何在工作表中插入线条。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](line2.png)  

## **使用Node.js在Excel工作表中插入箭头线条**  

箭头线条的形状属于**线条**类别。它是线条的一种特殊情况。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入箭头线的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“最近使用的形状”或“线条”选择箭头线条  

![](line_arrow1.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入箭头线。  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
此方法返回一个[LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape)对象。  
{{% /alert %}}  

以下示例展示了如何在工作表中插入箭头线条。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](line_arrow2.png)  

## **在Excel工作表中插入矩形的Node.js示例**  

矩形的形状属于**矩形**类别。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入矩形的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“最近使用的形状”或“矩形”中选择矩形  

![](rectangle.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入矩形。  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
此方法返回一个[RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape)对象。  
{{% /alert %}}  

以下示例展示了如何在工作表中插入矩形。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](rectangle2.png)  

## **使用Node.js在Excel工作表中插入立方体**  

立方体的形状属于**基本形状**类别。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入立方体的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“基本形状”中选择立方体  

![](cube.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入立方体。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示了如何在工作表中插入立方体。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](cube2.png)  

## **在Excel工作表中插入提示文本箭头（呼出四边形）Node.js示例**  

呼出四边形箭头的形状属于**块箭头**类别。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入标注四箭头的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从“块箭头”中选择呼出四边形箭头  

![](callout_quad_arrow.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入标注四箭头  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入调用箭头。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](callout_quad_arrow2.png)  

## **使用 Node.js 在 Excel 工作表中插入乘号**  

乘号的形状属于 **方程式形状** 类别。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入乘法符号的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从 **方程式形状** 中选择乘号  

![](multiplication_sign.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入乘法符号  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入乘号。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](multiplication_sign2.png)  

## **使用 Node.js 在 Excel 工作表中插入多文档**  

多文档的形状属于 **流程图** 类别。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入多文档的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从 **流程图** 中选择多文档  

![](multidocument.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入多文档。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入多文档。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](multidocument2.png)  

## **使用 Node.js 在 Excel 工作表中插入五角星**  

五角星的形状属于 **星星和旗帜** 类别。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入五角星的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从 **星星与旗帜** 中选择五角星  

![](star_5_points.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入五角星  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入五角星。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](star_5_points2.png)  

## **使用 Node.js 在 Excel 工作表中插入思维云泡泡**  

思维云泡泡的形状属于 **注释** 类别。  

***在Microsoft Excel中(例如2007年)：***  

- 选择要插入思维气泡云的单元格  
- 点击“插入”菜单，然后点击“形状”  
- 然后，从 **注释** 中选择思维云泡泡  

![](thought_bubble_cloud.png)  

***使用Aspose.Cells***  

您可以使用以下方法在工作表中插入思维气泡云。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
该方法返回一个 [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) 对象。  
{{% /alert %}}  

以下示例展示如何向工作表插入思维云泡泡。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

执行上述代码，您将获得以下结果：  

![](thought_bubble_cloud2.png)  

## **高级主题**  
- [改变形状的调整值](/cells/zh/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [在工作表之间复制形状](/cells/zh/nodejs-cpp/copy-shapes-between-worksheets/)  
- [非原始形状中的数据](/cells/zh/nodejs-cpp/data-in-non-primitive-shape/)  
- [查找工作表内形状的绝对位置](/cells/zh/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [从形状获取连接点](/cells/zh/nodejs-cpp/get-connection-points-from-shape/)  
- [管理控件](/cells/zh/nodejs-cpp/managing-controls/)  
- [向工作表添加图标](/cells/zh/nodejs-cpp/insert-svg-to-excel/)  
- [管理OLE对象](/cells/zh/nodejs-cpp/managing-ole-objects/)  
- [管理图片](/cells/zh/nodejs-cpp/managing-pictures/)  
- [管理智能图形](/cells/zh/nodejs-cpp/managing-smartart/)  
- [管理文本框](/cells/zh/nodejs-cpp/managing-textbox-of-excel/)  
- [在工作表中添加艺术字水印](/cells/zh/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [刷新链接形状的值](/cells/zh/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [在工作表内发送形状到最前或最后](/cells/zh/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [管理形状选项](/cells/zh/nodejs-cpp/managing-shape-options/)  
- [管理形状文本选项](/cells/zh/nodejs-cpp/managing-shape-text-options/)  
- [Web扩展 - 办公室加载项](/cells/zh/nodejs-cpp/web-extensions-office-add-ins/)  


