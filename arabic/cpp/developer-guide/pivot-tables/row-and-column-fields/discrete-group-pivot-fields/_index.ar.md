---
title: التجميع المنفصل لعناصر حقول الجدول المحوري
linktitle: التجميع المنفصل
description: تعرّف على كيفية تجميع عناصر حقول الجدول المحوري في مجموعات مخصصة ذات أسماء، مثل الفواكه والخضروات، باستخدام DiscreteGroupItem وPivotFieldGroupOptions.DiscreteGroupItems في Aspose.Cells for C++.
keywords: Aspose.Cells for C++, جدول محوري, التجميع المنفصل, DiscreteGroupItem, PivotFieldGroupOptions, تجميع عناصر الجدول المحوري, مجموعات مخصصة, PivotField.Group, C++, Excel جدول محوري
type: docs
weight: 90
url: /ar/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
- يجمع التجميع التلقائي العناصر حسب نوع البيانات، مثل تجميع التواريخ في الأشهر والأرباع أو الأرقام في نطاقات. أما التجميع المنفصل فيحل المشكلة المعاكسة، إذ يجمع عناصر محددة وغير مترابطة في مجموعات مخصصة ذات أسماء، على سبيل المثال تجميع المنتجات في الفواكه والخضروات، والمتاجر في المناطق، والحسابات في النطاقات. توفر Aspose.Cells التجميع المنفصل عبر الصنف `DiscreteGroupItem` والخاصية `PivotFieldGroupOptions.DiscreteGroupItems`.
- يمثّل `DiscreteGroupItem` اسم مجموعة مع العناصر التي تنتمي إليها. يمكن تحديد العناصر بإحدى طريقتين: بأسمائها (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) أو بمواضعها المرقّمة من الصفر في بيانات المصدر (`DiscreteGroupItem("fruit", { 0, 3 })`). تنتج كلتا الطريقتين النتيجة نفسها.
- يُطبَّق التجميع المنفصل على حقل في منطقة الصفوف أو الأعمدة في الجدول المحوري عن طريق تمرير الخيارات إلى `PivotField.Group(PivotFieldGroupOptions)`.

## **تجميع عناصر حقول الجدول المحوري حسب أسماء العناصر**
ينشئ المثال التالي قائمة مبيعات صغيرة (الحقول product وdate وamount)، ثم ينشئ منها جدولًا محوريًا يضع `product` في منطقة الصفوف و`date` في منطقة الأعمدة و`amount` في منطقة البيانات، ثم يعرّف مجموعتين مخصصتين حسب أسماء العناصر: fruit (grape, cherry) وvegetable (carrot, potato). تُظهر النتيجة تخطيط صفوف من مستويين، بحيث يكون اسم المجموعة هو المستوى الخارجي وتظهر العناصر الأصلية متداخلة تحته، مما يتيح قراءة الاتجاهات لكل مجموعة مخصصة ولكل عنصر.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

بعد `CalculateData()` تعرض منطقة الصفوف في الجدول المحوري fruit (grape بقيمة 50، cherry بقيمة 80) وvegetable (carrot بقيمة 60، potato بقيمة 70) مع الإجمالي الكلي 260، وتحتفي تسميات الأعمدة بالتواريخ الأربعة (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **تجميع عناصر حقول الجدول المحوري حسب فهارس العناصر**
عندما تكون أسماء العناصر طويلة أو مُعرَّبة، يحدد المُنشئ الثاني لـ `DiscreteGroupItem` العناصر عبر الفهرس. الفهارس هي مواضع العناصر المرقّمة من الصفر وفق ترتيب ظهورها في بيانات المصدر، وليست بالترتيب الأبجدي. في بيانات العينة أعلاه، grape هو العنصر 0، carrot هو العنصر 1، potato هو العنصر 2، وcherry هو العنصر 3، لذا تكون المجموعة fruit هي `{ 0, 3 }` والمجموعة vegetable هي `{ 1, 2 }`. النتيجة مطابقة تمامًا لمثال التجميع حسب الأسماء.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ملاحظة**

{{% alert color="primary" %}}
- العناصر غير المسندة إلى أي مجموعة مخصصة لا تضيع. تظل في الجدول المحوري عند المستوى نفسه الذي تقع فيه المجموعات المخصصة، كلٌّ منها في إدخال مستقل يتكون من عنصر واحد. في المثال أعلاه، يؤدي تعريف مجموعة fruit فقط إلى إبقاء carrot وpotato في منطقة الصفوف كإدخالات مستقلة إلى جانب مجموعة fruit.
- تتحكم الخاصية `PivotFieldGroupOptions.NewPivotField` في تخطيط التجميع المنفصل. قيمتها الافتراضية هي `true`، ما يضيف الحقل المُجمَّع كحقل جديد في المستوى الخارجي بجوار الحقل الأصلي، ويُنتج التخطيط من مستويين المبيَّن أعلاه (مع زيادة `RowFields` إلى 2). اضبطها على `false` لاستبدال الحقل الأصلي. عندئذ، تعرض منطقة الصفوف مستوى واحدًا يحتوي فقط على أسماء المجموعات مع قيمها المجمعة: fruit بقيمة 130 (50 + 80) وvegetable بقيمة 130 (60 + 70).
- يمكن مزج المُنشئين المعتمدين على الاسم والفهرس لـ `DiscreteGroupItem` داخل مجموعة `DiscreteGroupItems` نفسها.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري في الجدول المحوري](/cells/ar/cpp/group-pivot-fields-in-the-pivot-table/)
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/cpp/filter-by-label-or-value-of-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/cpp/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}