---
title: إضافة حقول الصفوف والأعمدة في الجدول المحوري في Aspose.Cells for C++
linktitle: إضافة حقول الصفوف والأعمدة في الجدول المحوري في Aspose.Cells for C++
description: تعلم كيفية إضافة الحقول الأساسية إلى مناطق الصفوف والأعمدة في الجدول المحوري والتحكم في الإجماليات الفرعية للحقول المحورية باستخدام PivotField.SetSubtotals في Aspose.Cells for C++
keywords: Aspose.Cells, C++, جدول محوري, حقل صف, حقل عمود, PivotField, SetSubtotals, PivotFieldSubtotalType, الإجماليات الفرعية
type: docs
weight: 220
url: /ar/cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**
تنقل الطريقة `PivotTable.AddFieldToArea(PivotFieldType fieldType, U16String fieldName)` حقلاً أساسيًا من البيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل الوسيطة `fieldType` إحدى قيم `PivotFieldType` التالية.
- `Row` — الحقول الموضوعة عموديًا على اليسار
- `Column` — الحقول الموضوعة أفقيًا عبر الأعلى
- `Data` — الحقول التي يتم تجميع قيمها
- `Page` — الحقول المستخدمة كمرشحات للتقرير
يهم ترتيب تداخل الحقول. تؤدي إضافة `Category` إلى منطقة الصفوف أولاً ثم `Item` إلى إنتاج جدول محوري يكون فيه التجميع الخارجي `Category` والتجميع الداخلي `Item`. يؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **الإجماليات الفرعية للحقول المحورية**
تتحكم الطريقة `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` في صفوف الإجماليات الفرعية التي تظهر للحقل المحوري. يقوم كل استدعاء بتبديل نوع إجمالي فرعي واحد بشكل مستقل. يعرض تمرير `shown = true` الإجمالي الفرعي، بينما يخفيه `shown = false`. نظرًا لأن كل استدعاء يؤثر على نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم `subtotalType` مختلفة ينشئ مجموعة فرعية مخصصة من الإجماليات الفرعية.
يحدد التعداد `PivotFieldSubtotalType` أنواع الإجماليات الفرعية المتاحة.
- `Automatic` — يختار Aspose.Cells التحديد الافتراضي (عادةً `Sum` للحقول الرقمية)
- `None` — إلغاء كل صف من الإجماليات الفرعية
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
لا تظهر الإجماليات الفرعية إلا عند وجود حقلين محوريين أو أكثر في منطقة الصفوف (أو في منطقة الأعمدة). الحقل الواحد لا يحتوي على ما يمكن حساب إجمالي فرعي له بشكل ذي معنى، لذلك لا يكون لاستدعاءات `SetSubtotals` أي تأثير مرئي في هذه الحالة. لذلك يضع هذا المقال حقلين للصفوف (`Category` خارجي، `Item` داخلي) في كل مثال بحيث يكون حد الإجمالي الفرعي بين كل مجموعة `Category` مرئيًا.
{{% /alert %}}

## **السيناريو 1 — الإجماليات الفرعية التلقائية (الافتراضية)**
عندما لا تستدعي `SetSubtotals` على الإطلاق، يطبق Aspose.Cells التحديد `Automatic` على الحقول الرقمية. يؤكد المثال التالي صراحةً هذا السلوك عن طريق استدعاء `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` على حقل الصف الخارجي `Category`.

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
يؤدي استدعاء `SetSubtotals(PivotFieldSubtotalType.None, true)` إلى إزالة كل صف من الإجماليات الفرعية من الجدول المحوري، تاركًا فقط صفوف الحقول والإجمالي الكلي في الأسفل. يكون هذا مفيدًا عندما تريد البيانات المجمعة الأولية بدون أي صفوف ملخصة.

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

## **السيناريو 3 — مجموعة الإجماليات الفرعية المخصصة (Sum + Average)**
لست مقيدًا بنوع إجمالي فرعي واحد. يعمل كل استدعاء لـ `SetSubtotals` بشكل مستقل على نوع واحد، لذلك فإن استدعاء الطريقة مرتين — مرة بـ `Sum` ومرة بـ `Average` — ينتج مجموعة فرعية مخصصة من صفين للإجماليات الفرعية لكل مجموعة `Category`.

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

## **مقالات ذات صلة**
- [حقول الصفحات في الجداول المحورية](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for C++](/cells/ar/cpp/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}