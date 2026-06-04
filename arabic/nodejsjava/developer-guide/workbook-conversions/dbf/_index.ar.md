---
title: قراءة وكتابة ملفات DBF
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات، تدعم قراءة وكتابة ملفات dBASE III وIV (DBF). توضح هذه المقالة كيفية استيراد البيانات من وتصدير البيانات إلى ملفات DBF باستخدام Aspose.Cells، بما في ذلك تفاصيل تنسيق الملف والميزات المدعومة والأمثلة خطوة بخطوة.
keywords: Aspose.Cells, Node.js library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf, Java
type: docs
weight: 200
url: /ar/nodejs-java/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

توفر Aspose.Cells دعمًا كاملًا لقراءة وكتابة ملفات DBF (dBASE). يمكنك تحميل ملفات dBASE III و dBASE IV الموجودة في كائن Workbook، ومعالجة البيانات باستخدام واجهة برمجة التطبيقات الغنية لـ Aspose.Cells، ثم حفظ المصنف مرة أخرى بتنسيق DBF لاستخدامه مع تطبيقات قواعد البيانات القديمة.

{{% /alert %}}

## **المقدمة**

DBF (ملف قاعدة البيانات) هو تنسيق ملف قاعدة بيانات قديم تم تقديمه في الأصل بواسطة dBASE في أوائل الثمانينيات. على الرغم من قدم هذا التنسيق، لا تزال ملفات DBF مستخدمة على نطاق واسع في العديد من الصناعات لتخزين البيانات المنظمة، لا سيما في المحاسبة ونظم المعلومات الجغرافية والتطبيقات المتخصصة الأخرى. تتيح لك Aspose.Cells دمج هذه الملفات القديمة في سير عمل جداول البيانات الحديثة في Node.js بسلاسة.

تدعم المكتبة كلًا من قراءة وكتابة ملفات DBF، مما يمنحك القدرة على:

- استيراد البيانات من ملفات DBF الموجودة إلى كائنات Workbook الخاصة بـ Aspose.Cells لمزيد من المعالجة أو التحويل إلى تنسيقات أخرى.
- إنشاء ملفات DBF جديدة من البداية أو عن طريق تحويل البيانات من تنسيقات جداول البيانات الأخرى.
- الحفاظ على تعريفات الحقول وأنواع البيانات وهياكل السجلات عند نقل البيانات من وإلى تنسيق DBF.

يمكن أيضًا فتح ملفات DBF مباشرة في Microsoft Excel وتطبيقات جداول البيانات الأخرى، مما يجعلها جسرًا ملائمًا بين الأنظمة القديمة وأدوات جداول البيانات الحديثة.

## **إصدارات وميزات DBF المدعومة**

تدعم Aspose.Cells إصدارات تنسيق DBF التالية:

- **dBASE III** — المتغير الأصلي والأكثر دعمًا على نطاق واسع لتنسيق DBF.
- **dBASE IV** — نسخة موسعة تدعم أنواع بيانات إضافية وأحجام حقول أكبر.

### الميزات المدعومة

توفر المكتبة دعمًا شاملًا للعمليات التالية:

- قراءة بيانات DBF في كائن Workbook، مع الحفاظ على جميع السجلات وتعريفات الحقول.
- كتابة بيانات المصنف مرة أخرى بتنسيق DBF للتصدير إلى التطبيقات المتوافقة مع dBASE.
- معالجة أنواع البيانات الشائعة المستخدمة في ملفات DBF، بما في ذلك الحقول الحرفية والرقمية والتاريخية والمنطقية.
- الحفاظ على تعريفات الحقول مثل اسم الحقل ونوعه وطوله أثناء عمليات القراءة/الكتابة.

### القيود والاعتبارات

عند العمل مع ملفات DBF، يجب مراعاة القيود التالية:

