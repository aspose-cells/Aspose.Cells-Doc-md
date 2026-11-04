---
title: تنسيق جزء من جدول محوري
linktitle: تنسيق جزء من جدول محوري
description: تنسيق جزء من جدول محوري في Aspose.Cells for C++ عن طريق تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea عبر PivotTable.Format، مع تخزين التنسيقات في PivotTable.GetPivotFormats والحفاظ عليها عند تحديث جدول المحوري.
keywords: Aspose.Cells, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /ar/cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
`PivotTable.FormatAll` يطبق نمطًا واحدًا على جدول المحوري بأكمله وتم تغطيته في الصفحة الأم. لا يميز بين التسميات والقيم والإجماليات أو مناطق معينة من التقرير.  
في الواقع، عادةً ما يحتاج جزء فقط من جدول المحوري إلى إبراز. تشمل الأهداف الشائعة التسميات التابعة لحقل صف واحد، خلايا القيم التي ينتجها حقل معين، الصف الإجمالي العام، أو مستطيل عشوائي مثل الصفين الأولين للعنصر.  
تطبيق نمط مباشرةً على خلايا ورقة العمل الخاصة بجدول المحوري لا يعادل ذلك. تخزن Excel تنسيق جدول المحوري كمناطق `PivotArea` دلالية بدلاً من سجلات نمط الخلية العادية. يظل تنسيق منطقة المحوري مرتبطًا بمنطقة مثل تسميات الحقل أو قيم البيانات، ويُعاد حلّه عندما يُعاد حساب جدول المحوري أو يُحدث أو يُوسّع. أما النمط المكتوب مباشرةً في خلية، فيخصّ تلك الخلية ولا يتعقّبها نموذج المحوري.  
توفر Aspose.Cells عائلة التحميل الزائدة `PivotTable.Format` الكاملة بحيث تتوفر كلا النوعين من التنسيق:
- `Format(const PivotArea&, const Style&)` يربط نمطًا بمنطقة دلالية تُبنى باستخدام `PivotArea.Select` أو `PivotArea.SelectField`.
- `Format(const CellArea&, const Style&)` يربط نمطًا بمستطيل في ورقة العمل داخل جدول المحوري.
- `Format(int32_t row, int32_t column, const Style&)` يستهدف خلية واحدة.
- `FormatAll(const Style&)` ينسق جدول المحوري بأكمله.

## **تنسيق منطقة محورية**
تُعدّ سير عمل المنطقة الدلالية النهج الموصى به عندما يجب أن يتبع التمييز حقلًا أو منطقة من التقرير.
1. أنشئ كائنًا من النوع `PivotArea` باستخدام `PivotArea pivotArea(pivotTable);`. يصف هذا الكائن منطقة دلالية تخص جدول المحوري المحدد.
2. اختر حقلًا بناءً على موضعه الصفري على محور معين باستخدام `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType::DataAndLabel` يختار كلًا من التسميات والبيانات الخاصة بالحقل.
   - `PivotTableSelectionType::LabelOnly` يختار تسميات الحقل فقط.
   - `PivotTableSelectionType::DataOnly` يختار خلايا بيانات الحقل فقط.
