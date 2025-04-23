---  
title: Grafik Sayfası için PdfBookmarkEntry Oluşturma (Node.js C++) ile  
linktitle: Grafik Sayfası için PdfBookmarkEntry Oluşturma  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: Aspose.Cells for Node.js via C++ kullanarak grafik sayfaları için PdfBookmarkEntry oluşturmayı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Önceleri, Aspose.Cells normal sayfa için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) oluştururdu. Ama şimdi, grafik sayfaları için de [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) oluşturabilir. Bir grafik sayfasında başka hücre yoktur, yalnızca A1 hücresi vardır, bu yüzden yalnızca A1 hücresi için [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) oluşturur.  

## **Grafik Tablosu için PdfBookmarkEntry Oluştur**  

Aşağıdaki örnek kod, dört çalışma sayfası içeren [örnek Excel dosyasını](61767756.xlsx) yükler. Bunlardan ikisi normal çalışma sayfalarıdır ve diğer ikisi grafik çalışma sayfalarıdır. Aşağıdaki gibi dört yer imi girişi oluşturur  

- Yer İmi-I  
- Yer İmi-II-Chart1  
- Yer İmi-III  
- Yer İmi-IV-Chart2  

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan [çıktı PDF'yi](61767757.pdf) göstermektedir.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleCreatePdfBookmarkEntryForChartSheet.xlsx");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access all four worksheets
const sheet1 = workbook.getWorksheets().get(0);
const sheet2 = workbook.getWorksheets().get(1);
const sheet3 = workbook.getWorksheets().get(2);
const sheet4 = workbook.getWorksheets().get(3);

// Create Pdf Bookmark Entry for Sheet1
const ent1 = new AsposeCells.PdfBookmarkEntry();
ent1.setDestination(sheet1.getCells().get("A1"));
ent1.setText("Bookmark-I");

// Create Pdf Bookmark Entry for Sheet2 - Chart
const ent2 = new AsposeCells.PdfBookmarkEntry();
ent2.setDestination(sheet2.getCells().get("A1"));
ent2.setText("Bookmark-II-Chart1");

// Create Pdf Bookmark Entry for Sheet3
const ent3 = new AsposeCells.PdfBookmarkEntry();
ent3.setDestination(sheet3.getCells().get("A1"));
ent3.setText("Bookmark-III");

// Create Pdf Bookmark Entry for Sheet4 - Chart
const ent4 = new AsposeCells.PdfBookmarkEntry();
ent4.setDestination(sheet4.getCells().get("A1"));
ent4.setText("Bookmark-IV-Chart2");

// Arrange all Bookmark Entries
const lst = [];
lst.push(ent2);
lst.push(ent3);
lst.push(ent4);

// Create Pdf Save Options with Bookmark Entries
const opts = new AsposeCells.PdfSaveOptions();
opts.setBookmark(ent1);

// Save the output Pdf
workbook.save("outputCreatePdfBookmarkEntryForChartSheet.pdf", opts);
```  

