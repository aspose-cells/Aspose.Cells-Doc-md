---
title: إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: إضافة حقول التصفية
description: تعلّم كيفية إضافة وتكوين حقول التصفية في الجداول المحورية باستخدام Aspose.Cells for Java، بما في ذلك إضافة حقول التصفية، والتصفية أحادية التحديد، والتصفية متعددة التحديد.
keywords: Aspose.Cells, Java, جدول محوري, حقل صفحة, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, تصفية
type: docs
weight: 250
url: /ar/java/add-filter-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells دورة الحياة الكاملة لحقول التصفية في الجداول المحورية. يمكنك إضافة حقل صفحة من خلال واجهة برمجة تطبيقات عالية المستوى للراحة أو من خلال المجموعة منخفضة المستوى `PageFields`، ويمكنك التحكم في مرشح الصفحة في وضع التحديد الفردي، أو مسحه لعرض كل عنصر من عناصر الصفحة، أو تبديل الحقل إلى التحديد المتعدد بحيث يمكن للمستخدمين اختيار عدة عناصر من عناصر الصفحة دفعةً واحدة من خلال واجهة المستخدم الخاصة بمربعات الاختيار في Excel.
{{% /alert %}}

## **المقدمة**

حقل التصفية هو حقل محوري يتحكم في *أي مجموعة فرعية* من بيانات المصدر يعرضها جسم الجدول المحوري. يراه المستخدمون النهائيون كقائمة منسدلة في الجزء العلوي من الجدول المحوري المُقدَّم في Excel، ويؤدي تحديد أحد عناصر الصفحة المتاحة إلى إعادة بناء جسم الجدول المحوري بحيث يتم تلخيص السجلات التي تنتمي إلى عنصر التصفية هذا فقط. يصبح حقل محوري حقل صفحة عند تسجيله كـ `PivotFieldType.Page` بدلاً من `PivotFieldType.Row` أو `PivotFieldType.Column` أو `PivotFieldType.Data`.

يمكن أن يعمل حقل التصفية بسلوكين. في سلوك **التحديد الفردي** الافتراضي، يكون عنصر صفحة واحد فقط مرئيًا في كل مرة، لذلك يُلخّص جسم الجدول المحوري مجموعة فرعية واحدة بالضبط. في سلوك **التحديد المتعدد**، يعرض الحقل قائمة مربعات اختيار، ويُلخّص جسم الجدول المحوري اتحاد كل عناصر الصفحات التي تم تحديدها. يمكن نقل حقل المصدر نفسه ذهابًا وإيابًا بين هذين السلوكين عن طريق تبديل خاصية واحدة.

يوفر Aspose.Cells for Java طريقتين متكافئتين لتسجيل حقل صفحة. واجهة برمجة التطبيقات عالية المستوى هي `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")`، والتي تأخذ اسم عمود المصدر وتضيف الحقل في استدعاء واحد. واجهة برمجة التطبيقات منخفضة المستوى هي `PivotTable.PageFields.add(PivotField)`، والتي تُستخدم عندما يكون لديك بالفعل مرجع `PivotField` وتريد إضافة نفس نسخة الحقل إلى منطقة التصفية. تنتهي كلتا واجهتي برمجة التطبيقات إلى ملء نفس مجموعة `PageFields`، وتوضح بقية هذه المقالة كيفية الاختيار بينهما وكيفية التحكم في كل وضع تصفية.

## **إضافة حقل صفحة**

هناك طريقتان لتسجيل حقل محوري في منطقة التصفية. يأخذ الاستدعاء عالي المستوى اسم عمود المصدر كسلسلة وهو المسار الأكثر شيوعًا. يقبل الاستدعاء منخفض المستوى نسخة `PivotField` موجودة وهو ملائم عندما يجب إعادة استخدام نفس كائن الحقل عبر مناطق محورية متعددة. يضع كلا الاستدعاءين الحقل في `PivotTable.PageFields`، وبعد ذلك يظهر كقائمة منسدلة للصفحة في الجزء العلوي من الجدول المحوري المُقدَّم.

### إضافة حقل صفحة باستخدام addFieldToArea

يبني المثال التالي مجموعة بيانات صغيرة تتكون من الفاكهة / السنة / المبلغ، ويضع جدولاً محوريًا في الخلية E3 مع `Fruit` في منطقة الصفوف، و`Amount` في منطقة البيانات، و`Year` في منطقة التصفية، ويقوم بتحديث الجدول المحوري، ويحفظ المصنف.

