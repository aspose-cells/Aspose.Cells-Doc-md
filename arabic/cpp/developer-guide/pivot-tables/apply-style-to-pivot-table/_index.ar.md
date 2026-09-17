---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for C++
linktitle: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for C++
description: تعلم كيفية تطبيق الأنماط المضمنة والمخصصة على الجداول المحورية في Aspose.Cells for C++، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، والأنماط الحديثة المسماة في Excel 2007+، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells C++ نمط الجدول المحوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تطبيق كل من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) والأنماط الحديثة المسماة أو المخصصة للجداول المحورية (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يتم حفظ المصنف به، وليس على التنسيق الذي تم تحميله منه.
{{% /alert %}}

## **المقدمة**
يوفر Aspose.Cells واجهتي برمجة تطبيقات متوازيتين للأنماط في الجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ المصنف المحمّل من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة يتم تطبيق واجهة برمجة التطبيقات الحديثة للأنماط بدلاً من القديمة.
- يحدد `PivotTable.PivotTableStyleType` أحد الأنماط المسماة المضمنة (الثيمات الفاتحة والداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- يحدد `PivotTable.PivotTableStyleName` نمطًا مخصصًا تقوم بتعريفه بنفسك من خلال `Worksheets.TableStyles.AddPivotTableStyle(...)`. تُعد الأنماط المخصصة ضرورية كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.
بالإضافة إلى ذلك، يُعد `PivotTable.FormatAll(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أي من واجهتي برمجة التطبيقات لاسم النمط أعلاه. يكون ذلك مفيدًا عند الحاجة إلى مظهر موحد بصرف النظر عن الثيمة الأساسية.

## **تطبيق تنسيق تلقائي مسبق لملف XLS القديم**
يقبل `PivotTable.AutoFormatType` قيمة من تعداد `Aspose.Cells.Pivot.PivotTableAutoFormatType`. القيم المتاحة هي `Report1` إلى `Report10`، و`Classic`، و`Table1` إلى `Table10`.
يقوم المثال التالي بتحميل مصنف جديد، ويملأه ببيانات العينة Fruit/Year/Amount، ويضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.Report5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}
**لماذا لا توجد حقول أعمدة؟** صُممت التنسيقات التلقائية من السلسلة Report (`Report1` إلى `Report10`، و`Table1` إلى `Table10`) في Excel الكلاسيكي لـ **الجداول المحورية أحادية البعد** التي تحتوي على حقول صفوف وقيم فقط — فهي لا تتضمن تنسيقًا مدمجًا لرؤوس حقول الأعمدة. إذا كان الجدول المحوري يحتاج إلى حقول أعمدة، فاستخدم بدلاً من ذلك الإعدادات المسبقة الحديثة لـ `PivotTableStyleType` من [السيناريو 2](#apply-a-modern-named-preset-pivot-table-style)، والتي صُممت لتخطيط ثنائي الأبعاد يستخدمه Excel الحديث.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // إنشاء مصنف جديد
    Workbook workbook;
    // الحصول على ورقة العمل الأولى
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // تعبئة البيانات المصدرية مع صف الترويسة (فاكهة، سنة، كمية)
    // و9 صفوف بيانات تغطي العنب، التوت الأزرق، الكيوي، الكرز عبر عامي 2020 و2021
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");
    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);
    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);
    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);
    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);
    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);
    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);
    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);
    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);
    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);
    // إضافة جدول محوري في خلية الوجهة E3، باسم "Pivot1"، باستخدام نطاق المصدر A1:C10
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);
    // تعيين الحقول: الفاكهة -> الصفوف، الكمية -> البيانات
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // تطبيق التنسيق التلقائي المحدد مسبقًا للإصدار القديم من XLS "Report5"
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);
    // حفظ المصنف بتنسيق .xls القديم
    workbook.Save(u"output.xls");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تطبيق نمط جدول محوري مسمى حديث مسبق**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);
    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);
    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);
    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);
    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);
    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تعريف وتطبيق نمط جدول محوري مخصص**
لا يمكن تعديل الإعدادات المسبقة المضمنة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب عليك تعريف نمط جدول محوري مخصص. تتكون سير العمل من ثلاث خطوات:
1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` في المصنف عبر `Worksheets.TableStyles.AddPivotTableStyle(string name)`. يُرجع ذلك فهرس النمط الذي تم إنشاؤه حديثًا.
2. قم بتكوين النمط بإضافة عناصر (مثل `WholeTable` أو `GrandTotalRow`) من خلال `TableStyle.TableStyleElements.Add(TableStyleElementType)`، ثم عيّن `Style` لكل عنصر عبر `TableStyleElement.SetElementStyle(Style)`.
3. طبّق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.PivotTableStyleName` إلى اسم النمط. لا تستخدم `PivotTableStyleType` هنا، لأن هذه الخاصية تحدد الإعدادات المسبقة المضمنة.

{{% alert color="primary" %}}
`PivotTableStyleName` و`PivotTableStyleType` ليسا قابلين للتبديل. استخدم `PivotTableStyleType` للإعدادات المسبقة المضمنة، واستخدم `PivotTableStyleName` للأنماط المخصصة التي قمت بتعريفها من خلال `AddPivotTableStyle`. تعيين كليهما غير ضار، ولكن فقط الإعداد المطابق للمصدر المطلوب هو الذي يتم عرضه.
{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة `WholeTable`، و`FirstRow`، و`LastRow`، و`FirstColumn`، و`LastColumn`، و`GrandTotalRow`، و`GrandTotalColumn`، و`PageFieldLabels`، و`PageFieldValues`.
يعرف المثال التالي نمط جدول محوري مخصص بحد أسود رفيع على `WholeTable` وخط أحمر عريض على `GrandTotalRow`، ثم يطبقه عبر `PivotTableStyleName` ويحفظ بصيغة `.xlsx`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // تعبئة بيانات المصدر: صف الرأس + 9 صفوف بيانات (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);
    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);
    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);
    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);
    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);
    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);
    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);
    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);
    // إضافة جدول محوري مصدره A1:C10، مثبت عند E3، باسم "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // الخطوة 1: تسجيل نمط جدول محوري مخصص جديد والتقاط فهرسه
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);
    // الخطوة 2: إضافة عنصر WholeTable وتطبيق حدود سوداء رفيعة على الجوانب الأربعة
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);
    // الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر عريض
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);
    // الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، وهو مخصص للإعدادات المسبقة المدمجة)
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام FormatAll**
يُعد `PivotTable.FormatAll(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات ورؤوس الصفوف والأعمدة والإجماليات. يتم تجاوز أي شيء تم تعيينه مسبقًا من خلال `PivotTableStyleType` أو `PivotTableStyleName`.

{{% alert color="primary" %}}
يتجاوز `FormatAll` كلًا من `PivotTableStyleType` و`PivotTableStyleName`. استخدمه فقط عندما يكون مطلوبًا مظهر موحد ومستقل عن الثيمة عبر الجدول المحوري بأكمله.
{{% /alert %}}

ينشئ المثال التالي `Style` بتعبئة صلبة باللون الأصفر وخط عريض بلون أزرق داكن وحواف سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `FormatAll` ويحفظ بصيغة `.xlsx`.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // صف الرأس
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // صفوف البيانات
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);
    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);
    // إضافة جدول محوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // تعيين حقول الجدول المحوري
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // بناء نمط سيتم فرضه على كل خلية في الجدول المحوري
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    // تطبيق FormatAll
    pivotTable.FormatAll(style);
    // حفظ المصنف
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **أي واجهة برمجة تطبيقات للأنماط يجب أن أستخدم؟**
يعتمد اختيار واجهة برمجة التطبيقات للأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول التالي كمرجع سريع.
| تنسيق الملف المستهدف | واجهة برمجة التطبيقات التي يجب استخدامها | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `PivotTable.AutoFormatType` | قيم من `Aspose.Cells.Pivot.PivotTableAutoFormatType` (مثل `Report1`–`Report10`، و`Classic`، و`Table1`–`Table10`). يتم تجاهلها عند الحفظ بالتنسيقات الحديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مضمّن) | `PivotTable.PivotTableStyleType` | قيم من `Aspose.Cells.PivotTableStyleType` (الثيمات الفاتحة/الداكنة، بما في ذلك الإضافات في Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | استخدم عندما لا تكون الإعدادات المسبقة المضمنة كافية. قم بالتكوين عبر `TableStyleElement.SetElementStyle(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.FormatAll(Style)` | اختصار يتجاوز أي إعداد نمط آخر عبر الجدول المحوري بأكمله. |
عند الشك، احفظ بصيغة `.xlsx` واستخدم `PivotTableStyleType` للثيمات المضمنة، أو `PivotTableStyleName` للثيمات المخصصة.

{{< app/cells/assistant language="cpp" >}}