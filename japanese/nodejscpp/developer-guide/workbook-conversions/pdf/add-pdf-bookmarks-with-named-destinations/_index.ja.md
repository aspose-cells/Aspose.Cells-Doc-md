---
title: Node.js経由でC++を使って名前付きデスティネーションを含むPDFブックマークを追加
linktitle: 名前付き目次でPDFブックマークを追加する
type: docs
weight: 20
url: /ja/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Aspose.Cells for Node.js via C++を使用して、名前付きデスティネーションを含むPDFブックマークの追加方法を学びましょう。ページの変更に関係なく、ブックマークが保持されることを確認してください。
---

## **可能な使用シナリオ**

名前付き目次はPDFページに依存しないPDF内のブックマークまたはリンクの特別な種類です。つまり、PDFにページが追加または削除されても、ブックマークは無効になる可能性がありますが、名前付き目次はそのままです。名前付き目次を作成するには、[**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--)プロパティを設定してください。

## **名前付き目次でPDFブックマークを追加する**

以下のサンプルコードとその[ソースExcelファイル](50528348.xlsx)、[出力PDFファイル](50528349.pdf)を参照してください。スクリーンショットには、出力PDF内のブックマークと名前付きデスティネーションが表示されます。スクリーンショットには、名前付きデスティネーションの表示方法と、Acrobat Readerのプロフェッショナルバージョンが必要であることが記載されています。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **サンプルコード**

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
