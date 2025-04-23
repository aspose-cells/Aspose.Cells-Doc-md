---  
title: Node.js経由でC++を使用したExcelのドキュメントワークブックとワークシートのプロパティをHTML変換でエクスポート  
linktitle: Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Aspose.Cells for Node.js via C++を使用してExcelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする方法を学びます。  
---  

## **可能な使用シナリオ**  

Microsoft ExcelファイルをMicrosoft ExcelまたはAspose.Cells for Node.js via C++を使ってHTMLにエクスポートする際、以下のスクリーンショットに示されているように、さまざまな種類のドキュメント、ワークブック、およびワークシートのプロパティもエクスポートされます。これらのプロパティのエクスポートを避けるには、[**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--)、[**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--)、および[**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--)を**false**に設定してください。これらのプロパティのデフォルト値は**true**です。次のスクリーンショットは、これらのプロパティがエクスポートされたHTML内でどのように見えるかを示しています。  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする**  

次のサンプルコードは、[サンプルExcelファイル](61767776.xlsx) を読み込み、ドキュメント、ワークブック、ワークシートのプロパティをエクスポートせずにHTMLに変換します（ [出力HTML](61767779.zip) 参照）。  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export document, workbook and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

