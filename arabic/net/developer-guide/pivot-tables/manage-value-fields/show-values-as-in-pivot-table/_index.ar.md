---
title: عرض القيم كـ في الجدول المحوري
linktitle: عرض القيم كـ في الجدول المحوري
description: عرض قيم حقول بيانات الجدول المحوري كنسب مئوية من الإجمالي، أو كفروق من عناصر أساسية، أو كإجماليات تراكمية، أو كمراتب، وغيرها باستخدام Aspose.Cells for .NET.
keywords: Aspose.Cells, جدول محوري, عرض القيم كـ, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /ar/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يجمع الجدول المحوري عادةً كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. تستبدل ميزة **عرض القيم كـ** في Excel كل نتيجة معروضة بحساب ثانوي مشتق من هذا التجميع، مثل نسبة مئوية من الإجمالي الكلي، أو إجمالي تراكمي، أو فرق من عنصر أساسي محدد، أو رتبة. ويتيح ذلك إجراء تحليل مقارن دون صيغ مساعدة أو أعمدة محسوبة.
تشمل الاستخدامات المعتادة تحليل نسبة العنصر إلى الإجمالي، بما في ذلك احتساب النسب المئوية لصف أو عمود أو للإجمالي الكلي؛ وإعداد التقارير التراكمية باستخدام إجمالي تراكمي في حقل فترة زمنية؛ وتحليل التباين مقارنةً بعنصر مرجعي باستخدام الفرق من عنصر أساسي أو نسبة الفرق منه؛ وتحديد رتب القيم من الأصغر إلى الأكبر أو من الأكبر إلى الأصغر.
في Aspose.Cells for .NET، يحدد التعداد `PivotShowValuesAsType` نوع الحساب الثانوي. وتعيد الخاصية للقراءة فقط `PivotField.ShowValuesSetting` كائن `PivotShowValuesSetting`، وتُستخدم خصائصه القابلة للكتابة، `ShowValuesAs` و`BaseFieldIndex` و`BaseItemIndex`، لضبط السلوك. وتطبق طريقة الاختصار `PivotField.ShowValuesAs(...)` الإعدادات نفسها في استدعاء واحد. طبّق هذه الإعدادات على حقل بيانات أو حقل قيمة يُؤخذ من `PivotTable.DataFields`.

## **أعضاء تعداد `PivotShowValuesAsType`**
يحتفظ حقل البيانات بدالة التجميع الخاصة به، مثل `Sum` أو `Count`، في حين لا يغيّر **عرض القيم كـ** سوى طريقة عرض القيمة المجمَّعة.
بالإضافة إلى كتابة خصائص `PivotShowValuesSetting` مباشرةً (راجع القسم الأخير)، تتيح طريقة اختصار يمكن استدعاؤها مرة واحدة تكوين الإعدادات نفسها. وتتتوفر لها صيغتان: الأولى تحدد الحقل الأساسي والعنصر الأساسي بالفهرس، والثانية تحددهما بالاسم:

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `showValuesAsType` | الحساب الثانوي من نوع `PivotShowValuesAsType` الذي يجب تطبيقه. | دائمًا. |
| `baseField` | فهرس الحقل الأساسي بدءًا من الصفر ضمن الحقول الأساسية للجدول المحوري، مثل فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي، أو، في الصيغة النصية، اسم الحقل الأساسي. | الصيغ الثماني القائمة على الحقل الأساسي أدناه (`DifferenceFrom` و`PercentageOf` و`PercentageDifferenceFrom` و`RunningTotalIn` و`PercentageOfParentTotal` و`PercentageOfRunningTotalIn` و`RankSmallestToLargest` و`RankLargestToSmallest`)؛ مرّر `0`، أو `null` في الصيغة النصية، لكل صيغة أخرى. |
| `baseItem` | فهرس العنصر الأساسي بدءًا من الصفر، مع قيمتين استثنائيتين: `PivotShowValuesSetting.PreviousPivotItem` (-1) لتحديد العنصر السابق و`PivotShowValuesSetting.NextPivotItem` (-2) لتحديد العنصر التالي. تأخذ الصيغة النصية تسمية العنصر الأساسي بدلًا من ذلك، وتستخدم `null` عندما لا تحتاج الصيغة المحددة إلى عنصر أساسي. | لا يُقيَّم العنصر الأساسي إلا في الصيغ الثلاث القائمة عليه (`DifferenceFrom` و`PercentageOf` و`PercentageDifferenceFrom`)؛ أما الصيغ الخمس القائمة على الحقل (`RunningTotalIn` و`PercentageOfParentTotal` و`PercentageOfRunningTotalIn` وصيغتا الترتيب) فتتجاهله. لذا مرّر `0` أو `null`. |

