---  
title: Créer une entrée PdfBookmarkEntry pour la feuille de graphique avec Node.js via C++  
linktitle: Créer une entrée PdfBookmark pour la feuille de graphique  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: Apprenez comment créer une PdfBookmarkEntry pour les feuilles de graphique en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Auparavant, Aspose.Cells créerait [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) pour une feuille normale. Mais désormais, Aspose.Cells peut également créer [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) pour les feuilles de graphique. Étant donné qu'une feuille de graphique ne possède pas d'autres cellules sauf la cellule A1, elle créera un [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) uniquement pour la cellule A1.  

## **Créer une entrée PdfBookmark pour une feuille de graphique**  

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767756.xlsx) qui contient quatre feuilles. Deux d'entre elles sont des feuilles normales et les deux autres sont des feuilles de graphique. Il crée quatre entrées de signet comme suit  

- Signet-I  
- Signet-II-Graph1  
- Signet-III  
- Signet-IV-Graph2  

La capture d'écran suivante montre le [PDF de sortie](61767757.pdf) généré par le code d'exemple pour référence.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Code d'exemple**  

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
