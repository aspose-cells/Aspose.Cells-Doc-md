---
title: إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: إضافة حقول التصفية
description: تعلم كيفية إضافة وتكوين حقول التصفية في الجداول المحورية باستخدام Aspose.Cells for Node.js via C++، بما في ذلك إضافة حقول التصفية والتصفية أحادية الاختيار والتصفية متعددة الاختيارات.
keywords: Aspose.Cells, Node.js via C++, جدول محوري, حقل صفحة, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, تصفية
type: docs
weight: 250
url: /ar/nodejs-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells دورة الحياة الكاملة لحقول التصفية في الجداول المحورية. يمكنك إضافة حقل صفحة من خلال واجهة برمجة تطبيقات عالية المستوى ملائمة أو من خلال مجموعة المستوى الأدنى `PageFields`، ويمكنك تشغيل مرشح الصفحة في وضع الاختيار الفردي، أو مسحه لإظهار كل عنصر من عناصر الصفحة، أو تبديل الحقل إلى الاختيار المتعدد بحيث يمكن للمستخدمين اختيار عدة عناصر من عناصر الصفحة دفعة واحدة عبر واجهة خانات الاختيار في Excel.
{{% /alert %}}

## **المقدمة**

حقل التصفية هو حقل محوري يتحكم في *أي مجموعة فرعية* من البيانات المصدر يعرضها جسم الجدول المحوري. يراه المستخدمون النهائيون كقائمة منسدلة في أعلى الجدول المحوري المُنشأ في Excel، ويؤدي اختيار أحد عناصر الصفحة المتاحة إلى إعادة بناء جسم الجدول المحوري بحيث يتم تلخيص السجلات التي تنتمي إلى عنصر التصفية هذا فقط. يصبح الحقل المحوري حقل صفحة عند تسجيله كـ `PivotFieldType.Page` بدلاً من `PivotFieldType.Row` أو `PivotFieldType.Column` أو `PivotFieldType.Data`.

يمكن أن يعمل حقل التصفية بسلوكين. في سلوك **الاختيار الفردي** الافتراضي، لا يظهر سوى عنصر صفحة واحد في كل مرة، لذلك يُلخص جسم الجدول المحوري مجموعة فرعية واحدة بالضبط. في سلوك **الاختيار المتعدد**، يعرض الحقل قائمة بخانات الاختيار، ويُلخص جسم الجدول المحوري اتحاد كل عناصر الصفحات المحددة. يمكن نقل نفس الحقل المصدر ذهاباً وإياباً بين هذين السلوكين عن طريق تبديل خاصية واحدة.

يوفر Aspose.Cells for Node.js via C++ طريقتين متكافئتين لتسجيل حقل صفحة. واجهة برمجة التطبيقات عالية المستوى هي `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`، والتي تأخذ اسم عمود المصدر وتضيف الحقل في استدعاء واحد. واجهة برمجة التطبيقات ذات المستوى الأدنى هي `PivotTable.pageFields.add(PivotField)`، والتي تُستخدم عندما يكون لديك بالفعل مرجع `PivotField` وتريد إضافة نفس مثيل الحقل إلى منطقة التصفية. تنتهي كلتا واجهتي برمجة التطبيقات إلى ملء نفس مجموعة `PageFields`، ويوضح بقية هذا المقال كيفية الاختيار بينهما وكيفية تشغيل كل وضع تصفية.

## **إضافة حقل صفحة**

هناك طريقتان لتسجيل حقل محوري في منطقة التصفية. يأخذ الاستدعاء عالي المستوى اسم عمود المصدر كسلسلة نصية وهو المسار الأكثر شيوعاً. يقبل الاستدعاء ذو المستوى الأدنى مثيل `PivotField` موجوداً وهو ملائم عندما يجب إعادة استخدام نفس كائن الحقل عبر مناطق محورية متعددة. يضع كلا الاستدعاءين الحقل في `PivotTable.pageFields`، وبعد ذلك يظهر كقائمة منسدلة للصفحة في أعلى الجدول المحوري المُنشأ.

### إضافة حقل صفحة باستخدام addFieldToArea

