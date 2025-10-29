---  
title: 用Node.js通过C++确定Shape是否为智能艺术形状  
linktitle: 确定形状是否为智能图形  
type: docs  
weight: 400  
url: /zh/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: 学习如何使用Aspose.Cells for Node.js via C++确定Excel中的形状是否为智能艺术形状。  
---  

## **可能的使用场景**  

智能艺术形状是Microsoft Excel中的特殊形状，允许你自动创建复杂的图表。你可以使用[**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--)属性判断形状是智能艺术形状还是普通形状。  

## **确定形状是否为智能图形**  

以下示例代码加载包含智能艺术形状的[示例Excel文件](55541792.xlsx)，如截图所示。然后它打印第一个形状的[**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--)属性值，请查看示例代码控制台输出。  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **控制台输出**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
