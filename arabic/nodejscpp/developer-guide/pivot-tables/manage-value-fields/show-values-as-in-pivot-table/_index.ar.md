---
title: عرض القيم كما في جدول محوري
linktitle: عرض القيم كما في جدول محوري
description: عرض قيم حقل بيانات جدول محوري كنسبة مئوية من الإجمالي، أو كفرق عن عنصر أساسي، أو كإجماليات متراكمة، أو كترتيب، وغير ذلك باستخدام Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, جدول محوري, عرض القيم كـ, تنسيق عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ar/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
عادةً ما يجمع جدول محوري كل حقل بيانات باستخدام دالة تجميع مثل `SUM` أو `COUNT`. تُستبدل النتيجة المعروضة في Excel بميزة **Show Values As** بحساب ثانوي مشتق من ذلك التجميع — على سبيل المثال، نسبة من الإجمالي الكلي، إجمالي متراكم، فرق عن عنصر أساسي مختار، أو ترتيب — مما يتيح لك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محوسبة. تشمل الاستخدامات النموذجية تحليل حصة الإجمالي، بما في ذلك النسب المئوية للصف، العمود، أو الإجمالي الكلي؛ التقارير التراكمية باستخدام إجمالي متراكم في حقل الفترة؛ تحليل الفروق مقابل عنصر مرجعي باستخدام الفرق أو الفرق النسبي عن عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر. في Aspose.Cells for Node.js via C++، يحدد `PivotFieldDataDisplayFormat` الحساب الثانوي. تُعيد طريقة الوصول للقراءة فقط `PivotField.getShowValuesSetting()` كائن `PivotShowValuesSetting`، التي يمكن كتابة خصائصه عبر الأساليب القابلة للكتابة `setCalculationType()`، `setBaseFieldIndex()`، `setBaseItemPositionType()`، و `setBaseItemIndex()` لتكوين السلوك؛ كما أن طريقة الراحة `PivotField.showValuesAs(...)` تُطبق الإعدادات الأربعة نفسها في استدعاء واحد. يُطبق هذه الإعدادات على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.getDataFields()`.

## **أعضاء تعداد PivotFieldDataDisplayFormat**
يحتفظ حقل البيانات بدالة التجميع الخاصة به، مثل SUM أو COUNT، بينما تقوم ميزة Show Values As بتحويل طريقة عرض القيمة المجمعة فقط.  
إلى جانب كتابة خصائص `PivotShowValuesSetting` مباشرةً (انظر القسم الأخير)، توفر طريقة الراحة ذات الاستدعاء الواحد نفس التكوين:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
function pickEnum(enumType, candidates, fallback) {
    const type = enumType || {};
    for (const name of candidates) {
        if (type[name] !== undefined && type[name] !== null) {
            return type[name];
        }
    }
    return fallback;
}
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().add("PivotData");
const cells = sheet.getCells();
// --- Source data -----------------------------------------------------------
const headers = ["Region", "Product", "Sales"];
for (const [c, header] of headers.entries()) {
    cells.get(0, c).putValue(header);
}
const rows = [
    ["East", "Apple", 100],
    ["East", "Banana", 120],
    ["West", "Apple", 90],
    ["West", "Banana", 60],
    ["North", "Apple", 75],
    ["North", "Banana", 45]
];
for (const [r, row] of rows.entries()) {
    for (const [c, value] of row.entries()) {
        cells.get(r + 1, c).putValue(value);
    }
}
// --- Pivot table ------------------------------------------------------------
const pivotTables = sheet.getPivotTables();
const pivotTable = pivotTables.add("A1:C7", 0, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Region");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
const salesField = pivotTable.getDataFields().get(0);
// --- ShowValuesAs -----------------------------------------------------------
const displayFormat = pickEnum(
    AsposeCells.PivotFieldDataDisplayFormat,
    ["PERCENT_OF_TOTAL", "PercentOfTotal", "PERCENTAGE_OF_TOTAL", "PercentageOfTotal"],
    7
);
const baseItemPositionType = pickEnum(
    AsposeCells.PivotItemPositionType,
    ["DEFAULT", "Default"],
    0
);
showValuesAs(salesField, displayFormat, -1, baseItemPositionType, -1);
// --- Save -------------------------------------------------------------------
workbook.save("ShowValuesAs.xlsx");
console.log("ShowValuesAs applied and workbook saved.");
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `displayFormat` | حساب `PivotFieldDataDisplayFormat` الثانوي الذي سيتم تطبيقه. | دائمًا. |
| `baseField` | الفهرس الصفري للحقل الأساسي بين الحقول الأساسية لجدول محوري (مثلاً، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItemPositionType` | طريقة اختيار العنصر الأساسي بالنسبة للعنصر الحالي: `PivotItemPositionType.PREVIOUS`, `.NEXT`, أو `.CUSTOM`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي. | فقط عندما يكون `baseItemPositionType` هو `CUSTOM` (يختار فهرس العنصر العنصر الأساسي الدقيق)؛ يتم تجاهله عند `PREVIOUS` / `NEXT` وفي جميع التنسيقات غير القائمة على العنصر الأساسي — مرّر `0`. |