```java
import com.aspose.cells.*;

// إنشاء مصنف جديد
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// إعداد صف الرأس
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// ملء 9 صفوف من بيانات العينة: الفاكهة، السنة، المبلغ
Object[][] data = new Object[][]
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

for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// إضافة جدول محوري مثبت عند الخلية E3
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// إضافة الحقول إلى مناطقها: الفاكهة كصف، المبلغ كبيانات، السنة كحقل صفحة
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// تحديث وحساب بيانات الجدول المحوري
pivotTable.calculateData();

// حفظ المصنف
workbook.save("pageFieldSample.xlsx");
```

### إضافة حقل صفحة باستخدام PageFields.add

عندما تعمل بالفعل مع نسخة `PivotField`، يمكنك تمريرها مباشرةً إلى `PivotTable.PageFields.add`. يتم إنشاء الجدول المحوري وحقل التصفية تمامًا كما في السيناريو السابق؛ لا يتم استبدال تسجيل منطقة التصفية النهائي إلا باستدعاء واجهة برمجة التطبيقات منخفضة المستوى.

```java
import com.aspose.cells.*;

// - يتم إنشاء الجدول المحوري وحقل الصفحة تمامًا كما في
//   السيناريو 1أ (بيانات الفاكهة/السنة/المبلغ، الجدول المحوري عند E3، الفاكهة->الصف،
//   المبلغ->البيانات). أدناه نحصل على حقل السنة المحوري من
//   مجموعة BaseFields ونمرره إلى PageFields.Add - وهو
//   البديل منخفض المستوى لـ AddFieldToArea. النتيجة
//   مطابقة وظيفيًا للسيناريو 1أ.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// العناوين
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// بيانات عينة (9 صفوف)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// إضافة جدول محوري عند E3 يغطي A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// الفاكهة -> الصف، المبلغ -> البيانات (السنة ستذهب إلى الصفحة أدناه)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// النهج منخفض المستوى: جلب حقل السنة المحوري الموجود من BaseFields
// وتسجيله في منطقة الصفحة عبر PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// التحديث ليعكس حقل الصفحة الجديد في المصنف المحفوظ
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **التصفية أحادية التحديد (عرض عنصر صفحة واحد)**

في سلوك التحديد الفردي الافتراضي، يُقدَّم حقل التصفية كقائمة منسدلة واحدة، ويحدد العدد الصحيح `PivotField.CurrentPageItem` عنصر التصفية الذي يقود جسم الجدول المحوري. يؤدي تعيين فهرس محدد إلى اختيار هذا العنصر فقط؛ ويؤدي تعيين القيمة الحارسة الخاصة `0x7FFD` (عشري 32765) إلى مسح المرشح بحيث يتم تلخيص كل عناصر الصفحات دفعةً واحدة. التحديد الفردي هو الوضع الافتراضي؛ لا تحتاج إلى تمكينه بشكل صريح.

### عرض كل العناصر

يعد تعيين `CurrentPageItem` على القيمة السحرية `0x7FFD` مكافئًا لمسح مرشح الصفحة: يُلخّص جسم الجدول المحوري كل عناصر الصفحات كما لو لم يتم تطبيق أي مرشح.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// ملء بيانات الفاكهة/السنة/المبلغ
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// إنشاء جدول محوري في E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);

// تكوين حقول الجدول المحوري: الفاكهة إلى الصف، المبلغ إلى البيانات، السنة إلى الصفحة
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");

pivot.calculateData();

// مسح مرشح الصفحة بحيث يكون كل عنصر في حقل الصفحة مرئياً.
// 0x7FFD (عشري 32765) هو القيمة الحارسية الخاصة التي تعني "كل العناصر"،
// يعادل تحديد "(الكل)" في القائمة المنسدلة لحقل الصفحة في Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);

workbook.save("output.xlsx");
```

### عرض عنصر محدد واحد

يؤدي تعيين `CurrentPageItem` على فهرس حقيقي إلى اختيار عنصر التصفية هذا فقط. الفهرس هو موضع العنصر في قائمة العناصر المرتبة لحقل التصفية، لذلك على سبيل المثال يحدد `1` العنصر الثاني بعد الفرز.

