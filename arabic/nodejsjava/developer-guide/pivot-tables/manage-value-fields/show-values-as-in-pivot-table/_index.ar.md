---
title: إظهار القيم كـ في جدول محوري
linktitle: إظهار القيم كـ في جدول محوري
description: عرض قيم حقول البيانات في جدول محوري كنسبة مئوية من الإجمالي الكلي، أو الفرق من عنصر أساسي، أو إجماليات متراكمة، أو ترتيب، والمزيد باستخدام Aspose.Cells for Node.js عبر Java.
keywords: Aspose.Cells, جدول محوري, إظهار القيم كـ, تنسيق عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js عبر Java
type: docs
weight: 145
url: /ar/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
عادةً ما يجمع جدول محوري كل حقل بيانات باستخدام وظيفة تجميع مثل `SUM` أو `COUNT`. ميزة **إظهار القيم كـ** في Excel تستبدل كل نتيجة معروضة بحساب ثانوي مشتق من ذلك التجميع — على سبيل المثال، نسبة مئوية من الإجمالي الكلي، إجمالي متراكم، فرق عن عنصر أساسي مختار، أو ترتيب — مما يتيح إجراء تحليلات مقارنة دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.  
تشمل الاستخدامات الشائعة تحليل حصة الإجمالي الكلي، بما في ذلك نسب الصف أو العمود أو الإجمالي الكلي؛ التقارير التراكمية باستخدام إجمالي متراكم في حقل الفترة؛ تحليل الفروقات مقابل عنصر مرجعي باستخدام الفرق أو الفرق النسبي من عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو العكس.  
في Aspose.Cells for Node.js عبر Java، يحدد `PivotFieldDataDisplayFormat` الحساب الثانوي. تعيد الطريقة للقراءة فقط `PivotField.getShowValuesSetting()` كائنًا من نوع `PivotShowValuesSetting`. تُكوّن طرق `setCalculationType()` و `setBaseFieldIndex()` و `setBaseItemPositionType()` و `setBaseItemIndex()` السلوك؛ تُطبق طريقة الراحة `PivotField.showValuesAs(...)` نفس الإعدادات الأربعة في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.getDataFields()`.

## **أعضاء تعداد PivotFieldDataDisplayFormat**
يحافظ حقل البيانات على وظيفة التجميع الخاصة به، مثل SUM أو COUNT، بينما يحول **إظهار القيم كـ** طريقة عرض القيمة المجمعة فقط.  
إلى جانب كتابة إعدادات `PivotShowValuesSetting` مباشرة (انظر القسم الأخير)، تُطبق طريقة الراحة ذات الاستدعاء الواحد نفس التكوين:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `displayFormat` | الحساب الثانوي من نوع `PivotFieldDataDisplayFormat` الذي سيُطبق. | دائمًا. |
| `baseField` | الفهرس الصفري للحقول الأساسية بين الحقول الأساسية لجدول محوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItemPositionType` | الطريقة التي يُختار بها العنصر الأساسي بالنسبة للعنصر الحالي: `PivotItemPositionType.PREVIOUS`، `.NEXT`، أو `.CUSTOM`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي. | فقط عندما تكون `baseItemPositionType` هي `CUSTOM` (يختار فهرس العنصر القاعدة المحدد)؛ يُتجاهل للخيارات `PREVIOUS` / `NEXT` وفي جميع الصيغ غير القائمة على عنصر أساسي — مرّر `0`. |

