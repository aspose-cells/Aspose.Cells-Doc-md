---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells لـ .NET
linktitle: تطبيق أنماط الجداول المحورية
description: تعرف على كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية في Aspose.Cells for Node.js via Java، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS وأنماط Excel 2007+ الحديثة المسماة وأنماط الجداول المحورية المخصصة والاختصار FormatAll.
keywords: Aspose.Cells Node.js via Java pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تطبيق كل من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) وأنماط الجداول المحورية الحديثة المسماة أو المخصصة (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يتم حفظ المصنف به، وليس على التنسيق الذي تم تحميله منه.

{{% /alert %}}

## **Introduction**

يوفر Aspose.Cells اثنتين من واجهات برمجة التطبيقات المتوازية للأنماط الخاصة بالجداول المحورية. يعتمد القرار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ المصنف المحمّل من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة تنطبق واجهة برمجة التطبيقات للأنماط الحديثة بدلاً من القديمة.

بالنسبة للمخرجات القديمة بصيغة `.xls`، استخدم الخاصية `PivotTable.autoFormatType` مع التعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. تتوافق واجهة برمجة التطبيقات هذه مع منتقي التنسيق التلقائي الذي كان Excel الكلاسيكي يوفره للجداول المحورية.

بالنسبة للمخرجات الحديثة بصيغة `.xlsx` و`.xlsm` و`.xlsb`، تتوفر نوعان من واجهات برمجة تطبيقات الأنماط:

- `PivotTable.pivotTableStyleType` يحدد أحد الأنماط المسماة المدمجة (النسق الفاتح والداكن، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- `PivotTable.pivotTableStyleName` يحدد نمطًا مخصصًا تقوم بتعريفه بنفسك من خلال `Worksheets.getTableStyles().addPivotTableStyle(...)`. الأنماط المخصصة مطلوبة كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما توفره الإعدادات المسبقة.

بالإضافة إلى ذلك، فإن `PivotTable.formatAll(Style)` هو اختصار يطبق كائن `Style` واحد على كل خلية في الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أي من واجهات برمجة تطبيقات أسماء الأنماط أعلاه. يكون هذا مفيدًا عندما يكون المظهر الموحد مطلوبًا بغض النظر عن النسق الأساسي.

## **Apply a Legacy XLS Preset Autoformat**

يقبل `PivotTable.autoFormatType` قيمة من تعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. القيم المتاحة هي `Report1` إلى `Report10`، و`Classic`، و`Table1` إلى `Table10`.

{{% alert color="primary" %}}

لا يتم الالتزام بـ `autoFormatType` إلا عند حفظ المصنف بصيغة `.xls`. عند حفظ نفس المصنف بصيغة `.xlsx` أو `.xlsm` أو `.xlsb`، يتجاهل Excel هذه الخاصية ويعود إلى إعدادات `pivotTableStyleType` و`pivotTableStyleName`.

{{% /alert %}}

يحمّل المثال التالي مصنفًا جديدًا، ويملأ بيانات نموذج Fruit/Year/Amount، ويضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.Report5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}

**لماذا لا توجد حقول أعمدة؟** تم تصميم التنسيقات التلقائية من سلسلة Report (`Report1` إلى `Report10`، `Table1` إلى `Table10`) في Excel الكلاسيكي لـ **جداول محورية أحادية البُعد** تحتوي على حقول صفوف وقيم فقط — وليس لديها تنسيق مدمج لرؤوس حقول الأعمدة. إذا احتاج الجدول المحوري إلى حقول أعمدة، فاستخدم الإعدادات المسبقة الحديثة `PivotTableStyleType` من السيناريو 2 أدناه بدلاً من ذلك، وهي مصممة للتخطيط ثنائي الأبعاد الذي يستخدمه Excel الحديث.

{{% /alert %}}

```javascript
let workbook = new AsposeCells.Workbook();

// الحصول على ورقة العمل الأولى
let sheet = workbook.getWorksheets().get(0);

// تعبئة البيانات المصدرية بصف الرأس (فاكهة، سنة، كمية)
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
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// تعيين الحقول: الفاكهة -> الصفوف، السنة -> الأعمدة، الكمية -> البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// تطبيق التنسيق التلقائي المحدد مسبقًا لـ XLS القديم "Report5"
// ملاحظة: هذه الخاصية ذات معنى فقط عند الحفظ بصيغة .xls.
// عند الحفظ بصيغة .xlsx/.xlsm/.xlsb، يتجاهل Excel خاصية AutoFormatType
// ويستخدم ما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// حفظ المصنف بصيغة .xls القديمة
workbook.save("output.xls");
```

## **Apply a Modern Named Preset Pivot Table Style**

يقبل `PivotTable.pivotTableStyleType` قيمة من تعداد `Aspose.Cells.PivotTableStyleType`. يغطي التعداد النسق الفاتح `PivotTableStyleLight1` إلى `PivotTableStyleLight28` والنسق الداكن `PivotTableStyleDark1` إلى `PivotTableStyleDark28`. يمكن الوصول إلى الأنماط المضافة في Excel 2017 (الموجة الثانية من النسق الفاتح والداكن) من خلال نفس التعداد.

هذه هي واجهة برمجة التطبيقات الموصى بها لأي تنسيق ملف حديث. على عكس التنسيق التلقائي القديم، يتم عرض النمط المحدد هنا بأمانة بواسطة Excel ويبقى سليمًا عبر الجولات مع أدوات Office الأخرى.

يستخدم المثال التالي نفس بيانات Fruit/Year/Amount، وينشئ جدولًا محوريًا مطابقًا، ويطبق `PivotTableStyleDark1`، ويحفظ المصنف بصيغة `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// صف الرأس: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 صفوف بيانات من الفاكهة / السنة / المبلغ
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

// إضافة جدول محوري في E3 باسم "Pivot1"، مصدره A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين حقول الجدول المحوري: الفاكهة -> منطقة الصفوف، السنة -> منطقة الأعمدة، المبلغ -> منطقة البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// تطبيق نمط جدول محوري مسمى حديث من Excel 2007+.
// PivotTableStyleType هي واجهة برمجة التطبيقات الصحيحة لملفات .xlsx / .xlsm / .xlsb؛ AutoFormatType
// يتم تجاهله بواسطة Excel لتلك التنسيقات. PivotTableStyleDark1 ينتمي إلى عائلة السمة الداكنة
// (PivotTableStyleDark1..PivotTableStyleDark28)، ويعرض نفس التعداد أيضًا سمات Excel 2017
// الفاتحة/الداكنة الأحدث (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// حفظ كـ .xlsx حديث — هذا هو التنسيق الذي يكون فيه PivotTableStyleType ذا معنى.
workbook.save("output.xlsx");
```

## **Define and Apply a Custom Pivot Table Style**

لا يمكن تعديل الإعدادات المسبقة المدمجة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب عليك تعريف نمط جدول محوري مخصص. تتكون سير العمل من ثلاث خطوات:

1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `Worksheets.getTableStyles().addPivotTableStyle(String name)`. يعيد هذا فهرس النمط الذي تم إنشاؤه حديثًا.
2. قم بتكوين النمط عن طريق إضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.tableStyleElements.add(TableStyleElementType)`، ثم قم بتعيين `Style` لكل عنصر عبر `TableStyleElement.setElementStyle(Style)`.
3. طبق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.pivotTableStyleName` إلى اسم النمط. لا تستخدم `pivotTableStyleType` هنا، لأن هذه الخاصية تحدد الإعدادات المسبقة المدمجة.

{{% alert color="primary" %}}

`pivotTableStyleName` و`pivotTableStyleType` ليسا قابلين للتبديل. استخدم `pivotTableStyleType` للإعدادات المسبقة المدمجة، واستخدم `pivotTableStyleName` للأنماط المخصصة التي حددتها من خلال `addPivotTableStyle`. تعيين كليهما غير ضار، ولكن يتم عرض فقط الذي يتطابق مع المصدر المقصود.

{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة `WholeTable` و`FirstRow` و`LastRow` و`FirstColumn` و`LastColumn` و`GrandTotalRow` و`GrandTotalColumn` و`PageFieldLabels` و`PageFieldValues`.

يحدد المثال التالي نمط جدول محوري مخصص بحد أسود رفيع على `WholeTable` وخط أحمر غامق على `GrandTotalRow`، ثم يطبقه عبر `pivotTableStyleName` ويحفظ بصيغة `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// تعبئة البيانات المصدرية: صف العناوين + 9 صفوف بيانات (A1:C10)
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
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

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
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر عريض
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// الخطوة 4: تطبيق النمط المخصص بالاسم (ليس بواسطة PivotTableStyleType، الذي يُستخدم للإعدادات المسبقة المضمنة)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Apply One Style to Every Pivot Cell with FormatAll**

`PivotTable.formatAll(Style)` هو اختصار يطبق كائن `Style` واحد على كل خلية في الجدول المحوري، بما في ذلك منطقة البيانات ورؤوس الصفوف والأعمدة والإجماليات. يتم تجاوز أي شيء تم تعيينه سابقًا من خلال `pivotTableStyleType` أو `pivotTableStyleName`.

{{% alert color="primary" %}}

يتجاوز `formatAll` كلًا من `pivotTableStyleType` و`pivotTableStyleName`. استخدمه فقط عندما يكون المظهر الموحد والمستقل عن النسق مطلوبًا عبر الجدول المحوري بأكمله.

{{% /alert %}}

ينشئ المثال التالي `Style` بتعبئة صلبة باللون الأصفر وخط غامق أزرق غامق وحدود سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `formatAll` ويحفظ بصيغة `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// تعبئة البيانات المصدرية: صف العناوين (الصف 1) + 9 صفوف بيانات (الصفوف 2-10)
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
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين حقول الجدول المحوري: الفاكهة -> منطقة الصفوف، السنة -> منطقة الأعمدة، المبلغ -> منطقة البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// بناء نمط سيتم فرضه على كل خلية في الجدول المحوري
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);

// تطبيق FormatAll: يفرض هذا النمط الوحيد على كل خلية في الجدول المحوري،
// متجاوزًا أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقًا
pivotTable.formatAll(style);

// حفظ المصنف بتنسيق .xlsx الحديث
workbook.save("output.xlsx");
```

## **Which Style API Should I Use?**

يعتمد اختيار واجهة برمجة تطبيقات الأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول التالي كمرجع سريع.

| Target file format | API to use | Notes |
|---|---|---|
| `.xls` (قديم) | `PivotTable.autoFormatType` | القيم من `Aspose.Cells.Pivot.PivotTableAutoFormatType` (مثل `Report1`–`Report10`، `Classic`، `Table1`–`Table10`). يتم تجاهلها عند الحفظ بالتنسيقات الحديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `PivotTable.pivotTableStyleType` | القيم من `Aspose.Cells.PivotTableStyleType` (النسق الفاتح/الداكن، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | استخدم عندما لا تكون الإعدادات المسبقة المدمجة كافية. قم بالتكوين عبر `TableStyleElement.setElementStyle(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.formatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر عبر الجدول المحوري بأكمله. |

في حالة الشك، احفظ بصيغة `.xlsx` واستخدم `pivotTableStyleType` للنسق المدمج، أو `pivotTableStyleName` للنسق المخصص.

{{< app/cells/assistant language="javascript" >}}