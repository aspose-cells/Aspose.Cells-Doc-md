---
title: إظهار القيم كـ في جدول محوري في Aspose.Cells for C++
linktitle: إظهار القيم كـ في جدول محوري في Aspose.Cells for C++
description: اعرض قيم حقل بيانات جدول محوري كنسبة مئوية من الإجمالي، أو كفرق عن عنصر أساسي، أو مجموع مستمر، أو ترتيب، والمزيد باستخدام Aspose.Cells for C++.
keywords: Aspose.Cells, C++, جدول محوري, إظهار القيم كـ, تنسيق عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ar/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
عادةً ما يقوم جدول محوري بتجميع كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. تُستبدل النتيجة المعروضة في ميزة **Show Values As** في Excel بحساب ثانوي مشتق من هذا التجميع — على سبيل المثال، نسبة مئوية من الإجمالي الكلي، أو مجموع مستمر، أو فرق عن عنصر أساسي مختار، أو رتبة — مما يتيح لك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.  
تشمل الاستخدامات الشائعة تحليل حصة الإجمالي، بما في ذلك النسب المئوية للصف أو العمود أو الإجمالي الكلي؛ وإعداد تقارير تراكمية باستخدام مجموع مستمر في حقل الفترة؛ وتحليل الفرق مقابل عنصر معيار باستخدام الفرق من أو الفرق المئوي من عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو العكس.  
في Aspose.Cells for C++، يحدد `PivotFieldDataDisplayFormat` الحساب الثانوي. تُعيد الدالة `PivotField.GetShowValuesSetting()` كائنًا من نوع `PivotShowValuesSetting`، الذي تُكوّن طرقه `SetCalculationType`، `SetBaseFieldIndex`، `SetBaseItemPositionType`، و `SetBaseItemIndex` السلوك؛ طريقة التسهيل `PivotField.ShowValuesAs(...)` تُطبق نفس الإعدادات الأربعة في استدعاء واحد. يُطبّق هذا الإعداد على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.GetDataFields()`.

## **قائمة أعضاء تعداد PivotFieldDataDisplayFormat**
يحتفظ حقل البيانات بدالة التجميع الخاصة به، مثل Sum أو Count، بينما يقوم Show Values As بتحويل طريقة عرض القيمة المجمعة فقط.  
بالإضافة إلى كتابة قيم `PivotShowValuesSetting` مباشرةً (انظر القسم الأخير)، تُطبق طريقة التسهيل ذات الاستدعاء الواحد نفس التكوين:

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `displayFormat` | الحساب الثانوي `PivotFieldDataDisplayFormat` المراد تطبيقه. | دائمًا. |
| `baseField` | الفهرس الصفري للحقل الأساسي بين الحقول الأساسية لجدول محوري (مثال: فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItemPositionType` | طريقة اختيار العنصر الأساسي بالنسبة للعنصر الحالي: `PivotItemPositionType::Previous`، `::Next`، أو `::Custom`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي. | فقط عندما يكون `baseItemPositionType` هو `Custom` (يتم اختيار الفهرس لتحديد العنصر الأساسي بدقة); يتم تجاهلها عندما يكون `Previous` / `Next` وفي جميع تنسيقات غير العنصر الأساسي — مرّر `0`. |

| نوع الحساب | السلوك | معلمات العنصر الأساسي |
| --- | --- | --- |
| `Normal` | لا حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (افتراضي). | — |
| `DifferenceFrom` | يعرض القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageOf` | يعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageDifferenceFrom` | يعرض القيمة كفرق مئوي عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `RunningTotalIn` | يعرض القيمة كمجموع مستمر للعناصر المتتالية لحقل أساسي. | `baseField` (الحقل الذي يحدد ترتيب العنصر لتجميع القيم) |
| `PercentageOfRow` | يعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PercentageOfColumn` | يعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PercentageOfTotal` | يعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `Index` | يعرض القيمة باستخدام صيغة الفهرس في Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | يعرض القيمة كنسبة مئوية من إجمالي الصف الأب (للحقول المتداخلة). | — |
| `PercentageOfParentColumnTotal` | يعرض القيمة كنسبة مئوية من إجمالي العمود الأب (للحقول المتداخلة). | — |
| `PercentageOfParentTotal` | يعرض القيمة كنسبة مئوية من مجموع الأب. | `baseField` (الحقل الأصل المرجعي) |
| `PercentageOfRunningTotalIn` | يعرض القيمة كنسبة مئوية من مجموع مستمر في حقل أساسي. | `baseField` (حقل التجميع) |
| `RankSmallestToLargest` | يرقم القيمة من الأصغر (1) إلى الأكبر. | — |
| `RankLargestToSmallest` | يرقم القيمة من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` تكتب القيم لكائن `PivotShowValuesSetting` (`CalculationType`، `BaseFieldIndex`، `BaseItemPositionType`، `BaseItemIndex`) — الطريقة وكائن الإعدادات يمثلان طريقتين لتكوين الحالة نفسها، مما يعكس أدوات اختيار الحقل الأساسي والعنصر الأساسي في مربع حوار Show Values As في Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.ShowValuesAs` مع `PivotFieldDataDisplayFormat::PercentageOfTotal` لتحويل كل خلية في حقل البيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. لذلك تُقرأ الأرقام المعروضة على أنها نسب من مجموعة النتائج الكاملة. هذا التنسيق يقيس كل قيمة مقارنة بالإجمالي الكلي فقط، لذا لا تحتاج إلى حقل أساسي أو عنصر أساسي — المعاملات الأخيرة (`0`، `PivotItemPositionType::Previous`، `0`) هي مجرد حجز موضع يتجاهله التنسيق، كما يُوضح جدول المعاملات أعلاه.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **قراءة وتكوين PivotField.ShowValuesSetting**
اقرأ التكوين الحالي عبر `PivotField.GetShowValuesSetting()`؛ تُعيد الدالة كائن `PivotShowValuesSetting` الخاص بالحقل، الذي تصف طرقه الأربعة للوصول القيم النشطة لـ Show Values As. لتغيير التكوين، استدعِ طريقة `PivotField.ShowValuesAs` — فهي تُكتب جميع الإعدادات الأربعة في استدعاء واحد، لذا لا تحتاج إلى تعيين القيم واحدةً تلو الأخرى.  
يُظهر كائن `PivotShowValuesSetting` القيم الأربعة التي تُكتبها `ShowValuesAs`:
- `GetCalculationType()` / `SetCalculationType()` يحددان الحساب الثانوي `PivotFieldDataDisplayFormat`.  
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` يحددان الفهرس الصفري للحقل الأساسي داخل الحقول المحورية. يُستخدم في تنسيقات المرجع.  
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` يحددان موضع العنصر الأساسي بالنسبة للعنصر الحالي ويقبلان `PivotItemPositionType::Next`، `PivotItemPositionType::Previous`، أو `PivotItemPositionType::Custom`.  
- `GetBaseItemIndex()` / `SetBaseItemIndex()` يحددان الفهرس الصفري للعنصر الأساسي ويُستخدمان عندما يكون نوع الموضع هو `Custom`.  
بعد استدعاء `ShowValuesAs`، استدعِ `PivotTable.CalculateData()` مرة أخرى حتى يُعاد حساب جسم الجدول المحوري وإعادة عرضه وفق التكوين المحدّث.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في جدول محوري](/cells/ar/cpp/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/cpp/refresh-pivot-table/)
- [تطبيق نمط على جدول محوري](/cells/ar/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}