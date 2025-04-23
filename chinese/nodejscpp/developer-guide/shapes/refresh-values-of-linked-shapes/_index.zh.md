---  
title: 使用Node.js通过C++刷新关联形状的数值  
linktitle: 刷新链接形状的值  
type: docs  
weight: 3200  
url: /zh/nodejs-cpp/refresh-values-of-linked-shapes/  
description: 学习如何使用Aspose.Cells for Node.js via C++在Excel中刷新关联形状的数值。  
---  

{{% alert color="primary" %}}  

有时，你的Excel文件中有与某个单元格关联的形状。Microsoft Excel中，改变关联单元格的值也会改变关联形状的值。如果你想用Aspose.Cells for Node.js via C++保存工作簿为XLS或XLSX格式，这也没问题。但如果你想保存为PDF或HTML格式，则必须调用[**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--)方法来刷新关联形状的值。  

{{% /alert %}}  

## 示例  

下图显示了示例代码所使用的源Excel文件。它包含一个链接到单元格A1到E4的图片。我们将用 Aspose.Cells 改变B4单元格的值，然后调用 [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) 方法刷新图片的值，并将其保存为PDF格式。  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

您可以从给定链接下载 [源Excel文件](95584291.xlsx) 和 [输出PDF](95584292.pdf)。  

### 使用Node.js代码刷新关联形状的数值  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
