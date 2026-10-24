---
title: قراءة وكتابة ملفات DBF
linktitle: قراءة وكتابة ملفات DBF
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات، وتدعم قراءة ملفات dBASE III وIV (DBF) وكتابتها. يشرح هذا المقال كيفية استيراد البيانات من ملفات DBF وتصديرها إليها باستخدام Aspose.Cells، بما في ذلك تفاصيل تنسيق الملف والميزات المدعومة وأمثلة خطوة بخطوة.
keywords: Aspose.Cells, مكتبة .NET, DBF, dBASE, قراءة DBF, كتابة DBF, استيراد DBF, تصدير DBF, تنسيق الملف, .dbf
type: docs
weight: 200
url: /ar/net/reading-and-writing-dbf-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells دعمًا كاملًا لقراءة ملفات DBF (dBASE) وكتابتها. يمكنك تحميل ملفات dBASE III وdBASE IV القائمة في كائن `Workbook`، ومعالجة البيانات باستخدام واجهة API الغنية في Aspose.Cells، ثم حفظ المصنف مرة أخرى بتنسيق DBF لاستخدامه مع تطبيقات قواعد البيانات القديمة.
{{% /alert %}}

## **مقدمة**
DBF (ملف قاعدة البيانات) هو تنسيق قديم لقواعد البيانات، أُطلق أولًا من قِبل dBASE في مطلع الثمانينيات. ورغم قِدم هذا التنسيق، لا تزال ملفات DBF مستخدمة على نطاق واسع في قطاعات عديدة لتخزين البيانات المنظمة، ولا سيما في المحاسبة ونظم المعلومات الجغرافية (GIS) والتطبيقات المتخصصة الأخرى. يتيح Aspose.Cells إدماج هذه الملفات القديمة بسلاسة ضمن تدفقات عمل جداول بيانات .NET الحديثة.
تدعم المكتبة القراءة وكتابة ملفات DBF، مما يمنحك القدرة على:
- استيراد البيانات من ملفات DBF الموجودة إلى كائنات `Workbook` في Aspose.Cells للمعالجة الإضافية أو التحويل إلى تنسيقات أخرى.
- إنشاء ملفات DBF جديدة من الصفر أو من خلال تحويل البيانات من تنسيقات جداول البيانات الأخرى.
- الحفاظ على تعريفات الحقول وأنواع البيانات وبنى السجلات عند نقل البيانات من تنسيق DBF وإليه.
كما يمكن فتح ملفات DBF مباشرةً في Microsoft Excel وتطبيقات جداول البيانات الأخرى، مما يجعلها جسرًا ملائمًا بين الأنظمة القديمة وأدوات جداول البيانات الحديثة.

## **إصدارات DBF المدعومة والميزات**
يدعم Aspose.Cells إصدارات تنسيق DBF التالية:
- **dBASE III** — التنويعة الأصلية والأكثر دعمًا لتنسيق DBF.
- **dBASE IV** — إصدار موسّع يدعم أنواع بيانات إضافية وأحجام حقول أكبر.

### **الميزات المدعومة**
توفر المكتبة دعمًا شاملًا للعمليات التالية:
- قراءة بيانات DBF في كائن `Workbook`، مع الحفاظ على جميع السجلات وتعريفات الحقول.
- كتابة بيانات المصنف مرة أخرى بتنسيق DBF لتصديرها إلى التطبيقات المتوافقة مع dBASE.
- معالجة أنواع البيانات الشائعة المستخدمة في ملفات DBF، بما في ذلك الحقول النصية والرقمية وحقول التاريخ والحقول المنطقية.
- الحفاظ على تعريفات الحقول مثل اسم الحقل ونوعه وطوله أثناء عمليات القراءة والكتابة.

### **القيود والاعتبارات**
عند العمل مع ملفات DBF، ضع القيود التالية في الاعتبار:
- الحد الأقصى لعدد الحقول في كل ملف هو **128**.
- الحد الأقصى لحجم السجل هو **4000 بايت**.
- تقتصر أسماء الحقول على **10 أحرف**، ويجب أن تكون بأحرف كبيرة، ولا أن تحتوي على مسافات.
- تُخزن قيم التاريخ في ملفات DBF بتنسيق `YYYYMMDD`.
- قد يختلف ترميز الأحرف حسب التطبيق الذي أنشأ الملف (وغالبًا يكون Windows-1252 أو صفحات ترميز OEM).

## **قراءة ملف DBF**
يبسّط Aspose.Cells تحميل البيانات من ملف DBF إلى كائن `Workbook`. تستخدم المكتبة فئة `LoadOptions` لتحديد تنسيق المصدر، مما يضمن تفسير البيانات بصورة صحيحة أثناء عملية التحميل.

