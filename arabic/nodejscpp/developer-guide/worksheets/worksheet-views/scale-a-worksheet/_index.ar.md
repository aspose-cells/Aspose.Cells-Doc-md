---
title: كيفية تكبير حجم ورقة عمل باستخدام Node.js عبر C++
linktitle: كيفية تكبير ورقة عمل
type: docs
weight: 130
url: /ar/nodejs-cpp/how-to-scale-a-worksheet/
description: تعرض هذه المقالة رمزاً يوضح كيفية تغيير مقياس ورقة العمل باستخدام Aspose.Cells for Node.js via C++.
keywords: Node.js قياس ورقة عمل، كيفية تغيير مقياس ورقة عمل باستخدام Node.js عبر C++، تغيير مقياس ورقة عمل في Node.js عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون تكبير ورقة العمل مفيدًا لأسباب متعددة، اعتمادًا على السياق الذي تعمل فيه. إليك بعض الأسباب الشائعة لتكبير ورقة العمل:
1. ملاءمة الصفحة: لضمان أن يتناسب كل المحتوى على صفحة واحدة أو عدد معين من الصفحات عند الطباعة، مما يسهل قراءتها وإدارتها بدون الحاجة للتنقل بين صفحات متعددة.

1. العرض التقديمي: لجعل ورقة العمل تبدو أكثر تنظيمًا ومهنية، خاصة عند مشاركتها مع الآخرين في الاجتماعات أو التقارير.

1. القابلية للقراءة: لضبط حجم النص والعناصر الأخرى لتحسين قابلية القراءة، خاصة للأشخاص الذين يواجهون صعوبة في قراءة الخطوط الصغيرة.

1. إدارة المساحات: لتحسين استخدام المساحة في ورقة العمل، مع ضمان عدم وجود مساحة بيضاء غير ضرورية وأن تكون جميع المعلومات المهمة مرئية دون تصفح مفرط.

1. تصور البيانات: في حالة الرسوم البيانية والجداول، يمكن أن يساعد الت scaling في جعلها أكثر قابلية للفهم من خلال تعديل حجمها لتتناسب مع المساحة المتاحة بشكل مناسب.

1. الاتساق: للحفاظ على مظهر وإحساس متناسق عبر عدة أوراق عمل أو مستندات، وهو أمر مهم بشكل خاص في البيئات المهنية والتعليمية.

## **كيفية تكبير ورقة عمل في Excel**
يمكن أن يساعد تكبير ورقة عمل في Excel على ملء المحتوى صفحة واحدة أو عدد محدد من الصفحات عند الطباعة. إليك خطوات تكبير ورقة العمل:

1. افتح ورقة العمل الخاصة بك: افتح ورقة العمل Excel التي تريد تكبيرها.

1. اذهب إلى علامة التبويب تخطيط الصفحة: انقر على التبويب تخطيط الصفحة في الشريط.

1. مجموعة التناسب مع الصفحات: في تبويب تخطيط الصفحة، ابحث عن مجموعة التناسب مع الصفحات. هنا لديك خيارات لضبط مقياس الت scaling. العرض: يتيح لك هذا الخيار تحديد عدد الصفحات بعرض الصفحة المطبوعة. الارتفاع: يتيح لك تحديد عدد الصفحات بارتفاع الصفحة المطبوعة. الت scaling: يمكنك أيضًا تحديد نسبة مئوية مخصصة للت scaling هنا.
<br>
<img src="1.png" width=60% />

1. ضبط العرض والارتفاع: اضبط العرض والارتفاع إلى العدد المطلوب من الصفحات. على سبيل المثال، ضعهما على صفحة واحدة إذا كنت تريد أن تتناسب الورقة مع صفحة واحدة.

1. ضبط نسبة الت scaling (إذا لزم الأمر): إذا كنت تفضل تحديد نسبة مئوية معينة للت scaling، قم بضبط مربع الت scaling. على سبيل المثال، ضبطها إلى 50% سيجعل كل شيء نصف الحجم.


## **كيفية تغيير مقياس ورقة العمل باستخدام Node.js عبر C++**
Aspose.Cells for Node.js via C++ هو مكتبة قوية للعمل مع ملفات Excel برمجياً. لتغيير مقياس ورقة العمل باستخدام Aspose.Cells، عليك اتباع هذه الخطوات: تحميل [ملف المثال](sample.xlsx) وضبط إعدادات الطباعة بحيث يتناسب المحتوى مع عدد الصفحات المطلوب أو نسبة مئوية معينة من الحجم الأصلي.

### **مثال: التناسب مع الصفحة**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the worksheet to fit to 1 page wide and 1 page tall
pageSetup.setFitToPagesWide(1);
pageSetup.setFitToPagesTall(1);

// Save the modified workbook
workbook.save("output_fit_to_page.xlsx");
```
<br>
<img src="3.png" width=60% />

### **مثال: التمدد إلى نسبة مئوية**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the scaling to a specific percentage (e.g., 75%)
pageSetup.setZoom(75);

// Save the modified workbook
workbook.save("output_scaled_percentage.xlsx");
```
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
