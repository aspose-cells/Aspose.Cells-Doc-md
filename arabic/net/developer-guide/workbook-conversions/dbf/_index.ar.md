---
title: قراءة وكتابة ملفات DBF
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات، وتدعم قراءة وكتابة ملفات dBASE III وIV (DBF). توضح هذه المقالة كيفية استيراد البيانات من وتصدير البيانات إلى ملفات DBF باستخدام Aspose.Cells، بما في ذلك تفاصيل تنسيق الملف والميزات المدعومة وأمثلة خطوة بخطوة.
keywords: Aspose.Cells, .NET library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /ar/net/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

توفر Aspose.Cells دعمًا كاملاً لقراءة وكتابة ملفات DBF (dBASE). يمكنك تحميل ملفات dBASE III وdBASE IV الموجودة في كائن Workbook، ومعالجة البيانات باستخدام واجهة برمجة التطبيقات الغنية لـ Aspose.Cells، ثم حفظ المصنف مرة أخرى بتنسيق DBF لاستخدامه مع تطبيقات قواعد البيانات القديمة.

{{% /alert %}}

## **المقدمة**

ملف DBF (DataBase File) هو تنسيق ملف قاعدة بيانات قديم تم تقديمه في الأصل بواسطة dBASE في أوائل الثمانينيات. على الرغم من قدم هذا التنسيق، لا تزال ملفات DBF تُستخدم على نطاق واسع في العديد من الصناعات لتخزين البيانات المنظمة، لا سيما في المحاسبة ونظم المعلومات الجغرافية والتطبيقات المتخصصة الأخرى. تتيح لك Aspose.Cells دمج هذه الملفات القديمة في سير عمل جداول البيانات الحديثة على .NET بسلاسة.

تدعم المكتبة كلاً من قراءة وكتابة ملفات DBF، مما يمنحك القدرة على:

- استيراد البيانات من ملفات DBF الموجودة إلى كائنات Workbook الخاصة بـ Aspose.Cells لمزيد من المعالجة أو التحويل إلى تنسيقات أخرى.
- إنشاء ملفات DBF جديدة من الصفر أو عن طريق تحويل البيانات من تنسيقات جداول بيانات أخرى.
- الحفاظ على تعريفات الحقول وأنواع البيانات وهياكل السجلات عند نقل البيانات من وإلى تنسيق DBF.

يمكن أيضًا فتح ملفات DBF مباشرة في Microsoft Excel وتطبيقات جداول البيانات الأخرى، مما يجعلها جسرًا ملائمًا بين الأنظمة القديمة وأدوات جداول البيانات الحديثة.

## **إصدارات وميزات DBF المدعومة**

تدعم Aspose.Cells إصدارات تنسيق DBF التالية:

- **dBASE III** — الإصدار الأصلي والأكثر دعمًا على نطاق واسع من تنسيق DBF.
- **dBASE IV** — إصدار موسع يدعم أنواع بيانات إضافية وأحجام حقول أكبر.

### الميزات المدعومة

توفر المكتبة دعمًا شاملاً للعمليات التالية:

- قراءة بيانات DBF في كائن Workbook، مع الحفاظ على جميع السجلات وتعريفات الحقول.
- كتابة بيانات المصنف مرة أخرى بتنسيق DBF للتصدير إلى التطبيقات المتوافقة مع dBASE.
- التعامل مع أنواع البيانات الشائعة المستخدمة في ملفات DBF، بما في ذلك الحقول الحرفية والرقمية والتاريخية والمنطقية.
- الحفاظ على تعريفات الحقول مثل اسم الحقل ونوعه وطوله أثناء عمليات القراءة/الكتابة.

### القيود والاعتبارات

عند العمل مع ملفات DBF، يجب مراعاة القيود التالية:

- الحد الأقصى لعدد الحقول في الملف هو **128**.
- الحد الأقصى لحجم السجل هو **4000 بايت**.
- أسماء الحقول محدودة بـ **10 أحرف**، ويجب أن تكون بأحرف كبيرة، ولا يمكن أن تحتوي على مسافات.
- تُخزن قيم التاريخ في ملفات DBF بتنسيق `YYYYMMDD`.
- قد يختلف ترميز الأحرف حسب التطبيق المصدر (عادةً Windows-1252 أو صفحات رموز OEM).

