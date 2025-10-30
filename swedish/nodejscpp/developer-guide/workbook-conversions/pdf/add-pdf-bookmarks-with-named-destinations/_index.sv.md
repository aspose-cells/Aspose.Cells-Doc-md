---
title: Lägg till PDF bokmärken med namngivna destinationer med Node.js via C++
linktitle: Lägg till PDF bokmärken med namngivna destinationer
type: docs
weight: 20
url: /sv/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Lär dig att lägga till PDF bokmärken med namngivna destinationer med Aspose.Cells for Node.js via C++. Säkerställ att bokmärken förblir intakta oavsett sidändringar.
---

## **Möjliga användningsscenario**

Namngivna destinationer är speciella typer av bokmärken eller länkar i PDF som inte är beroende av PDF-sidor. Det betyder att om sidor läggs till eller tas bort från PDF-filen kan bokmärken bli ogiltiga men namngivna destinationer kommer att förbli intakta. För att skapa namngiven destination, ange egenskapen [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--).

## **Lägg till bokmärken i PDF med namngivna destinationer**

Se följande exempelkod, dess [käll-Excelfil](50528348.xlsx) och dess [utdata-PDF-fil](50528349.pdf). Skärmdumpen visar bokmärken och namngivna destinationer i den resulterande PDF:en. Skärmdumpen beskriver också hur man visar namngivna destinationer och att du behöver en professionell version av Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load source Excel file
const dataDir = path.join(__dirname, "data");
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePdfBookmarkEntry_DestinationName.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell C5
let cell = worksheet.getCells().get("C5");

// Create Bookmark and Destination for this cell
const bookmarkEntry = new AsposeCells.PdfBookmarkEntry();
bookmarkEntry.setText("Text");
bookmarkEntry.setDestination(cell);
bookmarkEntry.setDestinationName("AsposeCells--" + cell.getName());

// Access cell G56
cell = worksheet.getCells().get("G56");

// Create Sub-Bookmark and Destination for this cell
const subbookmarkEntry1 = new AsposeCells.PdfBookmarkEntry();
subbookmarkEntry1.setText("Text1");
subbookmarkEntry1.setDestination(cell);
subbookmarkEntry1.setDestinationName("AsposeCells--" + cell.getName());

// Access cell L4
cell = worksheet.getCells().get("L4");

// Create Sub-Bookmark and Destination for this cell
const subbookmarkEntry2 = new AsposeCells.PdfBookmarkEntry();
subbookmarkEntry2.setText("Text2");
subbookmarkEntry2.setDestination(cell);
subbookmarkEntry2.setDestinationName("AsposeCells--" + cell.getName());

// Add Sub-Bookmarks in list
const list = [];
list.push(subbookmarkEntry1);
list.push(subbookmarkEntry2);

// Assign Sub-Bookmarks list to Bookmark Sub-Entry
bookmarkEntry.getSubEntries = function() {
return this.subEntries || (this.subEntries = []);
};
bookmarkEntry.getSubEntries().push(...list);

// Create PdfSaveOptions and assign Bookmark to it
const opts = new AsposeCells.PdfSaveOptions();
opts.setBookmark(bookmarkEntry);

// Save the workbook in Pdf format with given pdf save options
workbook.save(path.join(dataDir, "outputPdfBookmarkEntry_DestinationName.pdf"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
