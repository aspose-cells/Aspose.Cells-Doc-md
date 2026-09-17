---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Node.js via C++
linktitle: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Node.js via C++
description: تعلّم كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية باستخدام Aspose.Cells for Node.js via C++, بما في ذلك التنسيقات التلقائية القديمة في XLS، وأنماط الجداول المحورية الحديثة المسماة في Excel 2007+، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells Node.js via C++ نمط الجدول المحوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تطبيق كلٍّ من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) وأنماط الجداول المحورية الحديثة المسماة أو المخصصة (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة API التي يجب استدعاؤها على تنسيق الملف الذي يُحفظ إليه المصنف، وليس على التنسيق الذي تم تحميله منه.
{{% /alert %}}

## **المقدمة**
يكشف Aspose.Cells عن واجهتي API متوازيتين للأنماط الخاصة بالجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ مصنف تم تحميله من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة تُطبَّق واجهة API الحديثة للأنماط بدلاً من واجهة API القديمة.
- يحدد `PivotTable.PivotTableStyleType` أحد الأنماط المسماة المدمجة (السمات الفاتحة والداكنة، بما في ذلك الأنماط المُضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- يحدد `PivotTable.PivotTableStyleName` نمطًا مخصصًا تُعرِّفه بنفسك من خلال `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. تُعد الأنماط المخصصة ضرورية كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.
بالإضافة إلى ذلك، يُعد `PivotTable.FormatAll(Style)` اختصارًا يطبّق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أيٍّ من واجهتي API لاسم النمط المذكورتين أعلاه. يكون ذلك مفيدًا عند الحاجة إلى مظهر موحد بصرف النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مسبق الضبط قديم في XLS**
يقبل `PivotTable.AutoFormatType` قيمة من تعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. القيم المتاحة هي `Report1` إلى `Report10`، و`Classic`، و`Table1` إلى `Table10`.
يُحمِّل المثال التالي مصنفًا جديدًا، ويُعبِّئ بيانات النموذج Fruit/Year/Amount، ويُضيف جدولًا محوريًا، ويُطبِّق `PivotTableAutoFormatType.Report5`، ثم يحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}
**لماذا لا توجد حقول أعمدة؟** صُمِّمت التنسيقات التلقائية من سلسلة Report (`Report1` إلى `Report10`، و`Table1` إلى `Table10`) في Excel الكلاسيكي لـ **الجداول المحورية أحادية البعد** التي تحتوي على حقول صفوف وقيم فقط — إذ لا تتضمن تنسيقًا مدمجًا لترويسات حقول الأعمدة. إذا كان الجدول المحوري يحتاج إلى حقول أعمدة، فاستخدم بدلاً من ذلك إعدادات `PivotTableStyleType` المسبقة الحديثة من [السيناريو 2](#apply-a-modern-named-preset-pivot-table-style)، وهي مصممة لتخطيط ثنائي الأبعاد يستخدمه Excel الحديث.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// السيناريو 1: تطبيق تنسيق تلقائي جاهز من إصدارات XLS القديمة
// واجهة برمجة التطبيقات المستخدمة: PivotTable.AutoFormatType
// صيغة الملف الهدف: .xls (إصدار قديم)
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-cells/Aspose.Cells-for-.NET
// إنشاء مصنف جديد
const workbook = new AsposeCells.Workbook();
// الحصول على ورقة العمل الأولى
const sheet = workbook.getWorksheets().get(0);
// تعبئة datos fuente con fila de encabezado (Fruit, Year, Amount)
// y 9 filas de datos que cubren grape, blueberry, kiwi, cherry a lo largo de 2020 y 2021
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
// تعيين الحقول: Fruit -> الصفوف، Amount -> البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// تطبيق التنسيق التلقائي الجاهز للإصدارات القديمة من XLS "Report5"
// ملاحظة: هذه الخاصية تكون ذات معنى فقط عند الحفظ بصيغة .xls.
// عند الحفظ بصيغة .xlsx/.xlsm/.xlsb، يتجاهل Excel خاصية AutoFormatType
// ويستخدم ما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// حفظ المصنف بصيغة .xls القديمة
workbook.save("output.xls");
```

## **تطبيق نمط جدول محوري حديث مسمى مسبق الضبط**

## **تعريف وتطبيق نمط جدول محوري مخصص**
لا يمكن تعديل الإعدادات المسبقة المدمجة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب أن تُعرِّف نمط جدول محوري مخصص. تتكون سير العمل من ثلاث خطوات:
1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. يُرجِع هذا الأمر فهرس النمط الذي تم إنشاؤه حديثًا.
2. اضبط النمط بإضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.TableStyleElements.Add(TableStyleElementType)`، ثم عيّن كائن `Style` لكل عنصر عبر `TableStyleElement.SetElementStyle(Style)`.
3. طبِّق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.PivotTableStyleName` إلى اسم النمط. لا تستخدم `PivotTableStyleType` هنا، لأن هذه الخاصية تحدد الإعدادات المسبقة المدمجة.

{{% alert color="primary" %}}
لا يمكن استخدام `PivotTableStyleName` و`PivotTableStyleType` بالتبادل. استخدم `PivotTableStyleType` للإعدادات المسبقة المدمجة، واستخدم `PivotTableStyleName` للأنماط المخصصة التي تُعرِّفها عبر `AddPivotTableStyle`. تعيين كليهما غير ضار، ولكن يُعرض فقط النمط الذي يطابق المصدر المقصود.
{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة: `WholeTable`، و`FirstRow`، و`LastRow`، و`FirstColumn`، و`LastColumn`، و`GrandTotalRow`، و`GrandTotalColumn`، و`PageFieldLabels`، و`PageFieldValues`.
يُعرِّف المثال التالي نمط جدول محوري مخصصًا بحد أسود رفيع على `WholeTable`، وخط أحمر عريض على `GrandTotalRow`، ثم يُطبِّقه عبر `PivotTableStyleName` ويحفظه بصيغة `.xlsx`.

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
// الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، وهو مخصص للإعدادات المسبقة المدمجة)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **تطبيق نمط واحد على كل خلية من الجدول المحوري باستخدام FormatAll**
يُعد `PivotTable.FormatAll(Style)` اختصارًا يطبّق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات، وترويسات الصفوف والأعمدة، والإجماليات. يتم تجاوز كل ما تم تعيينه مسبقًا عبر `PivotTableStyleType` أو `PivotTableStyleName`.

{{% alert color="primary" %}}
يتجاوز `FormatAll` كلاً من `PivotTableStyleType` و`PivotTableStyleName`. استخدمه فقط عندما يكون مطلوبًا مظهر موحد ومستقل عن السمة في جميع أنحاء الجدول المحوري.
{{% /alert %}}

يُنشئ المثال التالي كائن `Style` بتعبئة صلبة باللون الأصفر، وخط عريض باللون الأزرق الداكن، وحدود سوداء رفيعة على جميع الجوانب، ثم يُطبِّقه باستخدام `FormatAll` ويحفظه بصيغة `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// تعبئة بيانات المصدر: صف العناوين (الصف 1) + 9 صفوف بيانات (الصفوف 2-10)
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
// بناء نمط (Style) سيتم فرضه على كل خلية في الجدول المحوري
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
// تطبيق formatAll: يفرض هذا النمط الوحيد على كل خلية من خلايا الجدول المحوري،
// متجاوزًا أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقًا
pivotTable.formatAll(style);
// حفظ المصنف بتنسيق .xlsx الحديث
workbook.save("output.xlsx");
```

## **أي واجهة API للأنماط يجب أن أستخدم؟**
يعتمد اختيار واجهة API للأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول التالي كمرجع سريع.
| تنسيق الملف المستهدف | الواجهة التي يجب استخدامها | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `PivotTable.AutoFormatType` | قيم من `Aspose.Cells.Pivot.PivotTableAutoFormatType` (مثل `Report1`–`Report10`، و`Classic`، و`Table1`–`Table10`). يتم تجاهلها عند الحفظ بتنسيقات حديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `PivotTable.PivotTableStyleType` | قيم من `Aspose.Cells.PivotTableStyleType` (السمات الفاتحة/الداكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | استخدم عندما لا تكفي الإعدادات المسبقة المدمجة. اضبط عبر `TableStyleElement.SetElementStyle(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.FormatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر في جميع أنحاء الجدول المحوري. |
عند الشك، احفظ بصيغة `.xlsx` واستخدم `PivotTableStyleType` للسمات المدمجة، أو `PivotTableStyleName` للسمات المخصصة.

{{< app/cells/assistant language="nodejs-cpp" >}}