## **قراءة ملف DBF**

تجعل Aspose.Cells تحميل البيانات من ملف DBF إلى كائن Workbook أمرًا سهلاً. تستخدم المكتبة الفئة `LoadOptions` لتحديد تنسيق المصدر، مما يضمن تفسير البيانات بشكل صحيح أثناء عملية التحميل.

### قراءة ملف DBF باستخدام Aspose.Cells

لقراءة ملف DBF، تحتاج إلى إنشاء مثيل من `LoadOptions`، وتعيين خاصية `LoadFormat` الخاصة به إلى `LoadFormat.Dbf`، وتمريرها إلى مُنشئ `Workbook` مع مسار الملف. بمجرد التحميل، تصبح البيانات قابلة للوصول من خلال مجموعة `Worksheets`، حيث يمكنك التكرار عبر الخلايا واستخراج القيم ومعالجة البيانات حسب الحاجة.

يوضح المثال التالي كيفية تحميل ملف DBF موجود في Aspose.Cells، والوصول إلى ورقة العمل الأولى، وقراءة قيم الخلايا.

```csharp
using System;
using System.IO;
using System.Text;
using Aspose.Cells;

string dataDir = "Data/";
string filePath = Path.Combine(dataDir, "example.dbf");

LoadOptions loadOptions = new LoadOptions(LoadFormat.Dbf);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.Worksheets[0];

Cells cells = worksheet.Cells;

StringBuilder sb = new StringBuilder();

int maxRow = cells.MaxDataRow;
int maxCol = cells.MaxDataColumn;

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells[i, j];
        string value = cell.StringValue;
        sb.Append("|").Append(value);
    }
    sb.Append("|").AppendLine();
}

Console.WriteLine(sb.ToString());

string outputPath = Path.Combine(dataDir, "output.xlsx");
workbook.Save(outputPath, SaveFormat.Xlsx);

Console.WriteLine("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

يمكنك فتح ملفات DBF مباشرة في Microsoft Excel عن طريق تحديد الملف في مربع حوار الفتح. سيعامل Excel ملف DBF كجدول بيانات، مع عرض سجلاته في تخطيط جدولي. يكون هذا مفيدًا للتحقق السريع من البيانات بعد قراءتها أو كتابتها باستخدام Aspose.Cells.

{{% /alert %}}

## **كتابة ملف DBF**

تتبع كتابة البيانات في ملف DBF نمطًا مشابهًا لحفظ أي تنسيق جدول بيانات آخر باستخدام Aspose.Cells. يمكنك إنشاء مصنف أو تحميله، وملء ورقة العمل بالبيانات، ثم استدعاء طريقة `Save` مع تحديد `SaveFormat.Dbf` كتنسيق هدف.

### كتابة ملف DBF باستخدام Aspose.Cells

لإنشاء ملف DBF، اتبع الخطوات التالية:

1. أنشئ مثيلًا جديدًا من `Workbook`.
2. الوصول إلى ورقة العمل الأولى من مجموعة `Worksheets`.
3. ملء ورقة العمل بالبيانات الخاصة بك، بما في ذلك العناوين في الصف الأول والسجلات في الصفوف اللاحقة.
4. استدعاء طريقة `Workbook.Save`، مع تمرير مسار الملف و`SaveFormat.Dbf` كمعاملات.

يوضح المثال التالي كيفية إنشاء ملف DBF جديد من الصفر. يملأ ورقة العمل ببيانات عينة تحتوي على أنواع بيانات مختلفة (سلاسل وأرقام وتواريخ) لتوضيح كيفية التعامل مع أنواع الحقول عند التصدير إلى تنسيق DBF.

```csharp
using System;
using System.IO;
using Aspose.Cells;

string outputDir = @"C:\Output\";
string filePath = Path.Combine(outputDir, "output.dbf");

if (!Directory.Exists(outputDir))
{
    Directory.CreateDirectory(outputDir);
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;

// رؤوس الأعمدة
cells[0, 0].PutValue("ID");
cells[0, 1].PutValue("Name");
cells[0, 2].PutValue("Department");
cells[0, 3].PutValue("Salary");
cells[0, 4].PutValue("HireDate");

// صف البيانات 1
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));

