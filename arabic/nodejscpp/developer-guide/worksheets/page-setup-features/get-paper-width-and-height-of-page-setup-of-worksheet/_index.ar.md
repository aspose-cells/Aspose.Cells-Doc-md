---
title: الحصول على عرض وارتفاع صفحة إعدادات الورقة لورقة العمل باستخدام Node.js عبر C++
linktitle: الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل
type: docs
weight: 50
url: /ar/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: اكتشف كيفية الحصول على عرض وارتفاع إعداد صفحة الورق لورقة العمل من خلال برمجياً باستخدام Node.js عبر C++.
keywords: إعداد الصفحة في Excel، عرض وارتفاع الورق ضمن إعدادات الصفحة لورقة العمل باستخدام Node.js عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، تحتاج إلى معرفة عرض وارتفاع حجم الورق كما تم تعيينه في إعداد الصفحة لورقة العمل. يرجى استخدام الخاصيتين [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) و [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) لهذا الغرض.

## **الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل**

يفسر الكود النموذجي التالي استخدام الخاصتين [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) و [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--). يغير أولاً حجم الورق إلى *A2* ثم يحدد عرض وارتفاع الورق، ثم يغير إلى *A3*, *A4*, و *Letter* ويحدد عرض وارتفاع الورق على التوالي.

### **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **مخرجات الوحدة**

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
