---
title: عرض القيم في الجدول المحوري
description: اعرض قيم حقول البيانات في الجدول المحوري كنسبة مئوية من الإجمالي، أو كفرق من عنصر أساسي، أو كمجاميع تراكمية، أو كمراتب، والمزيد باستخدام Aspose.Cells for Node.js via C++.
linktitle: عرض القيم
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, جدول محوري, عرض القيم, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ar/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
يجمع الجدول المحوري عادةً كل حقل بيانات باستخدام دالة تجميع مثل `SUM` أو `COUNT`. وتستبدل ميزة **عرض القيم** في Excel كل نتيجة معروضة بحساب ثانوي مشتق من القيمة المجمعة، مثل نسبة من الإجمالي الكلي، أو إجمالي تراكمي، أو فرق من عنصر أساسي مُختار، أو ترتيب، ما يتيح إجراء تحليلات مقارنة دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.
تشمل الاستخدامات المعتادة تحليل حصة كل عنصر من الإجمالي، بما في ذلك النسب المئوية لإجمالي الصف أو العمود أو الإجمالي الكلي؛ والتقارير التراكمية باستخدام مجموع تراكمي في حقل فترة؛ وتحليل التباين مقابل عنصر مرجعي باستخدام الفرق من عنصر أساسي أو نسبة الفرق منه؛ وترتيب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.
في Aspose.Cells for Node.js via C++، يحدد التعداد `PivotShowValuesAsType` الحساب الثانوي. وتعيد خاصية الوصول للقراءة فقط `PivotField.getShowValuesSetting()` كائن `PivotShowValuesSetting`، الذي تهيئ أساليبه `setShowValuesAs()` و`setBaseFieldIndex()` و`setBaseItemIndex()` السلوك؛ وتطبق طريقة الاختصار `PivotField.showValuesAs(...)` الإعدادات نفسها في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو حقل قيمة تم الحصول عليه من `PivotTable.getDataFields()`.

## **أعضاء تعداد `PivotShowValuesAsType`]
يحتفظ حقل البيانات بدالة التجميع، مثل `SUM` أو `COUNT`، بينما تغيّر ميزة **عرض القيم** طريقة عرض القيمة المجمعة فقط.
إلى جانب كتابة إعدادات `PivotShowValuesSetting` مباشرة، راجع القسم الأخير، تطبق طريقة مساعدة في استدعاء واحد الإعداد نفسه. وتأتي في صيغتين، إحداهما تحدد الحقل الأساسي والعنصر الأساسي بالفهرس والأخرى بالاسم:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `showValuesAsType` | نوع الحساب الثانوي `PivotShowValuesAsType` المراد تطبيقه. | دائمًا. |
| `baseField` | الفهرس القائم على الصفر للحقل الأساسي ضمن الحقول الأساسية للجدول المحوري، مثل فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي، أو اسم الحقل الأساسي في الصيغة التي تعتمد على الاسم. | الصيغ الثماني المرتبطة بالأساس أدناه، وهي `DifferenceFrom` و`PercentageOf` و`PercentageDifferenceFrom` و`RunningTotalIn` و`PercentageOfParentTotal` و`PercentageOfRunningTotalIn` و`RankSmallestToLargest` و`RankLargestToSmallest`؛ ومرّر `0` أو `null` في الصيغة التي تعتمد على الاسم لكل صيغة أخرى. |
| `baseItem` | الفهرس القائم على الصفر للعنصر الأساسي، مع قيمتَي حارس: يحدد `-1` العنصر السابق ويحدد `-2` العنصر التالي، ولا يصدّر ربط Node.js عبر C++ الثوابت المسماة، لذا مرّر القيم الحرفية. وتستخدم الصيغة التي تعتمد على الاسم تسمية العنصر الأساسي بدلاً من ذلك، وتستخدم `null` عندما لا تحتاج الصيغة المحددة إلى عنصر أساسي. | تقيّم الصيغ الثلاث المرتبطة بالعنصر الأساسي، وهي `DifferenceFrom` و`PercentageOf` و`PercentageDifferenceFrom`، العنصر الأساسي؛ وتتجاهله صيغ الحقل الخمس، وهي `RunningTotalIn` و`PercentageOfParentTotal` و`PercentageOfRunningTotalIn` وصيغتا الترتيب، لذا مرّر `0` أو `null`. |

