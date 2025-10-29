---
title: 通过Node.js via C++添加带有命名目的书签到PDF
linktitle: 使用命名目的地添加PDF书签
type: docs
weight: 20
url: /zh/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: 学习如何使用Aspose.Cells for Node.js via C++添加带有命名目的PDF书签。确保书签在页面变更时保持完整。
---

## **可能的使用场景**

命名目标是PDF中特殊类型的书签或链接，不依赖于PDF页面。这意味着，如果PDF中添加或删除页面，书签可能会失效，但命名目标将保持完整。要创建命名目标，请设置 [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--) 属性。

## **使用命名目标添加PDF书签**

请查看以下示例代码，其 [源Excel文件](50528348.xlsx)，以及 [输出PDF文件](50528349.pdf)。屏幕截图显示了输出PDF中的书签和命名目标。屏幕截图还描述了如何查看命名目标，以及您需要Acrobat Reader的专业版。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

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