// صف البيانات 2
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));

// صف البيانات 3
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));

// صف البيانات 4
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));

// صف البيانات 5
cells[5, 0].PutValue(105);
cells[5, 1].PutValue("Charlie Wilson");
cells[5, 2].PutValue("Operations");
cells[5, 3].PutValue(79500.80);
cells[5, 4].PutValue(new DateTime(2022, 5, 30));

// تعيين عرض الأعمدة لتحسين القراءة
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);

workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}

عند كتابة البيانات في ملف DBF، تأكد من أن بياناتك تتوافق مع قيود التنسيق. يجب ألا يتجاوز طول أسماء الحقول 10 أحرف ولا يجب أن تحتوي على مسافات. لن يتم حفظ السجلات التي يتجاوز حجمها الإجمالي 4000 بايت بشكل صحيح. يجب أن تكون التواريخ قيم تاريخ صالحة يمكن تمثيلها بتنسيق YYYYMMDD.

{{% /alert %}}

## **اعتبارات نوع البيانات والتنسيق**

عند نقل البيانات بين Aspose.Cells وتنسيق DBF، يعد فهم كيفية تعيين أنواع البيانات بين النظامين أمرًا مهمًا لضمان سلامة البيانات.

### أنواع الخلايا إلى أنواع حقول DBF

يتم تحويل قيم خلايا Aspose.Cells تلقائيًا إلى أنواع حقول DBF المناسبة عند الحفظ:

- يتم تعيين **السلاسل النصية** إلى حقول الأحرف (C).
- يتم تعيين **القيم الرقمية** (الأعداد الصحيحة والعشرية) إلى الحقول الرقمية (N).
- يتم تعيين **قيم التاريخ** إلى حقول التاريخ (D) بتنسيق `YYYYMMDD`.
- يتم تعيين **القيم المنطقية** إلى الحقول المنطقية (L).

### الترميز

قد تستخدم ملفات DBF ترميزات أحرف مختلفة حسب التطبيق الذي أنشأها. تتعامل Aspose.Cells مع الترميز بشفافية في معظم الحالات، ولكن إذا واجهت مشكلات في عرض الأحرف، فقد تحتاج إلى التحقق من ترميز الملف المصدر.

### قواعد أسماء الحقول

يجب أن تلتزم أسماء حقول DBF بالقواعد التالية:

- الحد الأقصى للطول هو 10 أحرف.
- يجب أن تبدأ بحرف.
- لا يمكن أن تحتوي على مسافات أو أحرف خاصة.
- يتم تخزينها بأحرف كبيرة بغض النظر عن الحالة المستخدمة في الإدخال.

### التحقق من الناتج

بعد كتابة ملف DBF، يمكنك التحقق من الناتج عن طريق فتحه في Microsoft Excel أو أي تطبيق متوافق مع dBASE. يجب أن تظهر البيانات في تخطيط جدولي مع أسماء الحقول كعناوين أعمدة، والسجلات مملوءة وفقًا للبيانات التي قدمتها.

## **التحويل بين DBF والتنسيقات الأخرى**

من أكثر حالات الاستخدام العملية لقراءة وكتابة ملفات DBF باستخدام Aspose.Cells هو تحويل البيانات بين تنسيق DBF وتنسيقات جداول البيانات الحديثة مثل XLSX أو XLS أو CSV. نظرًا لأن Aspose.Cells تدعم مجموعة واسعة من التنسيقات، يمكنك بسهولة تحميل ملف DBF وإعادة حفظه بأي تنسيق مدعوم آخر، أو العكس.

على سبيل المثال، يمكنك قراءة ملف DBF، وتطبيق التنسيق أو الحسابات باستخدام واجهة برمجة تطبيقات Aspose.Cells، ثم حفظ الناتج كملف XLSX لتوزيعه على المستخدمين الذين يعملون مع تطبيقات جداول البيانات الحديثة. وعلى العكس، يمكنك أخذ البيانات من ملف XLSX أو CSV وتصديرها إلى تنسيق DBF للتكامل مع الأنظمة القديمة.



{{< app/cells/assistant language="csharp" >}}