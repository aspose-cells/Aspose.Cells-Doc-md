---
title: Ajouter des signets PDF avec destinations nommées en utilisant Node.js via C++
linktitle: Ajouter des signets PDF avec des destinations nommées
type: docs
weight: 20
url: /fr/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Apprenez comment ajouter des signets PDF avec des destinations nommées en utilisant Aspose.Cells for Node.js via C++. Assurez vous que les signets restent intacts indépendamment des changements de pages.
---

## **Scénarios d'utilisation possibles**

Les destinations nommées sont des sortes spéciales de signets ou de liens dans les PDF qui ne dépendent pas des pages PDF. Cela signifie que si des pages sont ajoutées ou supprimées du PDF, les signets peuvent devenir invalides mais les destinations nommées resteront intacts. Pour créer une destination nommée, veuillez définir la propriété [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--).

## **Ajouter des signets PDF avec des destinations nommées**

Veuillez consulter le code d'exemple suivant, son fichier Excel source et son fichier PDF généré. La capture d'écran montre les signets et les destinations nommées à l'intérieur du PDF généré. La capture d'écran décrit également comment visualiser les Destinations Nommées et que vous avez besoin de la version professionnelle de Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Code d'exemple**

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
