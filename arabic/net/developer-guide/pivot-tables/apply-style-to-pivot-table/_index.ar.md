---
title: تطبيق الأنماط على الجداول المحورية
linktitle: تطبيق الأنماط
description: تعرّف على كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية في Aspose.Cells for .NET، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، وأنماط Excel 2007+ الحديثة المُسماة، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells .NET pivot table style, PivotTableStyleType, AutoFormatType, FormatAll, custom style, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تطبيق كل من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) وأنماط الجداول المحورية الحديثة المُسماة أو المخصصة (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يتم حفظ المصنف به، وليس على التنسيق الذي تم تحميله منه.

{{% /alert %}}

## **المقدمة**

يوفر Aspose.Cells واجهتي نمط متوازيتين للجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأ منه. يمكن إعادة حفظ المصنف المحمّل من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة يتم تطبيق واجهة برمجة التطبيقات للأنماط الحديثة بدلاً من الواجهة القديمة.

بالنسبة لمخرجات `.xls` القديمة، استخدم الخاصية `PivotTable.AutoFormatType` مع التعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. تتوافق واجهة برمجة التطبيقات هذه مع منتقي التنسيق التلقائي الذي كان Excel الكلاسيكي يقدمه للجداول المحورية.

بالنسبة لمخرجات `.xlsx` و`.xlsm` و`.xlsb` الحديثة، تتوفر نكهتان من واجهة برمجة تطبيقات الأنماط:

- `PivotTable.PivotTableStyleType` يحدد أحد الأنماط المُسماة المدمجة (السمات الفاتحة والداكنة، بما في ذلك الأنماط المُضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- `PivotTable.PivotTableStyleName` يحدد نمطًا مخصصًا تقوم بتعريفه بنفسك من خلال `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. تُعد الأنماط المخصصة ضرورية كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.

بالإضافة إلى ذلك، يُعد `PivotTable.FormatAll(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية في الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أي من واجهتي أسماء الأنماط أعلاه. يكون هذا مفيدًا عندما يكون المظهر الموحد مطلوبًا بغض النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مسبق لملف XLS القديم**

يقبل `PivotTable.AutoFormatType` قيمة من التعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. القيم المتاحة هي `Report1` إلى `Report10`، و`Classic`، و`Table1` إلى `Table10`.

{{% alert color="primary" %}}

لا يتم الالتزام بـ `AutoFormatType` إلا عند حفظ المصنف بصيغة `.xls`. عندما يتم حفظ نفس المصنف بصيغة `.xlsx` أو `.xlsm` أو `.xlsb`، يتجاهل Excel هذه الخاصية ويعود إلى إعدادات `PivotTableStyleType` و`PivotTableStyleName`.

{{% /alert %}}

يُحمّل المثال التالي مصنفًا جديدًا، ويملأ بيانات العينة الخاصة بـ Fruit/Year/Amount، ويُضيف جدولًا محوريًا، ويُطبق `PivotTableAutoFormatType.Report5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}

**لماذا لا توجد حقول أعمدة؟** تم تصميم التنسيقات التلقائية من سلسلة Report (`Report1` إلى `Report10`، `Table1` إلى `Table10`) في Excel الكلاسيكي لـ **جداول محورية أحادية البُعد** تحتوي على حقول صفوف وقيم فقط — وليس لديها تنسيق مدمج لرؤوس حقول الأعمدة. إذا احتاج الجدول المحوري إلى حقول أعمدة، فاستخدم الإعدادات المسبقة الحديثة `PivotTableStyleType` من السيناريو 2 أدناه بدلاً من ذلك، وهي مصممة للتخطيط ثنائي الأبعاد الذي يستخدمه Excel الحديث.

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// السيناريو 1: تطبيق تنسيق تلقائي مسبق الضبط بتنسيق XLS القديم
// واجهة برمجة التطبيقات المستخدمة: PivotTable.AutoFormatType
// تنسيق الملف المستهدف: .xls (قديم)
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-cells/Aspose.Cells-for-.NET

// إنشاء مصنف جديد
Workbook workbook = new Workbook();

// الحصول على ورقة العمل الأولى
Worksheet sheet = workbook.Worksheets[0];

// ملء البيانات المصدرية بصف الرأس (الفاكهة، السنة، المبلغ)
// و9 صفوف بيانات تغطي العنب، والتوت الأزرق، والكيوي، والكرز عبر عامي 2020 و2021
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

// تعيين الحقول: الفاكهة -> الصفوف، السنة -> الأعمدة، المبلغ -> البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// تطبيق التنسيق التلقائي المحدد مسبقًا لتنسيق XLS القديم "Report5"
// ملاحظة: هذه الخاصية ذات معنى فقط عند الحفظ بتنسيق .xls.
// عند الحفظ بتنسيق .xlsx/.xlsm/.xlsb، يتجاهل Excel الخاصية AutoFormatType
// ويستخدم ما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// حفظ المصنف بتنسيق .xls القديم
workbook.Save("output.xls");
```

## **تطبيق نمط جدول محوري مسمى مسبق حديث من Excel 2007+**

يقبل `PivotTable.PivotTableStyleType` قيمة من التعداد `Aspose.Cells.PivotTableStyleType`. يغطي التعداد السمات الفاتحة `PivotTableStyleLight1` إلى `PivotTableStyleLight28` والسمات الداكنة `PivotTableStyleDark1` إلى `PivotTableStyleDark28`. يمكن الوصول إلى الأنماط المُضافة في Excel 2017 (الموجة الثانية من السمات الفاتحة والداكنة) من خلال نفس التعداد.

هذه هي واجهة برمجة التطبيقات الموصى بها لأي تنسيق ملف حديث. على عكس التنسيق التلقائي القديم، يتم عرض النمط المحدد هنا بشكل دقيق بواسطة Excel ويظل ثابتًا عبر عمليات الحفظ والتحميل باستخدام أدوات Office الأخرى.

يستخدم المثال التالي نفس بيانات Fruit/Year/Amount، ويُنشئ جدولًا محوريًا مطابقًا، ويُطبق `PivotTableStyleDark1`، ويحفظ المصنف بصيغة `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// السيناريو 2: تطبيق نمط معياري مسمى حديث من Excel 2007+ باستخدام PivotTableStyleType.
// تنسيق الملف المستهدف: .xlsx. تعداد PivotTableStyleType موجود في مساحة الاسم Aspose.Cells
// (وليس في Aspose.Cells.Pivot) — لهذا السبب لا نحتاج إلى أي استخدام إضافي له.
// مرجع GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// صف الرأس: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 صفوف بيانات من Fruit / Year / Amount
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// إضافة جدول محوري في E3 باسم "Pivot1"، مصدره من A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// تعيين حقول المحور: Fruit -> منطقة الصف، Year -> منطقة العمود، Amount -> منطقة البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// تطبيق نمط محوري معياري مسمى حديث من Excel 2007+.
// PivotTableStyleType هو API الصحيح لملفات .xlsx / .xlsm / .xlsb؛ AutoFormatType
// يتم تجاهله بواسطة Excel لهذه التنسيقات. ينتمي PivotTableStyleDark1 إلى عائلة
// السمات الداكنة (PivotTableStyleDark1..PivotTableStyleDark28)، ويكشف نفس التعداد أيضاً عن
// سمات Excel 2017 الفاتحة/الداكنة الأحدث (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// الحفظ كملف .xlsx حديث — هذا هو التنسيق الذي يكون فيه PivotTableStyleType ذا معنى.
workbook.Save("output.xlsx");
```

## **تعريف وتطبيق نمط جدول محوري مخصص**

لا يمكن تعديل الإعدادات المسبقة المدمجة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب عليك تعريف نمط جدول محوري مخصص. تتكون سير العمل من ثلاث خطوات:

1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. يُرجع هذا فهرس النمط المُنشأ حديثًا.
2. قم بتهيئة النمط عن طريق إضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.TableStyleElements.Add(TableStyleElementType)`، ثم عيّن `Style` لكل عنصر عبر `TableStyleElement.SetElementStyle(Style)`.
3. طبق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.PivotTableStyleName` إلى اسم النمط. لا تستخدم `PivotTableStyleType` هنا، لأن هذه الخاصية تحدد الإعدادات المسبقة المدمجة.

{{% alert color="primary" %}}

لا يمكن تبادل `PivotTableStyleName` و`PivotTableStyleType`. استخدم `PivotTableStyleType` للإعدادات المسبقة المدمجة، و`PivotTableStyleName` للأنماط المخصصة التي قمت بتعريفها من خلال `AddPivotTableStyle`. تعيين كليهما غير ضار، ولكن يتم عرض فقط الذي يطابق المصدر المقصود.

{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة `WholeTable`، و`FirstRow`، و`LastRow`، و`FirstColumn`، و`LastColumn`، و`GrandTotalRow`، و`GrandTotalColumn`، و`PageFieldLabels`، و`PageFieldValues`.

يُعرّف المثال التالي نمط جدول محوري مخصص بحد أسود رفيع على `WholeTable` وخط أحمر غامق على `GrandTotalRow`، ثم يطبقه عبر `PivotTableStyleName` ويحفظ بصيغة `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using Aspose.Cells.Tables;
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

// الخطوة 1: تسجيل نمط جدول محوري مخصص جديد والتقاط فهرسه
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

// الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر غامق
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، الذي يُستخدم للإعدادات المسبقة المضمنة)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **تطبيق نمط واحد على كل خلية في الجدول المحوري باستخدام FormatAll**

يُعد `PivotTable.FormatAll(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية في الجدول المحوري، بما في ذلك منطقة البيانات ورؤوس الصفوف والأعمدة والإجماليات. يتم تجاوز أي شيء تم تعيينه سابقًا من خلال `PivotTableStyleType` أو `PivotTableStyleName`.

{{% alert color="primary" %}}

يتجاوز `FormatAll` كلًا من `PivotTableStyleType` و`PivotTableStyleName`. استخدمه فقط عندما يكون المظهر الموحد المستقل عن السمة مطلوبًا عبر كامل الجدول المحوري.

{{% /alert %}}

يُنشئ المثال التالي `Style` بتعبئة صلبة باللون الأصفر، وخط أزرق داكن غامق، وحدود سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `FormatAll` ويحفظ بصيغة `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// السيناريو 4: تطبيق نمط (Style) واحد على كل خلية في الجدول المحوري باستخدام FormatAll
// الـ API المستخدم: PivotTable.FormatAll(Style)
// التنسيق المستهدف: .xlsx
// مرجع GitHub: انظر إلى مستودع Aspose.Cells-for-.NET — أمثلة تنسيق الجدول المحوري

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

// إضافة جدول محوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// تعيين حقول الجدول المحوري: Fruit -> منطقة الصفوف، Year -> منطقة الأعمدة، Amount -> منطقة البيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// إنشاء كائن Style سيتم فرضه على كل خلية في الجدول المحوري
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

// تطبيق FormatAll: يفرض هذا النمط الواحد على كل خلية في الجدول المحوري،
// متجاوزًا أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقًا
pivotTable.FormatAll(style);

// حفظ المصنف بتنسيق .xlsx الحديث
workbook.Save("output.xlsx");
```

## **أي واجهة برمجة تطبيقات للأنماط يجب أن أستخدم؟**

يعتمد اختيار واجهة برمجة تطبيقات الأنماط على تنسيق الملف الذي تحفظ به. استخدم الجدول أدناه كمرجع سريع.

| تنسيق الملف الهدف | واجهة برمجة التطبيقات المستخدمة | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `PivotTable.AutoFormatType` | القيم من `Aspose.Cells.Pivot.PivotTableAutoFormatType` (مثل `Report1`–`Report10`، و`Classic`، و`Table1`–`Table10`). يتم تجاهلها عند الحفظ بتنسيقات حديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `PivotTable.PivotTableStyleType` | القيم من `Aspose.Cells.PivotTableStyleType` (السمات الفاتحة والداكنة، بما في ذلك الإضافات في Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | استخدم عندما لا تكون الإعدادات المسبقة المدمجة كافية. قم بالتهيئة عبر `TableStyleElement.SetElementStyle(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.FormatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر عبر كامل الجدول المحوري. |

عندما تكون في شك، احفظ بصيغة `.xlsx` واستخدم `PivotTableStyleType` للسمات المدمجة، أو `PivotTableStyleName` للسمات المخصصة.

{{< app/cells/assistant language="csharp" >}}