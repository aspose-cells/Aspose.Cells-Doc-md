---
title: إدارة انقطاعات الصفحة باستخدام Node.js عبر C++
linktitle: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/nodejs-cpp/managing-page-breaks/
description: تقدم هذه المقالة رمزًا نموذجيًا وتشرح كيفية إضافة، مسح، أو حذف انقطاعات صفحة محددة في أوراق عمل إكسل برمجياً باستخدام Aspose.Cells for Node.js via C++.
keywords: انقطاعات الصفحة باستخدام Node.js عبر C++، انقطاعات صفحات إكسل باستخدام Node.js عبر C++، مسح انقطاع صفحة باستخدام Node.js عبر C++، حذف انقطاع صفحة محدد باستخدام Node.js عبر C++
---

{{% alert color="primary" %}}

وفقًا للتعريف، فإن فاصل الصفحة هو المكان في تدفق النص حيث تنتهي صفحة وتبدأ الصفحة التالية. يتيح Microsoft Excel للمستخدمين إضافة فواصل صفحات في أي خلية محددة من ورقة العمل.

في الموقع الذي تمت إضافة كسر الصفحة فيه، تنتهي الصفحة ويتم طباعة بقية البيانات بعد كسر الصفحة على الصفحة التالية أثناء الطباعة. ببساطة، كسر الصفحة يقسم ورقة العمل إلى عدة صفحات وفقًا لمواصفاتك. يمكنك أيضًا إضافة كسر الصفحة إلى ورقة العمل الخاصة بك أثناء التشغيل باستخدام Aspose.Cells. تسمح Aspose.Cells للمطورين بإضافة نوعين من كسر الصفحة:

- فاصل صفحات أفقي
- فاصل صفحات عمودي

في بقية النقاش، سنصف كيف يمكنك إضافة فواصل صفحات أفقية أو عمودية إلى أوراق العمل الخاصة بك باستخدام Aspose.Cells.

{{% /alert %}}

## **كسرات الصفحة**

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب المستخدمة لإدارة ورقة العمل.

لإضافة كسر الصفحة، استخدم خصائص [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) للفئة والخصائص [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--).

الخصائص [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) و [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) هي مجموعات قد تحتوي على العديد من كسر الصفحة. تحتوي كل مجموعة على العديد من الطرق لإدارة كسر الصفحة الأفقي والعمودي.

### **إضافة فواصل الصفحات**

لإضافة فاصل صفحة في ورقة عمل، قم بإدراج فواصل صفحة أفقية وعمودية عند الخلية المحددة باستخدام استدعاء طريقتي [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-) و [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-). كل طريقة **إضافة** تأخذ اسم الخلية التي يجب إضافة الفاصل إليها.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

في وضع معاينة كسر الصفحة أو معاينة الطباعة، يمكنك رؤية كيف تعمل هذه الكسور.

{{% /alert %}}

### **إزالة كسر صفحة محدد**

لحذف انقطاع صفحة معين، استدعِ الطريقتين [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-) و [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-). كل طريقة **removeAt** تأخذ فهرس انقطاع الصفحة المراد حذفه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **مهم معرفته**

عند ضبط خصائص **fitToPages** (وهي [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) و [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)) في إعدادات الصفحة، تتأثر إعدادات انقطاع الصفحة، لذلك إذا قمت بطباعة ورقة العمل، لن تؤخذ بعين الاعتبار إعدادات انقطاع الصفحة على الرغم من أنها لا تزال مضبوطة.
{{< app/cells/assistant language="nodejs-cpp" >}}
