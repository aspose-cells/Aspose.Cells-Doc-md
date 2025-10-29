---
title: 通过Node.js via C++在转换为PDF时导出文档结构
linktitle: 在将其转换为PDF时导出文档结构
type: docs
weight: 360
url: /zh/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: 了解如何在将Excel文件转换为带标签的PDF时导出文档结构，使用编号Aspose.Cells for Node.js via C++。 
---

PDF逻辑结构功能提供一种机制，将有关文档内容结构的信息整合到PDF文件中。编号Aspose.Cells for Node.js via C++保留了Microsoft Excel文档中的结构信息，例如单元格、行、表格、工作表、图片、形状、页眉/页脚等。

通过选项[PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--)，您可以导出文档结构并保存为带标签的PDF。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "document-structure-example.xlsx");
// Open the excel file with image, shape, chart, etc.
const wb = new AsposeCells.Workbook(filePath);

// Set to export document structure.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setExportDocumentStructure(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
