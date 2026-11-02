---
title: عرض القيم كـ في جدول محوري
linktitle: عرض القيم كـ في جدول محوري
description: عرض قيم حقل البيانات في جدول محوري كنسبة مئوية من الإجمالي، أو فرق عن عنصر أساسي، مجموع متراكم، رتبة، وأكثر باستخدام Aspose.Cells for Go via C++.
keywords: Aspose.Cells for Go via C++, جدول محوري, عرض القيم كـ, تنسيق عرض البيانات, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /ar/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
عادةً ما يجمع جدول محوري كل حقل بيانات باستخدام دالة تجميع مثل `Sum` أو `Count`. تستبدل ميزة **عرض القيم كـ** في Excel كل نتيجة معروضة بحساب ثانوي مشتق من ذلك التجميع—على سبيل المثال، نسبة مئوية من الإجمالي الكلي، مجموع متراكم، فرق عن عنصر أساسي مختار، أو رتبة—ما يسمح بإجراء تحليلات مقارنة دون الحاجة إلى صيغ مساعدة أو أعمدة محسوبة. تشمل الاستخدامات الشائعة تحليل حصة الإجمالي، بما في ذلك النسب المئوية للصف، العمود، أو الإجمالي الكلي؛ تقارير متراكمية باستخدام مجموع متراكم في حقل الفترة؛ تحليل الفروقات مقابل عنصر مرجعي باستخدام الفرق أو الفرق النسبي من عنصر أساسي؛ وترتيب القيم من الأصغر إلى الأكبر أو العكس.  
في Aspose.Cells for Go via C++، يحدد `PivotFieldDataDisplayFormat` الحساب الثانوي. تُعيد الدالة `PivotField.GetShowValuesSetting()` كائنًا من نوع `PivotShowValuesSetting`، حيث تُكوّن طرق `SetCalculationType` و `SetBaseFieldIndex` و `SetBaseItemPositionType` و `SetBaseItemIndex` السلوك؛ وتطبيق الطريقة المريحة `PivotField.ShowValuesAs(...)` يضع الإعدادات الأربعة في استدعاء واحد. يُطبق هذا الإعداد على حقل بيانات أو قيمة يُستخرج من `PivotTable.GetDataFields()`.

## **أعضاء تعداد PivotFieldDataDisplayFormat**
يحتفظ حقل البيانات بدالة التجميع الخاصة به، مثل Sum أو Count، بينما يقوم عرض القيم كـ بتحويل طريقة عرض القيمة المجمعة فقط. إلى جانب كتابة قيم `PivotShowValuesSetting` يدويًا (انظر القسم الأخير)، تُطبق طريقة المريحة ذات الاستدعاء الواحد نفس الإعدادات:

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| المعامل | المعنى | متى يكون مطلوبًا |
| --- | --- | --- |
| `displayFormat` | الحساب الثانوي من نوع `PivotFieldDataDisplayFormat` الذي يُطبق. | دائمًا. |
| `baseField` | الفهرس الصفري للحقول الأساسية ضمن الحقول الأساسية للجدول المحوري (على سبيل المثال، فهرس حقل الصف الذي ينتمي إليه العنصر الأساسي). | فقط تنسيقات المرجع الستة أدناه (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItemPositionType` | طريقة اختيار العنصر الأساسي بالنسبة للعنصر الحالي: `PivotItemPositionType.Previous`، `.Next`، أو `.Custom`. | فقط تنسيقات العنصر الأساسي الثلاثة (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`)؛ يتم تجاهلها في جميع التنسيقات الأخرى. |
| `baseItem` | الفهرس الصفري للعنصر الأساسي. | فقط عندما تكون `baseItemPositionType` هي `Custom` (يتم اختيار الفهرس الدقيق للعنصر الأساسي)؛ يتم تجاهله عند `Previous` / `Next` وفي كل التنسيقات غير القائمة على العنصر الأساسي — يُمرَّر `0`. |

