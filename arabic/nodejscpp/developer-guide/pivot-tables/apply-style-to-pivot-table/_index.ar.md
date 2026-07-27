---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells لـ .NET
linktitle: تطبيق أنماط الجداول المحورية
description: تعرّف على كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية في Aspose.Cells for Node.js via C++، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، وأنماط Excel 2007+ الحديثة المُسماة، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells Node.js via C++ pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تطبيق كل من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) وأنماط الجداول المحورية الحديثة المسماة أو المخصصة (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يتم حفظ المصنف به، وليس على التنسيق الذي تم تحميله منه.

{{% /alert %}}

## **مقدمة**

يكشف Aspose.Cells عن واجهتي أنماط متوازيتين للجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ مصنف تم تحميله من ملف `.xls` بتنسيق `.xlsx`، وفي هذه الحالة تنطبق واجهة برمجة التطبيقات للأنماط الحديثة بدلاً من واجهة الأنماط القديمة.

للحصول على إخراج بصيغة `.xls` القديمة، استخدم الخاصية `PivotTable.AutoFormatType` مع تعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. تتوافق واجهة برمجة التطبيقات هذه مع منتقي التنسيق التلقائي الذي كان Excel الكلاسيكي يوفره للجداول المحورية.

للحصول على إخراج حديث بصيغة `.xlsx` و`.xlsm` و`.xlsb`، يتوفر نوعان من واجهة برمجة التطبيقات للأنماط:

- `PivotTable.PivotTableStyleType` تختار أحد الأنماط المسماة المضمنة (السمات الفاتحة والداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- `PivotTable.PivotTableStyleName` تختار نمطًا مخصصًا تحدده بنفسك من خلال `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. تكون الأنماط المخصصة مطلوبة كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.

بالإضافة إلى ذلك، فإن `PivotTable.FormatAll(Style)` هي اختصار يطبق كائن `Style` واحد على كل خلية من الجدول المحوري، متجاوزًا كل ما يتم تعيينه من خلال أي من واجهات برمجة تطبيقات أسماء الأنماط أعلاه. يكون هذا مفيدًا عندما يكون مطلوبًا مظهر موحد بغض النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مسبق الإعداد لـ XLS القديم**

يقبل `PivotTable.AutoFormatType` قيمة من تعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. القيم المتاحة هي `Report1` إلى `Report10`، و`Classic`، و`Table1` إلى `Table10`.

{{% alert color="primary" %}}

لا يتم الالتزام بـ `AutoFormatType` إلا عند حفظ المصنف بصيغة `.xls`. عندما يتم حفظ المصنف نفسه بصيغة `.xlsx` أو `.xlsm` أو `.xlsb`، يتجاهل Excel هذه الخاصية ويعود إلى إعدادات `PivotTableStyleType` و`PivotTableStyleName`.

{{% /alert %}}

يقوم المثال التالي بتحميل مصنف جديد، ويملأ بيانات الفاكهة/السنة/المبلغ النموذجية، ويضيف جدولاً محوريًا، ويطبق `PivotTableAutoFormatType.Report5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}

**لماذا لا توجد حقول أعمدة؟** تم تصميم التنسيقات التلقائية من سلسلة Report (`Report1` إلى `Report10`، `Table1` إلى `Table10`) في Excel الكلاسيكي لـ **جداول محورية أحادية البُعد** تحتوي على حقول صفوف وقيم فقط — وليس لديها تنسيق مدمج لرؤوس حقول الأعمدة. إذا احتاج الجدول المحوري إلى حقول أعمدة، فاستخدم الإعدادات المسبقة الحديثة `PivotTableStyleType` من السيناريو 2 أدناه بدلاً من ذلك، وهي مصممة للتخطيط ثنائي الأبعاد الذي يستخدمه Excel الحديث.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");

// السيناريو 1: تطبيق تنسيق تلقائي جاهز قديم بصيغة XLS
// واجهة برمجة التطبيقات المستخدمة: PivotTable.AutoFormatType
// صيغة الملف المستهدف: .xls (قديمة)
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-cells/Aspose.Cells-for-.NET

// إنشاء مصنف جديد
const workbook = new AsposeCells.Workbook();

// الحصول على ورقة العمل الأولى
const sheet = workbook.getWorksheets().get(0);

// ملء بيانات المصدر بصف الرأس (فاكهة، سنة، مبلغ)
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

// إضافة جدول محوري في خلية الوجهة E3، باسم "Pivot1"، باستخدام نطاق المصدر A1:C10
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);