| نوع الحساب | السلوك | معلمات عنصر القاعدة |
| --- | --- | --- |
| `NORMAL` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (الوضع الافتراضي). | — |
| `DIFFERENCE_FROM` | تعرض القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `PERCENTAGE_OF` | تعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | تعرض القيمة كنسبة فرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `RUNNING_TOTAL_IN` | تعرض القيمة كإجمالي متراكم لعناصر متتالية في حقل أساسي. | `baseField` (الحقل الذي يحدد ترتيب العنصر لتجميعه) |
| `PERCENTAGE_OF_ROW` | تعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PERCENTAGE_OF_COLUMN` | تعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PERCENTAGE_OF_TOTAL` | تعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `INDEX` | تعرض القيمة باستخدام صيغة الفهرس في Excel ((القيمة * الإجمالي الكلي) / (إجمالي الصف * إجمالي العمود)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | تعرض القيمة كنسبة مئوية من إجمالي الصف الوالد (لحقول الصف المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | تعرض القيمة كنسبة مئوية من إجمالي العمود الوالد (لحقول العمود المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | تعرض القيمة كنسبة مئوية من إجمالي الوالد. | `baseField` (الحقل الأصل المرجعي) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | تعرض القيمة كنسبة مئوية من إجمالي متراكم في حقل أساسي. | `baseField` (حقل التجميع) |
| `RANK_SMALLEST_TO_LARGEST` | ترتّب القيمة من الأصغر (1) إلى الأكبر. | — |
| `RANK_LARGEST_TO_SMALLEST` | ترتّب القيمة من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` يكتب الإعدادات لكائن `PivotShowValuesSetting` (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()`, و `setBaseItemIndex()`) — الطريقة وكائن الإعداد هما طريقتان لتكوين الحالة نفسها، مما يعكس محددات الحقل الأساسي والعنصر الأساسي في مربع حوار إظهار القيم كـ في Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.showValuesAs()` باستخدام `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` لتحويل كل خلية من حقل البيانات، بما في ذلك الإجمالي الكلي، إلى نصيبها من الإجمالي الكلي. وبالتالي تُعرض الأرقام كنسب من مجموعة النتائج الكاملة. هذا التنسيق يقيس كل قيمة مقابل الإجمالي الكلي فقط، لذا لا يتطلب حقلًا أساسيًا أو عنصرًا أساسيًا — المعاملات اللاحقة (`0`, `PivotItemPositionType.PREVIOUS`, `0`) هي مجرد نواقل يتجاهلها التنسيق كما هو موضح في جدول المعاملات أعلاه.

```javascript
const AsposeCells = require("aspose.cells");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **قراءة وتكوين PivotField.getShowValuesSetting()**
اقرأ التكوين الحالي عبر `PivotField.getShowValuesSetting()`؛ تُعيد الطريقة للقراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، والذي يحتوي على الإعدادات الأربعة التي تصف حساب إظهار القيم كـ النشط. لتغيير التكوين، استدعِ طريقة `PivotField.showValuesAs()` — فهي تكتب جميع الإعدادات الأربعة في استدعاء واحد، لذلك لن تحتاج إلى تعيينها بشكل منفرد.  
يُظهر كائن `PivotShowValuesSetting` الإعدادات الأربعة التي تُكتبها `showValuesAs()`:
- `getCalculationType()` / `setCalculationType()` يحددان الحساب الثانوي من نوع `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` يحددان الفهرس الصفري للحقول الأساسية داخل حقول محورية. يُستخدم في تنسيقات المرجع.
- `getBaseItemPositionType()` / `setBaseItemPositionType()` يحددان موضع العنصر الأساسي بالنسبة للعنصر الحالي ويقبلان `PivotItemPositionType.NEXT`، `PivotItemPositionType.PREVIOUS`، أو `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex()` يحددان الفهرس الصفري للعنصر الأساسي ويُستخدم عندما تكون `getBaseItemPositionType()` هي `CUSTOM`.  
بعد استدعاء `showValuesAs()`، استدعِ `PivotTable.calculateData()` مرة أخرى حتى يُعاد حساب جسم الجدول المحوري وإعادة عرضه وفق التكوين المحدث.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في جدول محوري](/cells/ar/nodejs-java/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/nodejs-java/refresh-pivot-table/)
- [تطبيق النمط على جدول محوري](/cells/ar/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}