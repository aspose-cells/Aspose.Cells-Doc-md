---  
title: 通过Node.js via C++嵌入附件到PDF  
linktitle: 将附件嵌入到PDF中  
type: docs  
weight: 380  
url: /zh/nodejs-cpp/embed-attachment-to-pdf/  
description: 了解如何使用Aspose.Cells for Node.js via C++将Ole对象作为附件嵌入到PDF中。  
---  

 在Excel中，你可以插入带有源数据的Ole对象（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。双击Ole对象，嵌入的文件将被打开。

 一般情况下，在转换为PDF时，Ole对象会以图标或缩略图的形式渲染，而不显示Ole对象的源数据。通过选项[PdfSaveOptions.getEmbedAttachments()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getEmbedAttachments--)，可以将Ole对象的源数据作为附件嵌入到PDF中。在PDF中双击图标或缩略图即可打开Ole对象的源文件。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "embedded-attachments-example.xlsx");

// Open the template file
const wb = new AsposeCells.Workbook(filePath);

// Set to embed Ole Object attachment.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setEmbedAttachments(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

![embedded-attachment.png](embedded-attachment.png)  

