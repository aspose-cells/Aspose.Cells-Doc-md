---
title: إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: إضافة حقول التصفية
description: تعرف على كيفية إضافة وتكوين حقول التصفية في الجداول المحورية باستخدام Aspose.Cells for .NET، بما في ذلك إضافة حقول التصفية، والتصفية بتحديد فردي، والتصفية بتحديد متعدد.
keywords: Aspose.Cells, .NET, جدول محوري, حقل صفحة, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, تصفية
type: docs
weight: 250
url: /ar/net/add-filter-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells دورة الحياة الكاملة لحقول التصفية في الجداول المحورية. يمكنك إضافة حقل صفحة من خلال واجهة برمجة تطبيقات عالية المستوى ملائمة أو من خلال المجموعة منخفضة المستوى `PageFields`، ويمكنك التحكم في مرشح الصفحة في وضع التحديد الفردي، أو مسحه لإظهار جميع عناصر الصفحة، أو تبديل الحقل إلى وضع التحديد المتعدد حتى يتمكن المستخدمون من اختيار عدة عناصر صفحة في وقت واحد من خلال واجهة المستخدم الخاصة بخانات الاختيار في Excel.
{{% /alert %}}

## **مقدمة**

حقل التصفية هو حقل محوري يتحكم في *أي مجموعة فرعية* من البيانات المصدر يعرضها جسم الجدول المحوري. يراه المستخدمون النهائيون كقائمة منسدلة في أعلى الجدول المحوري المُقدَّم في Excel، ويؤدي اختيار أحد عناصر الصفحة المتاحة إلى إعادة بناء جسم الجدول المحوري بحيث يتم تلخيص السجلات التي تنتمي إلى عنصر التصفية هذا فقط. يصبح الحقل المحوري حقل صفحة عند تسجيله كـ `PivotFieldType.Page` بدلاً من `PivotFieldType.Row` أو `PivotFieldType.Column` أو `PivotFieldType.Data`.

يمكن أن يعمل حقل التصفية بسلوكين. في سلوك **التحديد الفردي** الافتراضي، يكون عنصر صفحة واحد فقط مرئياً في كل مرة، لذلك يلخص جسم الجدول المحوري مجموعة فرعية واحدة بالضبط. في سلوك **التحديد المتعدد**، يعرض الحقل قائمة بخانات الاختيار، ويلخص جسم الجدول المحوري اتحاد كل عناصر الصفحة المحددة. يمكن نقل نفس الحقل المصدر ذهاباً وإياباً بين هذين السلوكين عن طريق تبديل خاصية واحدة فقط.

يوفر Aspose.Cells for .NET طريقتين متكافئتين لتسجيل حقل التصفية. واجهة برمجة التطبيقات عالية المستوى هي `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`، التي تأخذ اسم عمود المصدر وتضيف الحقل في استدعاء واحد. واجهة برمجة التطبيقات منخفضة المستوى هي `PivotTable.PageFields.Add(PivotField)`، التي تُستخدم عندما يكون لديك بالفعل مرجع `PivotField` وتريد إضافة نفس مثيل الحقل إلى منطقة التصفية. تنتهي كلتا واجهات برمجة التطبيقات بتعبئة نفس مجموعة `PageFields`، وتوضح بقية هذه المقالة كيفية الاختيار بينهما وكيفية التحكم في كل وضع تصفية.

## **إضافة حقل صفحة**

هناك طريقتان لتسجيل حقل محوري في منطقة التصفية. يأخذ الاستدعاء عالي المستوى اسم عمود المصدر كسلسلة نصية وهو المسار الأكثر شيوعاً. يقبل الاستدعاء منخفض المستوى مثيل `PivotField` موجوداً وهو ملائم عندما يجب إعادة استخدام نفس كائن الحقل عبر مناطق محورية متعددة. يضع كلا الاستدعاءين الحقل في `PivotTable.PageFields`، وبعد ذلك يظهر كقائمة منسدلة للصفحة في أعلى الجدول المحوري المُقدَّم.

### إضافة حقل صفحة باستخدام AddFieldToArea

يبني المثال التالي مجموعة بيانات صغيرة مكونة من الفاكهة / السنة / المبلغ، ويضع جدولاً محورياً في الخلية E3 مع `Fruit` في منطقة الصفوف، و`Amount` في منطقة البيانات، و`Year` في منطقة التصفية، ويقوم بتحديث الجدول المحوري، ويحفظ المصنف.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// إنشاء مصنف جديد
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// إعداد صف الرأس
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// تعبئة 9 صفوف من البيانات النموذجية: الفاكهة، السنة، المبلغ
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}

// إضافة جدول محوري مثبت عند الخلية E3
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// إضافة الحقول إلى مناطقها: الفاكهة كصف، المبلغ كبيانات، السنة كحقل صفحة
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// تحديث وحساب بيانات الجدول المحوري
pivotTable.RefreshData();
pivotTable.CalculateData();

