---
title: Agregar marcadores PDF con destinos nombrados usando Node.js a través de C++
linktitle: Agregar marcadores PDF con Destinos Nominados
type: docs
weight: 20
url: /es/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Aprende cómo agregar marcadores PDF con destinos nombrados usando Aspose.Cells for Node.js via C++. Asegúrate de que los marcadores permanezcan intactos independientemente de los cambios en las páginas.
---

## **Escenarios de uso posibles**

Los Destinos Nominados son un tipo especial de marcadores o enlaces en PDF que no dependen de las páginas PDF. Esto significa que si se añaden o eliminan páginas del PDF, los marcadores pueden volverse inválidos pero los destinos nominados permanecerán intactos. Para crear un Destino Nombrado, por favor establece la propiedad [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--).

## **Agregar Marcadores de PDF con Destinos Nombrados**

Por favor ve el siguiente código de ejemplo, su [archivo de Excel fuente](50528348.xlsx), y su [archivo PDF de salida](50528349.pdf). La captura de pantalla muestra los marcadores y destinos nominados dentro del PDF de salida. La captura de pantalla también describe cómo ver los Destinos Nominados y que necesitas la versión Profesional de Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Código de muestra**

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
