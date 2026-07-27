---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: حقول الصفوف والأعمدة
description: تعلّم كيفية إضافة حقول أساسية إلى منطقتي الصفوف والأعمدة في الجدول المحوري والتحكم في الإجماليات الفرعية لحقول الجدول المحوري باستخدام PivotField.SetSubtotals في Aspose.Cells for C++.
keywords: Aspose.Cells, C++, جدول محوري, حقل صف, حقل عمود, PivotField, SetSubtotals, PivotFieldSubtotalType, الإجماليات الفرعية
type: docs
weight: 220
url: /ar/cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**

ينقل الأسلوب `PivotTable.AddFieldToArea(PivotFieldType fieldType, intrusive_ptr<Aspose::Cells::Systems::String> fieldName)` حقلًا أساسيًا من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل وسيطة `fieldType` إحدى قيم `PivotFieldType` التالية.

- `Row` — الحقول الموضوعة عموديًا على اليسار
- `Column` — الحقول الموضوعة أفقيًا عبر الأعلى
- `Data` — الحقول التي يتم تجميع قيمها
- `Page` — الحقول المستخدمة كمرشحات للتقرير

بعد إضافة الحقول، يمكنك الوصول إليها من خلال خصائص `PivotTable.RowFields` و `PivotTable.ColumnFields`. تُرجع كل خاصية كائن `PivotFieldCollection`. الحقل عند الفهرس 0 في `RowFields` هو حقل الصف الخارجي، وتمثل الفهارس اللاحقة الحقول المتداخلة بداخله. ينطبق نفس اصطلاح الفهرسة على `ColumnFields`.

يعد ترتيب تداخل الحقول أمرًا مهمًا. فإضافة `Category` إلى منطقة الصفوف أولاً ثم إضافة `Item` ينتج جدولًا محوريًا يكون فيه التجميع الخارجي هو `Category` والتجميع الداخلي هو `Item`. وعكس الترتيب يعكس التسلسل الهرمي.

## **الإجماليات الفرعية لحقول الجدول المحوري**

يتحكم الأسلوب `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` في صفوف الإجمالي الفرعي التي تظهر لحقل محوري. يقوم كل استدعاء بتبديل نوع إجمالي فرعي واحد بشكل مستقل. يعرض تمرير `shown = true` الإجمالي الفرعي، بينما يخفيه `shown = false`. ولأن كل استدعاء يؤثر على نوع واحد فقط، فإن استدعاء الأسلوب عدة مرات بقيم مختلفة لـ `subtotalType` يبني مجموعة فرعية مخصصة من الإجماليات الفرعية.

يحدد التعداد `PivotFieldSubtotalType` أنواع الإجماليات الفرعية المتاحة.

- `Automatic` — يختار Aspose.Cells التحديد الافتراضي (عادةً `Sum` للحقول الرقمية)
- `None` — إلغاء كل صف إجمالي فرعي
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
لا تظهر الإجماليات الفرعية إلا عند وجود حقلين محوريين أو أكثر في منطقة الصفوف (أو في منطقة الأعمدة). فالحقل الواحد لا يوجد ما يمكن حساب إجمالي فرعي له، ولذلك فإن استدعاءات `SetSubtotals` ليس لها أي تأثير مرئي في هذه الحالة. لذلك تضع هذه المقالة حقلين في الصفوف (`Category` خارجي، `Item` داخلي) في كل مثال بحيث يكون الحد الفاصل للإجمالي الفرعي بين كل مجموعة `Category` مرئيًا.
{{% /alert %}}

## **السيناريو 1 — الإجماليات الفرعية التلقائية (الافتراضية)**

عندما لا تستدعي `SetSubtotals` على الإطلاق، يطبق Aspose.Cells التحديد `Automatic` على الحقول الرقمية. يؤكد المثال التالي صراحةً هذا السلوك من خلال استدعاء `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` على حقل الصف الخارجي `Category`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Automatic, true);

    pivotTable.CalculateData();

    workbook.Save(u"output_automatic.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **السيناريو 2 — إلغاء جميع الإجماليات الفرعية (None)**

يزيل استدعاء `SetSubtotals(PivotFieldSubtotalType.None, true)` كل صف إجمالي فرعي من الجدول المحوري، ولا يبقى سوى صفوف الحقول والإجمالي الكلي في الأسفل. يكون ذلك مفيدًا عندما تريد البيانات المجمعة الخام دون أي صفوف ملخصة.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.SetName(u"Data");

    U16String headers[] = { u"Category", u"Item", u"Year", u"Amount" };
    for (int j = 0; j < 4; j++) {
        sheet.GetCells().Get(0, j).PutValue(headers[j]);
    }

    U16String categories[] = { u"Fruit", u"Fruit", u"Fruit", u"Fruit",
                               u"Vegetable", u"Vegetable", u"Vegetable", u"Vegetable" };
    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana",
                          u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[]   = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = {  100,  150,   80,   90,   50,   60,   40,   45 };

    for (int i = 0; i < 8; i++) {
        sheet.GetCells().Get(i + 1, 0).PutValue(categories[i]);
        sheet.GetCells().Get(i + 1, 1).PutValue(items[i]);
        sheet.GetCells().Get(i + 1, 2).PutValue(years[i]);
        sheet.GetCells().Get(i + 1, 3).PutValue(amounts[i]);
    }

    int pivotIndex = sheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::None, true);
    pivotTable.CalculateData();

    wb.Save(u"output_none.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **السيناريو 3 — مجموعة فرعية مخصصة من الإجماليات الفرعية (Sum + Average)**

لست مقيدًا بنوع إجمالي فرعي واحد. كل استدعاء لـ `SetSubtotals` يعمل بشكل مستقل على نوع واحد، لذلك فإن استدعاء الأسلوب مرتين — مرة باستخدام `Sum` ومرة باستخدام `Average` — ينتج مجموعة فرعية مخصصة من صفّي إجمالي فرعي لكل مجموعة `Category`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(u"A1").PutValue(u"Category");
    worksheet.GetCells().Get(u"B1").PutValue(u"Item");
    worksheet.GetCells().Get(u"C1").PutValue(u"Year");
    worksheet.GetCells().Get(u"D1").PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Average, true);

    pivotTable.CalculateData();

    workbook.Save(u"output_custom.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ملخص**

تتشارك السيناريوهات الثلاثة أعلاه في نفس مجموعة البيانات ونفس بنية الجدول المحوري. الاختلاف الوحيد بينها هو استدعاء `SetSubtotals` المطبق على حقل الصف الخارجي `Category`. تذكّر قاعدة الحقلين: الحقل الواحد في منطقة ما لا يوجد ما يمكن حساب إجمالي فرعي بينه وبين غيره، لذلك ضع دائمًا حقلين على الأقل في منطقة الصفوف أو الأعمدة عندما تريد أن يكون لـ `SetSubtotals` تأثير مرئي.

## **مقالات ذات صلة**

- [حقول الصفحات في الجداول المحورية](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for C++](/cells/ar/cpp/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
