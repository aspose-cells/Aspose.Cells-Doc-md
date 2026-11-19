---
title: عرض القيم كـ في الجدول المحوري
linktitle: عرض القيم كـ في الجدول المحوري
description: اعرض قيم حقول بيانات الجدول المحوري كنسبة مئوية من الإجمالي، أو كفرق من عنصر أساسي، أو مجاميع تراكمية، أو مراتب، والمزيد باستخدام Aspose.Cells for Java.
keywords: Aspose.Cells, جدول محوري, عرض القيم كـ, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /ar/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يجمع الجدول المحوري عادةً كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. وتستبدل ميزة **عرض القيم كـ** في Excel كل نتيجة معروضة بحساب ثانٍ مشتق من دالة التجميع، مثل نسبة مئوية من الإجمالي الكلي، أو مجموع تراكمي، أو فرق من عنصر أساسي محدد، أو رتبة. ويتيح ذلك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.
تشمل الاستخدامات الشائعة تحليل حصة الإجمالي، بما في ذلك احتساب النسب المئوية لصف أو عمود أو الإجمالي الكلي؛ وإعداد التقارير التراكمية باستخدام مجموع تراكمي في حقل فترة؛ وتحليل التباين مقابل عنصر مرجعي باستخدام «الفرق من عنصر أساسي» أو «نسبة الفرق من عنصر أساسي»؛ وتحديد رتب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.
في Aspose.Cells for Java، يحدد التعداد `PivotShowValuesAsType` الحساب الثانوي. وتعيد دالة الوصول للقراءة فقط `PivotField.getShowValuesSetting()` كائن `PivotShowValuesSetting`، وتضبط الطرق `setShowValuesAs(...)` و`setBaseFieldIndex(...)` و`setBaseItemIndex(...)` سلوكه. وتتيح الطريقة الملائمة `PivotField.showValuesAs(...)` تطبيق الإعدادات نفسها في نداء واحد. وتُطبَّق هذه الإعدادات على حقل بيانات أو حقل قيمة تم الحصول عليه من `PivotTable.getDataFields()`.

