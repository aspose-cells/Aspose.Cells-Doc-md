---
title: إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: إضافة حقول التصفية
description: تعلّم كيفية إضافة وتكوين حقول الصفحة في الجداول المحورية باستخدام Aspose.Cells for Node.js via Java، بما في ذلك إضافة حقول الصفحة، والتصفية ذات التحديد الفردي، والتصفية متعددة التحديد.
keywords: Aspose.Cells, Node.js via Java, الجدول المحوري, حقل التصفية, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, تصفية
type: docs
weight: 250
url: /ar/nodejs-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells دورة الحياة الكاملة لحقول الصفحة في الجداول المحورية. يمكنك إضافة حقل صفحة من خلال واجهة برمجة تطبيقات ملائمة عالية المستوى أو من خلال المجموعة ذات المستوى الأدنى `PageFields`، ويمكنك تشغيل مرشح الصفحة في وضع التحديد الفردي، أو مسحه لإظهار كل عناصر الصفحة، أو تبديل الحقل إلى التحديد المتعدد بحيث يمكن للمستخدمين اختيار عدة عناصر صفحة في وقت واحد من خلال واجهة مربعات الاختيار في Excel.
{{% /alert %}}

## **المقدمة**

حقل التصفية هو حقل محوري يتحكم في *أي مجموعة فرعية* من البيانات المصدرية يعرضها جسم المحور. يراه المستخدمون النهائيون كقائمة منسدلة في أعلى المحور المعروض في Excel، ويؤدي اختيار أحد عناصر الصفحة المتاحة إلى إعادة بناء جسم المحور بحيث يتم تلخيص السجلات التي تنتمي إلى عنصر التصفية هذا فقط. يصبح الحقل المحوري حقل صفحة عند تسجيله كـ `PivotFieldType.Page` بدلاً من `PivotFieldType.Row` أو `PivotFieldType.Column` أو `PivotFieldType.Data`.

يمكن أن يعمل حقل التصفية بسلوكين. في السلوك الافتراضي **التحديد الفردي**، يكون عنصر صفحة واحد فقط مرئياً في كل مرة، لذلك يلخص جسم المحور مجموعة فرعية واحدة بالضبط. في سلوك **التحديد المتعدد**، يعرض الحقل قائمة مربعات اختيار، ويلخص جسم المحور اتحاد كل عناصر الصفحة المحددة. يمكن نقل نفس الحقل المصدر ذهاباً وإياباً بين هذه السلوكيات عن طريق تبديل خاصية واحدة.

يوفر Aspose.Cells for Node.js via Java طريقتين متكافئتين لتسجيل حقل صفحة. واجهة برمجة التطبيقات عالية المستوى هي `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`، التي تأخذ اسم عمود المصدر وتضيف الحقل في استدعاء واحد. واجهة برمجة التطبيقات ذات المستوى الأدنى هي `pivotTable.getPageFields().add(PivotField)`، التي تُستخدم عندما يكون لديك بالفعل مرجع `PivotField` وتريد إضافة نفس مثيل الحقل إلى منطقة التصفية. تنتهي كلتا واجهتي برمجة التطبيقات إلى ملء نفس مجموعة `PageFields`، وتوضح بقية هذه المقالة كيفية الاختيار بينهما وكيفية تشغيل كل وضع تصفية.

## **إضافة حقل صفحة**

هناك طريقتان لتسجيل حقل محوري في منطقة التصفية. يأخذ الاستدعاء عالي المستوى اسم عمود المصدر كسلسلة وهو المسار الأكثر شيوعاً. يقبل الاستدعاء ذو المستوى الأدنى مثيل `PivotField` موجوداً وهو مناسب عندما يجب إعادة استخدام نفس كائن الحقل عبر مناطق محورية متعددة. يضع كلا الاستدعاءين الحقل في `pivotTable.getPageFields()`، وبعد ذلك يظهر كقائمة منسدلة للصفحة في أعلى المحور المعروض.

### إضافة حقل صفحة باستخدام addFieldToArea

