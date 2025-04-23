---
title: Lesezeichen mit benannten Zielorten in PDF mit Node.js via C++ hinzufügen
linktitle: PDF Lesezeichen mit benannten Zielen hinzufügen
type: docs
weight: 20
url: /de/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Lernen Sie, wie man mit Aspose.Cells for Node.js via C++ PDF Lesezeichen mit benannten Zielorten hinzufügt. Stellen Sie sicher, dass die Lesezeichen unabhängig von Seitenänderungen erhalten bleiben.
---

## **Mögliche Verwendungsszenarien**

Benannte Ziele sind spezielle Arten von Lesezeichen oder Links in PDF, die nicht von PDF-Seiten abhängen. Das bedeutet, dass Lesezeichen ungültig werden können, wenn Seiten im PDF hinzugefügt oder gelöscht werden, benannte Ziele jedoch intakt bleiben. Für die Erstellung eines benannten Ziels setzen Sie bitte die [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--)-Eigenschaft.

## **PDF-Lesezeichen mit benannten Zielen hinzufügen**

Bitte sehen Sie sich den folgenden Beispielcode, die Quelldatei Excel (50528348.xlsx) und die Ausgabedatei PDF (50528349.pdf) an. Der Screenshot zeigt die Lesezeichen und benannten Ziele in der Ausgabedatei PDF. Der Screenshot beschreibt auch, wie benannte Ziele angezeigt werden können und dass Sie die professionelle Version von Acrobat Reader benötigen.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Beispielcode**

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