## **أعضاء تعداد `PivotShowValuesAsType`**
يحتفظ حقل البيانات بوظيفة التجميع الخاصة به، مثل `Sum` أو `Count`، بينما يقتصر «عرض القيم كـ» على تغيير طريقة عرض القيمة المجمَّعة.
بالإضافة إلى استخدام دوال الإعداد في `PivotShowValuesSetting` مباشرةً (راجع القسم الأخير)، تتوفر طريقة ملائمة بنداء واحد تطبق التكوين نفسه. ولها حِملتان: تحدد الحِمل الأولى الحقل الأساسي والعنصر الأساسي بواسطة الفهرس، وتحدد الحِمل الثانيةهما بواسطة الاسم:

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `showValuesAsType` | نوع الحساب الثانوي `PivotShowValuesAsType` المطلوب تطبيقه. | دائمًا. |
| `baseField` | فهرس الحقل الأساسي بدءًا من الصفر ضمن الحقول الأساسية للجدول المحوري (مثل فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي)، أو، في الحِمل الذي يستخدم `String`، اسم الحقل الأساسي. | تنسيقات الأساس الثمانية أدناه (`DIFFERENCE_FROM`، `PERCENTAGE_OF`، `PERCENTAGE_DIFFERENCE_FROM`، `RUNNING_TOTAL_IN`، `PERCENTAGE_OF_PARENT_TOTAL`، `PERCENTAGE_OF_RUNNING_TOTAL_IN`، `RANK_SMALLEST_TO_LARGEST`، `RANK_LARGEST_TO_SMALLEST`)؛ مرّر `0` (أو `null` في الحِمل الذي يستخدم `String`) لكل تنسيق آخر. |
| `baseItem` | فهرس العنصر الأساسي بدءًا من الصفر، مع قيمتَي حد خاصتين: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) لاختيار العنصر السابق و`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) لاختيار العنصر التالي. ويأخذ الحِمل الذي يستخدم `String` عنوان العنصر الأساسي بدلًا من ذلك، ويأخذ `null` عندما لا يتطلب التنسيق المحدد عنصرًا أساسيًا. | تستخدم التنسيقات الثلاثة المرتبطة بالعنصر الأساسي (`DIFFERENCE_FROM`، `PERCENTAGE_OF`، `PERCENTAGE_DIFFERENCE_FROM`) العنصر الأساسي؛ أما تنسيقات الحقل الخمسة (`RUNNING_TOTAL_IN`، `PERCENTAGE_OF_PARENT_TOTAL`، `PERCENTAGE_OF_RUNNING_TOTAL_IN`، وكلا تنسيقي الترتيب) فلا تستخدمه — مرّر `0` أو `null`. |

| نوع الحساب | السلوك | المعاملات المرتبطة بالأساس |
| --- | --- | --- |
| `NORMAL` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمَّعة كما هي (الإعداد الافتراضي). | — |
| `DIFFERENCE_FROM` | يعرض القيمة كفرق من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو عنوان، أو قيمة حد العنصر السابق/التالي) |
| `PERCENTAGE_OF` | يعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو عنوان، أو قيمة حد العنصر السابق/التالي) |
| `PERCENTAGE_DIFFERENCE_FROM` | يعرض قيمة الفرق بين القيمة الحالية وقيمة عنصر أساسي في حقل أساسي كنسبة مئوية. | `baseField` + `baseItem` (فهرس أو عنوان، أو قيمة حد العنصر السابق/التالي) |
| `RUNNING_TOTAL_IN` | يعرض القيمة بوصفها مجموعًا تراكميًا للعناصر المتعاقبة في حقل أساسي. | `baseField` (الحقل الذي يحدد ترتيب عناصره التراكم) |
| `PERCENTAGE_OF_ROW` | يعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PERCENTAGE_OF_COLUMN` | يعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PERCENTAGE_OF_TOTAL` | يعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `INDEX` | يعرض القيمة باستخدام صيغة الفهرس في Excel ((القيمة * الإجمالي الكلي) / (إجمالي الصف * إجمالي العمود)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي صف الأصل (لحقول الصف المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي عمود الأصل (لحقول العمود المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي الحقل الأصل. | `baseField` (الحقل الأصل الذي يكون إجماليه هو المرجع) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | يعرض القيمة كنسبة مئوية من المجموع التراكمي في حقل أساسي. | `baseField` (حقل التراكم) |
| `RANK_SMALLEST_TO_LARGEST` | يحدد رتبة القيمة من الأصغر (1) إلى الأكبر. | `baseField` (الحقل الذي تحدد عناصره نطاق الترتيب) |
| `RANK_LARGEST_TO_SMALLEST` | يحدد رتبة القيمة من الأكبر (1) إلى الأصغر. | `baseField` (الحقل الذي تحدد عناصره نطاق الترتيب) |

{{% alert color="primary" %}}
`showValuesAs(...)` يضبط حالة `PivotShowValuesSetting` بدقة من خلال `setShowValuesAs(...)` و`setBaseFieldIndex(...)` و`setBaseItemIndex(...)` — أي أن الطريقة وكائن الإعداد يوفران طريقتين لضبط الحالة نفسها، على نحو مماثل لوجود منتقيَي الحقل الأساسي والعنصر الأساسي في مربع الحوار «عرض القيم كـ» في Excel.
{{% /alert %}}

## **عرض القيم كنسبة مئوية من الإجمالي**
استدعِ الطريقة `PivotField.showValuesAs(...)` مع `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` لتحويل كل خلية في حقل البيانات، بما في ذلك خلية الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. وبذلك تمثل الأرقام المعروضة نسبًا من مجموعة النتائج الكاملة. ويقيس هذا التنسيق كل قيمة مقارنةً بالإجمالي الكلي فقط، ولذلك لا يحتاج إلى حقل أساسي أو عنصر أساسي. أما وسيطتا الاستدعاء الأخيرتان (`0`، `0`) فهما قيمتان نائبتان يتجاهلهما التنسيق، كما يوضح جدول المعاملات أعلاه.

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **الحصول على `PivotField.getShowValuesSetting` وتهيئة الإعدادات**
اقرأ التكوين الحالي من خلال `PivotField.getShowValuesSetting()`: إذ تعيد دالة الوصول للقراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، وتصف خصائصه حساب «عرض القيم كـ» النشط. ولتغيير الإعدادات، استدعِ الطريقة `PivotField.showValuesAs(...)`؛ فهي تعيّن جميع الإعدادات في نداء واحد، فلا تحتاج إلى تعيين الخصائص واحدًا تلو الأخرى.
يوفر كائن `PivotShowValuesSetting` الحالة التي تعيّنها `showValuesAs(...)`:
- `getShowValuesAs()` / `setShowValuesAs(...)`: تحدد نوع الحساب الثانوي `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)`: تحدد فهرس الحقل الأساسي بدءًا من الصفر ضمن حقول الجدول المحوري. وتُستخدم هذه الخاصية في التنسيقات المرتبطة بالأساس.
- `getBaseItemIndex()` / `setBaseItemIndex(...)`: تحدد العنصر الأساسي: فهرسًا بدءًا من الصفر لعنصر محدد في الجدول المحوري، أو إحدى قيمتَي الحد الخاصتين — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) للعنصر السابق، و`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) للعنصر التالي. وتُستخدم هذه الخاصية في التنسيقات المرتبطة بالعنصر الأساسي.
- `getBaseFieldName()` و`getBaseItemCaption()`: تتيحان قراءة اسم الحقل الأساسي الذي تم حله وعنوان العنصر الأساسي؛ على سبيل المثال، بعد اختيار قيمة حد العنصر السابق، تعيد `getBaseItemCaption()` القيمة `(previous)`.
بعد استدعاء `showValuesAs(...)`، استدعِ `PivotTable.calculateData()` مرة أخرى لإعادة حساب منطقة الجدول المحوري وإعادة عرضها بالإعدادات المحدَّثة.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/java/manage-value-fields/)
- [تحديث الجدول المحوري](/cells/ar/java/refresh-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}