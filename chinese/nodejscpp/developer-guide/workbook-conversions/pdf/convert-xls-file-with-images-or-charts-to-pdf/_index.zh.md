---
title: 使用C++ via Node.js将带有图片或图表的XLS文件转换为PDF
linktitle: 将带有图像或图表的XLS文件转换为PDF
type: docs
weight: 50
url: /zh/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

 Aspose.Cells支持将包含图片和图表的XLS文件转换为PDF文档。Aspose.Cells for Node.js via C++可以独立工作，将电子表格转换为PDF：无需使用Aspose.PDF for Node.js via C++进行转换。这个过程可以在内存中完成，因为它不依赖临时或中间XML文件。这意味着大型Excel文件（例如，包含图片、图表和其他绘图对象的文件）可以快速且高效地转换。

{{% /alert %}} 
## **示例代码**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

 如果电子表格包含公式，最好在渲染为PDF之前调用[Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)方法。这样可以确保公式依赖的值被重新计算，并在PDF中正确显示。

{{% /alert %}}
