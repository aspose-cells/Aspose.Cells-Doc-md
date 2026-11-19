---
title: عرض القيم كـ في الجدول المحوري
linktitle: عرض القيم كـ في الجدول المحوري
description: اعرض قيم حقول البيانات في الجدول المحوري كنسبة مئوية من الإجمالي الكلي، أو كفرق من عنصر أساسي، أو كإجماليات تراكمية، أو كمراتب، والمزيد باستخدام Aspose.Cells for Python via Java.
keywords: Aspose.Cells, جدول محوري, عرض القيم كـ, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /ar/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
يجمع الجدول المحوري عادةً بيانات كل حقل باستخدام دالة تجميع مثل `SUM` أو `COUNT`. تستبدل ميزة **عرض القيم كـ** في Excel كل نتيجة معروضة بحساب ثانوي مشتق من دالة التجميع — على سبيل المثال، نسبة مئوية من الإجمالي الكلي، أو إجمالي تراكمي، أو فرق من عنصر أساسي مُختار، أو رتبة — لإجراء تحليل مقارن دون صيغ مساعدة أو أعمدة محسوبة.
تشمل الاستخدامات المعتادة تحليل حصة كل عنصر من الإجمالي، بما في ذلك النسب المئوية للصف أو العمود أو الإجمالي الكلي؛ والتقارير التراكمية باستخدام إجمالي تراكمي في حقل فترة؛ وتحليل التباين مقابل عنصر مرجعي باستخدام الفرق من عنصر أساسي أو نسبة الفرق من عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.
في Aspose.Cells for Python via Java، يحدد التعداد `PivotShowValuesAsType` الحساب الثانوي. تُعيد الطريقة للقراءة فقط `PivotField.getShowValuesSetting()` كائن `PivotShowValuesSetting`، وتضبط طرائق `setShowValuesAs(...)` و`setBaseFieldIndex(...)` و`setBaseItemIndex(...)` السلوك؛ وتطبق الطريقة المختصرة `PivotField.showValuesAs(...)` الإعدادات نفسها في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو حقل قيمة تم استرجاعه من `PivotTable.getDataFields()`.

## **أعضاء تعداد PivotShowValuesAsType**
يحتفظ حقل البيانات بدالة التجميع الخاصة به، مثل `SUM` أو `COUNT`، بينما لا تغيّر ميزة **عرض القيم كـ** إلا طريقة عرض القيمة المجمّعة.
إلى جانب استخدام دوال التعيين في `PivotShowValuesSetting` مباشرةً (راجع القسم الأخير)، تتيح طريقة مختصرة تطبيق الإعداد نفسه في استدعاء واحد. وهي متاحة في صيغتين — واحدة تحدد الحقل الأساسي والعنصر الأساسي بواسطة الفهرس، والأخرى بواسطة الاسم:

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `show_values_as_type` | الحساب الثانوي `PivotShowValuesAsType` المراد تطبيقه. | دائمًا. |
| `base_field` | فهرس يبدأ العدّ من صفر للحقل الأساسي ضمن الحقول الأساسية للجدول المحوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي)، أو — في الصيغة المعتمدة على الاسم — اسم الحقل الأساسي. | الصيغ الثماني المعتمدة على الحقل الأساسي الموضحة أدناه (`DIFFERENCE_FROM`، `PERCENTAGE_OF`، `PERCENTAGE_DIFFERENCE_FROM`، `RUNNING_TOTAL_IN`، `PERCENTAGE_OF_PARENT_TOTAL`، `PERCENTAGE_OF_RUNNING_TOTAL_IN`، `RANK_SMALLEST_TO_LARGEST`، `RANK_LARGEST_TO_SMALLEST`)؛ ومرّر `0` (أو `None` في الصيغة المعتمدة على الاسم) لكل صيغة أخرى. |
| `base_item` | فهرس يبدأ العدّ من صفر للعنصر الأساسي، مع قيمتَي حارس: تختار `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) العنصر السابق، وتختار `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) العنصر التالي. وتأخذ الصيغة المعتمدة على الاسم عنوان العنصر الأساسي بدلًا من الفهرس، وتأخذ `None` عندما لا تحتاج الصيغة المحددة إلى عنصر أساسي. | لا تقيّم الصيغ الثلاث المعتمدة على العنصر الأساسي (`DIFFERENCE_FROM`، `PERCENTAGE_OF`، `PERCENTAGE_DIFFERENCE_FROM`) العنصرَ الأساسي؛ بينما تتجاهله الصيغ الخمس المعتمدة على الحقل (`RUNNING_TOTAL_IN`، `PERCENTAGE_OF_PARENT_TOTAL`، `PERCENTAGE_OF_RUNNING_TOTAL_IN`، وصيغتا الترتيب) — ومرّر `0` أو `None`. |

