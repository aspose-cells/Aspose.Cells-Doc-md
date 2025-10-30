---  
title: ExcelをPDFにレンダリング中のエラーを無視する  
linktitle: Excel を PDF にレンダリングする際のエラーを無視  
type: docs  
weight: 80  
url: /ja/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Aspose.Cells for Node.js via C++を使用してExcelファイルのPDF変換時にエラーを無視する方法を学びます。  
---  

## **可能な使用シナリオ**  

時にはExcelファイルをPDFに変換する際にエラーや例外が発生し、変換処理が終了することがあります。こうしたエラーをすべて無視したい場合は、[**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--)プロパティを利用してください。これにより、変換はエラーや例外なしでスムーズに完了しますが、データの損失が生じる可能性があります。  

## **Excel を PDF にレンダリングする際のエラーを無視**  

以下のコードは、[サンプルExcelファイル](55541778.xlsx)を読み込みますが、これはエラーがあり、[PDFへの変換](55541779.pdf)の際に17.11のバージョンでエラーが発生します。ただし、[**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--)プロパティを使用しているためエラーはスローされません。しかし、このスクリーンショットに示すような丸い赤い矢印型のシェイプは失われます。  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **サンプルコード**  

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
