---  
title: 使用Node.js via C++预览工作簿  
linktitle: 预览工作簿 
type: docs  
weight: 70  
url: /zh/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells支持在没有Microsoft Excel安装的情况下，用Node.js via C++打印和预览Excel文件。  
---  

## **打印预览**  

对于包含数百万页的Excel文件，转换为PDF或图片可能需要很长时间和大量资源。在这种情况下，工作簿和工作表的打印预览功能可能会很有帮助。在转换之前，用户可以检查总页数，然后决定是否转换该文件。本文重点介绍如何使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)类来统计总页数。  

Aspose.Cells提供了打印预览功能。API提供[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)类。要生成整个工作簿的打印预览，需要传入[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)对象实例化[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)类，创建它的实例。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)类提供一个[**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--)方法，返回预览中的总页数。与[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)类类似，[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)类用来为特定工作表生成打印预览，创建实例时传入[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)对象，调用其构造函数。[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)类还提供一个[**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--)方法，用于返回预览中的总页数。  

以下代码片段演示了如何使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/)类，配合[示例Excel文件](94896177.xlsx)。  

### **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

执行上述示例代码生成的输出如下。  

### **控制台输出**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **高级主题**  
- [为呈现电子表的字体进行配置](/cells/zh/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [将工作表转换为图像-去除数据周围的空白](/cells/zh/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [将工作表转为图像以及按页面转为图像](/cells/zh/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [使用ImageOrPrint Options将工作表转换为图像](/cells/zh/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [导出工作表中的单元格范围为图像](/cells/zh/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [使用所需的宽度和高度将工作表或图表导出为图像](/cells/zh/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [使用ImageOrPrintOptions从工作表中提取图像](/cells/zh/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [生成工作表的缩略图](/cells/zh/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [当没有要打印的内容时输出空白页](/cells/zh/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [页面设置和打印选项](/cells/zh/nodejs-cpp/page-setup-and-printing-options/)  
- [使用ImageOrPrintOptions的PageIndex和PageCount属性呈现页面序列](/cells/zh/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [将工作表渲染到图形上下文](/cells/zh/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [指定工作簿渲染的个体或私有字体集](/cells/zh/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

{{< app/cells/assistant language="nodejs-cpp" >}}
