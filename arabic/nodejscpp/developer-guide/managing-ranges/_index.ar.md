---
title: إدارة النطاقات باستخدام Node.js عبر C++
linktitle: النطاقات
type: docs
weight: 105
url: /ar/nodejs-cpp/managing-ranges/
description: تعلم كيف تدير النطاقات في إكسل باستخدام Aspose.Cells for Node.js via C++. أنشئ نطاقات، اضبط القيم والأنماط، وكرر العمليات المختلفة.
---

## **مقدمة**

في إكسل، يمكنك اختيار خلايا متعددة باستخدام تحديد الماوس؛ المجموعة المختارة تسمى "نطاق".

على سبيل المثال، يمكنك النقر بزر الماوس الأيسر في الخلية "A1" في إكسل ثم سحب إلى الخلية "C4". يمكن أيضًا إنشاء المنطقة المحددة بسهولة ككائن باستخدام Aspose.Cells for Node.js via C++.

إليك كيفية إنشاء نطاق، وضع قيمة، تعيين نمط، وأداء عمليات أكثر على كائن "النطاق".

## ** إدارة النطاقات باستخدام Aspose.Cells for Node.js via C++**

توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel، وتحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل تمثل بواسطة فئة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

### **إنشاء المدى**

عندما ترغب في إنشاء منطقة مستطيلية تمتد عبر A1:C4، يمكنك استخدام الشيفرة التالية:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **وضع قيمة في الخلايا من المدى**

فلنفترض أن لديك مدى من الخلايا يمتد عبر A1:C4. يحتوي المصفوفة على 4 * 3 = 12 خلية. ترتبت الخلايا الفردية للمدى على التوالي: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

توضح الأمثلة التالية كيفية إدخال بعض القيم في الخلايا للنطاق

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **تعيين أسلوب للخلايا من المدى**

 يوضح المثال التالي كيفية تعيين نمط خلايا النطاق.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **الحصول على النطاق الحالي من المدى**

CurrentRegion هو خاصية تقوم بإرجاع كائن Range يمثل المنطقة الحالية 

المنطقة الحالية هي نطاق محصور بأي مزيج من الصفوف الفارغة والأعمدة الفارغة. للقراءة فقط

 في إكسل، يمكنك الحصول على منطقة CurrentRegion بواسطة:
 1. حدد منطقة (نطاق1) باستخدام مربع الماوس.
 2. انقر على "الصفحة الرئيسية - تحرير - البحث والتحديد - الانتقال الخاص - المنطقة الحالية"، أو استخدم "Ctrl+Shift+*"، سترى أن إكسل يساعدك تلقائيًا على تحديد منطقة (نطاق2). الآن، أنشئها، نطاق2 هو المنطقة الحالية لنطاق1.

يرجى تحميل ملف الاختبار التالي، فتحه في إكسل، استخدام مربع الماوس لتحديد منطقة "A1:D7"، ثم النقر على "Ctrl+Shift+*"، سترى المنطقة "A1:C3" تم تحديدها.

[current_region.xlsx](current_region.xlsx)

الآن يرجى تشغيل المثال التالي لمعرفة كيف يعمل في Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **مواضيع متقدمة**
- [ملء تلقائي لنطاق ملف Excel](/cells/ar/nodejs-cpp/autofill-ranges/)
- [نسخ النطاقات من Excel](/cells/ar/nodejs-cpp/copy-ranges-of-Excel/)
- [نسخ بيانات النطاق فقط](/cells/ar/nodejs-cpp/copy-range-data-only/)
- [نسخ بيانات النطاق بالتنسيق](/cells/ar/nodejs-cpp/copy-range-data-with-style/)
- [نسخ نمط النطاق فقط](/cells/ar/nodejs-cpp/copy-range-style-only/)
- [إنشاء مجموعة الاتحاد](/cells/ar/nodejs-cpp/create-union-range/)
- [قص ولصق النطاق](/cells/ar/nodejs-cpp/cut-and-paste-cells/)
- [حذف النطاقات](/cells/ar/nodejs-cpp/delete-ranges-from-Excel/)
- [الحصول على عنوان خلية عدد الإزاحة الكاملة للعمود والصف الكامل للنطاق](/cells/ar/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [إدراج النطاقات](/cells/ar/nodejs-cpp/insert-ranges-to-Excel/)
- [دمج أو فصل نطاق الخلايا](/cells/ar/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [نقل مجموعة من الخلايا في ورقة العمل](/cells/ar/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [إنشاء أسماء مسماة محددة بنطاق العمل وورقة العمل](/cells/ar/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [البحث والاستبدال في بيانات النطاق](/cells/ar/nodejs-cpp/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="nodejs-cpp" >}}