| نوع الحساب | السلوك | معاملات العنصر الأساسي |
| --- | --- | --- |
| `Normal` | لا يوجد حساب ثانوي؛ تُعرض القيمة المجمَّعة كما هي (الافتراضي). | — |
| `DifferenceFrom` | يعرض القيمة كفرق من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو تسمية، أو قيمة استثنائية للعنصر السابق/التالي) |
| `PercentageOf` | يعرض القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `baseItem` (فهرس أو تسمية، أو قيمة استثنائية للعنصر السابق/التالي) |
| `PercentageDifferenceFrom` | يعرض القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي، معبرًا عنه كنسبة مئوية. | `baseField` + `baseItem` (فهرس أو تسمية، أو قيمة استثنائية للعنصر السابق/التالي) |
| `RunningTotalIn` | يعرض القيمة كإجمالي تراكمي للعناصر المتتابعة في حقل أساسي. | `baseField` (الحقل الذي يحدد ترتيب العناصر المستخدمة في التراكم) |
| `PercentageOfRow` | يعرض القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PercentageOfColumn` | يعرض القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PercentageOfTotal` | يعرض القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `Index` | يعرض القيمة باستخدام صيغة الفهرس في Excel: ((القيمة * الإجمالي الكلي) / (إجمالي الصف * إجمالي العمود)). | — |
| `PercentageOfParentRowTotal` | يعرض القيمة كنسبة مئوية من إجمالي الصف الأصل، في حققول الصفوف المتداخلة. | — |
| `PercentageOfParentColumnTotal` | يعرض القيمة كنسبة مئوية من إجمالي العمود الأصل، في حققول الأعمدة المتداخلة. | — |
| `PercentageOfParentTotal` | يعرض القيمة كنسبة مئوية من إجمالي العنصر الأصل. | `baseField` (الحقل الأصل الذي يكون إجماليه هو المرجع) |
| `PercentageOfRunningTotalIn` | يعرض القيمة كنسبة مئوية من الإجمالي التراكمي في حقل أساسي. | `baseField` (حقل التراكم) |
| `RankSmallestToLargest` | يحدد رتبة القيمة من الأصغر (1) إلى الأكبر. | `baseField` (الحقل الذي تحدد عناصره نطاق الترتيب) |
| `RankLargestToSmallest` | يحدد رتبة القيمة من الأكبر (1) إلى الأصغر. | `baseField` (الحقل الذي تحدد عناصره نطاق الترتيب) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` يكتب حالة `PivotShowValuesSetting` (`ShowValuesAs` و`BaseFieldIndex` و`BaseItemIndex`)، ويوفر الأسلوب وكائن الخاصية طريقتين لتكوين الحالة نفسها، بما يحاكي محددي الحقل الأساسي والعنصر الأساسي في مربع حوار «عرض القيم كـ» في Excel.
{{% /alert %}}

## **عرض القيم كنسبة مئوية من الإجمالي**
استدعِ الأسلوب `PivotField.ShowValuesAs` مع `PivotShowValuesAsType.PercentageOfTotal` لتحويل كل خلية من حقول البيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. لذلك تظهر الأرقام المعروضة كنسب من مجموعة النتائج بأكملها. تقيس هذه الصيغة كل قيمة مقارنةً بالإجمالي الكلي فقط، لذا لا تحتاج إلى حقل أساسي أو عنصر أساسي. ويُعد وسيطا الاستدعاء الأخيران (`0` و`0`) قيمتين نائبتين تتجاهلهما الصيغة، كما يوضح جدول المعاملات أعلاه.

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **قراءة `PivotField.ShowValuesSetting` وتكوينه**
اقرأ الإعدادات الحالية عبر `PivotField.ShowValuesSetting`: تعيد الخاصية للقراءة فقط كائن `PivotShowValuesSetting` الخاص بالحقل، وتصف خصائصه الحساب الثانوي النشط المرتبط بميزة «عرض القيم كـ». لتغيير الإعدادات، استدعِ الأسلوب `PivotField.ShowValuesAs`؛ فهو يكتب جميع الإعدادات في استدعاء واحد، ولا تحتاج إلى تعيين الخصائص واحدة تلو الأخرى.
يتيح كائن `PivotShowValuesSetting` الوصول إلى الحالة التي يكتبها `ShowValuesAs`:
- يحدد `ShowValuesAs` الحساب الثانوي من نوع `PivotShowValuesAsType`.
- يحدد `BaseFieldIndex` فهرس الحقل الأساسي بدءًا من الصفر ضمن حقول الجدول المحوري. ويستخدم في الصيغ القائمة على الحقل الأساسي.
- يحدد `BaseItemIndex` العنصر الأساسي، سواء كان فهرسًا بدءًا من الصفر لعنصر محدد في الجدول المحوري أو إحدى القيمتين الاستثنائيتين، `PivotShowValuesSetting.PreviousPivotItem` (-1) للعنصر السابق و`PivotShowValuesSetting.NextPivotItem` (-2) للعنصر التالي. ويستخدم في الصيغ القائمة على العنصر الأساسي.
- يعرض `BaseFieldName` و`BaseItemCaption`، للقراءة فقط، اسم الحقل الأساسي وتسمية العنصر الأساسي المحدَّدين؛ على سبيل المثال، بعد اختيار القيمة الاستثنائية للعنصر السابق، تُظهر `BaseItemCaption` القيمة `(previous)`.
بعد استدعاء `ShowValuesAs`، استدعِ `PivotTable.CalculateData()` مرة أخرى لإعادة حساب محتوى الجدول المحوري وإعادة عرضه بالإعدادات المحدَّثة.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **المقالات ذات الصلة**
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/net/manage-value-fields/)
- [العمل مع تنسيقات عرض البيانات في DataField ضمن الجدول المحوري](/cells/ar/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/net/refresh-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}