يبني المثال التالي مجموعة بيانات صغيرة مكونة من عمود Fruit وYear وAmount، ويضع جدولاً محورياً في الخلية E3 مع `Fruit` في منطقة الصفوف، و`Amount` في منطقة البيانات، و`Year` في منطقة التصفية، ويقوم بتحديث الجدول المحوري، وحفظ المصنف.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// إعداد صف الرأس
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// ملء 9 صفوف من البيانات النموذجية: الفاكهة، السنة، المبلغ
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

// إضافة جدول محوري مثبت عند الخلية E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// إضافة الحقول إلى مناطقها: الفاكهة كصف، المبلغ كبيانات، السنة كحقل صفحة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// تحديث وحساب بيانات الجدول المحوري
pivotTable.calculateData();

// حفظ المصنف
workbook.save("pageFieldSample.xlsx");
```

### إضافة حقل صفحة باستخدام pageFields.add

عندما تعمل بالفعل مع مثيل `PivotField`، يمكنك تمريره مباشرة إلى `PivotTable.pageFields.add`. يتم إنشاء الجدول المحوري وحقل التصفية تماماً كما في السيناريو السابق؛ لا يتم استبدال تسجيل منطقة التصفية النهائي إلا باستدعاء واجهة برمجة التطبيقات ذات المستوى الأدنى.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// العناوين
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// بيانات عينة (9 صفوف)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// إضافة جدول محوري عند E3 يغطي A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// الفاكهة -> الصف، المبلغ -> البيانات (السنة ستذهب إلى الصفحة أدناه)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// نهج منخفض المستوى: احصل على PivotField السنة الموجود من BaseFields
// وسجله في منطقة الصفحة عبر PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// قم بالتحديث حتى ينعكس حقل الصفحة الجديد في المصنف المحفوظ
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **التصفية أحادية الاختيار (إظهار عنصر صفحة واحد)**

في سلوك الاختيار الفردي الافتراضي، يُعرض حقل التصفية كقائمة منسدلة واحدة ويحدد العدد الصحيح `PivotField.currentPageItem` عنصر التصفية الذي يقود جسم الجدول المحوري. يؤدي تعيين فهرس محدد إلى اختيار هذا العنصر فقط؛ ويؤدي تعيين القيمة الحارس الخاصة `0x7FFD` (عشري 32765) إلى مسح المرشح بحيث يتم تلخيص كل عنصر من عناصر الصفحة دفعة واحدة. الاختيار الفردي هو الوضع الافتراضي؛ لست بحاجة إلى تفعيله بشكل صريح.

### إظهار جميع العناصر

يكون تعيين `currentPageItem` على القيمة السحرية `0x7FFD` مكافئاً لمسح مرشح الصفحة: يُلخص جسم الجدول المحوري كل عنصر من عناصر الصفحة كما لو لم يتم تطبيق أي مرشح.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// ملء بيانات الفاكهة/السنة/المبلغ
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// إنشاء جدول محوري عند E3
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// تكوين حقول الجدول المحوري: الفاكهة→الصف، المبلغ→البيانات، السنة→الصفحة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// مسح فلتر الصفحة بحيث يكون كل عنصر في حقل الصفحة مرئيًا.
// 0x7FFD (عشري 32765) هي القيمة الحارسية الخاصة التي تعني "جميع العناصر" —
// مكافئة لتحديد "(الكل)" في القائمة المنسدلة لحقل الصفحة في Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### إظهار عنصر محدد واحد

يؤدي تعيين `currentPageItem` على فهرس حقيقي إلى اختيار عنصر صفحة واحد فقط. الفهرس هو موضع العنصر في قائمة العناصر المرتبة لحقل التصفية، لذا على سبيل المثال يحدد `1` العنصر الثاني بعد الترتيب.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// إضافة بيانات عينة (فاكهة/سنة/مبلغ)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// إضافة جدول محوري عند E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// إضافة الحقول: الفاكهة→صف، المبلغ→بيانات، السنة→صفحة
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// عمليات خاصة بحقل الصفحة
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = العنصر الثاني بالترتيب (مثلاً "2021")

// تحديث وحساب الجدول المحوري
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **التصفية متعددة الاختيارات**

تحول التصفية متعددة الاختيارات القائمة المنسدلة للصفحة إلى قائمة بخانات الاختيار وتتيح للمستخدم النهائي اختيار عدة عناصر من عناصر الصفحة في وقت واحد. يعرض Aspose.Cells خاصيتين تعملان معاً. يجب تعيين `PivotField.isMultipleItemSelectionAllowed` على `true` قبل أن تصبح واجهة المستخدم متعددة الاختيارات فعالة على الإطلاق. بعد تفعيلها، تتحكم `PivotItem.isHidden` في العناصر التي تظهر في قائمة خانات الاختيار، بحيث يمكنك إما إظهار كل عنصر أو السماح فقط بعناصر محددة.

يقوم الكود أدناه بتفعيل الاختيار المتعدد على نفس حقل صفحة Year الذي تم إنشاؤه في السيناريو 1a، ثم يعرض نمطين: الجزء A يكشف عن كل عنصر من عناصر الصفحة عن طريق ترك `isHidden` مضبوطاً على `false` لكل إدخال، بينما يسمح الجزء B فقط بقيم المصدر التي تختارها ويخفي كل شيء آخر من خلال كتلة `switch (pivotItems[i].getStringValue())`.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// بيانات نموذجية: الفاكهة | السنة | المبلغ
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// — تفعيل التحديد المتعدد في حقل الصفحة
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// الجزء A — تحديد جميع العناصر (جعل كل عنصر مرئياً)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// الجزء B — تحديد عناصر محددة فقط حسب القيمة المصدرية
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **ملاحظة:** عند استخدام التصفية متعددة الاختيارات من خلال `PivotItem.isHidden`، **يجب أن يظل `PivotItem` واحد على الأقل مرئياً** (`isHidden == false`). إذا تم إخفاء كل العناصر، فإن Excel إما يتعطل عند فتح الملف أو يعرض جدولاً محورياً فارغاً. تحقق دائماً من أن قائمة السماح متعددة الاختيارات تتضمن عنصراً واحداً على الأقل من بيانات المصدر.

## **أي واجهة برمجة تطبيقات وأي وضع يجب أن أستخدم؟**

يلخص الجدول التالي متى تستخدم كل واجهة برمجة تطبيقات وكل وضع حتى تتمكن من اختيار التركيبة الصحيحة دون قراءة كل سيناريو بالتفصيل.

| السيناريو / حالة الاستخدام | واجهة برمجة التطبيقات الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل صفحة باسم عمود المصدر (الأكثر شيوعاً) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | غير قابل للتطبيق | عالي المستوى، سطر واحد. استخدم هذا ما لم تكن بحاجة إلى مرجع `PivotField`. |
| إضافة حقل صفحة عندما يكون لديك بالفعل كائن `PivotField` | `PivotTable.pageFields.add(PivotField)` | غير قابل للتطبيق | استخدم عندما تم الحصول على كائن الحقل من مكان آخر أو يحتاج إلى إعادة استخدامه. |
| التصفية إلى عنصر صفحة واحد (الوضع الافتراضي) | `PivotField.currentPageItem` | تعيين على فهرس محدد | على سبيل المثال، يعرض `1` العنصر الثاني في القائمة المرتبة. |
| إظهار كل العناصر / مسح مرشح الصفحة | `PivotField.currentPageItem` | تعيين على `0x7FFD` | القيمة السحرية `0x7FFD` (عشري 32765) هي القيمة الحارس لـ "كل العناصر". |
| تفعيل واجهة المستخدم متعددة الاختيارات في Excel | `PivotField.isMultipleItemSelectionAllowed` | تعيين على `true` | مطلوب قبل أن تصبح أي استدعاءات لـ `isHidden` فعالة. |
| إخفاء / إظهار عناصر فردية في قائمة متعددة الاختيارات | `PivotItem.isHidden` | تعيين لكل عنصر | يجب أن يظل عنصر واحد على الأقل مرئياً (`isHidden == false`). |

{{% alert color="primary" %}}
تذكر دائماً قيد الرؤية عند تكوين التصفية متعددة الاختيارات. إذا تم إخفاء كل `PivotItem` في حقل صفحة متعدد الاختيارات، فإن Excel يتعطل عند الفتح أو يعرض جدولاً محورياً فارغاً. أنشئ قائمة السماح الخاصة بك بناءً على بيانات المصدر بحيث يظل عنصر واحد على الأقل مرئياً، وستفتح المصنفات المحفوظة لديك بشكل موثوق على كل جهاز.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
