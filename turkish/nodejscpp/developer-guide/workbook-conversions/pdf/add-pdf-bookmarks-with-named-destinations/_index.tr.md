---
title: Node.js ile C++ kullanarak PDF Yer İmleri ve Adsız Hedefler Ekle
linktitle: Adlandırılmış hedeflerle PDF Yer İmlerini Ekleyin
type: docs
weight: 20
url: /tr/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/
description: Aspose.Cells for Node.js via C++ kullanarak PDF yer imleri ve adsız hedefler nasıl eklenir öğrenin. Yer imlerinin sayfa değişikliklerinden bağımsız olarak bütünlüğünü korumasını sağlayın.
---

## **Olası Kullanım Senaryoları**

Adlandırılmış hedefler, PDF'de PDF sayfalarına bağlı olmayan özel yer işaretleri veya bağlantılardır. Bu, PDF'ye sayfalar eklenip çıkarıldığında yer işaretlerinin geçersiz olabileceği anlamına gelir, ancak adlandırılmış hedefler aynı kalır. Adlandırılmış Hedef oluşturmak için lütfen [**PdfBookmarkEntry.getDestinationName()**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry/#getDestinationName--) özelliğini ayarlayınız.

## **Adlandırılmış Yer İmleriyle PDF Yer İmi Ekleyin**

Aşağıdaki örnek kodu, [kaynak Excel dosyasını](50528348.xlsx) ve [çıktı PDF dosyasını](50528349.pdf) inceleyin. Ekran görüntüsü, çıktı PDF içindeki yer imlerini ve isimli hedefleri gösterir. Ekran görüntüsü ayrıca İsimli Hedeflerin nasıl görüntüleneceğini ve Adobe Acrobat Reader'ın Profesyonel sürümüne ihtiyacınız olduğunu açıklar.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Örnek Kod**

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