3. اختر حقلًا حسب اسمه باستخدام `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)`. عند اختيار حقل صف بالاسم، تُحل المنطقة إلى خلايا القيم التي تنتجها عناصر ذلك الحقل.
4. أنشئ كائنًا من النوع `Style` عبر `Workbook.CreateStyle()`، واضبط الخط، ولون المقدّمة، ونمط الخلفية الصلبة، ثم مرّر النمط إلى `PivotTable.Format(pivotArea, style)`.
5. كل استدعاء للتحميل الزائدة `PivotArea` يُضيف إدخالًا واحدًا من نوع `PivotTableFormat` إلى `PivotTable.GetPivotFormats()`.
6. تُرسم التنسيقات المرتبطة بالحقل عندما تُحسب بيانات المحوري. لذلك، استدعِ `PivotTable.CalculateData()` بعد تطبيق التنسيقات لكي تصبح الأنماط مرئية.
المثال التالي يُنشئ جدول محوري صغير لمبيعات الفواكه، يُنسق تسميات صف `Fruit` باستخدام `PivotArea.Select` و `PivotTableSelectionType::LabelOnly`، يُنسق خلايا القيم الناتجة عن نفس حقل الصف باستخدام `PivotArea.SelectField`، ثم يُعيد حساب جدول المحوري بحيث تُظهر كلا النمطين.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تنسيق منطقة خلية في جدول المحوري**
استخدم `PivotTable.Format(const CellArea&, const Style&)` عندما تكون المنطقة المستهدفة مستطيلًا عاديًا في ورقة العمل وليس منطقة محورية دلالية.  
يُوصف `CellArea` بالحقول العامة `StartRow`، `StartColumn`، `EndRow`، و `EndColumn`. القيم إحداثيات ورقة عمل صفرية الأساس، وتحدد إحداثيات النهاية الصف والعمود الأخيرين المشمولين بالمستطيل، لذا يغطي المجال الخلايا من الموضع الابتدائي إلى الموضع النهائي شاملًا.  
على عكس تنسيق مُرتبط بالحقل، يُطبّق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء إضافي لـ `CalculateData()` لظهور النمط.  
قد يحتوي مستطيل `CellArea` على خلايا تسميات وخلايا قيم معًا. يصف القسم التالي كيف تمثّل Aspose.Cells وExcel ذلك المستطيل داخليًا.  
المثال التالي يُنسّق المستطيل `E4:F5` في جدول المحوري بنمط مائل أزرق فاتح ويحفظ المصنف دون أي عملية إعادة حساب إضافية.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **كيفية تطابق مناطق المحوري ومناطق الخلية**
تخزن Excel تنسيق جدول المحوري كسجلات `pivotArea` بدلاً من سجلات نمط خلايا ورقة العمل العادية. يستخدم Aspose.Cells نفس النموذج، لذا تُترجم طلبات التنسيق إلى مناطق محورية عند تسجيلها.  
العلاقة بين `CellArea` التي يحددها المستخدم ومناطق المحوري المخزنة داخليًا متعددة إلى متعدد في كلا الاتجاهين.
- قد ينتج `CellArea` واحد عدة مناطق محورية. إذا كان المستطيل يشمل كلًا من خلايا التسميات والقيم، يُقسم إلى قواعد تسميات وبيانات منفصلة، لأن نموذج المحوري يعالج تنسيق التسميات وتنسيق البيانات بشكل مستقل.
- قد تُحل منطقة محورية واحدة إلى عدة مثيلات `CellArea` منفصلة. يمكن لمنطقة دلالية مثل صف الإجمالي العام، أو حقل لا تكون عناصره متصلة، أن يغطي مستطيلات متعددة. لهذا السبب تُعيد `PivotArea.GetCellAreas()` مجموعة `Vector<CellArea>` بدلاً من مستطيل واحد.
كل عملية تنسيق تُجرى عبر `PivotTable.Format` تُسجل في `PivotTable.GetPivotFormats()`. كل إدخال من نوع `PivotTableFormat` يُظهر الـ `PivotArea` المرتبط والـ `Style` المُطبق عليها. التحميل الزائد للـ `PivotArea` يضيف إدخالًا واحدًا بالضبط لكل استدعاء، بينما يمكن أن يضيف `CellArea` يحتوي على مناطق دلالية مختلفة عدة إدخالات.  
لتمييز المناطق المخزنة، يُظهر كل `PivotArea` أعلام `GetOnlyLabel()` و `GetOnlyData()`. المثال أدناه يُنسق مستطيلًا واحدًا يغطي كلًا من التسميات والقيم، يفحص `PivotTable.GetPivotFormats()`، ويطبع إحداثيات `CellArea` التي تُحلّ كل منطقة محورية مخزنة إليها.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
نظرًا لأن التنسيقات تُخزن كمناطق محورية بدلاً من نمط خلايا عادي، فإنها تبقى محفوظة بعد إعادة الحساب والتحديث. عندما يُحدَّث جدول المحوري عبر `PivotTable.RefreshData`، أو يُعاد حسابه بـ `CalculateData`، أو يُحفظ ويُعاد تحميله، تُعيد كل منطقة محورية مخزنة حلّها إلى الموضع الحالي لمنطقتها ويُعاد تطبيق النمط.
{{% /alert %}}

استخدم `PivotArea` مبنيًا بـ `Select` أو `SelectField` عندما يجب أن يظل التمييز مرتبطًا بحقل أو بمنطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عندما يكون تنسيق مستطيل ثابت في تخطيط جدول المحوري الحالي كافيًا. التحميل الزائد `Format(int32_t row, int32_t column, const Style&)` يستهدف خلية واحدة. استخدم `FormatAll`، المذكور في الصفحة الأم، عندما يرغب المستخدم في إعادة تنسيق جدول المحوري بأكمله دفعة واحدة.

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/cpp/apply-style-to-pivot-table/)
- [إضافة حقول صف وعمود إلى جدول محوري](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في جدول محوري](/cells/ar/cpp/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}