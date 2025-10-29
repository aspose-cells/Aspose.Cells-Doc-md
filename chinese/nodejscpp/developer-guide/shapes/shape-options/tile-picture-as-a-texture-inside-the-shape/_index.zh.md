---  
title: 在 Node.js 和 C++ 中用图像作为纹理平铺在形状内  
linktitle: 在形状内作为纹理平铺图片  
type: docs  
weight: 1700  
url: /zh/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: 学习如何用 Aspose.Cells for Node.js via C++ 将一张小图片作为纹理平铺在形状内  
---  

## **可能的使用场景**  

当图片较小且不覆盖整个形状表面而又不失真时，可以选择将其平铺。平铺会通过重复小图像来填充形状表面，就像它们是瓷砖一样。  

## **在形状内部将图片作为纹理平铺**  

你可以用一些图片填充形状表面，并用 [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) 属性平铺，设置为 **true**。请参考下面的示例代码、样例Excel文件（46465050.xlsx）和截图。  

## **屏幕截图**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