يبني المثال التالي مجموعة بيانات صغيرة مكونة من أعمدة Fruit وYear وAmount، ويضع جدولاً محورياً في الخلية E3 مع `Fruit` في منطقة الصفوف، و`Amount` في منطقة البيانات، و`Year` في منطقة التصفية، ويقوم بتحديث المحور، ويحفظ المصنف.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// إعداد صف الرأس
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// تعبئة 9 صفوف من البيانات النموذجية: الفاكهة، السنة، المبلغ
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// إضافة جدول محوري مثبت في الخلية E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// إضافة الحقول إلى مناطقها: الفاكهة كصف، المبلغ كبيانات، السنة كحقل صفحة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// تحديث وحساب بيانات الجدول المحوري
pivotTable.refreshData();
pivotTable.calculateData();

// حفظ المصنف
workbook.save("pageFieldSample.xlsx");
```

### إضافة حقل صفحة باستخدام getPageFields().add

عندما تعمل بالفعل مع مثيل `PivotField`، يمكنك تمريره مباشرة إلى `pivotTable.getPageFields().add`. يتم إنشاء الجدول المحوري وحقل التصفية تماماً كما في السيناريو السابق؛ فقط تسجيل منطقة التصفية النهائي يتم استبداله باستدعاء واجهة برمجة التطبيقات ذات المستوى الأدنى.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// العناوين
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// بيانات نموذجية (9 صفوف)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// إضافة جدول محوري في E3 يغطي A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// الفاكهة -> الصف، المبلغ -> البيانات (السنة ستذهب إلى الصفحة أدناه)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// نهج منخفض المستوى: احصل على حقل السنة المحوري الموجود من BaseFields
// وقم بتسجيله في منطقة الصفحة عبر PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// قم بالتحديث حتى ينعكس حقل الصفحة الجديد في المصنف المحفوظ
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **التصفية ذات التحديد الفردي (إظهار عنصر صفحة واحد)**

في سلوك التحديد الفردي الافتراضي، يُعرض حقل التصفية كقائمة منسدلة واحدة ويحدد العدد الصحيح `PivotField.CurrentPageItem` عنصر التصفية الذي يقود جسم المحور. يؤدي تعيين فهرس محدد إلى اختيار هذا العنصر الوحيد؛ ويؤدي تعيين القيمة الحارسة الخاصة `0x7FFD` (عشري 32765) إلى مسح المرشح بحيث يتم تلخيص كل عناصر الصفحة دفعة واحدة. التحديد الفردي هو الافتراضي؛ لست بحاجة إلى تمكينه صراحةً.

### **إظهار كل العناصر**

يعد تعيين `CurrentPageItem` على القيمة السحرية `0x7FFD` مكافئاً لمسح مرشح الصفحة، حيث يلخص جسم المحور كل عناصر الصفحة كما لو لم يتم تطبيق أي مرشح.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// تعبئة بيانات الفاكهة/السنة/المبلغ
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// إنشاء جدول محوري عند E3
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// تكوين حقول الجدول المحوري: الفاكهة→الصف، المبلغ→البيانات، السنة→الصفحة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// مسح مرشح الصفحة بحيث يكون كل عنصر في حقل الصفحة مرئيًا.
// 0x7FFD (عشري 32765) هي القيمة الحارسة الخاصة التي تعني "كل العناصر" —
// تعادل تحديد "(الكل)" في القائمة المنسدلة لحقل الصفحة في Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### **إظهار عنصر محدد واحد**

يؤدي تعيين `CurrentPageItem` على فهرس حقيقي إلى اختيار عنصر التصفية الواحد فقط. الفهرس هو موضع العنصر في قائمة العناصر المرتبة لحقل التصفية، لذلك على سبيل المثال يحدد `1` العنصر الثاني بعد الترتيب.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// إضافة بيانات عينة (فاكهة/سنة/مبلغ)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// إضافة جدول محوري عند E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// إضافة الحقول: فاكهة→صف، مبلغ→بيانات، سنة→صفحة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// عمليات خاصة بحقل الصفحة
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = العنصر الثاني بالترتيب (مثلاً "2021")

// تحديث وحساب الجدول المحوري
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **التصفية متعددة التحديد**

تحول التصفية متعددة التحديد القائمة المنسدلة للصفحة إلى قائمة مربعات اختيار وتتيح للمستخدم النهائي اختيار عدة عناصر صفحة في وقت واحد. يعرض Aspose.Cells خاصيتين تعملان معاً. يجب تعيين `PivotField.IsMultipleItemSelectionAllowed` على `true` قبل أن تصبح واجهة المستخدم متعددة التحديد فعالة على الإطلاق. بعد تمكينها، تتحكم `PivotItem.IsHidden` في العناصر التي تظهر في قائمة مربعات الاختيار، لذلك يمكنك إما إظهار كل العناصر أو السماح فقط بعناصر محددة.

يقوم الكود أدناه بتمكين التحديد المتعدد على نفس حقل صفحة Year المبني في السيناريو 1a، ثم يعرض نمطين: الجزء A يكشف كل عناصر الصفحة بترك `IsHidden` مضبوطاً على `false` لكل إدخال، بينما الجزء B يسمح فقط بقيم المصدر التي تختارها ويخفي كل شيء آخر من خلال كتلة `switch (pivotItems[i].getStringValue())`.

```javascript
const AsposeCells = require("aspose.cells");

