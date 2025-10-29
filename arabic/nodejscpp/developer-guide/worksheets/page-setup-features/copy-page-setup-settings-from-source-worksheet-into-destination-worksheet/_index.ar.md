---
title: نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الوجهة باستخدام Node.js عبر C++
linktitle: نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الهدف
type: docs
weight: 80
url: /ar/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: يشرح هذا المقال كيفية استخدام واجهة برمجة تطبيقات Node.js أو رمز مكتبة C++ لنسخ إعدادات إعداد الصفحة من ورقة عمل مصدر إلى ورقة عمل وجهة برمجياً.
keywords: نسخ إعدادات إعداد الصفحة Node.js عبر C++، نسخ إعدادات إعداد الصفحة إلى ورقة العمل الهدف باستخدام Node.js عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

عند إضافة ورقة جديدة إلى مصنف، تحتوي على إعدادات إعداد الصفحة الافتراضية. قد تحتاج أحيانًا إلى نقل الإعدادات ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) من ورقة عمل إلى أخرى. يوضح هذا المستند كيفية نسخ إعدادات إعداد الصفحة من ورقة عمل إلى أخرى باستخدام واجهات برمجة تطبيقات Aspose.Cells for Node.js via C++.

## **نسخ إعدادات إعداد الصفحة من ورقة العمل المصدر إلى ورقة العمل الوجهة**

الشيفرة النموذجية التالية توضح كيفية نسخ إعدادات إعداد الصفحة من ورقة عمل واحدة إلى أخرى باستخدام طريقة [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-). يُرجى الاطلاع على الشيفرة النموذجية التالية وإخراجها إلى وحدة التحكم كمرجع.

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **مخرجات الوحدة**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
