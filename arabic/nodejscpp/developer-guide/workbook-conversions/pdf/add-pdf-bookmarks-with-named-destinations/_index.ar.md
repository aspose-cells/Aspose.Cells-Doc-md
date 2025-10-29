---
title: إضافة علامات مرجعية بصيغة PDF مع وجهات مسماة باستخدام Node.js عبر C++
linktitle: إضافة إشارات مرجعية لملف PDF بأهداف مسماة
type: docs
weight: 20
url: /ar/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: تعلم كيفية إضافة علامات مرجعية بصيغة PDF مع وجهات مسماة باستخدام Aspose.Cells for Node.js via C++. تأكد من بقاء العلامات المرجعية سليمة بغض النظر عن تغييرات الصفحة.
---

## **سيناريوهات الاستخدام المحتملة**

الوجهات المسماة هي أنواع خاصة من الإشارات المرجعية أو الروابط في ملفات PDF التي لا تعتمد على صفحات PDF. يعني ذلك، إذا تمت إضافة صفحات أو حذفها من PDF، فإن الإشارات المرجعية قد تصبح غير صالحة ولكن الوجهات المسماة ستظل سليمة. لإنشاء وجهة مسماة، يرجى تعيين الخاصية [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--).

## **إضافة علامات مرجعية لملف PDF باستخدام وجهات مسماة**

يرجى الرجوع إلى الكود العيني التالي، و[ملف Excel المصدر](50528348.xlsx)، و[ملف PDF الناتج](50528349.pdf). تُظهر اللقطة الشاشة الإشارات المرجعية والوجهات المسماة داخل ملف PDF الناتج. توصف اللقطة الشاشة أيضا كيفية عرض الوجهات المسماة وأنك بحاجة إلى إصدار احترافي من قارئ أكروبات.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **الكود المثالي**

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
