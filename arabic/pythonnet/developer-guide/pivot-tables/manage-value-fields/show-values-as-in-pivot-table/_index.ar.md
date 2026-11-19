---
title: عرض القيم حسب في الجدول المحوري
linktitle: عرض القيم حسب في الجدول المحوري
description: اعرض قيم حقول بيانات الجدول المحوري كنسب مئوية من الإجمالي، أو كفروق من عنصر أساسي، أو كإجماليات تراكمية، أو كمراتب، وغيرها، باستخدام Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, جدول محوري, عرض القيم حسب, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /ar/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
يجمع الجدول المحوري عادةً كل حقل بيانات باستخدام دالة تجميع مثل `SUM` أو `COUNT`. وتستبدل ميزة **عرض القيم حسب** في Excel كل نتيجة معروضة بحساب ثانوي مشتق من نتيجة التجميع؛ على سبيل المثال، كنسبة مئوية من الإجمالي الكلي، أو إجمالي تراكمي، أو فارق عن عنصر أساسي محدد، أو رتبة؛ ما يتيح لك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.
تشمل الاستخدامات النموذجية تحليل حصة كل عنصر من الإجمالي، بما في ذلك النسب المئوية للصف أو العمود أو الإجمالي الكلي؛ إعداد تقارير تراكمية باستخدام إجمالي تراكمي في حقل فترة؛ تحليل التباين مقابل عنصر مرجعي باستخدام الفارق عن عنصر أساسي أو الفارق بالنسبة المئوية عن عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.
في Aspose.Cells for Python via .NET، يحدد تعداد `PivotShowValuesAsType` الحساب الثانوي. وتعيد الخاصية `PivotField.show_values_setting`، وهي للقراءة فقط، كائن `PivotShowValuesSetting`، وتضبط الخصائص القابلة للكتابة `show_values_as` و`base_field_index` و`base_item_index` سلوك العرض؛ كما تطبق طريقة الاختصار `PivotField.show_values_as(...)` الإعدادات نفسها في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو حقل قيمة تم الحصول عليه من `PivotTable.data_fields`.