// حفظ المصنف
workbook.Save("pageFieldSample.xlsx");
```

### إضافة حقل صفحة باستخدام PageFields.Add

عندما تعمل بالفعل مع مثيل `PivotField`، يمكنك تمريره مباشرة إلى `PivotTable.PageFields.Add`. يتم إنشاء الجدول المحوري وحقل التصفية تماماً كما في السيناريو السابق؛ فقط تسجيل منطقة التصفية النهائي يتم استبداله باستدعاء واجهة برمجة التطبيقات منخفض المستوى.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — يتم إنشاء الجدول المحوري وحقل الصفحة تمامًا كما في
//   السيناريو 1أ (بيانات الفاكهة/السنة/المبلغ، المحور عند E3، الفاكهة→صف،
//   المبلغ→بيانات). أدناه نحصل على حقل المحور للسنة من
//   مجموعة BaseFields ونمرره إلى PageFields.Add — وهو
//   البديل منخفض المستوى لـ AddFieldToArea. النتيجة هي
//   مطابقة وظيفيًا للسيناريو 1أ.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// الرؤوس
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// بيانات العينة (9 صفوف)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// إضافة جدول محوري عند E3 يغطي A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// الفاكهة -> صف، المبلغ -> بيانات (ستذهب السنة إلى الصفحة أدناه)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// نهج منخفض المستوى: استرد حقل المحور الحالي للسنة من BaseFields
// وسجله في منطقة الصفحة عبر PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// قم بالتحديث حتى ينعكس حقل الصفحة الجديد في المصنف المحفوظ
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **التصفية بتحديد فردي (إظهار عنصر صفحة واحد)**

في سلوك التحديد الفردي الافتراضي، يُقدَّم حقل التصفية كقائمة منسدلة مفردة ويحدد عدد صحيح `PivotField.CurrentPageItem` عنصر التصفية الذي يقود جسم الجدول المحوري. يؤدي تعيين فهرس محدد إلى اختيار هذا العنصر فقط؛ ويؤدي تعيين القيمة الحارسية الخاصة `0x7FFD` (بالعشري 32765) إلى مسح المرشح بحيث يتم تلخيص جميع عناصر الصفحة دفعة واحدة. التحديد الفردي هو الوضع الافتراضي؛ لست بحاجة إلى تمكينه صراحةً.

### إظهار جميع العناصر

يعد تعيين `CurrentPageItem` على القيمة السحرية `0x7FFD` مكافئاً لمسح مرشح الصفحة: يلخص جسم الجدول المحوري جميع عناصر الصفحة كما لو لم يتم تطبيق أي مرشح.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // إنشاء مصنف جديد
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // تعبئة بيانات الفاكهة/السنة/المبلغ
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");

        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };

        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }

        // إنشاء جدول محوري في E3
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // تكوين حقول الجدول المحوري: الفاكهة→الصف، المبلغ→البيانات، السنة→الصفحة
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.RefreshData();
        pivotTable.CalculateData();

        // مسح مرشح الصفحة بحيث تكون كل العناصر في حقل الصفحة مرئية.
        // 0x7FFD (عشري 32765) هي قيمة الحارس الخاصة التي تعني "كل العناصر" —
        // مكافئة لتحديد "(الكل)" في القائمة المنسدلة لحقل الصفحة في Excel.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}
```

### إظهار عنصر محدد واحد

يؤدي تعيين `CurrentPageItem` على فهرس حقيقي إلى اختيار عنصر صفحة واحد فقط. الفهرس هو موضع العنصر في قائمة العناصر المرتبة لحقل التصفية، فعلى سبيل المثال يحدد `1` العنصر الثاني بعد الترتيب.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// إنشاء مصنف
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// إضافة بيانات عينة (فاكهة/سنة/مبلغ)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");

cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");

cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");

cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");

cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");

// إضافة جدول محوري في E3
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// إضافة الحقول: فاكهة→صف، مبلغ→بيانات، سنة→صفحة
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// عمليات خاصة بحقل الصفحة
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = العنصر الثاني بالترتيب الفرز (مثلاً "2021")

// تحديث وحساب الجدول المحوري
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **التصفية بتحديد متعدد**

تحول التصفية بتحديد متعدد القائمة المنسدلة للصفحة إلى قائمة بخانات الاختيار وتتيح للمستخدم النهائي اختيار عدة عناصر صفحة في وقت واحد. يكشف Aspose.Cells عن خاصيتين تعملان معاً. يجب تعيين `PivotField.IsMultipleItemSelectionAllowed` على `true` قبل أن تصبح واجهة المستخدم متعددة التحديد فعالة على الإطلاق. بعد تمكينها، تتحكم `PivotItem.IsHidden` في العناصر التي تظهر في قائمة خانات الاختيار، بحيث يمكنك إما إظهار جميع العناصر أو السماح فقط بعناصر محددة.

