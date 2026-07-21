---
title: تطبيق الأنماط على الجداول المحورية
linktitle: تطبيق الأنماط على الجداول المحورية
description: تعلم كيفية تطبيق الأنماط المضمنة والمخصصة على الجداول المحورية في Aspose.Cells for Java، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، والأنماط الحديثة المسماة في Excel 2007+، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells Java نمط الجدول المحوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تطبيق التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) والأنماط الحديثة المسماة أو المخصصة للجداول المحورية (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يُحفظ إليه المصنف، وليس على التنسيق الذي تم تحميله منه.

{{% /alert %}}

## **المقدمة**

يوفر Aspose.Cells واجهتي أنماط متوازيتين للجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف فيه، وليس على التنسيق الذي قرأته منه. يمكن إعادة حفظ مصنف تم تحميله من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة تنطبق واجهة الأنماط الحديثة بدلاً من الواجهة القديمة.

للحصول على مخرجات `.xls` قديمة، استخدم خاصية `PivotTable.AutoFormatType` مع تعداد `com.aspose.cells.PivotTableAutoFormatType`. تتوافق واجهة برمجة التطبيقات هذه مع أداة اختيار التنسيق التلقائي التي كان Excel الكلاسيكي يوفرها للجداول المحورية.

لمخرجات `.xlsx` و`.xlsm` و`.xlsb` الحديثة، يتوفر نوعان من واجهات الأنماط:

- `PivotTable.PivotTableStyleType` يحدد أحد الأنماط المسماة المضمنة (سمات فاتحة وداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- `PivotTable.PivotTableStyleName` يحدد نمطًا مخصصًا تقوم بتعريفه بنفسك من خلال `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)`. الأنماط المخصصة مطلوبة كلما أردت تعديل الألوان أو الحدود أو الخطوط بخلاف ما تقدمه الإعدادات المسبقة.

بالإضافة إلى ذلك، فإن `PivotTable.formatAll(Style)` هو اختصار يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أي من واجهات أسماء الأنماط أعلاه. يكون هذا مفيدًا عند الحاجة إلى مظهر موحد بغض النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مسبق لملفات XLS القديمة**

يقبل `PivotTable.AutoFormatType` قيمة من تعداد `com.aspose.cells.PivotTableAutoFormatType`. القيم المتاحة هي `REPORT_1` إلى `REPORT_10`، و`CLASSIC`، و`TABLE_1` إلى `TABLE_10`.

{{% alert color="primary" %}}

لا يتم الالتزام بـ `AutoFormatType` إلا عند حفظ المصنف بصيغة `.xls`. عندما يتم حفظ المصنف نفسه بصيغة `.xlsx` أو `.xlsm` أو `.xlsb`، يتجاهل Excel هذه الخاصية ويعود إلى إعدادات `PivotTableStyleType` و`PivotTableStyleName`.

{{% /alert %}}

يحمل المثال التالي مصنفًا جديدًا، ويملأ بيانات النموذج Fruit/Year/Amount، ويضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.REPORT_5`، ويحفظ النتيجة بصيغة `.xls`.

```java
import com.aspose.cells.*;

// السيناريو 1: تطبيق تنسيق تلقائي محدد مسبقًا بتنسيق XLS القديم
// واجهة برمجة التطبيقات المستخدمة: PivotTable.AutoFormatType
// تنسيق الملف المستهدف: .xls (قديم)
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-cells/Aspose.Cells-for-.NET

// إنشاء مصنف جديد
Workbook workbook = new Workbook();

// الحصول على ورقة العمل الأولى
Worksheet sheet = workbook.getWorksheets().get(0);

// ملء بيانات المصدر بصف الرأس (فاكهة، سنة، مبلغ)
// و9 صفوف بيانات تغطي العنب، التوت الأزرق، الكيوي، الكرز عبر عامي 2020 و2021
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");

sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);

sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);

sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);

sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);

sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);

sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);

sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);

sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);

sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);