// — يتم إنشاء الجدول المحوري وحقل الصفحة تمامًا كما في
//   السيناريو 1a (بيانات الفاكهة/السنة/المبلغ، محوري عند E3، الفاكهة→الصف،
//   المبلغ→البيانات، السنة→الصفحة عبر AddFieldToArea).
//   أدناه نطبق تصفية الاختيار المتعدد على حقل الصفحة.

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// بيانات العينة: الفاكهة | السنة | المبلغ
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — تمكين الاختيار المتعدد على حقل الصفحة
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// الجزء A — تحديد جميع العناصر (جعل كل عنصر مرئيًا)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// الجزء B — تحديد عناصر محددة فقط حسب قيمة المصدر
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **ملاحظة:** عند استخدام التصفية متعددة التحديد من خلال `PivotItem.IsHidden`، **يجب أن يظل عنصر `PivotItem` واحد على الأقل مرئياً** (`IsHidden == false`). إذا تم إخفاء كل العناصر، فإن Excel إما يتعطل عند فتح الملف أو يعرض محوراً فارغاً. تحقق دائماً من أن القائمة البيضاء متعددة التحديد تتضمن عنصراً واحداً على الأقل من بيانات المصدر الخاصة بك.

## **أي واجهة برمجة تطبيقات وأي وضع يجب أن أستخدم؟**

يلخص الجدول أدناه متى تستخدم كل واجهة برمجة تطبيقات ووضع حتى تتمكن من اختيار التركيبة الصحيحة دون قراءة كل سيناريو بالتفصيل.

| السيناريو / حالة الاستخدام | واجهة برمجة التطبيقات الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل صفحة حسب اسم عمود المصدر (الأكثر شيوعاً) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | لا ينطبق | عالية المستوى، سطر واحد. استخدم هذا ما لم تكن بحاجة إلى مرجع `PivotField`. |
| إضافة حقل صفحة عندما يكون لديك بالفعل كائن `PivotField` | `pivotTable.getPageFields().add(PivotField)` | لا ينطبق | استخدم عندما تم الحصول على كائن الحقل من مكان آخر أو يحتاج إلى إعادة استخدامه. |
| التصفية إلى عنصر صفحة واحد (الوضع الافتراضي) | `PivotField.CurrentPageItem` | تعيين إلى فهرس محدد | على سبيل المثال، يعرض `1` العنصر الثاني في القائمة المرتبة. |
| إظهار كل العناصر / مسح مرشح الصفحة | `PivotField.CurrentPageItem` | تعيين إلى `0x7FFD` | القيمة السحرية `0x7FFD` (عشري 32765) هي القيمة الحارسة لـ "كل العناصر". |
| تمكين واجهة المستخدم متعددة التحديد في Excel | `PivotField.IsMultipleItemSelectionAllowed` | تعيين إلى `true` | مطلوب قبل أن تصبح أي استدعاءات لـ `IsHidden` فعالة. |
| إخفاء / إظهار عناصر فردية في قائمة متعددة التحديد | `PivotItem.IsHidden` | تعيين لكل عنصر | يجب أن يظل عنصر واحد على الأقل مرئياً (`IsHidden == false`). |

{{% alert color="primary" %}}
تذكر دائماً قيد الرؤية عند تكوين التصفية متعددة التحديد. إذا تم إخفاء كل `PivotItem` في حقل صفحة متعدد التحديد، فإن Excel يتعطل عند الفتح أو يعرض محوراً فارغاً. أنشئ قائمتك البيضاء مقابل بيانات المصدر بحيث يظل عنصر واحد على الأقل مرئياً، وستفتح المصنفات المحفوظة لديك بشكل موثوق على كل جهاز.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}