## **أعضاء تعداد `PivotShowValuesAsType`**
يحتفظ حقل البيانات بدالة التجميع الخاصة به، مثل `SUM` أو `COUNT`، بينما يغير **عرض القيم حسب** طريقة عرض القيمة المجمعة فحسب.
بالإضافة إلى كتابة خصائص `PivotShowValuesSetting` مباشرة (راجع القسم الأخير)، تتيح طريقة اختصار في استدعاء واحد تطبيق الإعداد نفسه. وهي متاحة في نموذجين، أحدهما يحدد حقل الأساس والعنصر الأساسي بواسطة الفهرس، والآخر يحددهما بالاسم:

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `show_values_as_type` | الحساب الثانوي من نوع `PivotShowValuesAsType` المطلوب تطبيقه. | دائمًا. |
| `base_field` | فهرس قائم على الصفر لحقل الأساس ضمن حقول الأساس في الجدول المحوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي)، أو — في النموذج الذي يعتمد على الأسماء — اسم حقل الأساس. | التنسيقات الثمانية القائمة على الأساس أدناه (`DIFFERENCE_FROM` و`PERCENTAGE_OF` و`PERCENTAGE_DIFFERENCE_FROM` و`RUNNING_TOTAL_IN` و`PERCENTAGE_OF_PARENT_TOTAL` و`PERCENTAGE_OF_RUNNING_TOTAL_IN` و`RANK_SMALLEST_TO_LARGEST` و`RANK_LARGEST_TO_SMALLEST`)؛ ومرر `0` (أو `None` في النموذج الذي يعتمد على الأسماء) لكل تنسيق آخر. |
| `base_item` | فهرس قائم على الصفر للعنصر الأساسي، مع قيمتَي إشارة: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) لتحديد العنصر السابق، و`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) لتحديد العنصر التالي. ويأخذ النموذج الذي يعتمد على الأسماء تسمية العنصر الأساسي بدلاً من الفهرس، ويستخدم `None` عندما لا يحتاج التنسيق المحدد إلى عنصر أساسي. | تستخدم تنسيقات العنصر الأساسي الثلاثة (`DIFFERENCE_FROM` و`PERCENTAGE_OF` و`PERCENTAGE_DIFFERENCE_FROM`) العنصر الأساسي، بينما تتجاهل التنسيقات الخمسة النسبية إلى الحقل (`RUNNING_TOTAL_IN` و`PERCENTAGE_OF_PARENT_TOTAL` و`PERCENTAGE_OF_RUNNING_TOTAL_IN` وتنسيقَي الترتيب) هذا العنصر؛ ومرر `0` أو `None`. |

| نوع الحساب | السلوك | معاملات العنصر الأساسي |
| --- | --- | --- |
| `NORMAL` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (الافتراضي). | — |
| `DIFFERENCE_FROM` | يعرض القيمة كفارق عن قيمة عنصر أساسي في حقل الأساس. | `base_field` + `base_item` (فهرس أو تسمية، أو قيمة إشارة للعنصر السابق/التالي) |
| `PERCENTAGE_OF` | يعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل الأساس. | `base_field` + `base_item` (فهرس أو تسمية، أو قيمة إشارة للعنصر السابق/التالي) |
| `PERCENTAGE_DIFFERENCE_FROM` | يعرض القيمة كالفارق بالنسبة المئوية عن قيمة عنصر أساسي في حقل الأساس. | `base_field` + `base_item` (فهرس أو تسمية، أو قيمة إشارة للعنصر السابق/التالي) |
| `RUNNING_TOTAL_IN` | يعرض القيمة كإجمالي تراكمي للعناصر المتتالية في حقل الأساس. | `base_field` (الحقل الذي تحدد عناصره مسار التراكم) |
| `PERCENTAGE_OF_ROW` | يعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PERCENTAGE_OF_COLUMN` | يعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PERCENTAGE_OF_TOTAL` | يعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `INDEX` | يعرض القيمة باستخدام صيغة الفهرس في Excel `((value * grand total) / (row total * column total))`. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي الصف الأب (لحقول الصفوف المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي العمود الأب (لحقول الأعمدة المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي حقله الأب. | `base_field` (الحقل الأب الذي يُستخدم إجماليه كمرجع) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | يعرض القيمة كنسبة مئوية من إجمالي تراكمي في حقل أساس. | `base_field` (حقل التراكم) |
| `RANK_SMALLEST_TO_LARGEST` | يرتب القيمة من الأصغر (1) إلى الأكبر. | `base_field` (الحقل الذي تحدد عناصره نطاق الترتيب) |
| `RANK_LARGEST_TO_SMALLEST` | يرتب القيمة من الأكبر (1) إلى الأصغر. | `base_field` (الحقل الذي تحدد عناصره نطاق الترتيب) |

{{% alert color="primary" %}}
يكتب `show_values_as(...)` خصائص `PivotShowValuesSetting` (`show_values_as` و`base_field_index` و`base_item_index`)؛ وتكوّن الطريقة وكائن الخاصية وسيلتين لضبط الحالة نفسها، تمامًا مثل أدوات اختيار حقل الأساس والعنصر الأساسي في مربع حوار **عرض القيم حسب** في Excel.
{{% /alert %}}

## **عرض القيم كنسبة مئوية من الإجمالي**
استدعِ أسلوب `PivotField.show_values_as` مع `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` لتحويل كل خلية في حقل البيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. لذلك تُعرض الأرقام بوصفها نسبًا من مجموعة النتائج الكاملة. يقيس هذا التنسيق كل قيمة مقارنةً بالإجمالي الكلي فقط، لذا لا يحتاج إلى حقل أساس أو عنصر أساسي؛ أما المعاملان الأخيران (`0`، `0`) فهما قيمتان بديلتان يتجاهلهما التنسيق، كما يوضح جدول المعاملات أعلاه.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
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
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **الحصول على `PivotField.show_values_setting` وتهيئته**
اقرأ الإعداد الحالي من خلال `PivotField.show_values_setting`: تعيد الخاصية للقراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، وتصف خصائصه حساب **عرض القيم حسب** النشط. لتغيير الإعداد، استدعِ أسلوب `PivotField.show_values_as`؛ فهو يكتب جميع الإعدادات في استدعاء واحد، ولا تحتاج إلى تعيين الخصائص واحدة تلو الأخرى.
يكشف كائن `PivotShowValuesSetting` الحالة التي يكتبها `show_values_as`:
- يحدد `show_values_as` الحساب الثانوي من نوع `PivotShowValuesAsType`.
- يحدد `base_field_index` الفهرس القائم على الصفر لحقل الأساس ضمن حقول الجدول المحوري. ويُستخدم في التنسيقات القائمة على الأساس.
- يحدد `base_item_index` العنصر الأساسي: فهرسًا قائمًا على الصفر لعنصر محوري محدد، أو إحدى قيمتَي الإشارة: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) للعنصر السابق، أو `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) للعنصر التالي. ويُستخدم في التنسيقات القائمة على العنصر الأساسي.
- `base_field_name` و`base_item_caption` يعرضان اسم حقل الأساس وتسمية العنصر الأساسي بعد تحديدهما، وهما للقراءة فقط؛ على سبيل المثال، بعد اختيار قيمة الإشارة الخاصة بالعنصر السابق، تكون قراءة `base_item_caption` هي `(previous)`.
بعد استدعاء `show_values_as`، استدعِ `PivotTable.calculate_data()` مرة أخرى لإعادة حساب بيانات الجدول المحوري وإعادة عرضها بالإعداد المحدث.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/python-net/manage-value-fields/)
- [تحديث الجدول المحوري](/cells/ar/python-net/refresh-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}