---
title: إضافة تنسيق شرطي إلى جدول محوري
linktitle: إضافة تنسيق شرطي إلى جدول محوري
description: إضافة التنسيق الشرطي إلى جدول محوري في Aspose.Cells for C++ - ربط قاعدة بمنطقة البيانات باستخدام ApplyTo ونطاق PivotConditionFormatScopeType، أو تحديد الهدف باستخدام AddCellArea وPivotAreas، ثم إرفاق القواعد والأنماط عبر FormatConditions.AddCondition.
keywords: Aspose.Cells for C++, جدول محوري, التنسيق الشرطي, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /ar/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
الأنماط الموصوفة في الصفحة الأم والصفحة الشقيقة ثابتة - يتم تلوين منطقة `PivotArea` أو `CellArea` مرة واحدة وتحتفظ بنمطها بغض النظر عن القيم. التنسيق الشرطي هو المقابل القائم على القواعد - إبراز كل مبلغ يزيد عن 200، تظليل الخمسين في المئة الوسطى، أو تحديد العناصر ذات الترتيب الأدنى - ويتبع الإبراز القيم كلما تم إعادة حساب أو تحديث جدول محوري.  
في Aspose.Cells، يعيش التنسيق الشرطي لجدول محوري في مجموعة `pivotTable.GetConditionalFormats()` . كل إدخال هو `PivotConditionalFormat` يجيب على سؤالين بشكل مستقل:
- **أين يتم تطبيق القاعدة؟** يتم تعريف منطقة الهدف إما عبر `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` التي تحاكي أداة اختيار النطاق في واجهة مستخدم Excel، أو عبر `AddCellArea(CellArea)` ومجموعة `GetPivotAreas()` التي تحدد المنطقة صراحةً.
- **ما الذي تختبره القاعدة؟** يتم إضافة شرط واحد أو أكثر عبر `GetFormatConditions()` باستخدام `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`، وكل شرط يحمل خاصية `Style` الخاصة به.

{{% alert color="primary" %}}
لا تقم باستدعاء `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` أو `FormatConditionCollection.AddArea(CellArea)` على كائن `GetFormatConditions()` لتنسيق شرطي محوري. هاتان الدالتان موروستان من واجهة برمجة تطبيقات التنسيق الشرطي للورقة العادية ولا تعملان مع الجداول المحورية - لا يتم تحويل منطقة الخلية إلى منطقة محورية، لذا يتم تجاهل الطلب بصمت. عرّف دائمًا المنطقة على `PivotConditionalFormat` نفسه (`ApplyTo`، `AddCellArea` أو `GetPivotAreas()`) وأضف القاعدة باستخدام أحد أشكال `AddCondition`.
{{% /alert %}}

## **تطبيق قاعدة بنطاق (طريقة واجهة Excel)**
الطريقة الأولى تضع القاعدة كما تفعل واجهة مستخدم Excel. تُحدد خلية جدول محوري بإحداثيات ورقة عمل صفرية، ويحدد نطاق `PivotConditionFormatScopeType` إلى أي مدى يجب أن تمتد القاعدة من تلك الخلية:
- `PivotConditionFormatScopeType::Data` - جميع خلايا القيم التي ينتجها جدول محوري، بما في ذلك المجاميع الكلية.
- `PivotConditionFormatScopeType::Field` - خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، باستثناء المجاميع الكلية. يجب أن تكون الخلية خلية حقل مثل تسمية حقل صف؛ تمرير خلية قيمة يثير استثناء.
- `PivotConditionFormatScopeType::Selection` - فقط خلايا القيم عند التقاطع التي تحددها الخلية، عادةً خلية قيمة واحدة.  
المثال أدناه يبني جدولًا محوريًا لمبيعات الفواكه حيث الزاوية العليا اليسرى في E3، يربط تنسيقًا شرطيًا بالخلية F4 (الصف 3، العمود 5) بنطاق `Data`، ويبرز كل مبلغ أكبر من 200 بخط أبيض عريض على خلفية حمراء. مع القيم Apple 220، Banana 330، Cherry 200، والمجموع الكلي 750، تقوم القاعدة بتلوين F4 وF5 وF7 – المنطقة التي تم حلها هي كامل عمود البيانات F4:F7، وتضيء فقط الخلايا التي قيمتها تتجاوز القاعدة.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

ربط نفس القاعدة بتسمية حقل الصف E4 (الصف 3، العمود 4) بنطاق `Field` يحل إلى F4:F6 بدلاً من ذلك – نفسه عمود البيانات بدون صف المجموع الكلي – لأن النطاق الآن يصف حقل `Fruit` بدلاً من كامل مساحة القيم. النطاق `Selection` المرتبط بالخلية F4 يحل إلى F4 فقط.

## **تعريف المنطقة يدويًا**
الطريقة الثانية تتخطى أداة اختيار النطاق وتحدد المنطقة صراحةً على `PivotConditionalFormat`.

### **مستطيل ورقة عمل باستخدام AddCellArea**
`AddCellArea(CellArea)` يسجل المستطيل المعطى كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة عمل صفرية، والمنطقة هي بالضبط المستطيل المقدم – لا توسع إلى عمود البيانات ولا تتضمن منطق المجاميع الكلية. استخدمه عندما تكون الخلايا المثيرة للاهتمام مستطيلًا ثابتًا معروفًا في تخطيط الجدول المحوري الحالي.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **منطقة محورية دلالية باستخدام PivotAreas**
`GetPivotAreas()` توفر نفس نموذج المنطقة الدلالية الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. أنشئ `PivotArea`، اختر حقلًا أو منطقة باستخدام `Select` أو `SelectField`، وأضفه عبر `GetPivotAreas().AddPivotArea(PivotArea)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذا يتبع التنسيق الشرطي الحقل عندما يتم تحديث جدول محوري ويتغير التخطيط. ما يزال الشكل `GetPivotAreas().Add(PivotArea)` يُجمع لكنه مؤرشّف – يفضَّل استخدام `AddPivotArea`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **أين يتم تخزين القواعد وكيفية بقاءها بعد إعادة التحميل**
كل استدعاء `pivotTable.GetConditionalFormats().Add()` يضيف `PivotConditionalFormat` إلى جدول محوري. تُحفظ الشروط وصيغها وأنماطها مع المصنف – إعادة فتح الملف في المثال أدناه تُظهر القاعدة نفسها مع أنواعها، عوامل التشغيل، والصيغة كما هي، وتُظهر `GetCellAreas()` نفس المناطق. تُحذف الإدخالات التي لم تتلقَ شرطًا عندما يتم حفظ المصنف، بنفس الطريقة التي يتخلص بها Excel من تنسيق شرطي لا يحتوي على قاعدة.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/cpp/apply-style-to-pivot-table/)
- [تنسيق جزء من جدول محوري](/cells/ar/cpp/format-part-of-pivot-table/)
- [عرض أو تصفية أعلى 10 في جدول محوري](/cells/ar/cpp/top-10-show-or-filter-in-pivot-table/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}