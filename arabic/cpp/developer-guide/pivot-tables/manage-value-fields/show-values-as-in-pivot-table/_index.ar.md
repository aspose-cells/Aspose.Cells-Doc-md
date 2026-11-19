---
title: عرض القيم كـ في الجدول المحوري في Aspose.Cells for C++
linktitle: عرض القيم كـ في الجدول المحوري في Aspose.Cells for C++
description: اعرض قيم حقول بيانات الجدول المحوري كنسبة مئوية من الإجمالي، أو الفرق عن عنصر أساسي، أو إجماليات تراكمية، أو رتب، والمزيد باستخدام Aspose.Cells for C++.
keywords: Aspose.Cells, C++, جدول محوري, عرض القيم كـ, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ar/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يجمع الجدول المحوري عادةً بيانات كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. تستبدل ميزة **عرض القيم كـ** في Excel كل نتيجة معروضة بحساب ثانوي مشتق من هذا التجميع، مثل نسبة من الإجمالي الكلي، أو إجمالي تراكمي، أو الفرق عن عنصر أساسي مختار، أو رتبة؛ ما يتيح لك إجراء تحليل مقارن من دون صيغ مساعدة أو أعمدة محسوبة.
تشمل الاستخدامات النموذجية تحليل حصة كل عنصر من الإجمالي، بما في ذلك النسب المئوية لصف أو عمود أو الإجمالي الكلي؛ وإعداد التقارير التراكمية باستخدام إجمالي تراكمي في حقل فترة؛ وتحليل التباين مقابل عنصر معياري باستخدام الفرق عن العنصر الأساسي أو نسبة الفرق عنه؛ وترتيب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.
في Aspose.Cells for C++، يحدد تعداد `PivotShowValuesAsType` الحساب الثانوي. تعيد طريقة الوصول `PivotField.GetShowValuesSetting()` كائن `PivotShowValuesSetting`، وتهيئ طرائق `SetShowValuesAs` و`SetBaseFieldIndex` و`SetBaseItemIndex` السلوك؛ وتطبق الطريقة المختصرة `PivotField.ShowValuesAs(...)` الإعدادات نفسها في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو حقل قيم تم استرجاعه من `PivotTable.GetDataFields()`.

## **أعضاء تعداد `PivotShowValuesAsType`**
يحتفظ حقل البيانات بدالة التجميع، مثل `Sum` أو `Count`، بينما يغيّر **عرض القيم كـ** طريقة عرض القيمة المجمّعة فقط.
إلى جانب كتابة قيم `PivotShowValuesSetting` مباشرةً (راجع القسم الأخير)، تتوفر طريقة مختصرة تطبق الإعداد نفسه في استدعاء واحد. وتأتي في صورتين: إحداهما تحدد الحقل الأساسي والعنصر الأساسي بالفهرس، والأخرى تحددهما بالاسم:

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `showValuesAsType` | حساب `PivotShowValuesAsType` الثانوي المطلوب تطبيقه. | دائمًا. |
| `baseField` | فهرس يبدأ من الصفر للحقل الأساسي ضمن الحقول الأساسية للجدول المحوري، مثل فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي، أو، في صيغة الاسم، اسم الحقل الأساسي. | التنسيقات الثمانية المرتبطة بالأساس أدناه (`DifferenceFrom` و`PercentageOf` و`PercentageDifferenceFrom` و`RunningTotalIn` و`PercentageOfParentTotal` و`PercentageOfRunningTotalIn` و`RankSmallestToLargest` و`RankLargestToSmallest`)؛ مرّر `0`، أو `U16String` فارغة في صيغة الاسم، لكل تنسيق آخر. |
| `baseItem` | فهرس يبدأ من الصفر للعنصر الأساسي، مع قيمتَي إشارة خاصتين: تحدد `-1` العنصر السابق وتحدد `-2` العنصر التالي. لا يحدد C++ API أي ثوابت مسماة لقيمتَي الإشارة، لذا مرّر القيمتين حرفيتين. وتأخذ صيغة الاسم تسمية العنصر الأساسي بدلاً من ذلك، وتستخدم `U16String` فارغة عندما لا يحتاج التنسيق المحدد إلى عنصر أساسي. | تستخدم التنسيقات الثلاثة المرتبطة بالعنصر الأساسي (`DifferenceFrom` و`PercentageOf` و`PercentageDifferenceFrom`) العنصر الأساسي في الحساب، بينما تتجاهله التنسيقات الخمسة المرتبطة بالحقل (`RunningTotalIn` و`PercentageOfParentTotal` و`PercentageOfRunningTotalIn` وكلا تنسيقي الترتيب)؛ مرّر `0` أو `U16String` فارغة. |

