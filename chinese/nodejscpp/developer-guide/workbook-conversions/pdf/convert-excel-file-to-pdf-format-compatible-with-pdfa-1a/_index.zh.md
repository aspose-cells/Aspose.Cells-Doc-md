---  
title: 使用 C++ via Node.js 将Excel文件转换为兼容PDF/A 1a的PDF格式  
linktitle: 将Excel文件转换为PDF/A 1a兼容的PDF格式  
type: docs  
weight: 130  
url: /zh/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: 了解如何使用Aspose.Cells for Node.js via C++将Excel文件转换为符合PDF/A标准的PDF文件。  
---  

## **可能的使用场景**  

 PDF/A是一种专门为文档长期保存设计的PDF变体。PDF/A是ISO标准的便携式文档格式（PDF）版本，是一种存档格式，它将文档中使用的所有字体嵌入到PDF文件中。PDF/A不同于普通PDF，禁止使用字体链接（而非字体嵌入）和加密等功能。Aspose.Cells for Node.js via C++支持将Excel文件保存为PDF/A兼容的PDF文件（支持PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab和PDF/A-3u）。本主题描述如何将Excel工作簿保存为符合PDF/A标准（PDF/A-1a）的PDF文件。  

## **将Excel文件转换为与PDF/A-1a兼容的PDF格式**  

 开发者可以使用[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)类设置转换的不同属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)类的不同属性，可以控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是[**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--)，它允许你将Excel文件保存为符合PDF/A标准的PDF文件。  

 以下示例代码说明如何将Excel文件转换为兼容PDF/A-1a的PDF格式。请参考其[输出PDF](outputCompliancePdfA1a.pdf)及截图。  

## **屏幕截图**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