| نوع الحساب | السلوك | معاملات العنصر الأساسي |
| --- | --- | --- |
| `NORMAL` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمّعة كما هي (الافتراضي). | — |
| `DIFFERENCE_FROM` | يعرض القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `base_field` + `base_item` (فهرس أو عنوان، أو قيمة حارس العنصر السابق أو التالي) |
| `PERCENTAGE_OF` | يعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `base_field` + `base_item` (فهرس أو عنوان، أو قيمة حارس العنصر السابق أو التالي) |
| `PERCENTAGE_DIFFERENCE_FROM` | يعرض القيمة كنسبة مئوية للفرق عن قيمة عنصر أساسي في حقل أساسي. | `base_field` + `base_item` (فهرس أو عنوان، أو قيمة حارس العنصر السابق أو التالي) |
| `RUNNING_TOTAL_IN` | يعرض القيمة كإجمالي تراكمي للعناصر المتتابعة في حقل أساسي. | `base_field` (الحقل الذي يحدد ترتيب عناصره التراكم) |
| `PERCENTAGE_OF_ROW` | يعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PERCENTAGE_OF_COLUMN` | يعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PERCENTAGE_OF_TOTAL` | يعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `INDEX` | يعرض القيمة باستخدام صيغة الفهرس في Excel `((value * grand total) / (row total * column total))`. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي صف الأصل (لحقول الصفوف المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي عمود الأصل (لحقول الأعمدة المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي الأصل. | `base_field` (الحقل الأصل الذي يكون إجماليه هو المرجع) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | يعرض القيمة كنسبة مئوية من إجمالي تراكمي في حقل أساسي. | `base_field` (حقل التراكم) |
| `RANK_SMALLEST_TO_LARGEST` | يحدد رتبة القيمة من الأصغر (1) إلى الأكبر. | `base_field` (الحقل الذي تحدد عناصره نطاق الترتيب) |
| `RANK_LARGEST_TO_SMALLEST` | يحدد رتبة القيمة من الأكبر (1) إلى الأصغر. | `base_field` (الحقل الذي تحدد عناصره نطاق الترتيب) |

{{% alert color="primary" %}}
تكتب `showValuesAs(...)` قيم `PivotShowValuesSetting` عبر `setShowValuesAs` و`setBaseFieldIndex` و`setBaseItemIndex` — وتُعد الطريقة وكائن الإعداد طريقتين لتهيئة الحالة نفسها، بما يعكس أداتَي اختيار الحقل الأساسي والعنصر الأساسي في مربع حوار **عرض القيم كـ** في Excel.
{{% /alert %}}

## **عرض القيم كنسبة مئوية من الإجمالي**
استدعِ الطريقة `PivotField.showValuesAs` مع `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` لتحويل كل خلية من حقول البيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. لذلك تظهر الأرقام المعروضة كنسب من مجموعة النتائج الكاملة. تقيس هذه الصيغة كل قيمة مقابل الإجمالي الكلي فقط، لذا لا تحتاج إلى حقل أساسي أو عنصر أساسي — وتُعد الوسائط الأخيرة (`0`, `0`) قيمًا نائبة تتجاهلها الصيغة، كما يوضح جدول المعاملات أعلاه.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **الحصول على PivotField.getShowValuesSetting() وتهيئته**
اقرأ الإعداد الحالي عبر `PivotField.getShowValuesSetting()`: تُعيد هذه الطريقة للقراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، وتصف خصائصه حساب **عرض القيم كـ** النشط. لتغيير الإعداد، استدعِ الطريقة `PivotField.showValuesAs` — فهي تكتب جميع الإعدادات في استدعاء واحد، لذا لا تحتاج إلى تعيين الخصائص واحدة تلو الأخرى.
يعرض كائن `PivotShowValuesSetting` الحالة التي تكتبها `showValuesAs`:
- تعيد `getShowValuesAs()` الحساب الثانوي `PivotShowValuesAsType`، بينما تغيّره `setShowValuesAs(...)`.
- تحدد `getBaseFieldIndex()` و`setBaseFieldIndex(...)` فهرسًا يبدأ العدّ من صفر للحقل الأساسي ضمن حقول الجدول المحوري. وتستخدمه الصيغ المعتمدة على الحقل الأساسي.
- تحدد `getBaseItemIndex()` و`setBaseItemIndex(...)` العنصر الأساسي: فهرسًا يبدأ العدّ من صفر لعنصر محدد في الجدول المحوري، أو إحدى قيمتَي الحارس — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) للعنصر السابق، و`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) للعنصر التالي. وتستخدمه الصيغ المعتمدة على العنصر الأساسي.
- توفّر `getBaseFieldName()` و`getBaseItemCaption()` معلومات للقراءة فقط عن اسم الحقل الأساسي وعنوان العنصر الأساسي بعد تحديدهما؛ على سبيل المثال، بعد اختيار قيمة حارس العنصر السابق، تعيد `getBaseItemCaption()` القيمة `(previous)`.
بعد استدعاء `showValuesAs`، استدعِ `PivotTable.calculateData()` مرة أخرى حتى يُعاد حساب جسم الجدول المحوري وإعادة عرضه بالإعداد المحدّث.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/python-java/manage-value-fields/)
- [تحديث الجدول المحوري](/cells/ar/python-java/refresh-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}