### **قراءة ملف DBF باستخدام Aspose.Cells**
لقراءة ملف DBF، أنشئ مثيل `LoadOptions`، واضبط الخاصية `LoadFormat` على `LoadFormat.Dbf`، ثم مرّر هذا المثيل إلى المُنشئ `Workbook` مع مسار الملف. بمجرد التحميل، تصبح البيانات متاحة عبر مجموعة `Worksheets`، حيث يمكنك المرور على الخلايا واستخراج القيم أو معالجة البيانات حسب الحاجة.
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
يمكنك فتح ملفات DBF مباشرةً في Microsoft Excel عن طريق تحديد الملف في مربع حوار «فتح». سيعامل Excel ملف DBF على أنه جدول بيانات، ويعرض سجلاته في تخطيط جدولي. وهذا مفيد للتحقق سريعًا من البيانات بعد قراءتها أو كتابتها باستخدام Aspose.Cells.
{{% /alert %}}

## **كتابة ملف DBF**
تتبع كتابة البيانات إلى ملف DBF نمطًا مشابهًا لحفظ أي تنسيق آخر لجداول البيانات باستخدام Aspose.Cells. أنشئ مصنفًا أو حمّله، واملأ ورقة العمل بالبيانات، ثم استدعِ طريقة `Save` مع تحديد `SaveFormat.Dbf` كتنسيق هدف.

### **كتابة ملف DBF باستخدام Aspose.Cells**
لإنشاء ملف DBF، اتبع الخطوات التالية:
1. أنشئ مثيلاً جديدًا من `Workbook`.
2. احصل على ورقة العمل الأولى من مجموعة `Worksheets`.
3. املأ ورقة العمل ببياناتك، بما في ذلك رؤوس الأعمدة في الصف الأول والسجلات في الصفوف التالية.
4. استدعِ طريقة `Workbook.Save`، مع تمرير مسار الملف و`SaveFormat.Dbf` كمعاملات.
يوضح المثال التالي كيفية إنشاء ملف DBF جديد من الصفر. يملأ ورقة العمل ببيانات نموذجية تتضمن أنواع بيانات مختلفة (نصوص وأرقام وتواريخ) لتوضيح كيفية معالجة أنواع الحقول عند التصدير إلى تنسيق DBF.

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
// الصف الأول من البيانات
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));
// الصف الثاني من البيانات
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));
// الصف الثالث من البيانات
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));
// الصف الرابع من البيانات
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));
// الصف الخامس من البيانات
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
عند كتابة البيانات إلى ملف DBF، تأكد من توافق بياناتك مع قيود التنسيق. يجب ألا يزيد طول أسماء الحقول على 10 أحرف، ولا تحتوي على مسافات. لن تُحفظ السجلات التي يتجاوز حجمها الإجمالي 4000 بايت بصورة صحيحة. يجب أن تكون التواريخ قيمًا تاريخية صالحة يمكن تمثيلها بتنسيق YYYYMMDD.
{{% /alert %}}

## **اعتبارات أنواع البيانات والتنسيق**
عند نقل البيانات بين Aspose.Cells وتنسيق DBF، من المهم فهم كيفية مطابقة أنواع البيانات بين النظامين لضمان سلامة البيانات.

### **أنواع الخلايا إلى أنواع حقول DBF**
يتم تحويل قيم الخلايا في Aspose.Cells تلقائيًا إلى أنواع حقول DBF المناسبة عند الحفظ:
- **النصوص** تُعيَّن إلى حقول المحارف (C).
- **القيم الرقمية** (الأعداد الصحيحة والعشرية) تُعيَّن إلى الحقول الرقمية (N).
- **قيم التاريخ** تُعيَّن إلى حقول التاريخ (D) بتنسيق `YYYYMMDD`.
- **القيم المنطقية** تُعيَّن إلى الحقول المنطقية (L).

### **الترميز**
قد تستخدم ملفات DBF ترميزات أحرف مختلفة حسب التطبيق الذي أنشأها. يتعامل Aspose.Cells مع الترميز بشفافية في معظم الحالات، لكن إذا واجهت مشكلات في عرض الأحرف، فقد تحتاج إلى التحقق من ترميز الملف المصدر.

### **قواعد أسماء الحقول**
يجب أن تلتزم أسماء حقول DBF بالقواعد التالية:
- الحد الأقصى للطول هو 10 أحرف.
- يجب أن تبدأ بحرف.
- لا يمكن أن تحتوي على مسافات أو أحرف خاصة.
- تُخزن بأحرف كبيرة بغض النظر عن الأحرف الكبيرة والصغيرة المستخدمة في الإدخال.

### **التحقق من الناتج**
بعد كتابة ملف DBF، يمكنك التحقق من النتيجة عن طريق فتحه في Microsoft Excel أو أي تطبيق متوافق مع dBASE. ينبغي أن تظهر البيانات في تخطيط جدولي، وأن تظهر أسماء الحقول كرؤوس للأعمدة، مع ملء السجلات وفقًا للبيانات التي أدخلتها.

## **التحويل بين DBF والتنسيقات الأخرى**
يُعد تحويل البيانات بين تنسيق DBF وتنسيقات جداول البيانات الحديثة مثل XLSX وXLS أوCSV، عند قراءة ملفات DBF وكتابتها باستخدام Aspose.Cells، من أكثر حالات الاستخدام العملية. وبما أن Aspose.Cells يدعم مجموعة واسعة من التنسيقات، يمكنك بسهولة تحميل ملف DBF وإعادة حفظه بأي تنسيق آخر مدعوم، أو إجراء العملية العكسية.

{{< app/cells/assistant language="csharp" >}}