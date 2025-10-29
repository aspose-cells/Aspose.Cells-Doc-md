---  
title: 用Node.js通过C++替换智能艺术中的文本  
linktitle: 替换智能图中的文本  
type: docs  
weight: 1200  
url: /zh/nodejs-cpp/replace-text-in-smart-art/  
description: 学习如何使用Aspose.Cells for Node.js via C++替换智能艺术中的文本。  
---  

## **可能的使用场景**  

智能艺术是工作簿中的主要对象之一。经常需要更新智能艺术中的文本。Aspose.Cells for Node.js via C++通过设置[**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--)属性提供此功能。  

可以从以下链接下载示例源文件：  

[SmartArt.xlsx](77496338.xlsx)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SmartArt.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(sourceFilePath);

const worksheets = wb.getWorksheets();
for (let i = 0; i < worksheets.getCount(); i++) 
{
const worksheet = worksheets.get(i);
const shapes = worksheet.getShapes();
for (let j = 0; j < shapes.getCount(); j++) 
{
const shape = shapes.get(j);
shape.setAlternativeText("ReplacedAlternativeText"); // This works fine just as the normal Shape objects do.
if (shape.isSmartArt()) 
{
const smartArtShapes = shape.getResultOfSmartArt().getGroupedShapes();
for (let k = 0; k < smartArtShapes.length; k++) 
{
const smartart = smartArtShapes[k];
smartart.setText("ReplacedText"); // This doesn't update the text in Workbook which I save to the another file.
}
}
}
}

const options = new AsposeCells.OoxmlSaveOptions();
options.setUpdateSmartArt(true);
const outputFilePath = path.join(dataDir, "outputSmartArt.xlsx");
wb.save(outputFilePath, options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
