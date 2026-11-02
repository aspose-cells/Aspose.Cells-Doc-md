---
title: إظهار القيم كما في جدول محوري
linktitle: إظهار القيم كما في جدول محوري
description: عرض قيم حقول بيانات جدول محوري كنسبة مئوية من الإجمالي، أو فرقًا عن عنصر أساسي، أو مجاميع تراكمية، أو ترتيب، وأكثر باستخدام Aspose.Cells for Python via Java.
keywords: Aspose.Cells, جدول محوري, إظهار القيم كـ, صيغة عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /ar/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
عادةً ما يجمع جدول محوري كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. تستبدل ميزة **Show Values As** في Excel كل نتيجة معروضة بحساب ثانوي مشتق من ذلك التجميع — على سبيل المثال، نسبة مئوية من الإجمالي العام، أو مجموع متسلسل، أو فرق عن عنصر أساسي مختار، أو ترتيب — بحيث يمكنك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.  
تشمل الاستخدامات الشائعة تحليل حصة الإجمالي، بما في ذلك النسب المئوية للصف أو العمود أو الإجمالي العام؛ التقارير التراكمية باستخدام مجموع متسلسل في حقل الفترة؛ تحليل التباين مقابل عنصر معيار باستخدام الفرق أو الفرق بالنسبة المئوية من عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.  
في Aspose.Cells for Python via Java، يحدد `PivotFieldDataDisplayFormat` الحساب الثانوي. تُرجع الطريقة للقراءة فقط `PivotField.getShowValuesSetting()` كائنًا من نوع `PivotShowValuesSetting`، وتقوم الطرق القابلة للكتابة `setCalculationType`، `setBaseFieldIndex`، `setBaseItemPositionType`، و `setBaseItemIndex` بتكوين السلوك؛ وتطبق الطريقة المساعدة `PivotField.showValuesAs(...)` نفس الإعدادات الأربعة في استدعاء واحد. استخدم هذه الإعدادات على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.getDataFields()`.

## **أعضاء تعداد PivotFieldDataDisplayFormat**
يحتفظ حقل البيانات بدالته التجميعية، مثل Sum أو Count، بينما يقوم إظهار القيم كـ بتغيير طريقة عرض القيمة المجمعة فقط.  
إلى جانب ضبط خصائص `PivotShowValuesSetting` مباشرة (انظر القسم الأخير)، تُطبق طريقة المساعدة ذات الاستدعاء الواحد نفس التكوين:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `displayFormat` | الحساب الثانوي `PivotFieldDataDisplayFormat` الذي سيتم تطبيقه. | دائمًا. |
| `baseField` | الفهرس الصفري للحقول الأساسية بين الحقول الأساسية لجدول محوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItemPositionType` | كيفية اختيار العنصر الأساسي نسبةً إلى العنصر الحالي: `PivotItemPositionType.Previous`، `.Next` أو `.Custom`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي. | فقط عندما تكون `baseItemPositionType` هي `Custom` (يتم اختيار الفهرس لتحديد العنصر الأساسي بدقة)؛ يتم تجاهله في حالات `Previous` / `Next` وفي جميع التنسيقات غير القائمة على عنصر أساسي — أعِد `0`. |

