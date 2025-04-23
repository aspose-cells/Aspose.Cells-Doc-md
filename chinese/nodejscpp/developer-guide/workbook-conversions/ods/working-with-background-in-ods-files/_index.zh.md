---  
title: 在Node.js via C++中处理ODS文件的背景  
linktitle: 在ODS文件中使用背景  
type: docs  
weight: 150  
url: /zh/nodejs-cpp/working-with-background-in-ods-files/  
description: 学习如何使用Aspose.Cells for Node.js via C++管理ODS文件中的背景。  
---  

## **ODS文件中的背景**  

可以将背景添加到ODS文件中的工作表。背景可以是彩色背景或图形背景。在打开文件时背景不可见，但如果文件作为PDF打印，则在生成的PDF中可以看到背景。在打印预览对话框中也可以看到背景。  

Aspose.Cells for Node.js via C++提供读取背景信息和添加背景到ODS文件的功能。  

## **从ODS文件读取背景信息**  

Aspose.Cells for Node.js via C++提供 [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) 类管理ODS文件的背景。以下代码示例演示如何使用 [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) 类加载[源ODS](90112030.ods) 文件并读取背景信息。请参考代码生成的控制台输出。  

### **示例代码**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "GraphicBackground.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const background = worksheet.getPageSetup().getODSPageBackground();

console.log("Background Type: " + background.getType().toString());
console.log("Background Position: " + background.getGraphicPositionType().toString());

// Save background image
const imagePath = outputDir + "background.jpg";
fs.writeFileSync(imagePath, Buffer.from(background.getGraphicData()));
```  

### **控制台输出**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **向ODS文件添加彩色背景**  

Aspose.Cells for Node.js via C++提供 [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) 类管理ODS文件的背景。以下示例演示如何使用 [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--) 属性向ODS文件添加颜色背景。请参考由代码生成的[输出ODS](90112031.ods) 文件。  

### **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setColor(AsposeCells.Color.Azure);
background.setType(AsposeCells.OdsPageBackgroundType.Color);

workbook.save(outputDir + "ColoredBackground.ods", AsposeCells.SaveFormat.Ods);
```  

## **向ODS文件添加图形背景**  

Aspose.Cells for Node.js via C++提供 [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) 类管理ODS文件的背景。以下示例演示如何使用 [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--) 属性为ODS文件添加图形背景。请参考由代码生成的[输出ODS](90112030.ods) 文件。  

### **示例代码**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setType(AsposeCells.OdsPageBackgroundType.Graphic);
background.setGraphicData(fs.readFileSync(path.join(sourceDir, "background.jpg")));
background.setGraphicType(AsposeCells.OdsPageBackgroundGraphicType.Area);

workbook.save(outputDir + "GraphicBackground.ods", AsposeCells.SaveFormat.Ods);
```  

