---
title: إظهار القيم كـ في جدول محوري
description: عرض قيم حقول البيانات في جدول محوري كنسبة مئوية من المجموع، أو كفرق من عنصر أساسي، أو إجماليات تشغيلية، أو ترتيب، وغيرها باستخدام Aspose.Cells for Node.js via Java.
linktitle: إظهار القيم كـ
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, جدول محوري, إظهار القيم كـ, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ar/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
عادةً ما يجمع جدول محوري كل حقل بيانات باستخدام دالة تجميع مثل `SUM` أو `COUNT`. ميزة **Show Values As** في Excel تستبدل كل نتيجة معروضة بحساب ثانوي مشتق من تلك التجميع—على سبيل المثال، نسبة مئوية من المجموع العام، إجمالي تشغيلي، فرق من عنصر أساسي مختار، أو ترتيب—مما يتيح لك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.  
تشمل الاستخدامات الشائعة تحليل حصة الإجمالي، بما في ذلك النسب المئوية لصف أو عمود أو المجموع الكلي؛ إعداد تقارير تراكمية باستخدام إجمالي تشغيلي في حقل الفترة؛ تحليل الفروق مقابل عنصر مرجعي باستخدام الفرق من أو الفرق النسبي من عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو العكس.  
في Aspose.Cells for Node.js via Java، يحدد تعداد `PivotShowValuesAsType` الحساب الثانوي. تُعيد الطريقة للقراءة فقط `PivotField.getShowValuesSetting()` كائنًا من نوع `PivotShowValuesSetting`، وتُعيد أساليب `setShowValuesAs()` و`setBaseFieldIndex()` و`setBaseItemIndex()` ضبط السلوك؛ كما تُطبق طريقة المساعدة `PivotField.showValuesAs(...)` نفس الإعدادات في استدعاء واحد. يُمكن تطبيق هذه الإعدادات على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.getDataFields()`.

## **أعضاء تعداد PivotShowValuesAsType**
يحتفظ حقل البيانات بدالته التجميعية، مثل SUM أو COUNT، بينما يتم تحويل طريقة عرض القيم فقط عبر **Show Values As**.  
إلى جانب استخدام أساليب `PivotShowValuesSetting` مباشرةً (انظر القسم الأخير)، تُطبق طريقة المساعدة التي تُنفّذ تكوينًا واحدًا. وتتوفر بطريقتين — إحداهما تتعامل مع حقل وأساسي بالرقم، والأخرى بالاسم:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| المعلمة | المعنى | متى تكون مطلوبة |
| --- | --- | --- |
| `showValuesAsType` | حساب `PivotShowValuesAsType` الثانوي الذي سيُطبق. | دائمًا. |
| `baseField` | الفهرس الصفري للحقول الأساسية بين الحقول الأساسية لجدول المحوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي)، أو — في الشكل القائم على الاسم — اسم الحقل الأساسي. | الصيغ الثمانية المرتبطة بالأساس أدناه (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`)؛ مرّر `0` (أو `null` في الشكل القائم على الاسم) لكل صيغة أخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي، مع اثنين من القيم الحارسة: -1 يختار العنصر السابق و-2 التالي (حزمة الجذر لا تُصدّر ثوابت `PivotShowValuesSetting` — استخدم القيم الحرفية). الشكل القائم على الاسم يأخذ تسمية العنصر الأساسي بدلاً من ذلك، ويُعطى `null` عندما لا تحتاج الصيغة المختارة إلى عنصر أساسي. | فقط الصيغ الثلاث المرتبطة بالعنصر الأساسي (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) تتطلب العنصر الأساسي؛ الصيغ الخمس المرتبطة بالحقل (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, كلا الترتيبين) تتجاهله — مرّر `0` أو `null`. |