- الحد الأقصى لعدد الحقول في الملف الواحد هو **128**.
- الحد الأقصى لحجم السجل هو **4000 بايت**.
- أسماء الحقول محدودة بـ **10 أحرف**، ويجب أن تكون بأحرف كبيرة، ولا يمكن أن تحتوي على مسافات.
- يتم تخزين قيم التاريخ في ملفات DBF بتنسيق `YYYYMMDD`.
- قد يختلف ترميز الأحرف حسب التطبيق المصدر (شائع Windows-1252 أو صفحات كود OEM).

## **قراءة ملف DBF**

تجعل Aspose.Cells من السهل تحميل البيانات من ملف DBF إلى كائن Workbook. تستخدم المكتبة الفئة `LoadOptions` لتحديد تنسيق المصدر، مما يضمن تفسير البيانات بشكل صحيح أثناء عملية التحميل.

### قراءة ملف DBF باستخدام Aspose.Cells

لقراءة ملف DBF، تحتاج إلى إنشاء مثيل `LoadOptions` مكون بتنسيق `LoadFormat.Dbf`، وتمريره إلى مُنشئ `Workbook` مع مسار الملف. بمجرد التحميل، تصبح البيانات قابلة للوصول من خلال مجموعة `Worksheets`، حيث يمكنك التكرار عبر الخلايا واستخراج القيم أو معالجة البيانات حسب الحاجة.

يوضح المثال التالي كيفية تحميل ملف DBF موجود في Aspose.Cells، والوصول إلى ورقة العمل الأولى، وقراءة قيم الخلايا.

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "path/to/data";
const filePath = path.join(dataDir, "input.dbf");

// تحميل ملف DBF
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

const lines = [];
for (let i = 0; i <= maxRow; i++) {
    let row = "";
    for (let j = 0; j <= maxCol; j++) {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        row += "|" + value;
    }
    row += "|" + "\n";
    lines.push(row);
}

console.log(lines.join(""));

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

يمكنك فتح ملفات DBF مباشرة في Microsoft Excel عن طريق تحديد الملف في مربع الحوار فتح. سيتعامل Excel مع ملف DBF كجدول بيانات، ويعرض سجلاته في تخطيط جدولي. هذا مفيد للتحقق السريع من البيانات بعد قراءتها أو كتابتها باستخدام Aspose.Cells.

{{% /alert %}}

## **كتابة ملف DBF**

تتبع كتابة البيانات في ملف DBF نمطًا مشابهًا لحفظ أي تنسيق جدول بيانات آخر باستخدام Aspose.Cells. يمكنك إنشاء أو تحميل Workbook، وتعبئة ورقة العمل بالبيانات، ثم استدعاء طريقة `save` مع تحديد `SaveFormat.Dbf` كتنسيق الهدف.

### كتابة ملف DBF باستخدام Aspose.Cells

لإنشاء ملف DBF، اتبع الخطوات التالية:

1. أنشئ مثيل `Workbook` جديد.
2. الوصول إلى ورقة العمل الأولى من مجموعة `Worksheets`.
3. تعبئة ورقة العمل ببياناتك، بما في ذلك العناوين في الصف الأول والسجلات في الصفوف اللاحقة.
4. استدعاء طريقة `Workbook.save`، مع تمرير مسار الملف و `SaveFormat.Dbf` كمعلمات.

يوضح المثال التالي كيفية إنشاء ملف DBF جديد من البداية. يقوم بتعبئة ورقة العمل ببيانات نموذجية تحتوي على أنواع بيانات مختلفة (سلاسل وأرقام وتواريخ) لتوضيح كيفية معالجة أنواع الحقول عند التصدير إلى تنسيق DBF.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// رؤوس الأعمدة
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// صف البيانات 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new Date(2020, 2, 15));

// صف البيانات 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new Date(2019, 6, 22));

// صف البيانات 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new Date(2021, 0, 10));

// صف البيانات 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new Date(2018, 10, 5));

