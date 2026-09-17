---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Node.js via Java
linktitle: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Node.js via Java
description: تعرف على كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية في Aspose.Cells for Node.js via Java، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، والأنماط المسماة الحديثة في Excel 2007+، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
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
// إضافة جدول محوري في خلية الوجهة E3، باسم "Pivot1"، باستخدام نطاق المصدر A1:C10
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);
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

## **تحديد نمط جدول محوري مخصص وتطبيقه**
لا يمكن تعديل الإعدادات المسبقة المدمجة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب تحديد نمط محوري مخصص. تتكون سير العمل من ثلاث خطوات:
1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `Worksheets.getTableStyles().addPivotTableStyle(String name)`. يُرجع هذا فهرس النمط المُنشأ حديثًا.
2. اضبط النمط بإضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.tableStyleElements.add(TableStyleElementType)`، ثم عيّن كائن `Style` لكل عنصر عبر `TableStyleElement.setElementStyle(Style)`.
3. طبِّق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.pivotTableStyleName` إلى اسم النمط. لا تستخدم `pivotTableStyleType` هنا، لأن هذه الخاصية تحدد الإعدادات المسبقة المدمجة.

{{% alert color="primary" %}}
لا يمكن استخدام `pivotTableStyleName` و`pivotTableStyleType` بالتبادل. استخدم `pivotTableStyleType` للإعدادات المسبقة المدمجة، و`pivotTableStyleName` للأنماط المخصصة التي حددتها عبر `addPivotTableStyle`. تعيين كليهما لا يضر، ولكن يُعرض فقط النمط المطابق للمصدر المطلوب.
{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة: `WholeTable`، و`FirstRow`، و`LastRow`، و`FirstColumn`، و`LastColumn`، و`GrandTotalRow`، و`GrandTotalColumn`، و`PageFieldLabels`، و`PageFieldValues`.
يُعرِّف المثال التالي نمطًا محوريًا مخصصًا بحد أسود رفيع على `WholeTable` وخط أحمر غامق على `GrandTotalRow`، ثم يطبقه عبر `pivotTableStyleName` ويحفظه بصيغة `.xlsx`.

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
// الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، وهو للإعدادات المسبقة المضمنة)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **تطبيق نمط واحد على كل خلية في الجدول المحوري باستخدام FormatAll**
يُعد `PivotTable.formatAll(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات وترويسات الصفوف والأعمدة والإجماليات. يتم تجاوز كل ما تم تعيينه سابقًا عبر `pivotTableStyleType` أو `pivotTableStyleName`.

{{% alert color="primary" %}}
يتجاوز `formatAll` كلًا من `pivotTableStyleType` و`pivotTableStyleName`. استخدمه فقط عندما يكون مطلوبًا مظهر موحد ومستقل عن النسق في جميع أنحاء الجدول المحوري.
{{% /alert %}}

يُنشئ المثال التالي كائن `Style` بتعبئة صلبة صفراء، وخط أزرق داكن غامق، وحواف سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `formatAll` ويحفظه بصيغة `.xlsx`.

```javascript
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
// إضافة جدول محوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// تعيين حقول الجدول المحوري: Fruit -> منطقة الصفوف، Year -> منطقة الأعمدة، Amount -> منطقة البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// بناء نمط Style سيتم فرضه على كل خلية في الجدول المحوري
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
// تطبيق FormatAll: يفرض هذا النمط الواحد على كل خلية في الجدول المحوري،
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