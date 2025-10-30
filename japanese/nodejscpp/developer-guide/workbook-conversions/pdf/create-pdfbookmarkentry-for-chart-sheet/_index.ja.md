---  
title: チャートシート用のPdfBookmarkEntryをNode.jsを使用してC++で作成する  
linktitle: チャートシートの PdfBookmarkEntry を作成  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: Aspose.Cells for Node.js via C++を使用してチャートシート用のPdfBookmarkEntryを作成する方法を学びます。  
---  

## **可能な使用シナリオ**  

以前は、Aspose.Cellsは通常のシート用に[**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry)を作成していました。しかし今では、チャートシートのために[**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry)も作成できます。チャートシートには他のセルがなく、セルA1のみがあるため、セルA1のために[**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry)を作成します。  

## **チャートシートの PdfBookmarkEntry を作成**  

次のサンプルコードは、4つのシートを持つ[サンプルExcelファイル](61767756.xlsx)をロードします。そのうち2つは通常のシートであり、残り2つはチャートシートです。次のように、以下のように4つのブックマークエントリを作成します。  

- ブックマーク-I  
- ブックマーク-II-Chart1  
- ブックマーク-III  
- ブックマーク-IV-Chart2  

次のスクリーンショットは、サンプルコードによって生成された[出力PDF](61767757.pdf)を示しています。  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleCreatePdfBookmarkEntryForChartSheet.xlsx");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access all four worksheets
const sheet1 = workbook.getWorksheets().get(0);
const sheet2 = workbook.getWorksheets().get(1);
const sheet3 = workbook.getWorksheets().get(2);
const sheet4 = workbook.getWorksheets().get(3);

// Create Pdf Bookmark Entry for Sheet1
const ent1 = new AsposeCells.PdfBookmarkEntry();
ent1.setDestination(sheet1.getCells().get("A1"));
ent1.setText("Bookmark-I");

// Create Pdf Bookmark Entry for Sheet2 - Chart
const ent2 = new AsposeCells.PdfBookmarkEntry();
ent2.setDestination(sheet2.getCells().get("A1"));
ent2.setText("Bookmark-II-Chart1");

// Create Pdf Bookmark Entry for Sheet3
const ent3 = new AsposeCells.PdfBookmarkEntry();
ent3.setDestination(sheet3.getCells().get("A1"));
ent3.setText("Bookmark-III");

// Create Pdf Bookmark Entry for Sheet4 - Chart
const ent4 = new AsposeCells.PdfBookmarkEntry();
ent4.setDestination(sheet4.getCells().get("A1"));
ent4.setText("Bookmark-IV-Chart2");

// Arrange all Bookmark Entries
const lst = [];
lst.push(ent2);
lst.push(ent3);
lst.push(ent4);

// Create Pdf Save Options with Bookmark Entries
const opts = new AsposeCells.PdfSaveOptions();
opts.setBookmark(ent1);

// Save the output Pdf
workbook.save("outputCreatePdfBookmarkEntryForChartSheet.pdf", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
