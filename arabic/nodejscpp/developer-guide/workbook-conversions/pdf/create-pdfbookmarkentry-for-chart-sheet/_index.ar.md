---  
title: إنشاء إدخال Bookmark لورقة الرسوم البيانية باستخدام Node.js عبر C++  
linktitle: إنشاء إدخال PdfBookmarkEntry لورقة الرسم البياني  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/  
description: تعلم كيفية إنشاء PdfBookmarkEntry لورقات الرسوم البيانية باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

في السابق، كانت Aspose.Cells تنشئ [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) للورقة العادية. لكن الآن، يمكن لـ Aspose.Cells أيضًا إنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) لورقات الرسوم البيانية. نظرًا لعدم وجود خلايا أخرى في ورقة الرسم البياني غير الخلية A1، فستقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/nodejs-cpp/pdfbookmarkentry) فقط للخلية A1.  

## **إنشاء PdfBookmarkEntry لورقة الرسم البياني**  

يقوم الكود النموذجي التالي بتحميل [ملف Excel عينة](61767756.xlsx) الذي يحتوي على أربع صفحات. اثنتان منها عادية والأخرتان صفحات رسم بياني. ويقوم بإنشاء أربعة إدخالات للإشارة كما يلي  

- إشارة-I  
- إشارة-II-Chart1  
- إشارة-III  
- إشارة-IV-Chart2  

تظهر الصورة الملتقطة التالية [PDF المولد](61767757.pdf) بواسطة الكود النموذجي للإشارة.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **الكود المثالي**  

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

