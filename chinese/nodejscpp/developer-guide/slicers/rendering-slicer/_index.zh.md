---  
title: 使用Node.js通过C++渲染切片器  
linktitle: 渲染切片器  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/rendering-slicer/  
---  

## **可能的使用场景**  
Aspose.Cells for Node.js via C++支持切片器形状的渲染。如果将工作表转换为图片或保存为PDF或HTML格式，您将看到切片器被正确渲染。  

## **呈现切片器**  
以下示例代码加载了包含一个现有切片器的[示例Excel文件](67338479.xlsx)。它通过设置仅覆盖切片器的打印区域，将工作表转换为图片。生成的图片即为[输出图片](67338480.png)，显示了已渲染的切片器。如您所见，切片器已被正确渲染，并与示例Excel文件中的效果一致。  

![todo:image_alt_text](rendering-slicer_1)  
## **示例代码**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  