// تعيين الحقول: الفاكهة -> الصفوف، السنة -> الأعمدة، المبلغ -> البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تطبيق التنسيق التلقائي الجاهز القديم الخاص بـ XLS "Report5"
// ملاحظة: هذه الخاصية تكون ذات معنى فقط عند الحفظ بصيغة .xls.
// عند الحفظ بصيغة .xlsx/.xlsm/.xlsb، يتجاهل Excel خاصية AutoFormatType
// ويستخدم ما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// حفظ المصنف بصيغة .xls القديمة
workbook.save("output.xls");
```

## **تطبيق نمط جدول محوري مسمى مسبق الإعداد حديث**

يقبل `PivotTable.PivotTableStyleType` قيمة من تعداد `Aspose.Cells.PivotTableStyleType`. يغطي التعداد السمات الفاتحة `PivotTableStyleLight1` إلى `PivotTableStyleLight28` والسمات الداكنة `PivotTableStyleDark1` إلى `PivotTableStyleDark28`. يمكن الوصول إلى الأنماط المضافة في Excel 2017 (الموجة الثانية من السمات الفاتحة والداكنة) من خلال نفس التعداد.

هذه هي واجهة برمجة التطبيقات الموصى بها لأي تنسيق ملف حديث. وعلى عكس التنسيق التلقائي القديم، يتم عرض النمط المحدد هنا بأمانة بواسطة Excel ويصمد أمام عمليات النقل ذهابًا وإيابًا عبر أدوات Office الأخرى.

يستخدم المثال التالي نفس بيانات الفاكهة/السنة/المبلغ، وينشئ جدولاً محوريًا مطابقًا، ويطبق `PivotTableStyleDark1`، ويحفظ المصنف بصيغة `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// صف الرأس: فاكهة / سنة / كمية
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 صفوف بيانات من فاكهة / سنة / كمية
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

// إضافة جدول محوري عند E3 باسم "Pivot1"، مصدره A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين حقول الجدول المحوري: فاكهة -> منطقة الصفوف، سنة -> منطقة الأعمدة، كمية -> منطقة البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// تطبيق نمط جدول محوري مسمى حديث من Excel 2007+.
// PivotTableStyleType هو واجهة برمجة التطبيقات الصحيحة لملفات .xlsx / .xlsm / .xlsb؛ يتم تجاهل AutoFormatType من قبل Excel لتلك التنسيقات.
// ينتمي PivotTableStyleDark1 إلى عائلة السمات الداكنة (PivotTableStyleDark1..PivotTableStyleDark28)، ويكشف نفس التعداد أيضًا عن سمات Excel 2017 الأحدث الفاتحة/الداكنة (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);