// صف البيانات 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new Date(2022, 4, 30));

// تعيين عرض الأعمدة لتحسين القراءة
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, AsposeCells.SaveFormat.Dbf);
```

{{% alert color="primary" %}}

عند كتابة البيانات في ملف DBF، تأكد من أن بياناتك تتوافق مع قيود التنسيق. يجب ألا يتجاوز طول أسماء الحقول 10 أحرف ولا ينبغي أن تحتوي على مسافات. لن يتم حفظ السجلات التي يتجاوز حجمها الإجمالي 4000 بايت بشكل صحيح. يجب أن تكون التواريخ قيم تاريخ صالحة يمكن تمثيلها بتنسيق YYYYMMDD.

{{% /alert %}}

## **اعتبارات نوع البيانات والتنسيق**

عند نقل البيانات بين Aspose.Cells وتنسيق DBF، فإن فهم كيفية تعيين أنواع البيانات بين النظامين أمر مهم لضمان سلامة البيانات.

### أنواع الخلايا إلى أنواع حقول DBF

يتم تحويل قيم خلايا Aspose.Cells تلقائيًا إلى أنواع حقول DBF المناسبة عند الحفظ:

- يتم تعيين **السلاسل النصية** إلى الحقول الحرفية (C).
- يتم تعيين **القيم الرقمية** (الأعداد الصحيحة والعشرية) إلى الحقول الرقمية (N).
- يتم تعيين **قيم التاريخ** إلى حقول التاريخ (D) بتنسيق `YYYYMMDD`.
- يتم تعيين **القيم المنطقية** إلى الحقول المنطقية (L).

### الترميز

قد تستخدم ملفات DBF ترميزات أحرف مختلفة اعتمادًا على التطبيق الذي أنشأها. تتعامل Aspose.Cells مع الترميز بشفافية في معظم الحالات، ولكن إذا واجهت مشكلات في عرض الأحرف، فقد تحتاج إلى التحقق من ترميز الملف المصدر.

### قواعد أسماء الحقول

يجب أن تلتزم أسماء حقول DBF بالقواعد التالية:

- الحد الأقصى للطول هو 10 أحرف.
- يجب أن تبدأ بحرف.
- لا يمكن أن تحتوي على مسافات أو أحرف خاصة.
- يتم تخزينها بأحرف كبيرة بغض النظر عن الحالة المستخدمة في الإدخال.

### التحقق من الإخراج

بعد كتابة ملف DBF، يمكنك التحقق من النتيجة عن طريق فتحه في Microsoft Excel أو أي تطبيق متوافق مع dBASE. يجب أن تظهر البيانات في تخطيط جدولي مع أسماء الحقول كرؤوس أعمدة، والسجلات ممتلئة وفقًا للبيانات التي قدمتها.

## **التحويل بين DBF والتنسيقات الأخرى**

تعد القدرة على قراءة وكتابة ملفات DBF باستخدام Aspose.Cells من أكثر حالات الاستخدام العملية لتحويل البيانات بين تنسيق DBF وتنسيقات جداول البيانات الحديثة مثل XLSX أو XLS أو CSV. نظرًا لأن Aspose.Cells تدعم مجموعة واسعة من التنسيقات، يمكنك بسهولة تحميل ملف DBF وإعادة حفظه بأي تنسيق مدعوم آخر، أو العكس.

على سبيل المثال، يمكنك قراءة ملف DBF، وتطبيق التنسيق أو الحسابات باستخدام واجهة برمجة تطبيقات Aspose.Cells، ثم حفظ النتيجة كملف XLSX لتوزيعها على المستخدمين الذين يعملون مع تطبيقات جداول البيانات الحديثة. وعلى العكس من ذلك، يمكنك أخذ البيانات من ملف XLSX أو CSV وتصديرها إلى تنسيق DBF للتكامل مع الأنظمة القديمة.



{{< app/cells/assistant language="javascript" >}}