```java
import com.aspose.cells.*;

// إنشاء مصنف
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

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

// إضافة جدول محوري في E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// إضافة الحقول: فاكهة→صف، مبلغ→بيانات، سنة→صفحة
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// عمليات خاصة بحقل الصفحة
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = العنصر الثاني بالترتيب المرتب (مثال: "2021")

// تحديث وحساب الجدول المحوري
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **التصفية متعددة التحديد**

تحوّل التصفية متعددة التحديد القائمة المنسدلة للصفحة إلى قائمة مربعات اختيار وتتيح للمستخدم النهائي اختيار عدة عناصر من عناصر الصفحة في وقت واحد. يعرض Aspose.Cells خاصيتين تعملان معًا. يجب تعيين `PivotField.IsMultipleItemSelectionAllowed` على `true` قبل أن تصبح واجهة المستخدم متعددة التحديد سارية المفعول على الإطلاق. بعد تمكينها، تتحكم `PivotItem.IsHidden` في العناصر التي تظهر في قائمة مربعات الاختيار، بحيث يمكنك إما عرض كل العناصر أو إدراج عناصر محددة فقط في القائمة البيضاء.

يقوم الكود أدناه بتمكين التحديد المتعدد على نفس حقل صفحة Year الذي تم إنشاؤه في السيناريو 1a، ثم يعرض نمطين: يكشف الجزء A عن كل عناصر الصفحة من خلال ترك `IsHidden` معينًا على `false` لكل إدخال، بينما يضع الجزء B في القائمة البيضاء قيم المصدر التي تختارها فقط ويخفي كل شيء آخر من خلال كتلة `switch (pivotItems[i].getStringValue())`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// بيانات العينة: الفاكهة | السنة | المبلغ
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

String[][] data = new String[][]
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

for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}

Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// -- تفعيل التحديد المتعدد في حقل الصفحة
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// الجزء أ -- تحديد جميع العناصر (جعل كل عنصر مرئيًا)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}

// الجزء ب -- تحديد عناصر محددة فقط حسب قيمة المصدر
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
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

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **ملاحظة:** عند استخدام التصفية متعددة التحديد من خلال `PivotItem.IsHidden`، **يجب أن يظل عنصر `PivotItem` واحد على الأقل مرئيًا** (`IsHidden == false`). إذا تم إخفاء كل العناصر، فإن Excel إما يتعطل عند فتح الملف أو يقدّم جدولاً محوريًا فارغًا. تحقق دائمًا من أن القائمة البيضاء متعددة التحديد تتضمن عنصرًا واحدًا على الأقل من بيانات المصدر.

## **أي واجهة برمجة تطبيقات وأي وضع يجب أن أستخدم؟**

يلخص الجدول أدناه متى تستخدم كل واجهة برمجة تطبيقات ووضع بحيث يمكنك اختيار التركيبة الصحيحة دون قراءة كل سيناريو بالتفصيل.

| السيناريو / حالة الاستخدام | واجهة برمجة التطبيقات الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل صفحة حسب اسم عمود المصدر (الأكثر شيوعًا) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | لا ينطبق | عالية المستوى، في سطر واحد. استخدم هذا ما لم تكن بحاجة إلى مرجع `PivotField`. |
| إضافة حقل صفحة عندما يكون لديك بالفعل كائن `PivotField` | `PivotTable.PageFields.add(PivotField)` | لا ينطبق | استخدم عندما يتم الحصول على كائن الحقل من مكان آخر أو يحتاج إلى إعادة الاستخدام. |
| التصفية إلى عنصر صفحة واحد (الوضع الافتراضي) | `PivotField.CurrentPageItem` | تعيين على فهرس محدد | على سبيل المثال، يعرض `1` العنصر الثاني في القائمة المرتبة. |
| عرض كل العناصر / مسح مرشح الصفحة | `PivotField.CurrentPageItem` | تعيين على `0x7FFD` | القيمة السحرية `0x7FFD` (عشري 32765) هي القيمة الحارسة لـ "كل العناصر". |
| تمكين واجهة المستخدم متعددة التحديد في Excel | `PivotField.IsMultipleItemSelectionAllowed` | تعيين على `true` | مطلوب قبل أن تصبح أي استدعاءات لـ `IsHidden` سارية المفعول. |
| إخفاء / إظهار عناصر فردية في قائمة متعددة التحديد | `PivotItem.IsHidden` | تعيين لكل عنصر | يجب أن يظل عنصر واحد على الأقل مرئيًا (`IsHidden == false`). |

{{% alert color="primary" %}}
تذكر دائمًا قيد الرؤية عند تكوين التصفية متعددة التحديد. إذا تم إخفاء كل `PivotItem` في حقل صفحة متعدد التحديد، فإن Excel يتعطل عند الفتح أو يقدّم جدولاً محوريًا فارغًا. أنشئ قائمتك البيضاء مقابل بيانات المصدر بحيث يظل عنصر واحد على الأقل مرئيًا، وستفتح المصنفات المحفوظة بشكل موثوق على كل جهاز.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
