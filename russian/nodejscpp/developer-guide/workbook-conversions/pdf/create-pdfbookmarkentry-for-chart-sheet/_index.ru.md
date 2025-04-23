---  
title: Создание PdfBookmarkEntry для листа с графиком с помощью Node.js через C++  
linktitle: Создание PdfBookmarkEntry для листа с диаграммой  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: Узнайте, как создавать PdfBookmarkEntry для листов с графиками с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Ранее Aspose.Cells создавал [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) для обычного листа. Но теперь Aspose.Cells также может создавать [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) для листов с графиками. Так как в листе с графиком нет других ячеек, кроме ячейки A1, он создаст [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) только для ячейки A1.  

## **Создание PdfBookmarkEntry для листа с диаграммой**  

Приведенный ниже пример кода загружает [образец Excel-файла](61767756.xlsx), который содержит четыре листа. Два из них обычные листы, а остальные два - листы диаграмм. Он создает четыре закладки следующим образом  

- Закладка-I  
- Закладка-II-Chart1  
- Закладка-III  
- Закладка-IV-Chart2  

На следующем скриншоте показан [выходной PDF-файл](61767757.pdf), сгенерированный примером кода для справки.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Образец кода**  

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