| نوع الحساب | السلوك | معاملات الحقل والعنصر الأساسيين |
| --- | --- | --- |
| `Normal` | لا يُطبَّق حساب ثانوي؛ تُعرض القيمة المجمعة كما هي، وهي القيمة الافتراضية. | — |
| `DifferenceFrom` | يعرض القيمة كفرق من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem`، أي فهرس أو تسمية أو قيمة حارس العنصر السابق/التالي. |
| `PercentageOf` | يعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem`، أي فهرس أو تسمية أو قيمة حارس العنصر السابق/التالي. |
| `PercentageDifferenceFrom` | يعرض القيمة كنسبة مئوية للفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem`، أي فهرس أو تسمية أو قيمة حارس العنصر السابق/التالي. |
| `RunningTotalIn` | يعرض القيمة كإجمالي تراكمي للعناصر المتتالية في حقل أساسي. | `baseField`، وهو الحقل الذي يحدد ترتيب عناصره التراكم. |
| `PercentageOfRow` | يعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PercentageOfColumn` | يعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PercentageOfTotal` | يعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `Index` | يعرض القيمة باستخدام صيغة مؤشر Excel `((value * grand total) / (row total * column total))`. | — |
| `PercentageOfParentRowTotal` | يعرض القيمة كنسبة مئوية من إجمالي صف الأصل، لحقول الصفوف المتداخلة. | — |
| `PercentageOfParentColumnTotal` | يعرض القيمة كنسبة مئوية من إجمالي عمود الأصل، لحقول الأعمدة المتداخلة. | — |
| `PercentageOfParentTotal` | يعرض القيمة كنسبة مئوية من إجمالي أصلها. | `baseField`، وهو الحقل الأصل الذي يكون إجماليه مرجعًا. |
| `PercentageOfRunningTotalIn` | يعرض القيمة كنسبة مئوية من إجمالي تراكمي في حقل أساسي. | `baseField`، وهو حقل التراكم. |
| `RankSmallestToLargest` | يرتب القيمة من الأصغر، أي 1، إلى الأكبر. | `baseField`، وهو الحقل الذي تحدد عناصره نطاق الترتيب. |
| `RankLargestToSmallest` | يرتب القيمة من الأكبر، أي 1، إلى الأصغر. | `baseField`، وهو الحقل الذي تحدد عناصره نطاق الترتيب. |

{{% alert color="primary" %}}
يكتب `showValuesAs(...)` إعدادات `PivotShowValuesSetting`، بما في ذلك `getShowValuesAs()`/`setShowValuesAs()` و`getBaseFieldIndex()`/`setBaseFieldIndex()` و`getBaseItemIndex()`/`setBaseItemIndex()`؛ وتوفر الطريقة وكائن الخاصية طريقتين لتهيئة الحالة نفسها، بما يعكس منتقي الحقل الأساسي والعنصر الأساسي في مربع حوار **عرض القيم** في Excel.
{{% /alert %}}

## **عرض القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.showValuesAs()` مع `PivotShowValuesAsType.PercentageOfTotal` لتحويل كل خلية في حقل البيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. لذلك تُعرض الأرقام كنسب من مجموعة النتائج الكاملة. يقيس هذا التنسيق كل قيمة مقابل الإجمالي الكلي فقط، لذا لا يحتاج إلى حقل أساسي أو عنصر أساسي. وسائط `0` و`0` في النهاية هي قيم نائبة يتجاهلها التنسيق، كما يوضح جدول المعاملات أعلاه.

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
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **الحصول على `PivotField.getShowValuesSetting()` وتهيئته**
اقرأ الإعدادات الحالية من خلال `PivotField.getShowValuesSetting()`؛ إذ تعيد خاصية القراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، وتصف إعداداته حساب **عرض القيم** النشط. لتغيير الإعدادات، استدعِ طريقة `PivotField.showValuesAs()`؛ فهي تكتب جميع الإعدادات في استدعاء واحد، لذا لا حاجة إلى تعيينها واحدًا تلو الآخر.
يعرض كائن `PivotShowValuesSetting` الحالة التي تكتبها `showValuesAs()`:
- تحدد `getShowValuesAs()` و`setShowValuesAs()` حساب `PivotShowValuesAsType` الثانوي.
- تحدد `getBaseFieldIndex()` و`setBaseFieldIndex()` الفهرس القائم على الصفر للحقل الأساسي ضمن حقول الجدول المحوري. ويُستخدم في الصيغ المرتبطة بالأساس.
- تحدد `getBaseItemIndex()` و`setBaseItemIndex()` العنصر الأساسي، سواء كان فهرسًا قائمًا على الصفر لعنصر جدول محوري محدد أو إحدى قيمتَي الحارس، `-1` للعنصر السابق و`-2` للعنصر التالي؛ ولا يصدّر الربط الثوابت المسماة. وتُستخدم في الصيغ المرتبطة بالعنصر الأساسي.
- تمثّل `getBaseFieldName()` و`getBaseItemCaption()` مشاهدتين للقراءة فقط تعرضان الاسم المحسوم للحقل الأساسي والتسمية المحسومة للعنصر الأساسي؛ على سبيل المثال، بعد اختيار قيمة الحارس الخاصة بالعنصر السابق، تعيد `getBaseItemCaption()` القيمة `(previous)`.
بعد استدعاء `showValuesAs()`، استدعِ `PivotTable.calculateData()` مرة أخرى حتى يُعاد حساب جسم الجدول المحوري وإعادة عرضه بالإعدادات المحدّثة.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/nodejs-cpp/manage-value-fields/)
- [تحديث الجدول المحوري](/cells/ar/nodejs-cpp/refresh-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}