---  
title: Crea PdfBookmarkEntry per foglio di grafico con Node.js tramite C++  
linktitle: Create PdfBookmarkEntry per Chart Sheet  
type: docs  
weight: 50  
url: /it/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: Impara come creare PdfBookmarkEntry per fogli di grafico usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

In precedenza, Aspose.Cells creava [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) per un foglio normale. Ma ora Aspose.Cells può anche creare [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) per fogli di grafico. Poiché un foglio di grafico non ha altre celle oltre a celle A1, creerà un [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) solo per la cella A1.  

## **Crea PdfBookmarkEntry per Chart Sheet**  

Il seguente codice di esempio carica il [file Excel di esempio](61767756.xlsx) che ha quattro fogli. Due di essi sono fogli normali e gli altri due sono fogli grafico. Crea quattro voci di segnalibro come segue  

- Segnalibro-I  
- Segnalibro-II-Grafico1  
- Segnalibro-III  
- Segnalibro-IV-Grafico2  

La seguente schermata mostra l'{output PDF](61767757.pdf) generato dal codice di esempio come riferimento.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Codice di Esempio**  

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

