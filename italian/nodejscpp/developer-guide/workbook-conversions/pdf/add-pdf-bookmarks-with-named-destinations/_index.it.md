---
title: Aggiungi segnalibri PDF con destinazioni nominate usando Node.js tramite C++
linktitle: Aggiungi Segnalibri PDF con Destinazioni con Nome
type: docs
weight: 20
url: /it/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Scopri come aggiungere segnalibri PDF con destinazioni nominate usando Aspose.Cells for Node.js via C++. Assicurati che i segnalibri rimangano intatti indipendentemente dalle modifiche alle pagine.
---

## **Possibili Scenari di Utilizzo**

Le Destinazioni con Nome sono un tipo speciale di segnalibri o collegamenti nei PDF che non dipendono dalle pagine PDF. Ciò significa che, se vengono aggiunte o eliminate pagine dal PDF, i segnalibri possono diventare non validi ma le destinazioni con nome rimarranno integre. Per creare una Destinazione con Nome, si prega di impostare la proprietà [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--).

## **Aggiungi Segnalibri PDF con Destinazioni con Nome**

Si prega di consultare il codice di esempio seguente, il [file Excel di origine](50528348.xlsx) e il [file PDF di output](50528349.pdf). La schermata mostra i segnalibri e le destinazioni con nome all'interno del PDF di output. La schermata descrive anche come visualizzare le Destinazioni con Nome e che è necessaria la versione Professionale di Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Codice di Esempio**

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
