---
title: إظهار القيم كما في جدول محوري
linktitle: إظهار القيم كـ
description: عرض قيم حقل بيانات جدول محوري كنسبة مئوية من الإجمالي، أو فرق عن عنصر أساسي، إجماليات متراكمة، تصنيفات، والمزيد باستخدام Aspose.Cells for .NET.
keywords: Aspose.Cells, جدول محوري, إظهار القيم كـ, تنسيق عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /ar/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يجمع الجدول المحوري عادةً كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. ميزة **Show Values As** في Excel تستبدل كل نتيجة معروضة بحساب ثانوي مشتق من ذلك التجميع — على سبيل المثال، نسبة مئوية من الإجمالي الكلي، إجمالي متراكم، فرق عن عنصر أساسي مختار، أو تصنيف — بحيث يمكنك إجراء تحليل مقارن دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة.
تشمل الاستخدامات النموذجية تحليل حصة الإجمالي، بما في ذلك النسب المئوية لصف أو عمود أو الإجمالي الكلي؛ تقارير تراكمية باستخدام إجمالي متراكم في حقل الفترة؛ تحليل الفروقات مقارنةً بعنصر مرجعي باستخدام الفرق أو الفرق بالنسبة المئوية من عنصر أساسي؛ وتصنيف القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.
في Aspose.Cells for .NET، يحدد `PivotFieldDataDisplayFormat` الحساب الثانوي. الخاصية للقراءة فقط `PivotField.ShowValuesSetting` تُعيد كائن `PivotShowValuesSetting`، التي تُكوّن خصائصه القابلة للكتابة `CalculationType` و `BaseFieldIndex` و `BaseItemPositionType` و `BaseItemIndex` السلوك؛ طريقة الراحة `PivotField.ShowValuesAs(...)` تطبق الإعدادات الأربعة نفسها في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو قيمة يتم الحصول عليه من `PivotTable.DataFields`.

## **أعضاء تعداد PivotFieldDataDisplayFormat**
يحتفظ حقل البيانات بدالة التجميع الخاصة به، مثل Sum أو Count، بينما يقوم Show Values As بتغيير طريقة عرض القيمة المجمعة فقط.
بالإضافة إلى كتابة خصائص `PivotShowValuesSetting` مباشرةً (انظر القسم الأخير)، تطبق طريقة الراحة ذات الاستدعاء الواحد نفس الإعدادات:

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `displayFormat` | الحساب الثانوي `PivotFieldDataDisplayFormat` الذي يجب تطبيقه. | دائمًا. |
| `baseField` | الفهرس الصفري للحقل الأساسي بين حقول قاعدة جدول المحور (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItemPositionType` | طريقة اختيار العنصر الأساسي بالنسبة إلى العنصر الحالي: `PivotItemPositionType.Previous`، `.Next`، أو `.Custom`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي. | فقط عندما يكون `baseItemPositionType` هو `Custom` (يختار فهرس العنصر العنصر الأساسي المحدد)؛ يتم تجاهله لـ `Previous` / `Next` وفي جميع التنسيقات غير القائمة على العنصر الأساسي — مرّر `0`. |

| نوع الحساب | السلوك | معاملات العنصر الأساسي |
| --- | --- | --- |
| `Normal` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (افتراضي). | — |
| `DifferenceFrom` | تُظهر القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageOf` | تُظهر القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageDifferenceFrom` | تُظهر القيمة كالفرق بالنسبة المئوية عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `RunningTotalIn` | تُظهر القيمة كإجمالي متراكم لعناصر متتالية في حقل أساسي. | `baseField` (الحقل الذي يقود ترتيب العناصر المتراكم) |
| `PercentageOfRow` | تُظهر القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PercentageOfColumn` | تُظهر القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PercentageOfTotal` | تُظهر القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `Index` | تُظهر القيمة باستخدام صيغة الفهرس في Excel ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | تُظهر القيمة كنسبة مئوية من إجمالي الصف الأب (للحقول الصفية المتداخلة). | — |
| `PercentageOfParentColumnTotal` | تُظهر القيمة كنسبة مئوية من إجمالي العمود الأب (للحقول العمودية المتداخلة). | — |
| `PercentageOfParentTotal` | تُظهر القيمة كنسبة مئوية من إجمالي الأب. | `baseField` (الحقل الأصل المرجعي) |
| `PercentageOfRunningTotalIn` | تُظهر القيمة كنسبة مئوية من إجمالي متراكم في حقل أساسي. | `baseField` (حقل التجميع) |
| `RankSmallestToLargest` | تصنّف القيمة من الأصغر (1) إلى الأكبر. | — |
| `RankLargestToSmallest` | تصنّف القيمة من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` يكتب خصائص `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — الطريقة وكائن الخاصية طريقتان لتكوين الحالة نفسها، مما يعكس محددات الحقل الأساسي والعنصر الأساسي في مربع حوار Show Values As في Excel.
{{% /alert %}}

## **إظهار القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.ShowValuesAs` مع `PivotFieldDataDisplayFormat.PercentageOfTotal` لتحويل كل خلية في حقل البيانات، بما فيها الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. وبالتالي تُقرأ الأرقام المعروضة كنسب من مجموعة النتائج الكاملة. هذا التنسيق يقيس كل قيمة مقابل الإجمالي الكلي فقط، لذلك لا يحتاج إلى حقل أساسي أو عنصر أساسي — المعاملات اللاحقة (`0`, `PivotItemPositionType.Previous`, `0`) هي قيم نائبة يتجاهلها التنسيق، كما هو موضح في جدول المعاملات أعلاه.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **قراءة وتكوين PivotField.ShowValuesSetting**
اقرأ التكوين الحالي عبر `PivotField.ShowValuesSetting`: الخاصية للقراءة فقط تُعيد كائن `PivotShowValuesSetting` الخاص بالحقل، الذي يحتوي على الخصائص الأربعة التي تصف حساب Show Values As النشط. لتغيير التكوين، استدعِ طريقة `PivotField.ShowValuesAs` — فهي تكتب جميع الإعدادات الأربعة في استدعاء واحد، لذا لا تحتاج إلى تعيين الخصائص واحدةً تلو الأخرى.
كائن `PivotShowValuesSetting` يكشف الخصائص الأربعة التي تكتبها `ShowValuesAs`:
- `CalculationType` يحدّد الحساب الثانوي `PivotFieldDataDisplayFormat`.
- `BaseFieldIndex` يحدد الفهرس الصفري للحقل الأساسي داخل حقول الجدول المحوري. يُستعمل في تنسيقات المرجع.
- `BaseItemPositionType` يقرّر كيفية وضع العنصر الأساسي بالنسبة إلى العنصر الحالي ويقبل القيم `PivotItemPositionType.Next`، `PivotItemPositionType.Previous`، أو `PivotItemPositionType.Custom`.
- `BaseItemIndex` يحدد الفهرس الصفري للعنصر الأساسي ويُستعمل عندما تكون `BaseItemPositionType` هي `Custom`.
بعد استدعاء `ShowValuesAs`، استدعِ `PivotTable.CalculateData()` مرة أخرى حتى يُعاد حساب وعرض جسم الجدول المحوري بالتكوين المحدَّث.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **مقالات ذات صلة**
- [إدارة حقول القيم في جدول محوري](/cells/ar/net/manage-value-fields/)
- [العمل مع تنسيقات عرض البيانات لحقل البيانات في جدول محوري](/cells/ar/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [تحديث جدول محوري](/cells/ar/net/refresh-pivot-table/)
- [تطبيق نمط على جدول محوري](/cells/ar/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}