| نوع الحساب | السلوك | معاملات العنصر الأساسي |
| --- | --- | --- |
| `Normal` | لا يُطبَّق أي حساب ثانوي؛ تُعرض القيمة المجمّعة كما هي، وهو السلوك الافتراضي. | — |
| `DifferenceFrom` | يعرض القيمة بوصفها الفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem`، أي فهرس أو تسمية أو قيمة إشارة للعنصر السابق/التالي |
| `PercentageOf` | يعرض القيمة بوصفها نسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem`، أي فهرس أو تسمية أو قيمة إشارة للعنصر السابق/التالي |
| `PercentageDifferenceFrom` | يعرض القيمة بوصفها النسبة المئوية للفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem`، أي فهرس أو تسمية أو قيمة إشارة للعنصر السابق/التالي |
| `RunningTotalIn` | يعرض القيمة بوصفها إجماليًا تراكميًا للعناصر المتتابعة في حقل أساسي. | `baseField`، أي الحقل الذي يحدد ترتيب عناصره عملية التراكم |
| `PercentageOfRow` | يعرض القيمة بوصفها نسبة مئوية من إجمالي الصف. | — |
| `PercentageOfColumn` | يعرض القيمة بوصفها نسبة مئوية من إجمالي العمود. | — |
| `PercentageOfTotal` | يعرض القيمة بوصفها نسبة مئوية من الإجمالي الكلي. | — |
| `Index` | يعرض القيمة باستخدام صيغة الفهرس في Excel، أي `(value * grand total) / (row total * column total)`. | — |
| `PercentageOfParentRowTotal` | يعرض القيمة بوصفها نسبة مئوية من إجمالي صف الأصل (للحقول المتداخلة في الصفوف). | — |
| `PercentageOfParentColumnTotal` | يعرض القيمة بوصفها نسبة مئوية من إجمالي عمود الأصل (للحقول المتداخلة في الأعمدة). | — |
| `PercentageOfParentTotal` | يعرض القيمة بوصفها نسبة مئوية من إجمالي الحقل الأصل. | `baseField`، أي الحقل الأصل الذي يُستخدم إجماليه كمرجع |
| `PercentageOfRunningTotalIn` | يعرض القيمة بوصفها نسبة مئوية من الإجمالي التراكمي في حقل أساسي. | `baseField`، أي حقل التراكم |
| `RankSmallestToLargest` | يحدد رتبة القيمة من الأصغر (1) إلى الأكبر. | `baseField`، أي الحقل الذي تحدد عناصره نطاق الترتيب |
| `RankLargestToSmallest` | يحدد رتبة القيمة من الأكبر (1) إلى الأصغر. | `baseField`، أي الحقل الذي تحدد عناصره نطاق الترتيب |

{{% alert color="primary" %}}
`ShowValuesAs(...)` يكتب قيم `PivotShowValuesSetting` (`ShowValuesAs` و`BaseFieldIndex` و`BaseItemIndex`)، وتُعد الطريقة وكائن الإعداد طريقتين لتهيئة الحالة نفسها، بما يعكس أداتَي تحديد الحقل الأساسي والعنصر الأساسي في مربع حوار **عرض القيم كـ** في Excel.
{{% /alert %}}

## **عرض القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.ShowValuesAs` مع `PivotShowValuesAsType::PercentageOfTotal` لتحويل كل خلية في حقل البيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. لذلك تُعرض الأرقام بوصفها نِسبًا من مجموعة النتائج الكاملة. يقيس هذا التنسيق كل قيمة مقارنةً بالإجمالي الكلي فقط، لذا لا يحتاج إلى حقل أساسي أو عنصر أساسي؛ وتُعد الوسائط الأخيرة (`0`، `0`) قيمًا نائبة يتجاهلها التنسيق، كما يوضح جدول المعاملات أعلاه.

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
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الحصول على `PivotField.ShowValuesSetting` وتهيئته**
اقرأ الإعداد الحالي من خلال `PivotField.GetShowValuesSetting()`: تعيد طريقة الوصول كائن `PivotShowValuesSetting` الخاص بالحقل، وتصف طرائق القراءة حساب **عرض القيم كـ** النشط. لتغيير الإعداد، استدعِ طريقة `PivotField.ShowValuesAs`؛ فهي تكتب جميع الإعدادات في استدعاء واحد، لذا لا تحتاج إلى تعيين القيم واحدًا تلو الآخر.
يعرض كائن `PivotShowValuesSetting` حالة الإعداد التي تكتبها `ShowValuesAs`:
- `GetShowValuesAs()` / `SetShowValuesAs()` يحددان حساب `PivotShowValuesAsType` الثانوي.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` يحددان الفهرس الذي يبدأ من الصفر للحقل الأساسي ضمن حقول الجدول المحوري. تُستخدم هذه القيمة في التنسيقات المرتبطة بالأساس.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` يحددان العنصر الأساسي، سواء كان فهرسًا يبدأ من الصفر لعنصر محوري محدد أو إحدى قيمتَي الإشارة، `-1` للعنصر السابق و`-2` للعنصر التالي. لا يحدد C++ API أي ثوابت مسماة لقيمتَي الإشارة. تُستخدم هذه القيمة في التنسيقات المرتبطة بالعنصر الأساسي.
- `GetBaseFieldName()` و`GetBaseItemCaption()` يمثلان عرضين للقراءة فقط يعرضان اسم الحقل الأساسي وتسمية العنصر الأساسي كما حُدِّدتا؛ على سبيل المثال، بعد تحديد قيمة إشارة العنصر السابق، تُرجع `GetBaseItemCaption()` القيمة `(previous)`.
بعد استدعاء `ShowValuesAs`، استدعِ `PivotTable.CalculateData()` مرة أخرى، بحيث يُعاد حساب جسم الجدول المحوري وإعادة عرضه بالإعداد المحدّث.

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
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **المقالات ذات الصلة**
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/cpp/manage-value-fields/)
- [تحديث الجدول المحوري](/cells/ar/cpp/refresh-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}