// حفظ بصيغة .xlsx الحديثة - هذه هي الصيغة التي يكون فيها PivotTableStyleType ذا معنى.
workbook.save("output.xlsx");
```

## **تحديد وتطبيق نمط جدول محوري مخصص**

لا يمكن تعديل الإعدادات المسبقة المضمنة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب تحديد نمط محوري مخصص. تتكون سير العمل من ثلاث خطوات:

1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. يُرجع هذا فهرس النمط الذي تم إنشاؤه حديثًا.
2. قم بتكوين النمط عن طريق إضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.TableStyleElements.Add(TableStyleElementType)`، ثم قم بتعيين `Style` لكل عنصر عبر `TableStyleElement.SetElementStyle(Style)`.
3. طبق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.PivotTableStyleName` إلى اسم النمط. لا تستخدم `PivotTableStyleType` هنا، لأن هذه الخاصية تختار الإعدادات المسبقة المضمنة.

{{% alert color="primary" %}}

لا يمكن استبدال `PivotTableStyleName` و`PivotTableStyleType` ببعضهما البعض. استخدم `PivotTableStyleType` للإعدادات المسبقة المضمنة، و`PivotTableStyleName` للأنماط المخصصة التي حددتها من خلال `AddPivotTableStyle`. تعيين كليهما لا يضر، ولكن يتم عرض فقط ما يطابق المصدر المقصود.

{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة `WholeTable` و`FirstRow` و`LastRow` و`FirstColumn` و`LastColumn` و`GrandTotalRow` و`GrandTotalColumn` و`PageFieldLabels` و`PageFieldValues`.

يحدد المثال التالي نمطًا محوريًا مخصصًا بحد أسود رفيع على `WholeTable` وخط أحمر عريض على `GrandTotalRow`، ثم يطبقه عبر `PivotTableStyleName` ويحفظه بصيغة `.xlsx`.

```javascript
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

// إضافة جدول محوري مصدره A1:C10، مثبت عند E3، باسم "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// الخطوة 1: تسجيل نمط جدول محوري مخصص جديد والتقاط فهرسه
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// الخطوة 2: إضافة عنصر WholeTable وتطبيق حدود سوداء رفيعة على الجوانب الأربعة
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);

// الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر عريض
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);

// الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، وهو للإعدادات المسبقة المضمنة)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **تطبيق نمط واحد على كل خلية من الجدول المحوري باستخدام FormatAll**

`PivotTable.FormatAll(Style)` هي اختصار يطبق كائن `Style` واحدًا على كل خلية من الجدول المحوري، بما في ذلك منطقة البيانات ورؤوس الصفوف والأعمدة والإجماليات. يتم تجاوز كل ما تم تعيينه مسبقًا من خلال `PivotTableStyleType` أو `PivotTableStyleName`.

{{% alert color="primary" %}}

تتجاوز `FormatAll` كلًا من `PivotTableStyleType` و`PivotTableStyleName`. استخدمها فقط عندما يكون مطلوبًا مظهر موحد ومستقل عن السمة عبر الجدول المحوري بأكمله.

{{% /alert %}}

ينشئ المثال التالي كائن `Style` بتعبئة صفراء صلبة وخط أزرق داكن عريض وحدود سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `FormatAll` ويحفظه بصيغة `.xlsx`.

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

// إنشاء نمط سيُفرض على كل خلية في الجدول المحوري
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
pivotTable.formatAll(style);

// متجاوزًا أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقًا
workbook.save("output.xlsx");
```

## **أي واجهة برمجة تطبيقات للأنماط يجب أن أستخدم؟**

يعتمد اختيار واجهة برمجة تطبيقات الأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول أدناه كمرجع سريع.

| تنسيق الملف المستهدف | واجهة برمجة التطبيقات المراد استخدامها | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `PivotTable.AutoFormatType` | القيم من `Aspose.Cells.Pivot.PivotTableAutoFormatType` (مثل `Report1`–`Report10`، و`Classic`، و`Table1`–`Table10`). يتم تجاهلها عند الحفظ بتنسيقات حديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مضمّن) | `PivotTable.PivotTableStyleType` | القيم من `Aspose.Cells.PivotTableStyleType` (السمات الفاتحة/الداكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | استخدم عندما لا تكون الإعدادات المسبقة المضمنة كافية. قم بالتكوين عبر `TableStyleElement.SetElementStyle(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.FormatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر عبر الجدول المحوري بأكمله. |

عند الشك، احفظ بصيغة `.xlsx` واستخدم `PivotTableStyleType` للسمات المضمنة، أو `PivotTableStyleName` للسمات المخصصة.

{{< app/cells/assistant language="javascript" >}}