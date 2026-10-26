---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Node.js via Java
linktitle: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Node.js via Java
description: تعرف على كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية في Aspose.Cells for Node.js via Java، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، والأنماط المسماة الحديثة في Excel 2007+، وأنماط الجداول المحورية المخصصة، واختصار formatAll.
keywords: Aspose.Cells Node.js via Java نمط جدول محوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تطبيق كلٍّ من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) والأنماط الحديثة المسماة أو المخصصة للجداول المحورية (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يُحفظ إليه المصنف، وليس على التنسيق الذي تم تحميله منه.
{{% /alert %}}

## **المقدمة**
يوفر Aspose.Cells واجهتي برمجة تطبيقات متوازيتين للأنماط في الجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ مصنف تم تحميله من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة تُطبَّق واجهة الأنماط الحديثة بدلاً من واجهة الأنماط القديمة.
- يحدد `PivotTable.pivotTableStyleType` أحد الأنماط المسماة المدمجة (النسقات الفاتحة والداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- يحدد `PivotTable.pivotTableStyleName` نمطًا مخصصًا تُعرّفه بنفسك من خلال `Worksheets.getTableStyles().addPivotTableStyle(...)`. تُعد الأنماط المخصصة ضرورية كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.
بالإضافة إلى ذلك، يُعد `PivotTable.formatAll(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية في الجدول المحوري، متجاوزًا أيًا كان قد تم تعيينه عبر أي من واجهتي أسماء الأنماط أعلاه. يكون ذلك مفيدًا عند الحاجة إلى مظهر موحد بصرف النظر عن النسق الأساسي.

## **تطبيق تنسيق تلقائي معرّف مسبقًا من XLS القديم**
يقبل `PivotTable.autoFormatType` قيمة من تعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. القيم المتاحة هي `Report1` إلى `Report10`، و`Classic`، و`Table1` إلى `Table10`.
يُحمِّل المثال التالي مصنفًا جديدًا، ويملأ بيانات العينة الخاصة بالفاكهة/السنة/المبلغ، ويُضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.Report5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}
**لماذا لا توجد حقول أعمدة؟** صُمِّمت التنسيقات التلقائية من سلسلة Report (`Report1` إلى `Report10`، `Table1` إلى `Table10`) في الإصدار الكلاسيكي من Excel لـ **جداول محورية أحادية البعد** التي تحتوي على حقول صفوف وقيم فقط — إذ لا تتضمن تنسيقًا مدمجًا لترويسات حقول الأعمدة. إذا كان جدولك المحوري يحتاج إلى حقول أعمدة، فاستخدم الإعدادات المسبقة الحديثة لـ `PivotTableStyleType` من [السيناريو 2](#apply-a-modern-named-preset-pivot-table-style) بدلاً من ذلك، فهي مصممة للتخطيط ثنائي الأبعاد الذي يستخدمه الإصدار الحديث من Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// الحصول على ورقة العمل الأولى
let sheet = workbook.getWorksheets().get(0);
// تعبئة بيانات المصدر بصف الرأس (الفاكهة، السنة، المبلغ)
// و9 صفوف بيانات تغطي العنب، والتوت الأزرق، والكيوي، والكرز عبر عامي 2020 و2021
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
// إضافة جدول محوري في خلية الوجهة E3، باسم ، باستخدام نطاق المصدر A1:C10
let pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// تعيين الحقول: الفاكهة -> الصفوف، المبلغ -> البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// تطبيق التنسيق التلقائي المحدد مسبقًا للإصدار القديم من XLS "Report5"
// ملاحظة: هذه الخاصية لها معنى فقط عند الحفظ بصيغة .xls.
// عند الحفظ بصيغة .xlsx/.xlsm/.xlsb، يتجاهل Excel AutoFormatType
// ويستخدم أيًا مما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);
// حفظ المصنف بصيغة .xls القديمة
workbook.save("output.xls");
```

## **تطبيق نمط جدول محوري معرّف مسبقًا حديث مسمى**
`PivotTable.setPivotTableStyleType(int)` يختار أحد الأنماط المدمجة ذات الأسماء التي قدّمها Excel 2007 للجداول المحورية. يوفّر تعداد `PivotTableStyleType` ثلاث عائلات من سمات المظهر: العائلة الفاتحة من `PIVOT_TABLE_STYLE_LIGHT1` إلى `PIVOT_TABLE_STYLE_LIGHT28`، والعائلة المتوسطة من `PIVOT_TABLE_STYLE_MEDIUM1` إلى `PIVOT_TABLE_STYLE_MEDIUM28`، والعائلة الداكنة من `PIVOT_TABLE_STYLE_DARK1` إلى `PIVOT_TABLE_STYLE_DARK_28`. كما يعرّف `None` و`Custom`. الأعضاء ذات الأرقام الأعلى في كل عائلة هي الأنماط التي أُضيفت في Excel 2017.
هذه الإعدادات المسبقة للقراءة فقط. فور حاجتك إلى تغيير الألوان أو الحدود أو الخطوط بما يتجاوز ما توفره الإعدادات المسبقة، يجب عليك تعريف نمط جدول محوري مخصص بدلاً من ذلك، كما هو موضح في [السيناريو 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**لماذا نستخدم الإعدادات المسبقة الحديثة بدلاً من التنسيقات التلقائية لسلسلة التقارير؟** قيم `Report1` إلى `Report10` وقيم `Table1` إلى `Table10` في `PivotTableAutoFormatType` تسبق حقول أعمدة الجداول المحورية، لذلك لا تتضمن أي تنسيق لعناوين حقول الأعمدة، ويعرض Excel تلك العناوين دون تنسيق. صُممت الإعدادات المسبقة `PivotTableStyleType` للتخطيط ثنائي الأبعاد الذي تستخدمه إصدارات Excel الحديثة، وتنسّق عناوين حقول الصفوف وحقول الأعمدة على حد سواء.
{{% /alert %}}

يعيد هذا السيناريو استخدام مجموعة بيانات Fruit/Year/Amount من السيناريو 1، ويضيف `Year` إلى منطقة الأعمدة إلى جانب حقل الصف `Fruit` عبر `PivotFieldType.COLUMN`، ويطبق الإعداد المسبق `PIVOT_TABLE_STYLE_DARK1` ذي المظهر الداكن باستخدام `pivotTable.setPivotTableStyleType`، ثم يحفظ النتيجة بصيغة `.xlsx` — الصيغة التي يكون فيها `PivotTableStyleType` ذا معنى.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
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
// Add a pivot table at E3, sourced from A1:C10
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **تحديد نمط جدول محوري مخصص وتطبيقه**
لا يمكن تعديل الإعدادات المسبقة المدمجة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب تحديد نمط محوري مخصص. تتكون سير العمل من ثلاث خطوات:
1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `Worksheets.getTableStyles().addPivotTableStyle(String name)`. يُرجع هذا فهرس النمط المُنشأ حديثًا.
2. اضبط النمط بإضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.tableStyleElements.add(TableStyleElementType)`، ثم عيّن كائن `Style` لكل عنصر عبر `TableStyleElement.setElementStyle(Style)`.
3. طبِّق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.pivotTableStyleName` إلى اسم النمط. لا تستخدم `pivotTableStyleType` هنا، لأن هذه الخاصية تحدد الإعدادات المسبقة المدمجة.

{{% alert color="primary" %}}
لا يمكن استخدام `pivotTableStyleName` و`pivotTableStyleType` بالتبادل. استخدم `pivotTableStyleType` للإعدادات المسبقة المدمجة، و`pivotTableStyleName` للأنماط المخصصة التي حددتها عبر `addPivotTableStyle`. تعيين كليهما لا يضر، ولكن يُعرض فقط النمط المطابق للمصدر المطلوب.
تتضمن قيم `TableStyleElementType` المتاحة: `WholeTable`، و`FirstRow`، و`LastRow`، و`FirstColumn`، و`LastColumn`، و`GrandTotalRow`، و`GrandTotalColumn`، و`PageFieldLabels`، و`PageFieldValues`.
يُعرِّف المثال التالي نمطًا محوريًا مخصصًا بحد أسود رفيع على `WholeTable` وخط أحمر غامق على `GrandTotalRow`، ثم يطبقه عبر `pivotTableStyleName` ويحفظه بصيغة `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
// إضافة جدول محوري مصدره A1:C10، مثبت عند E3، باسم
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// الخطوة 1: تسجيل نمط جدول محوري مخصص جديد والتقاط فهرسه
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// الخطوة 2: إضافة عنصر WholeTable وتطبيق حدود سوداء رفيعة على الجوانب الأربعة
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.getBlack());
let bottomBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.getBlack());
let leftBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.getBlack());
let rightBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر عريض
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، وهو للإعدادات المسبقة المضمنة)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **تطبيق نمط واحد على كل خلية في الجدول المحوري باستخدام formatAll**
يُعد `PivotTable.formatAll(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات وترويسات الصفوف والأعمدة والإجماليات. يتم تجاوز كل ما تم تعيينه سابقًا عبر `pivotTableStyleType` أو `pivotTableStyleName`.

{{% alert color="primary" %}}
يتجاوز `formatAll` كلًا من `pivotTableStyleType` و`pivotTableStyleName`. استخدمه فقط عندما يكون مطلوبًا مظهر موحد ومستقل عن النسق في جميع أنحاء الجدول المحوري.
يُنشئ المثال التالي كائن `Style` بتعبئة صلبة صفراء، وخط أزرق داكن غامق، وحواف سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `formatAll` ويحفظه بصيغة `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// تعبئة البيانات المصدرية: صف الرأس (الصف 1) + 9 صفوف بيانات (الصفوف 2-10)
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
// إضافة جدول محوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// تعيين حقول الجدول المحوري: Fruit -> منطقة الصفوف، Year -> منطقة الأعمدة، Amount -> منطقة البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// بناء نمط Style سيتم فرضه على كل خلية في الجدول المحوري
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.getYellow());
style.setPattern(AsposeCells.BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getDarkBlue());
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setColor(AsposeCells.Color.getBlack());
// تطبيق formatAll: يفرض هذا النمط الواحد على كل خلية في الجدول المحوري،
// متجاوزاً أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقاً
pivotTable.formatAll(style);
// حفظ المصنف بتنسيق .xlsx الحديث
workbook.save("output.xlsx");
```

## **أي واجهة برمجة تطبيقات للأنماط يجب أن أستخدم؟**
يعتمد اختيار واجهة برمجة التطبيقات للأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول أدناه كمرجع سريع.
| تنسيق الملف الهدف | واجهة برمجة التطبيقات المراد استخدامها | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `PivotTable.autoFormatType` | القيم من `Aspose.Cells.Pivot.PivotTableAutoFormatType` (مثل `Report1`–`Report10`، و`Classic`، و`Table1`–`Table10`). يتم تجاهلها عند الحفظ بالتنسيقات الحديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `PivotTable.pivotTableStyleType` | القيم من `Aspose.Cells.PivotTableStyleType` (النسقات الفاتحة/الداكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | استخدمه عندما لا تكون الإعدادات المسبقة المدمجة كافية. اضبطه عبر `TableStyleElement.setElementStyle(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.formatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر في جميع أنحاء الجدول المحوري. |
عند الشك، احفظ بصيغة `.xlsx` واستخدم `pivotTableStyleType` للنسقات المدمجة، أو `pivotTableStyleName` للنسقات المخصصة.

{{< app/cells/assistant language="nodejs-java" >}}