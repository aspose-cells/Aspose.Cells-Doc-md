---
title: إظهار القيم كـ في جدول محوري
linktitle: إظهار القيم كـ في جدول محوري
description: اعرض قيم حقول بيانات جدول محوري كنسبة من الإجمالي، أو فرقًا عن عنصر أساسي، أو مجموعًا متراكمًا، أو مرتبة، وأكثر باستخدام Aspose.Cells for Java.
keywords: Aspose.Cells, جدول محوري, إظهار القيم كـ, تنسيق عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /ar/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
عادةً ما يقوم **الجدول المحوري** بتجميع كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. تُستبدل النتيجة المعروضة في Excel بميزة **إظهار القيم كـ** بحساب ثانوي مشتق من ذلك التجميع — على سبيل المثال، نسبة من الإجمالي الكلي، مجموع متراكم، فرق عن عنصر أساسي مختار، أو ترتيب — مما يتيح لك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.  
تشمل الاستخدامات النموذجية تحليل حصة الإجمالي، بما في ذلك نسب الصف، العمود، أو الإجمالي الكلي؛ إعداد تقارير تراكمية باستخدام مجموع متراكم في حقل فترة؛ تحليل الفروق مقابل عنصر مرجعي باستخدام الفرق عن أو الفرق بالنسبة المئوية من عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو العكس.

## **أعضاء تعداد PivotFieldDataDisplayFormat**
يحافظ حقل البيانات على دالة التجميع الخاصة به، مثل Sum أو Count، بينما يقوم **إظهار القيم كـ** بتحويل طريقة عرض القيمة المجمعة فقط.  
إلى جانب استخدام الـ setters الخاصة بـ `PivotShowValuesSetting` مباشرةً (انظر القسم الأخير)، تقوم طريقة الاستدعاء الواحد بتطبيق نفس التكوين:

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `displayFormat` | الحساب الثانوي `PivotFieldDataDisplayFormat` المراد تطبيقه. | دائمًا. |
| `baseField` | الفهرس الصفري للحقل الأساسي ضمن الحقول الأساسية للجدول المحوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItemPositionType` | طريقة اختيار العنصر الأساسي بالنسبة للعنصر الحالي: `PivotItemPositionType.PREVIOUS`، `NEXT`، أو `CUSTOM`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي. | فقط عندما تكون `baseItemPositionType` هي `CUSTOM` (يحدد الفهرس العنصر الأساسي الدقيق)؛ يتم تجاهله عند `PREVIOUS` / `NEXT` وفي كل التنسيقات غير القائمة على العنصر الأساسي — مرّر `0`. |

| نوع الحساب | السلوك | معلمات العنصر الأساسي |
| --- | --- | --- |
| `NORMAL` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (الافتراضي). | — |
| `DIFFERENCE_FROM` | يعرض القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `PERCENTAGE_OF` | يعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | يعرض القيمة كفرق نسبي مئوي عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `RUNNING_TOTAL_IN` | يعرض القيمة كمجموع متراكم للعناصر المتتابعة في حقل أساسي. | `baseField` (الحقل الذي يحدد ترتيب العناصر المتراكم) |
| `PERCENTAGE_OF_ROW` | يعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PERCENTAGE_OF_COLUMN` | يعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PERCENTAGE_OF_TOTAL` | يعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `INDEX` | يعرض القيمة باستخدام صيغة الفهرس في Excel ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي الصف الأب (لحقول الصف المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي العمود الأب (لحقول العمود المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي الأب. | `baseField` (الحقل الأصل المرجعي) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | يعرض القيمة كنسبة مئوية من مجموع متراكم في حقل أساسي. | `baseField` (حقل التجميع) |
| `RANK_SMALLEST_TO_LARGEST` | يرتب القيمة من الأصغر (1) إلى الأكبر. | — |
| `RANK_LARGEST_TO_SMALLEST` | يرتب القيمة من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` يضبط القيم لـ `PivotShowValuesSetting` عبر `setCalculationType(...)`، `setBaseFieldIndex(...)`، `setBaseItemPositionType(...)`، و `setBaseItemIndex(...)` — الطريقة وكائن الخاصية هما طريقتان لتكوين الحالة نفسها، مما يعكس منتقي الحقل الأساسي والعنصر الأساسي في نافذة **إظهار القيم كـ** في Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.showValuesAs(...)` مع `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` لتحويل كل خلية حقل بيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. وبالتالي تُظهر الأرقام كنسب من مجموعة النتائج الكاملة. يقيس هذا التنسيق كل قيمة مقابل الإجمالي الكلي فقط، لذا لا يحتاج إلى حقل أساسي أو عنصر أساسي — المعاملات اللاحقة (`0`، `PivotItemPositionType.PREVIOUS`، `0`) هي معاملات نائبة يتجاهلها التنسيق، كما هو موضح في جدول المعاملات أعلاه.

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
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **الحصول على وتكوين PivotField.getShowValuesSetting**
اقرأ التكوين الحالي عبر `PivotField.getShowValuesSetting()`: تُعيد الدالة getter للقراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، والتي تصف خصائصه الأربعة للحساب النشط في **إظهار القيم كـ**. لتغيير التكوين، استدعِ طريقة `PivotField.showValuesAs(...)` — فهي تكتب جميع الإعدادات الأربعة في استدعاء واحد، لذلك لا تحتاج إلى ضبط الخصائص واحدةً تلو الأخرى.  
كائن `PivotShowValuesSetting` يُظهر الخصائص الأربع التي تُكتبها `showValuesAs(...)`:
- `getCalculationType()` / `setCalculationType(...)` يختار الحساب الثانوي `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` يحدد الفهرس الصفري للحقل الأساسي داخل حقول الجدول المحوري. يُستخدم في تنسيقات المرجع.
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` يحدد كيفية تموضع العنصر الأساسي بالنسبة للعنصر الحالي ويقبل `PivotItemPositionType.NEXT`، `PivotItemPositionType.PREVIOUS`، أو `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` يحدد الفهرس الصفري للعنصر الأساسي ويُستخدم عندما تكون `BaseItemPositionType` هي `CUSTOM`.
بعد استدعاء `showValuesAs(...)`، استدعِ `PivotTable.calculateData()` مرةً أخرى حتى يتم إعادة حساب وعرض جسم الجدول المحوري بالتكوين المحدث.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في جدول محوري](/cells/ar/java/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/java/refresh-pivot-table/)
- [تطبيق النمط على جدول محوري](/cells/ar/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}