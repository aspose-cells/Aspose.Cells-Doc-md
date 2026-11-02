---
title: إظهار القيم كما في جدول محوري
linktitle: إظهار القيم كما في جدول محوري
description: عرض قيم حقول البيانات في جدول محوري كنسبة مئوية من الإجمالي، أو كفرق عن عنصر أساسي، أو كقيم تراكمية، أو كترتيب، والمزيد باستخدام Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, جدول محوري, إظهار القيم كـ, تنسيق عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /ar/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
عادةً ما يجمع جدول محوري كل حقل بيانات باستخدام دالة تجميع مثل `SUM` أو `COUNT`. تُستبدل النتيجة المعروضة في ميزة **Show Values As** في Excel بحساب ثانوي مشتق من ذلك التجميع — على سبيل المثال، نسبة مئوية من الإجمالي الكلي، أو قيمة تراكمية، أو فرق عن عنصر أساسي مختار، أو ترتيب — بحيث يمكنك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.  
تشمل الاستخدامات الشائعة تحليل حصة الإجمالي، بما في ذلك النسب المئوية للصف، أو العمود، أو الإجمالي الكلي؛ تقارير تراكمية باستخدام قيمة تراكمية في حقل فترة؛ تحليل الفروقات مقابل عنصر معيار باستخدام الفرق عن أو الفرق المئوي عن عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.  
في Aspose.Cells for Python via .NET، يحدد `PivotFieldDataDisplayFormat` الحساب الثانوي. تُعيد الخاصية للقراءة فقط `PivotField.show_values_setting` كائنًا من النوع `PivotShowValuesSetting`، حيث تُكوّن الخصائص القابلة للكتابة `calculation_type` و `base_field_index` و `base_item_position_type` و `base_item_index` السلوك؛ وتطبيق الطريقة المريحة `PivotField.show_values_as(...)` يطبق الإعدادات الأربعة نفسها في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.data_fields`.

## **أعضاء تعداد PivotFieldDataDisplayFormat**
يحتفظ حقل البيانات بدالة التجميع الخاصة به، مثل `SUM` أو `COUNT`، بينما يقوم Show Values As بتحويل طريقة عرض القيمة المجمعة فقط.  
بالإضافة إلى كتابة خصائص `PivotShowValuesSetting` مباشرة (انظر القسم الأخير)، تطبق طريقة مريحة استدعاء واحد نفس التكوين:

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| معامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `display_format` | حساب `PivotFieldDataDisplayFormat` الثانوي الذي سيُطبق. | دائمًا. |
| `base_field` | الفهرس الصفري للحقول الأساسية بين الحقول الأساسية لجدول محوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `base_item_position_type` | كيفية موضع العنصر الأساسي بالنسبة للعنصر الحالي: `PivotItemPositionType.PREVIOUS`، `.NEXT`، أو `.CUSTOM`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `base_item` | الفهرس الصفري للعنصر الأساسي. | فقط عندما تكون `base_item_position_type` هي `CUSTOM` (يختار فهرس العنصر الأساسي العنصر المحدد)؛ يُهمل للخيارات `PREVIOUS` / `NEXT` ومن قبل جميع التنسيقات غير القائمة على العنصر الأساسي — مرر `0`. |

| نوع الحساب | السلوك | معامل العنصر الأساسي |
| --- | --- | --- |
| `NORMAL` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (الإعداد الافتراضي). | — |
| `DIFFERENCE_FROM` | يعرض القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` فقط مع `CUSTOM`) |
| `PERCENTAGE_OF` | يعرض القيمة كنسبة مئوية لقيمة عنصر أساسي في حقل أساسي. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` فقط مع `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | يعرض القيمة كفرق نسبي (نسبة مئوية) عن قيمة عنصر أساسي في حقل أساسي. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` فقط مع `CUSTOM`) |
| `RUNNING_TOTAL_IN` | يعرض القيمة كقيمة تراكمية للعناصر المتتابعة في حقل أساسي. | `base_field` (الحقل الذي يحدد ترتيب التجميع) |
| `PERCENTAGE_OF_ROW` | يعرض القيمة كنسبة مئوية لإجمالي الصف. | — |
| `PERCENTAGE_OF_COLUMN` | يعرض القيمة كنسبة مئوية لإجمالي العمود. | — |
| `PERCENTAGE_OF_TOTAL` | يعرض القيمة كنسبة مئوية للإجمالي الكلي. | — |
| `INDEX` | يعرض القيمة باستخدام صيغة الفهرس في Excel ((القيمة * الإجمالي الكلي) / (إجمالي الصف * إجمالي العمود)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | يعرض القيمة كنسبة مئوية لإجمالي الصف الأصل (للحقول الصفية المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | يعرض القيمة كنسبة مئوية لإجمالي العمود الأصل (للحقول العمودية المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | يعرض القيمة كنسبة مئوية لإجمالي الأصل. | `baseField` (الحقل الأصل المرجعي) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | يعرض القيمة كنسبة مئوية لقيمة تراكمية في حقل أساسي. | `base_field` (حقل التجميع) |
| `RANK_SMALLEST_TO_LARGEST` | يرتب القيمة من الأصغر (1) إلى الأكبر. | — |
| `RANK_LARGEST_TO_SMALLEST` | يرتب القيمة من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`show_values_as(...)` يكتب الخصائص لكائن `PivotShowValuesSetting` (`calculation_type` و `base_field_index` و `base_item_position_type` و `base_item_index`) — الطريقة وكائن الخاصية هما طريقتان لتكوين الحالة نفسها، معكوسين لأدوات اختيار الحقل الأساسي والعنصر الأساسي في مربع حوار Show Values As في Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.show_values_as` مع `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` لتحويل كل خلية حقل بيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. وبالتالي تُظهر الأرقام كحصص من مجموعة النتائج الكاملة. يقيس هذا التنسيق كل قيمة مقابل الإجمالي الكلي فقط، لذلك لا يحتاج إلى حقل أساسي أو عنصر أساسي — المعاملات اللاحقة (`0`، `PivotItemPositionType.PREVIOUS`، `0`) هي نائيات يتجاهلها التنسيق، كما هو موضح في جدول المعاملات أعلاه.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **الحصول على وتكوين PivotField.show_values_setting**
اقرأ التكوين الحالي عبر `PivotField.show_values_setting`: تُعيد الخاصية للقراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، حيث تصف خصائصه الأربعة عملية Show Values As النشطة. لتغيير التكوين، استدعِ طريقة `PivotField.show_values_as` — فهي تكتب جميع الإعدادات الأربعة في استدعاء واحد، لذا لا تحتاج أبدًا إلى تعيين الخصائص واحدةً تلو الأخرى.  
كائن `PivotShowValuesSetting` يكشف عن الخصائص الأربعة التي تكتبها `show_values_as`:
- `calculation_type` يختار الحساب الثانوي `PivotFieldDataDisplayFormat`.
- `base_field_index` يحدد الفهرس الصفري للحقول الأساسية داخل الحقول المحورية. يُستخدم في تنسيقات المرجع.
- `base_item_position_type` يحدد كيفية موضع العنصر الأساسي بالنسبة للعنصر الحالي ويقبل `PivotItemPositionType.NEXT` أو `PivotItemPositionType.PREVIOUS` أو `PivotItemPositionType.CUSTOM`.
- `base_item_index` يحدد الفهرس الصفري للعنصر الأساسي ويُستخدم عندما تكون `base_item_position_type` هي `CUSTOM`.
بعد استدعاء `show_values_as`, استدعِ `PivotTable.calculate_data()` مرة أخرى حتى يُعاد حساب جسم الجدول المحوري وإعادة رسمه بالإعدادات المحدثة.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في جدول محوري](/cells/ar/python-net/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/python-net/refresh-pivot-table/)
- [تطبيق نمط على جدول محوري](/cells/ar/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}