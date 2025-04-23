---  
title: Erstellen Sie PdfBookmarkEntry für Diagrammblatt mit Node.js via C++  
linktitle: PdfBookmarkEntry für Diagrammblatt erstellen  
type: docs  
weight: 50  
url: /de/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: Erfahren Sie, wie Sie PdfBookmarkEntry für Diagrammblätter mit Aspose.Cells for Node.js via C++ erstellen.  
---  

## **Mögliche Verwendungsszenarien**  

Früher erstellte Aspose.Cells für ein normales Blatt [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry). Aber jetzt kann Aspose.Cells auch [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) für Diagrammblätter erstellen. Da ein Diagrammblatt keine anderen Zellen außer Zelle A1 hat, wird nur für Zelle A1 ein [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) erstellt.  

## **Erstellen Sie PdfBookmarkEntry für Diagrammblatt**  

Der folgende Beispielcode lädt die [Beispieldatei Excel](61767756.xlsx), die vier Blätter hat. Zwei davon sind normale Blätter und die anderen beiden sind Diagrammblätter. Es erstellt vier Lesezeichen-Einträge wie folgt  

- Lesezeichen-I  
- Lesezeichen-II-Diagramm1  
- Lesezeichen-III  
- Lesezeichen-IV-Diagramm2  

Der folgende Screenshot zeigt die [Ausgabe-PDF](61767757.pdf), die vom Beispielcode zur Referenz erzeugt wird.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Beispielcode**  

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

