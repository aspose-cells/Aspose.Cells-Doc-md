---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for .NET
linktitle: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for .NET
description: تعلّم كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية في Aspose.Cells for .NET، بما في ذلك التنسيقات التلقائية القديمة في XLS، والأنماط الحديثة المسماة في Excel 2007+، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells .NET نمط الجدول المحوري، PivotTableStyleType، AutoFormatType، FormatAll، نمط مخصص، PivotTableStyleName، TableStyles
type: docs
weight: 200
url: /ar/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تطبيق كلٍّ من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) والأنماط الحديثة المسماة أو المخصصة للجداول المحورية (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يُحفظ إليه المصنف، وليس على التنسيق الذي تم تحميله منه.
{{% /alert %}}

## **المقدمة**
يوفّر Aspose.Cells واجهتي برمجة تطبيقات متوازيتين للأنماط الخاصة بالجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تُحفظ إليه المصنف، وليس على التنسيق الذي تقرأ منه. يمكن إعادة حفظ مصنف تم تحميله من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة تنطبق واجهة الأنماط الحديثة وليس القديمة.
- `PivotTable.PivotTableStyleType` يختار أحد الأنماط المسماة المدمجة (سمات فاتحة وداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- `PivotTable.PivotTableStyleName` يختار نمطًا مخصصًا تُعرّفه بنفسك من خلال `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. تُعدّ الأنماط المخصصة ضرورية كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.
بالإضافة إلى ذلك، تُعدّ `PivotTable.FormatAll(Style)` اختصارًا يُطبّق كائن `Style` واحدًا على كل خلية في الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أيٍّ من واجهتي أسماء الأنماط أعلاه. يكون ذلك مفيدًا عند الحاجة إلى مظهر موحّد بصرف النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مسبق من XLS الكلاسيكي**
تقبل `PivotTable.AutoFormatType` قيمة من تعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. القيم المتاحة هي `Report1` إلى `Report10`، و`Classic`، و`Table1` إلى `Table10`.
يقوم المثال التالي بتحميل مصنف جديد، وملء بيانات العينة الخاصة بالفاكهة/السنة/المبلغ، وإضافة جدول محوري، وتطبيق `PivotTableAutoFormatType.Report5`، وحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}
**لماذا لا توجد حقول أعمدة؟** صُمّمت التنسيقات التلقائية من سلسلة التقارير (`Report1` إلى `Report10`، و`Table1` إلى `Table10`) في Excel الكلاسيكي للجداول المحورية **أحادية البعد** التي تحتوي على حقول صفوف وقيم فقط — ولا تتضمن تنسيقًا مدمجًا لرؤوس حقول الأعمدة. إذا كان الجدول المحوري الخاص بك يحتاج إلى حقول أعمدة، فاستخدم إعدادات `PivotTableStyleType` الحديثة من [السيناريو 2](#apply-a-modern-named-preset-pivot-table-style) بدلاً من ذلك، فهي مصممة لتخطيط ثنائي الأبعاد يستخدمه Excel الحديث.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// السيناريو 1: تطبيق تنسيق تلقائي سابق XLS
// واجهة API المستخدمة: PivotTable.AutoFormatType
// تنسيق الملف المستهدف: .xls (قديم)
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-cells/Aspose.Cells-for-.NET
// إنشاء مصنف جديد
Workbook workbook = new Workbook();
// الحصول على ورقة العمل الأولى
Worksheet sheet = workbook.Worksheets[0];
// تعبئة بيانات المصدر بصف رأس (فاكهة، سنة، مبلغ)
// و9 صفوف بيانات تغطي العنب، التوت الأزرق، الكيوي، الكرز عبر 2020 و2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");
sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);
sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);
sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);
sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);
sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);
sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);
sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);
sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);
sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);
// إضافة جدول محوري في خلية الوجهة E3، باسم "Pivot1"، باستخدام نطاق المصدر A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];
// تعيين الحقول: فاكهة -> صفوف، مبلغ -> بيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// تطبيق التنسيق التلقائي المحدد مسبقًا لـ XLS القديم "Report5"
// ملاحظة: هذه الخاصية ذات معنى فقط عند الحفظ بصيغة .xls.
// عند الحفظ بصيغة .xlsx/.xlsm/.xlsb، يتجاهل Excel AutoFormatType
// ويستخدم ما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// حفظ المصنف بصيغة .xls القديمة
workbook.Save("output.xls");
```

## **تطبيق نمط جدول محوري مسمى مسبق حديث**

## **تحديد نمط جدول محوري مخصص وتطبيقه**
لا يمكن تعديل الإعدادات المسبقة المدمجة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب تحديد نمط محوري مخصص. تتكون سير العمل من ثلاث خطوات:
1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. يُرجع ذلك فهرس النمط الذي تم إنشاؤه حديثًا.
2. قم بتكوين النمط بإضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.TableStyleElements.Add(TableStyleElementType)`، ثم عيّن `Style` لكل عنصر عبر `TableStyleElement.SetElementStyle(Style)`.
3. طبّق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.PivotTableStyleName` إلى اسم النمط. لا تستخدم `PivotTableStyleType` هنا، إذ أن هذه الخاصية تختار الإعدادات المسبقة المدمجة.

{{% alert color="primary" %}}
`PivotTableStyleName` و`PivotTableStyleType` ليسا قابلين للتبادل. استخدم `PivotTableStyleType` للإعدادات المسبقة المدمجة، واستخدم `PivotTableStyleName` للأنماط المخصصة التي قمت بتعريفها من خلال `AddPivotTableStyle`. تعيين كليهما غير ضار، ولكن يُعرض فقط النمط المطابق للمصدر المقصود.
{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة: `WholeTable`، و`FirstRow`، و`LastRow`، و`FirstColumn`، و`LastColumn`، و`GrandTotalRow`، و`GrandTotalColumn`، و`PageFieldLabels`، و`PageFieldValues`.
يحدد المثال التالي نمطًا محوريًا مخصصًا بحد أسود رفيع على `WholeTable` وخط أحمر عريض على `GrandTotalRow`، ثم يطبّقه عبر `PivotTableStyleName` ويحفظ بصيغة `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// تعبئة البيانات المصدرية: صف العناوين + 9 صفوف بيانات (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);
// إضافة جدول محوري مصدره A1:C10، مثبت عند E3، باسم "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// الخطوة 1: تسجيل نمط جدول محوري مخصص جديد وحفظ فهرسه
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];
// الخطوة 2: إضافة عنصر WholeTable وتطبيق حدود سوداء رفيعة على الجوانب الأربعة
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);
// الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر عريض
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);
// الخطوة 4: تطبيق النمط المخصص بالاسم (وليس عن طريق PivotTableStyleType، الذي يُستخدم للإعدادات المسبقة المدمجة)
pivotTable.PivotTableStyleName = "CustomPivotStyle";
workbook.Save("output.xlsx");
```

## **تطبيق نمط واحد على كل خلية محورية باستخدام FormatAll**
تُعدّ `PivotTable.FormatAll(Style)` اختصارًا يُطبّق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات ورؤوس الصفوف والأعمدة والإجماليات. يتم تجاوز أي شيء تم تعيينه سابقًا من خلال `PivotTableStyleType` أو `PivotTableStyleName`.

{{% alert color="primary" %}}
يتجاوز `FormatAll` كلًا من `PivotTableStyleType` و`PivotTableStyleName`. استخدمه فقط عند الحاجة إلى مظهر موحّد ومستقل عن السمة في جميع أنحاء الجدول المحوري.
{{% /alert %}}

ينشئ المثال التالي `Style` بتعبئة صلبة باللون الأصفر، وخط عريض بلون أزرق داكن، وحدود سوداء رفيعة على جميع الجوانب، ثم يطبّقه باستخدام `FormatAll` ويحفظ بصيغة `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// السيناريو 4: تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام FormatAll
// API المستخدم: PivotTable.FormatAll(Style)
// الصيغة المستهدفة: .xlsx
// مرجع GitHub: راجع مستودع Aspose.Cells-for-.NET — أمثلة تنسيق الجدول المحوري
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// ملء بيانات المصدر: صف الرأس (الصف 1) + 9 صفوف بيانات (الصفوف 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);
// إضافة الجدول المحوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// تعيين حقول الجدول المحوري: Fruit -> منطقة الصفوف، Year -> منطقة الأعمدة، Amount -> منطقة البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// بناء نمط Style سيتم فرضه على كل خلية من خلايا الجدول المحوري
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;
// تطبيق FormatAll: يفرض هذا النمط الوحيد على كل خلية من خلايا الجدول المحوري،
// متجاوزًا أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقًا
pivotTable.FormatAll(style);
// حفظ المصنف بالصيغة الحديثة .xlsx
workbook.Save("output.xlsx");
```

## **أيّ واجهة برمجة تطبيقات للأنماط ينبغي أن أستخدم؟**
يعتمد اختيار واجهة الأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول أدناه كمرجع سريع.
| تنسيق الملف المستهدف | واجهة برمجة التطبيقات المستخدمة | ملاحظات |
|---|---|---|
| `.xls` (كلاسيكي) | `PivotTable.AutoFormatType` | القيم من `Aspose.Cells.Pivot.PivotTableAutoFormatType` (مثل `Report1`–`Report10`، و`Classic`، و`Table1`–`Table10`). يتم تجاهلها عند الحفظ بالتنسيقات الحديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `PivotTable.PivotTableStyleType` | القيم من `Aspose.Cells.PivotTableStyleType` (سمات فاتحة وداكنة، بما في ذلك الإضافات في Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | يُستخدم عندما لا تكفي الإعدادات المسبقة المدمجة. يتم التكوين عبر `TableStyleElement.SetElementStyle(...)`. |
| أي تنسيق (تجاوز موحّد) | `PivotTable.FormatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر في جميع أنحاء الجدول المحوري. |
عند الشك، احفظ بصيغة `.xlsx` واستخدم `PivotTableStyleType` للسمات المدمجة، أو `PivotTableStyleName` للسمات المخصصة.

## المقالات ذات الصلة
- [إضافة حقول صفوف وأعمدة للجدول المحوري في Aspose.Cells for .NET](/cells/ar/net/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في الجدول المحوري في Aspose.Cells for .NET](/cells/ar/net/manage-value-fields/)
- [تحديث الجداول المحورية في Aspose.Cells for .NET](/cells/ar/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}