---
title: Добавление закладок PDF с именованными пунктами назначения с помощью Node.js через C++
linktitle: Добавление закладок PDF с именованными местами назначения
type: docs
weight: 20
url: /ru/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Узнайте, как добавлять закладки PDF с именованными пунктами назначения с помощью Aspose.Cells for Node.js via C++. Убедитесь, что закладки останутся неизменными независимо от изменений страниц.
---

## **Возможные сценарии использования**

Именованные места назначения - это особые виды закладок или ссылок в PDF, которые не зависят от страниц PDF. Это означает, что если страницы добавляются или удаляются из PDF, закладки могут стать недействительными, но именованные места назначения останутся неизменными. Чтобы создать именованное место назначения, пожалуйста, установите свойство [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--).

## **Добавление закладок PDF с именованными местами назначения**

Пожалуйста, обратитесь к следующему образцу кода, его [исходному файлу Excel](50528348.xlsx) и [выходному файлу PDF](50528349.pdf). Снимок экрана показывает закладки и именованные места в выходном PDF. На снимке также описано, как просматривать именованные места и что для этого требуется профессиональная версия Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Образец кода**

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
