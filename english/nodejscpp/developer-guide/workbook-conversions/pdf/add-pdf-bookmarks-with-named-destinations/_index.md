---
title: Add PDF Bookmarks with Named Destinations using Node.js via C++
linktitle: Add PDF Bookmarks with Named Destinations
type: docs
weight: 20
url: /nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Learn how to add PDF bookmarks with named destinations using Aspose.Cells for Node.js via C++. Ensure bookmarks remain intact regardless of page changes.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Named Destinations are a special kind of bookmark or link in a PDF that does not depend on specific pages. This means that if pages are added or deleted from the PDF, regular bookmarks may become invalid, but named destinations will remain intact. To create a named destination, set the [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--) property.

## **Add PDF Bookmarks with Named Destinations**

Please see the following sample code, its [source Excel file](50528348.xlsx), and its [output PDF file](50528349.pdf). The screenshot shows the bookmarks and named destinations in the output PDF. It also explains how to view named destinations and indicates that you need the Professional version of Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Sample Code**

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

// Add sub‑bookmarks to list
const list = [];
list.push(subbookmarkEntry1);
list.push(subbookmarkEntry2);

// Assign the sub‑bookmarks list to the bookmark's sub‑entries
bookmarkEntry.getSubEntries = function() {
return this.subEntries || (this.subEntries = []);
};
bookmarkEntry.getSubEntries().push(...list);

// Create PdfSaveOptions and assign Bookmark to it
const opts = new AsposeCells.PdfSaveOptions();
opts.setBookmark(bookmarkEntry);

// Save the workbook in PDF format with the given PDF save options
workbook.save(path.join(dataDir, "outputPdfBookmarkEntry_DestinationName.pdf"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