// إضافة جدول محوري في خلية الوجهة E3، باسم "Pivot1"، باستخدام نطاق المصدر A1:C10
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// تعيين الحقول: الفاكهة -> الصفوف، السنة -> الأعمدة، المبلغ -> البيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// تطبيق التنسيق التلقائي المحدد مسبقًا "Report5" الخاص بـ XLS القديم
// ملاحظة: هذه الخاصية تكون ذات معنى فقط عند الحفظ بتنسيق .xls.
// عند الحفظ بتنسيق .xlsx/.xlsm/.xlsb، يتجاهل Excel خاصية AutoFormatType
// ويستخدم ما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);

// حفظ المصنف بتنسيق .xls القديم
workbook.save("output.xls");
```

## **تطبيق نمط جدول محوري مسمى مسبق حديث**

يقبل `PivotTable.PivotTableStyleType` قيمة من تعداد `com.aspose.cells.PivotTableStyleType`. يغطي التعداد السمات الفاتحة `PIVOT_TABLE_STYLE_LIGHT_1` إلى `PIVOT_TABLE_STYLE_LIGHT_28` والسمات الداكنة `PIVOT_TABLE_STYLE_DARK_1` إلى `PIVOT_TABLE_STYLE_DARK_28`. يمكن الوصول إلى الأنماط المضافة في Excel 2017 (الموجة الثانية من السمات الفاتحة والداكنة) من خلال نفس التعداد.

هذه هي واجهة برمجة التطبيقات الموصى بها لأي تنسيق ملف حديث. على عكس التنسيق التلقائي القديم، يتم عرض النمط المحدد هنا بأمانة بواسطة Excel ويصمد أمام عمليات الحفظ والتحميل المتكررة عبر أدوات Office الأخرى.

يستخدم المثال التالي نفس بيانات Fruit/Year/Amount، وينشئ جدولًا محوريًا مطابقًا، ويطبق `PIVOT_TABLE_STYLE_DARK_1`، ويحفظ المصنف بصيغة `.xlsx`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// صف الترويسة: فاكهة / سنة / مبلغ
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 صفوف بيانات من فاكهة / سنة / مبلغ
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);

// إضافة جدول محوري في E3 باسم "Pivot1"، مصدره من A1:C10
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين حقول الجدول المحوري: فاكهة -> منطقة الصفوف، سنة -> منطقة الأعمدة، مبلغ -> منطقة البيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// تطبيق نمط جدول محوري مسمى مسبقًا حديث من Excel 2007+.
// PivotTableStyleType هي واجهة برمجة التطبيقات الصحيحة لملفات .xlsx / .xlsb؛ AutoFormatType
// يتم تجاهلها بواسطة Excel في تلك التنسيقات. ينتمي PivotTableStyleDark1 إلى عائلة السمة الداكنة
// العائلة (PivotTableStyleDark1..PivotTableStyleDark28)، ويكشف نفس التعداد أيضًا عن
// سمات Excel 2017 الفاتحة/الداكنة الأحدث (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// الحفظ بصيغة .xlsx الحديثة - هذا هو التنسيق الذي يكون فيه PivotTableStyleType ذا معنى.
workbook.save("output.xlsx");
```

## **تعريف وتطبيق نمط جدول محوري مخصص**

لا يمكن تعديل الإعدادات المسبقة المضمنة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب عليك تعريف نمط محوري مخصص. يتكون سير العمل من ثلاث خطوات:

1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. يُرجع هذا فهرس النمط الذي تم إنشاؤه حديثًا.
2. قم بتكوين النمط بإضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.getTableStyleElements().add(TableStyleElementType)`، ثم قم بتعيين `Style` لكل عنصر عبر `TableStyleElement.setElementStyle(Style)`.
3. قم بتطبيق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.PivotTableStyleName` على اسم النمط. لا تستخدم `PivotTableStyleType` هنا، لأن هذه الخاصية تختار الإعدادات المسبقة المضمنة.

{{% alert color="primary" %}}

