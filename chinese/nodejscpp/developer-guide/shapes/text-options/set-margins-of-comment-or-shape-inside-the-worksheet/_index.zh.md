---  
title: 在工作表内使用Node.js通过C++设置评论或形状的边距  
linktitle: 在工作表内设置评论或形状的边距  
type: docs  
weight: 1500  
url: /zh/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: 学习如何使用Aspose.Cells for Node.js via C++设置Excel工作表内评论或形状的边距。  
---  

## **可能的使用场景**  

Aspose.Cells允许你使用[**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/)属性设置任何形状或评论的边距，该属性返回[**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment)类的对象，具有不同的属性（如[**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--)、[**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--)、[**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--)、[**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--)等）可用于设置上下左右边距。  

## **设置工作表内批注或形状的边距**  

请参阅以下示例代码。它加载包含两个形状的[示例Excel文件](61767851.xlsx)。代码逐个访问形状，并设置它们的顶部、左侧、底部和右侧边距。请参阅由代码生成的[输出Excel文件](61767852.xlsx)以及显示代码对输出Excel文件的影响的屏幕截图。  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

const shapes = ws.getShapes();
for (let i = 0; i < shapes.getCount(); i++) {
const sh = shapes.get(i);
// Access the text alignment
const txtAlign = sh.getTextBody().getTextAlignment();

// Set auto margin false
txtAlign.setIsAutoMargin(false);

// Set the top, left, bottom and right margins
txtAlign.setTopMarginPt(10);
txtAlign.setLeftMarginPt(10);
txtAlign.setBottomMarginPt(10);
txtAlign.setRightMarginPt(10);
}

// Save the output Excel file
workbook.save("outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
