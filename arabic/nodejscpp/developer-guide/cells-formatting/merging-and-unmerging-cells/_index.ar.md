---
title: دمج وفك دمج الخلايا باستخدام Node.js عبر C++
linktitle: دمج وفك دمج الخلايا
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جدول البيانات، والتي تدعم دمج وفك دمج الخلايا. ستقدم هذه المقالة مقدمة عن كيفية دمج وفك دمج الخلايا باستخدام مكتبة Aspose.Cells، مع خيارات لتخصيص نمط الخلايا المدمجة.
keywords: Aspose.Cells، مكتبة Node.js، جدول البيانات، دمج الخلايا، فك دمج الخلايا، إعدادات النمط، الأنماط المخصصة
type: docs
weight: 190
url: /ar/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

تدعم Aspose.Cells هذه الميزة ويمكنها أيضًا دمج الخلايا في ورقة العمل. يمكنك فصل أو تقسيم الخلايا المدمجة أيضًا. الإشارة المرجعية للخلية المدمجة هي الإشارة المرجعية للخلية اليسرى العلوية في النطاق المحدد الأصلي.

{{% /alert %}} 
## **مقدمة**
غالبًا ما لا ترغب في نفس عدد الخلايا في كل صف أو عمود. على سبيل المثال، قد ترغب في وضع عنوان في خلية تمتد عبر عدة أعمدة. أو، إذا كنت تقوم بإنشاء فاتورة، قد ترغب في أقل عدد من الأعمدة للمجموع. لدمج خلية واحدة من خلايا أكثر من اثنين، قم بدمجهم. يتيح Microsoft Excel للمستخدمين تحديد الملفات ودمجها لتنظيم جدول البيانات بالطريقة التي يرغبون فيها.

{{% alert color="primary" %}} 

يرجى ملاحظة أنه عند دمج الخلايا، يتم الاحتفاظ فقط بالبيانات الموجودة في الخلية العليا اليسرى. إذا كانت هناك بيانات في الخلايا الأخرى في النطاق، فسيتم حذف هذه البيانات. التشكيل أيضًا يعتمد على خلية المرجع بحيث عند دمج الخلايا، يتم تطبيق إعدادات التنسيق الخاصة بالخلية العليا اليسرى على الخلية المدمجة. عند تقسيم الخلية، تحتفظ الخلايا الجديدة بإعدادات التنسيق الأصلية الخاصة بها.

{{% /alert %}} 
## **دمج الخلايا في ورقة العمل**
### **دمج الخلايا في Microsoft Excel**
الخطوات التالية تصف كيفية دمج الخلايا في ورق العمل باستخدام برنامج MS Excel.

1. قم بنسخ البيانات التي تريدها إلى أعلى يسار الخلية ضمن النطاق.
1. حدد الخلايا التي تريد دمجها.
1. لدمج الخلايا في صف أو عمود وتوسيط محتوى الخلية، انقر على أيقونة **دمج وتوسيط** في شريط الأدوات **التنسيق**.

### **دمج الخلايا باستخدام Aspose.Cells**
فئة خانات Aspose.Cells.Cells تحتوي على بعض الطرق المفيدة للمهمة. على سبيل المثال، الطريقة `merge()` تدمج الخلايا في خلية واحدة ضمن نطاق محدد.

المثال التالي يوضح كيفية دمج الخلايا (C6:E7) في ورق العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **رفع الدمج (تقسيم) الخلايا المدمجة**
### **استخدام Microsoft Excel**
الخطوات التالية تصف كيفية تقسيم الخلايا المدمجة باستخدام Microsoft Excel.

1. حدد الخلية المدمجة.
   عندما يتم دمج الخلايا، يتم تحديد **دمج وتوسيط** في شريط الأدوات **التنسيق**.
1. انقر على **دمج وتوسيط** في شريط الأدوات **التنسيق**.

### **استخدام Aspose.Cells**
فئة خلايا Aspose.Cells.Cells تحتوي على طريقة تسمى `unmerge()` تفصل الخلايا إلى حالتها الأصلية. تقوم الطريقة بإلغاء دمج الخلايا باستخدام مرجع الخلية في نطاق الخلايا المدمجة.

المثال التالي يوضح كيفية تقسيم الخلايا المدمجة (C6). يستخدم المثال الملف الذي تم إنشاؤه في المثال السابق ويقوم بتقسيم الخلايا المدمجة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **مواضيع متقدمة**
- [كشف الخلايا المدمجة في ورقة العمل](/cells/ar/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="nodejs-cpp" >}}