| نوع الحساب | السلوك | معلمات العنصر الأساسي |
| --- | --- | --- |
| `NORMAL` | لا حساب ثانوي؛ يتم عرض القيمة المجمعة كما هي (الافتراضي). | — |
| `DIFFERENCE_FROM` | يعرض القيمة كفرق عن قيمة العنصر الأساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `PERCENTAGE_OF` | يعرض القيمة كنسبة مئوية من قيمة العنصر الأساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | يعرض القيمة كفرق نسبي عن قيمة العنصر الأساسي في حقل أساسي. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` فقط مع `CUSTOM`) |
| `RUNNING_TOTAL_IN` | يعرض القيمة كإجمالي متراكم للعناصر المتتابعة لحقل أساسي. | `baseField` (الحقل الذي يتحكم بترتيب العناصر لتجميع القيم) |
| `PERCENTAGE_OF_ROW` | يعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PERCENTAGE_OF_COLUMN` | يعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PERCENTAGE_OF_TOTAL` | يعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `INDEX` | يعرض القيمة باستخدام صيغة الفهرس في Excel ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي الصف الأصلي (للحقول المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي العمود الأصلي (للحقول المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | يعرض القيمة كنسبة مئوية من إجمالي الأصل. | `baseField` (الحقل الأصل المرجعي) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | يعرض القيمة كنسبة مئوية من إجمالي متراكم في حقل أساسي. | `baseField` (حقل التجميع) |
| `RANK_SMALLEST_TO_LARGEST` | يرتب القيمة من الأصغر (1) إلى الأكبر. | — |
| `RANK_LARGEST_TO_SMALLEST` | يرتب القيمة من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` يكتب الإعدادات لـ `PivotShowValuesSetting` (`getCalculationType()`/`setCalculationType()`، `getBaseFieldIndex()`/`setBaseFieldIndex()`، `getBaseItemPositionType()`/`setBaseItemPositionType()`، و `getBaseItemIndex()`/`setBaseItemIndex()`) — الطريقة وكائن الخاصية يمثلان طريقتين لتكوين الحالة نفسها، مما يعكس محددات الحقل الأساسي والعنصر الأساسي في مربع حوار **Show Values As** في Excel.
{{% /alert %}}

## **عرض القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.showValuesAs()` مع `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` لتحويل كل خلية حقل بيانات، بما فيها الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. وبالتالي تُقرأ الأرقام المعروضة كنسب من مجموعة النتائج الكاملة. هذا التنسيق يقيس كل قيمة مقابل الإجمالي الكلي فقط، لذا لا يحتاج إلى حقل أساسي أو عنصر أساسي — الوسيطات المتتبقة (`0`, `PivotItemPositionType.PREVIOUS`, `0`) هي دلائل يُهملها التنسيق، كما هو موضح في جدول المعاملات أعلاه.

```javascript
const AsposeCells = require("aspose.cells.node");
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
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
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
اقرأ الإعداد الحالي عبر `PivotField.getShowValuesSetting()`: طريقة الوصول للقراءة فقط تُعيد كائن `PivotShowValuesSetting` الخاص بالحقل، الذي تصف خصائصه الأربعة الحساب النشط لـ **Show Values As**. لتغيير الإعداد، استدعِ طريقة `PivotField.showValuesAs()` — فهي تكتب جميع الإعدادات الأربعة في استدعاء واحد، لذا لا تحتاج إلى تعيين الخصائص واحدةً تلو الأخرى. يُظهر كائن `PivotShowValuesSetting` الإعدادات الأربعة التي تكتبها `showValuesAs()`:
- `getCalculationType()` و `setCalculationType()` يحددان حساب `PivotFieldDataDisplayFormat` الثانوي.
- `getBaseFieldIndex()` و `setBaseFieldIndex()` يحددان الفهرس الصفري للحقل الأساسي ضمن حقول المحور. يُستخدم في تنسيقات المرجع.
- `getBaseItemPositionType()` و `setBaseItemPositionType()` يحددان موضع العنصر الأساسي بالنسبة للعنصر الحالي وتقبل القيم `PivotItemPositionType.NEXT`، `PivotItemPositionType.PREVIOUS`، أو `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` و `setBaseItemIndex()` يحددان الفهرس الصفري للعنصر الأساسي ويُستخدمان عندما يكون `getBaseItemPositionType()` هو `CUSTOM`.
بعد استدعاء `showValuesAs()`، استدعِ `PivotTable.calculateData()` مرة أخرى لإعادة حساب وإعادة رسم جسم جدول محوري وفق الإعدادات المحدثة.

```javascript
const AsposeCells = require("aspose.cells.node");
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
- [إدارة حقول القيم في جدول محوري](/cells/ar/nodejs-cpp/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/nodejs-cpp/refresh-pivot-table/)
- [تطبيق النمط على جدول محوري](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}