لا يمكن استخدام `PivotTableStyleName` و`PivotTableStyleType` بالتبادل. استخدم `PivotTableStyleType` للإعدادات المسبقة المضمنة، واستخدم `PivotTableStyleName` للأنماط المخصصة التي قمت بتعريفها من خلال `addPivotTableStyle`. تعيين كليهما ليس ضارًا، ولكن يُعرض فقط العنصر الذي يتطابق مع المصدر المقصود.

{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة `WHOLE_TABLE` و`FIRST_ROW` و`LAST_ROW` و`FIRST_COLUMN` و`LAST_COLUMN` و`GRAND_TOTAL_ROW` و`GRAND_TOTAL_COLUMN` و`PAGE_FIELD_LABELS` و`PAGE_FIELD_VALUES`.

يعرّف المثال التالي نمطًا محوريًا مخصصًا بحد أسود رفيع على `WholeTable` وخط أحمر غامق عريض على `GrandTotalRow`، ثم يطبقه عبر `PivotTableStyleName` ويحفظ بصيغة `.xlsx`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// تعبئة البيانات المصدرية: صف الرأس + 9 صفوف بيانات (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

// إضافة جدول محوري مصدره A1:C10، مثبت عند E3، باسم "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// الخطوة 1: تسجيل نمط جدول محوري مخصص جديد والتقاط فهرسه
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// الخطوة 2: إضافة عنصر WholeTable وتطبيق حدود سوداء رفيعة على الجوانب الأربعة
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);

// الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر غامق
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);

// الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، المستخدم للإعدادات المسبقة المدمجة)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام FormatAll**

`PivotTable.formatAll(Style)` هو اختصار يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات، ورؤوس الصفوف والأعمدة، والإجماليات. يتم تجاوز أي شيء تم تعيينه سابقًا من خلال `PivotTableStyleType` أو `PivotTableStyleName`.

{{% alert color="primary" %}}

يتجاوز `FormatAll` كلًا من `PivotTableStyleType` و`PivotTableStyleName`. استخدمه فقط عندما يكون هناك حاجة إلى مظهر موحد ومستقل عن السمة في جميع أنحاء الجدول المحوري بأكمله.

{{% /alert %}}

ينشئ المثال التالي `Style` بتعبئة صلبة صفراء وخط أزرق داكن عريض وحدود سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `formatAll` ويحفظ بصيغة `.xlsx`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// تعبئة بيانات المصدر: صف الرأس (الصف 1) + 9 صفوف بيانات (الصفوف 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);

// إضافة جدول محوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين حقول الجدول المحوري: Fruit -> منطقة الصفوف، Year -> منطقة الأعمدة، Amount -> منطقة البيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// بناء نمط (Style) سيتم فرضه على كل خلية من خلايا الجدول المحوري
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());

style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());

// تطبيق formatAll: يفرض هذا النمط الوحيد على كل خلية من خلايا الجدول المحوري،
pivotTable.formatAll(style);

// حفظ المصنف بصيغة .xlsx الحديثة
workbook.save("output.xlsx");
```

## **أي واجهة أنماط يجب أن أستخدم؟**

يعتمد اختيار واجهة الأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول التالي كمرجع سريع.

| تنسيق الملف الهدف | واجهة برمجة التطبيقات التي يجب استخدامها | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `PivotTable.AutoFormatType` | قيم من `com.aspose.cells.PivotTableAutoFormatType` (مثل `REPORT_1`–`REPORT_10`، و`CLASSIC`، و`TABLE_1`–`TABLE_10`). يتم تجاهله عند الحفظ بتنسيقات حديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `PivotTable.PivotTableStyleType` | قيم من `com.aspose.cells.PivotTableStyleType` (سمات فاتحة/داكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | يُستخدم عندما لا تكون الإعدادات المسبقة المضمنة كافية. قم بالتكوين عبر `TableStyleElement.setElementStyle(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.formatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر في جميع أنحاء الجدول المحوري بأكمله. |

عند الشك، احفظ بصيغة `.xlsx` واستخدم `PivotTableStyleType` للسمات المضمنة، أو `PivotTableStyleName` للسمات المخصصة.

{{< app/cells/assistant language="java" >}}