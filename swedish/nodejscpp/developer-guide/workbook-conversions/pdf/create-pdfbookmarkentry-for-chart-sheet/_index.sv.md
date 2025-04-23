---  
title: Skapa PdfBookmarkEntry för diagramblad med Node.js via C++  
linktitle: Skapa PdfBookmarkEntry för diagramkalkylblad  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: Lär dig hur du skapar PdfBookmarkEntry för diagramblad med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Tidigare skapade Aspose.Cells [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) för ett normalt blad. Men nu kan Aspose.Cells också skapa [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) för diagramblad. Eftersom ett diagramblad inte har några andra celler än cell A1, kommer det att skapa ett [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) för endast cell A1.  

## **Skapa PdfBookmarkEntry för diagramblad**  

Följande exempelkod laddar in [prov Excelfil](61767756.xlsx) som har fyra ark. Två av dem är normala ark och de andra två är diagramark. Den skapar fyra bokmärkesposter enligt följande  

- Bokmärke-I  
- Bokmärke-II-Chart1  
- Bokmärke-III  
- Bokmärke-IV-Chart2  

Följande skärmbild visar [utdata PDF](61767757.pdf) genererad av exemplet.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Exempelkod**  

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