| نوع الحساب | السلوك | معلمات العنصر الأساسي |
| --- | --- | --- |
| `NORMAL` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمّعة كما هي (الإعداد الافتراضي). | — |
| `DIFFERENCE_FROM` | تُظهر القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو تسمية، أو القيم الحارسة السابقة/التالية) |
| `PERCENTAGE_OF` | تُظهر القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو تسمية، أو القيم الحارسة السابقة/التالية) |
| `PERCENTAGE_DIFFERENCE_FROM` | تُظهر القيمة كفرق نسبي عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو تسمية، أو القيم الحارسة السابقة/التالية) |
| `RUNNING_TOTAL_IN` | تُظهر القيمة كإجمالي تشغيلي لعناصر متتالية في حقل أساسي. | `baseField` (الحقل الذي يُحدد ترتيب العناصر لتجميعها) |
| `PERCENTAGE_OF_ROW` | تُظهر القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PERCENTAGE_OF_COLUMN` | تُظهر القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PERCENTAGE_OF_TOTAL` | تُظهر القيمة كنسبة مئوية من المجموع الكلي. | — |
| `INDEX` | تُظهر القيمة باستخدام صيغة الفهرس في Excel ((القيمة * المجموع الكلي) / (إجمالي الصف * إجمالي العمود)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | تُظهر القيمة كنسبة مئوية من إجمالي الصف الأب (لحقول الصف المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | تُظهر القيمة كنسبة مئوية من إجمالي العمود الأب (لحقول العمود المتداخلة). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | تُظهر القيمة كنسبة مئوية من إجمالي العنصر الأب. | `baseField` (الحقل الأب الذي يُستند إلى إجماله) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | تُظهر القيمة كنسبة مئوية من إجمالي تشغيلي في حقل أساسي. | `baseField` (حقل التجميع) |
| `RANK_SMALLEST_TO_LARGEST` | تُرتّب القيمة من الأصغر (1) إلى الأكبر. | `baseField` (الحقل الذي تُحدّد عناصره نطاق الترتيب) |
| `RANK_LARGEST_TO_SMALLEST` | تُرتّب القيمة من الأكبر (1) إلى الأصغر. | `baseField` (الحقل الذي تُحدّد عناصره نطاق الترتيب) |

{{% alert color="primary" %}}
`showValuesAs(...)` يكتب حالة `PivotShowValuesSetting` عبر `setShowValuesAs()`، `setBaseFieldIndex()`، و`setBaseItemIndex()` — الطريقة وكائن الخاصية هما طريقتان لضبط الحالة نفسها، وتعكسان محددات الحقل الأساسي والعنصر الأساسي في مربع الحوار **Show Values As** في Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من المجموع الكلي**
استدعِ الطريقة `PivotField.showValuesAs()` مع `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` لتحويل كل خلية حقل بيانات، بما فيها المجموع الكلي، إلى نصيبها من المجموع الكلي. وبالتالي تُقرأ الأرقام المعروضة كنسب من مجموعة النتائج الكاملة. تُقَيّم هذه الصيغة كل قيمة مقابل المجموع الكلي فقط، لذا لا تحتاج إلى حقل أساسي أو عنصر أساسي — الوسيطات اللاحقة (`0`, `0`) هي عناصر نائبة تتجاهلها الصيغة، كما هو موضح في جدول المعلمات أعلاه.

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **قراءة وتكوين PivotField.getShowValuesSetting()**
اقرأ التكوين الحالي عبر `PivotField.getShowValuesSetting()`؛ تُعيد الطريقة للقراءة فقط كائن `PivotShowValuesSetting` للحقول، الذي تصف إعداداته عملية **Show Values As** النشطة. لتغيير التكوين، استدعِ الطريقة `PivotField.showValuesAs()` — فهي تُكتب جميع الإعدادات في استدعاء واحد، لذلك لن تحتاج إلى ضبطها واحدةً تلو الأخرى.  
يعرض كائن `PivotShowValuesSetting` الحالة التي تكتبها `showValuesAs()`:
- `getShowValuesAs()` / `setShowValuesAs()` يختار حساب `PivotShowValuesAsType` الثانوي.  
- `getBaseFieldIndex()` / `setBaseFieldIndex()` يحدِّد الفهرس الصفري للحقول الأساسية داخل حقول المحوري. يُستَخدم في الصيغ المرتبطة بالأساس.  
- `getBaseItemIndex()` / `setBaseItemIndex()` يحدِّد العنصر الأساسي: فهرس صفري لعنصر محوري محدد، أو أحد القيم الحارسة — -1 للعنصر السابق، -2 للعنصر التالي (حزمة الجذر لا تُصدّر الثوابت المسماة). يُستَخدم في الصيغ المرتبطة بالعنصر الأساسي.  
- `getBaseFieldName()` و`getBaseItemCaption()` هما رؤى للقراءة فقط تُبلِغان اسم الحقل الأساسي المُحلّ وحساب العنصر الأساسي؛ على سبيل المثال، بعد اختيار القيمة الحارسة للعنصر السابق، تُعيد `getBaseItemCaption()` القيمة `(previous)`.  
بعد استدعاء `showValuesAs()`، استدعِ `PivotTable.calculateData()` مرةً أخرى لتُعيد حساب جسم المحوري وإعادة عرضه بالإعدادات المحدَّثة.

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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
- [إدارة حقول القيم في جدول محوري](/cells/ar/nodejs-java/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/nodejs-java/refresh-pivot-table/)
- [تطبيق نمط على جدول محوري](/cells/ar/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}