يقوم الكود أدناه بتمكين التحديد المتعدد على نفس حقل صفحة Year الذي تم إنشاؤه في السيناريو 1a، ثم يعرض نمطين: الجزء A يكشف عن جميع عناصر الصفحة عن طريق ترك `IsHidden` معيناً على `false` لكل إدخال، بينما يقوم الجزء B بالسماح بقيم المصدر التي تختارها فقط وإخفاء كل شيء آخر من خلال كتلة `switch (pivotItems[i].GetStringValue())`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — يتم إنشاء الجدول المحوري وحقل الصفحة تمامًا كما في
//   السيناريو 1a (بيانات الفاكهة/السنة/المبلغ، الجدول المحوري عند E3، الفاكهة→صف،
//   المبلغ→بيانات، السنة→صفحة عبر AddFieldToArea).
//   أدناه نطبق تصفية التحديد المتعدد على حقل الصفحة.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// بيانات النموذج: الفاكهة | السنة | المبلغ
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");

string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}

Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — تفعيل التحديد المتعدد على حقل الصفحة
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// الجزء A — تحديد جميع العناصر (جعل كل عنصر مرئيًا)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}

// الجزء B — تحديد عناصر محددة فقط حسب القيمة المصدر
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

> **ملاحظة:** عند استخدام التصفية بتحديد متعدد من خلال `PivotItem.IsHidden`، **يجب أن يظل عنصر `PivotItem` واحد على الأقل مرئياً** (`IsHidden == false`). إذا تم إخفاء كل العناصر، فإن Excel إما يتعطل عند فتح الملف أو يُقدِّم جدولاً محورياً فارغاً. تحقق دائماً من أن قائمتك المسموح بها متعددة التحديد تتضمن عنصراً واحداً على الأقل من بياناتك المصدر.

## **أي واجهة برمجة تطبيقات وأي وضع يجب أن أستخدم؟**

يلخص الجدول أدناه متى تستخدم كل واجهة برمجة تطبيقات ووضع حتى تتمكن من اختيار التركيبة المناسبة دون قراءة كل سيناريو بالتفصيل.

| السيناريو / حالة الاستخدام | واجهة برمجة التطبيقات الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل صفحة حسب اسم عمود المصدر (الأكثر شيوعاً) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | غير قابل للتطبيق | عالية المستوى، سطر واحد. استخدم هذا ما لم تكن بحاجة إلى مرجع `PivotField`. |
| إضافة حقل صفحة عندما يكون لديك بالفعل كائن `PivotField` | `PivotTable.PageFields.Add(PivotField)` | غير قابل للتطبيق | استخدم عندما يتم الحصول على كائن الحقل من مكان آخر أو يحتاج إلى إعادة الاستخدام. |
| التصفية إلى عنصر صفحة واحد (الوضع الافتراضي) | `PivotField.CurrentPageItem` | عيّن على فهرس محدد | على سبيل المثال، يعرض `1` العنصر الثاني في القائمة المرتبة. |
| إظهار جميع العناصر / مسح مرشح الصفحة | `PivotField.CurrentPageItem` | عيّن على `0x7FFD` | القيمة السحرية `0x7FFD` (بالعشري 32765) هي القيمة الحارسية لـ "جميع العناصر". |
| تمكين واجهة المستخدم متعددة التحديد في Excel | `PivotField.IsMultipleItemSelectionAllowed` | عيّن على `true` | مطلوب قبل أن تصبح أي استدعاءات لـ `IsHidden` فعالة. |
| إخفاء / إظهار عناصر فردية في قائمة متعددة التحديد | `PivotItem.IsHidden` | عيّن لكل عنصر | يجب أن يظل عنصر واحد على الأقل مرئياً (`IsHidden == false`). |

{{% alert color="primary" %}}
تذكر دائماً قيد الرؤية عند تكوين التصفية بتحديد متعدد. إذا تم إخفاء كل `PivotItem` في حقل صفحة متعدد التحديد، فإن Excel يتعطل عند الفتح أو يُقدِّم جدولاً محورياً فارغاً. أنشئ قائمتك المسموح بها مقابل بياناتك المصدر بحيث يظل عنصر واحد على الأقل مرئياً، وستفتح مصنفاتك المحفوظة بشكل موثوق على كل جهاز.
{{% /alert %}}

## **مقالات ذات صلة**

- [تحديث الجداول المحورية في Aspose.Cells for .NET](/cells/ar/net/refresh-pivot-table/)
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/net/splitting-excel-files-into-multiple-files/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/net/apply-style-to-pivot-table/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/net/ofd/)
- [عرض مصفوفة خلية واحدة في SmartMarker | Aspose.Cells .NET](/cells/ar/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}