| نوع الحساب | السلوك | معلمات العنصر الأساسي |
| --- | --- | --- |
| `Normal` | لا حساب ثانوي؛ تُعرض القيمة المجمعة كما هي (الافتراضية). | — |
| `DifferenceFrom` | تُظهر القيمة كفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageOf` | تُظهر القيمة كنسبة مئوية من قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `PercentageDifferenceFrom` | تُظهر القيمة كنسبة مئوية للفرق عن قيمة عنصر أساسي في حقل أساسي. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` فقط مع `Custom`) |
| `RunningTotalIn` | تُظهر القيمة كمجموع متراكم للعناصر المتتالية لحقل أساسي. | `baseField` (الحقل الذي يُحدد ترتيب العناصر لتجميع القيمة) |
| `PercentageOfRow` | تُظهر القيمة كنسبة مئوية من إجمالي الصف. | — |
| `PercentageOfColumn` | تُظهر القيمة كنسبة مئوية من إجمالي العمود. | — |
| `PercentageOfTotal` | تُظهر القيمة كنسبة مئوية من الإجمالي الكلي. | — |
| `Index` | تُظهر القيمة باستخدام صيغة الفهرس في Excel ((القيمة * الإجمالي الكلي) / (إجمالي الصف * إجمالي العمود)). | — |
| `PercentageOfParentRowTotal` | تُظهر القيمة كنسبة مئوية من إجمالي صف الأب (للحقول المتداخلة). | — |
| `PercentageOfParentColumnTotal` | تُظهر القيمة كنسبة مئوية من إجمالي عمود الأب (للحقول المتداخلة). | — |
| `PercentageOfParentTotal` | تُظهر القيمة كنسبة مئوية من إجمالي الأب. | `baseField` (الحقل الأصل المرجعي) |
| `PercentageOfRunningTotalIn` | تُظهر القيمة كنسبة مئوية لمجموع متراكم في حقل أساسي. | `baseField` (حقل التجميع) |
| `RankSmallestToLargest` | يرتب القيمة من الأصغر (1) إلى الأكبر. | — |
| `RankLargestToSmallest` | يرتب القيمة من الأكبر (1) إلى الأصغر. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` تكتب القيم `PivotShowValuesSetting` (`CalculationType`، `BaseFieldIndex`، `BaseItemPositionType`، `BaseItemIndex`) — الطريقة وكائن الإعدادات طريقتان لتكوين الحالة نفسها، متماثلتين مع محددات الحقل الأساسي والعنصر الأساسي في مربع حوار **عرض القيم كـ** في Excel.
{{% /alert %}}

## **عرض القيم كنسبة مئوية من الإجمالي**
استدعِ طريقة `PivotField.ShowValuesAs` مع `PivotFieldDataDisplayFormat.PercentageOfTotal` لتحويل كل خلية حقل بيانات، بما في ذلك الإجمالي الكلي، إلى حصتها من الإجمالي الكلي. لذلك تُعرض الأرقام كنسب من مجموعة النتائج الكاملة. هذا التنسيق يقيس كل قيمة مقابل الإجمالي الكلي فقط، لذا لا يحتاج إلى حقل أساسي أو عنصر أساسي — الوسائط الأخيرة (`0`، `PivotItemPositionType.Previous`، `0`) هي مجرد نواقل placeholder يتجاهلها التنسيق كما هو موضح في جدول المعاملات أعلاه.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load or create a workbook with source data
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	dataSheet, _ := worksheets.Get_Int(0)
	cells, _ := dataSheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"}
	amounts := []int{10, 20, 30, 40, 50, 60}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		amountCell.PutValue_Int(int32(amounts[i]))
	}
	// Add a pivot table on a new worksheet
	pivotSheetIndex, _ := worksheets.Add()
	pivotSheet, _ := worksheets.Get_Int(pivotSheetIndex)
	pivotTables, _ := pivotSheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=Sheet1!A1:B7", 2, 2)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Show the Amount data field as a percentage of the grand total with the
	// one-call method; PercentageOfTotal takes no base item, so the trailing
	// base arguments (0, Previous, 0) are placeholders the format ignores
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_PercentageOfTotal,
		int32(0),
		PivotItemPositionType_Previous,
		int32(0),
	)
	pivotTable.CalculateData()
	// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
	workbook.Save_String("ShowValuesAsPercentageOfTotal.xlsx")
}
```

## **الحصول على وتكوين PivotField.ShowValuesSetting**
اقرأ التكوين الحالي عبر `PivotField.GetShowValuesSetting()`؛ تُعيد الدالة كائنًا من نوع `PivotShowValuesSetting` يحتوي على أربع قيم توضح حساب **عرض القيم كـ** النشط. لتغيير التكوين، استدعِ طريقة `PivotField.ShowValuesAs` — فهي تكتب جميع الإعدادات الأربعة في استدعاء واحد، لذا لن تحتاج إلى ضبط القيم واحدةً تلو الأخرى.  
يُظهر كائن `PivotShowValuesSetting` القيم الأربعة التي تُكتبها `ShowValuesAs`:
- `GetCalculationType()` / `SetCalculationType()` تحددان الحساب الثانوي من نوع `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` يحددان الفهرس الصفري للحقل الأساسي ضمن حقول الجدول المحوري. يُستخدم في تنسيقات المرجع.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` تحددان موضع العنصر الأساسي بالنسبة للعنصر الحالي وتقبل القيم `PivotItemPositionType.Next`، `PivotItemPositionType.Previous`، أو `PivotItemPositionType.Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` يحددان الفهرس الصفري للعنصر الأساسي ويُستخدمان عندما يكون نوع الموضع هو `Custom`.
بعد استدعاء `ShowValuesAs`، استدعِ `PivotTable.CalculateData()` مرةً أخرى لتُعيد حساب جسم الجدول المحوري وإعادة عرضه وفق الإعدادات الجديدة.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("ShowValuesAsPercentageOfTotal.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	// Read the current show-values settings
	settings, _ := dataField.GetShowValuesSetting()
	calculationType, _ := settings.GetCalculationType()
	baseFieldIndex, _ := settings.GetBaseFieldIndex()
	baseItemPositionType, _ := settings.GetBaseItemPositionType()
	baseItemIndex, _ := settings.GetBaseItemIndex()
	fmt.Println("CalculationType:", calculationType)
	fmt.Println("BaseFieldIndex:", baseFieldIndex)
	fmt.Println("BaseItemPositionType:", baseItemPositionType)
	fmt.Println("BaseItemIndex:", baseItemIndex)
	// Switch to a base-item calculation with the one-call method: difference
	// from the value of the previous item in the row field
	rowFields, _ := pivotTable.GetRowFields()
	rowField, _ := rowFields.Get_Int(0)
	baseIndex, _ := rowField.GetBaseIndex()
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_DifferenceFrom,
		baseIndex,
		PivotItemPositionType_Previous,
		0,
	)
	pivotTable.CalculateData()
	// Note: the percentage number format saved by the previous example still
	// clings to the data field cells; the underlying values are now differences
	// Re-read the applied configuration
	updatedSettings, _ := dataField.GetShowValuesSetting()
	updatedCalculationType, _ := updatedSettings.GetCalculationType()
	fmt.Println("CalculationType now:", updatedCalculationType)
	workbook.Save_String("ShowValuesAsDifferenceFrom.xlsx")
}
```

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري في جدول محوري](/cells/ar/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [أفضل 10 عرض أو تصفية في جدول محوري](/cells/ar/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [تحديث Slicer](/cells/ar/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}