---  
title: 在使用Node.js通过C++将Excel渲染为PDF时忽略错误  
linktitle: 在将Excel渲染为PDF时忽略错误  
type: docs  
weight: 80  
url: /zh/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: 了解在将Excel文件转换为PDF时如何忽略错误，使用编号Aspose.Cells for Node.js via C++。  
---  

## **可能的使用场景**  

有时候在将Excel文件转换为PDF时会出现错误或异常，导致转换过程终止。您可以使用[**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--)属性在转换过程中忽略所有此类错误。这样，转换过程将顺利完成，不会抛出任何错误或异常，但可能会丢失部分数据。因此，仅在数据丢失对您不重要的情况下使用此属性。  

## **在将Excel渲染为PDF时忽略错误**  

以下代码加载了[示例Excel文件](55541778.xlsx)，但该示例Excel文件在[转换为PDF](55541779.pdf)时出现错误，发生在17.11版本中，但由于使用[**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--)属性，不会抛出错误。不过截图中显示的一个*圆角红箭头形状*会丢失。  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