| نوع الحساب | السلوك | معلمات العنصر الأساسي |
| --- | --- | --- |
| `Normal` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (الافتراضي). | — |
| `DifferenceFrom` | تعرض القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageOf` | تعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageDifferenceFrom` | تعرض القيمة كنسبة الفرق المئوية عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `RunningTotalIn` | تعرض القيمة كمجموع متسلسل للعناصر المتتالية في حقل أساسي. | `baseField` (الحقل الذي يحدد ترتيب تراكم العناصر) |
| `PercentageOfRow` | تعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PercentageOfColumn` | تعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PercentageOfTotal` | تعرض القيمة كنسبة مئوية من الإجمالي العام. | — |
| `Index` | تعرض القيمة باستخدام صيغة الفهرس في Excel ((القيمة * الإجمالي العام) / (إجمالي الصف * إجمالي العمود)). | — |
| `PercentageOfParentRowTotal` | تعرض القيمة كنسبة مئوية من إجمالي الصف الأب (للحقول الصفية المتداخلة). | — |
| `PercentageOfParentColumnTotal` | تعرض القيمة كنسبة مئوية من إجمالي العمود الأب (للحقول العمودية المتداخلة). | — |
| `PercentageOfParentTotal` | تعرض القيمة كنسبة مئوية من إجمالي الأب. | `baseField` (الحقل الأصل المرجعي) |
| `PercentageOfRunningTotalIn` | تعرض القيمة كنسبة مئوية من مجموع متسلسل في حقل أساسي. | `baseField` (حقل التجميع) |
| `RankSmallestToLargest` | ترتيب القيمة من الأصغر (1) إلى الأكبر. | — |
| `RankLargestToSmallest` | ترتيب القيمة من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` يكتب القيم لـ `PivotShowValuesSetting` عبر `setCalculationType`، `setBaseFieldIndex`، `setBaseItemPositionType`، و `setBaseItemIndex` — الطريقة وكائن الإعداد هما طريقتان لتكوين الحالة نفسها، مما يعكس محددات الحقل الأساسي والعنصر الأساسي في مربع حوار Show Values As في Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من الإجمالي**
استدعِ الطريقة `PivotField.showValuesAs` مع `PivotFieldDataDisplayFormat.PercentageOfTotal` لتحويل كل خلية في حقل البيانات، بما في ذلك الإجمالي العام، إلى حصتها من الإجمالي العام. لذلك تُقرأ الأرقام المعروضة كجزء من مجموعة النتائج الكاملة. يقوم هذا التنسيق بقياس كل قيمة مقابل الإجمالي العام فقط، لذا لا يحتاج إلى حقل أساسي أو عنصر أساسي — الوسيطات اللاحقة (`0`، `PivotItemPositionType.Previous`، `0`) هي حاملات لا يستخدمها التنسيق، كما هو موضح في جدول المعاملات أعلاه.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **الحصول على وتكوين PivotField.getShowValuesSetting()**
اقرأ التكوين الحالي عبر `PivotField.getShowValuesSetting()`؛ تُرجع الطريقة للقراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، وتصف خصائصه الأربعة الحساب النشط لـ Show Values As. لتغيير التكوين، استدعِ الطريقة `PivotField.showValuesAs` — فهي تكتب جميع الإعدادات الأربعة في استدعاء واحد، لذلك لا تحتاج إلى تعيين الخصائص واحدةً تلو الأخرى.  
يُظهر كائن `PivotShowValuesSetting` الخصائص الأربعة التي تكتبها `showValuesAs`:
- `getCalculationType()` تُعيد الحساب الثانوي `PivotFieldDataDisplayFormat`، بينما `setCalculationType(...)` يغيّره.
- `getBaseFieldIndex()` و `setBaseFieldIndex(...)` يحددان الفهرس الصفري للحقول الأساسية داخل حقول الجدول المحوري. يُستخدمان في تنسيقات المرجع.
- `getBaseItemPositionType()` و `setBaseItemPositionType(...)` يحددان كيفية وضع العنصر الأساسي نسبةً إلى العنصر الحالي وتقبلان القيم `PivotItemPositionType.Next`، `PivotItemPositionType.Previous`، أو `PivotItemPositionType.Custom`.
- `getBaseItemIndex()` و `setBaseItemIndex(...)` يحددان الفهرس الصفري للعنصر الأساسي ويُستَخدَمان عندما تكون `BaseItemPositionType` هي `Custom`.
بعد استدعاء `showValuesAs`، استدعِ `PivotTable.calculateData()` مرة أخرى حتى يتم إعادة حساب جسم الجدول المحوري وإعادة عرضه بالتكوين المحدث.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في جدول محوري](/cells/ar/python-java/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/python-java/refresh-pivot-table/)
- [تطبيق نمط على جدول محوري](/cells/ar/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}