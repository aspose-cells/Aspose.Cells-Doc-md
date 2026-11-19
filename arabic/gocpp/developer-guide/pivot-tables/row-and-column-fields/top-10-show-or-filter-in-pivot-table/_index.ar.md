---
title: أعلى 10 إظهار أو تصفية في جدول محوري
linktitle: أعلى 10 إظهار أو تصفية في جدول محوري
description: تعلم كيفية إظهار العناصر الأعلى أو الأدنى ترتيبًا في حقل محوري في Aspose.Cells for Go via C++. تغطي هذه المقالة طريقة Excel 97‑2003 Top10AutoShow، قراءة الخيارات باستخدام Top10AutoShowSettings، وفلتر Excel 2007‑365 أعلى 10 عبر FilterTop10.
keywords: Aspose.Cells, Go via C++, جدول محوري, أعلى 10, العرض التلقائي, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /ar/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون جدولًا محوريًا يعرض كل عنصر من حقل الصف صعب القراءة عندما يحتوي الحقل على عشرات الأعضاء. تقرير أعلى 10 يحتفظ فقط بأعلى أو أدنى العناصر ترتيبًا، وهو ما تحتاجه تقارير الترتيب — “أعلى 5 منتجات حسب الإيرادات” أو “أدنى 3 مناطق حسب عدد المبيعات”. يدعم Aspose.Cells آليتين لهذه الميزة، وهما تمثيلان لجيلين من Microsoft Excel.
- **Excel 97‑2003 AutoShow** — طريقة `PivotField.Top10AutoShow()`. هذه هي الإعداد الكلاسيكي “إظهار أعلى/أدنى N عناصر” المخزن مباشرة على حقل Pivot. يعمل في كل إصدارات Excel، القديمة والجديدة، لأنه جزء من تنسيق جدول Pivot الأصلي.
- **Excel 2007‑365 Top 10 Filter** — طريقة `PivotField.FilterTop10()`. هذا هو مرشح القيمة أعلى 10 الحديث الموجود ضمن قائمة مرشحات القيمة في حقل القائمة. يُخزن ككائن `PivotFilter` مرتبط بالحقل ويوفر ترتيبات قائمة حسب عدد العناصر أو النسبة المئوية.

## **إظهار أعلى 10 في Excel 97‑2003 (Top10AutoShow)**
يتم تكوين AutoShow الكلاسيكي باستدعاء واحد للطريقة `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)`:
- `isAutoShow` — يفعّل أو يعطل إعداد AutoShow على الحقل.
- `isTop` — `true` يبقي العناصر ذات الترتيب الأعلى (Top)، `false` يبقي الأقل (Bottom).
- `count` — عدد العناصر التي سيتم الاحتفاظ بها، على سبيل المثال 10 لتقرير أعلى 10 كلاسيكي.
- `rankBy` — الفهرس الصفري **لحقل البيانات** الذي تُرتّب قيمه العناصر. مرّر -1 لترتيب العناصر حسب الحقل نفسه.

يمكن أن يتم الترتيب بناءً على حقل قيمة أو حسب الحقل نفسه. يوجد نوعان طبيعيان، موضحان أدناه.

### **الترتيب حسب حقل القيمة**
ترتيب عناصر حقل الصف حسب حقل قيمة عادي مثل مجموع المبيعات. المثال التالي يبني جدولًا محوريًا بحقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يُظهر أعلى 2 رياضات حسب المبيعات. `rankBy` هو 0 لأن “Sum of Sales” هو حقل البيانات عند الفهرس 0.

```go
package main
import (
	"strconv"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String("Qtr" + strconv.Itoa(int(quarter)))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
	sportField.Top10AutoShow(true, true, 2, 0)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **الترتيب حسب الحقل نفسه**
يمكن أيضًا ترتيب الحقل بنفسه — مرّر -1 إلى `rankBy`. لا يحتاج هذا النوع إلى حقل بيانات إضافي؛ يكفي أن يكون الحقل موجودًا في منطقة الصف (أو العمود). المثال التالي يُظهر أدنى 3 رياضات مرتبة حسب الحقل نفسه. عند حفظ هذا الإعداد، يُحذف سمة `rankBy` من XML جدول Pivot لأن -1 هو القيمة الافتراضية للتنسيق، وتُعيد `GetRankBy()` القيمة -1.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Show the bottom 3 items ranked by the field itself (rankBy = -1)
	sportField.Top10AutoShow(true, false, 3, -1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **قراءة خيارات AutoShow الحالية**
تُعيد الطريقة `PivotField.GetTop10AutoShowSettings()` كائن `PivotFieldTop10AutoShowSettings` يُظهر خيارات AutoShow المخزَّنة حالياً على الحقل. استخدمه لتفحص كيف سيعرض مصنف موجود مسبقًا، أو جدول Pivot قمت بتهيئته لتوًّا، العناصر الخاصة به — بما في ذلك المصنفات المحمَّلة من ملف.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("output-top10-by-value-field.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	settings, _ := sportField.GetTop10AutoShowSettings()
	isAutoShow, _ := settings.IsAutoShow()
	isTop, _ := settings.IsTop()
	autoShowCount, _ := settings.GetAutoShowCount()
	rankBy, _ := settings.GetRankBy()
	direction := "Bottom"
	if isTop {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", rankBy)
}
```

تُطابق الإعدادات سمات AutoShow الكلاسيكية المكتوبة في XML جدول Pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`)، لذا القيم المرتجعة هي القيم التي سيُحترمها كل إصدار من Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- بعد استدعاء `Top10AutoShow()`، استدعِ `PivotTable.CalculateData()` مرة أخرى — الإعدادات تُطبق فقط في التخطيط المرسوم عند إعادة الحساب التالية.
- تعمل إعدادات AutoShow مع حقول الصف والعمود. لا يمكن ترتيب حقل موجود فقط في منطقة الصفحات (الفلتر) بهذه الطريقة لأن عناصره لا تُعرض في جسم جدول Pivot.
{{% /alert %}}

## **Excel 2007‑365: فلتر أعلى 10 (FilterTop10)**
تُظهر إصدارات Excel الحديثة فلتر أعلى 10 كمرشح قيمة في قائمة الحقل (Value Filters, Top 10…). يُنمذج Aspose.Cells ذلك بطريقة `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` التي تُعيد كائن `PivotFilter` المُنشأ:
- `valueFieldIndex` — الفهرس الصفري لحقل البيانات الذي تُرتّب قيمه المُجمَّعة للعناصر.
- `type` — ما يعنيه `itemCount`. `PivotFilterType.Count` يحتفظ بعدد ثابت من العناصر (خيار Items في الحوار). `PivotFilterType.Percent` يحتفظ بنسبة مئوية من العناصر، لذا `itemCount` هو النسبة نفسها — 30 يعني أعلى 30 ٪. `PivotFilterType.Sum` يُرتّب حسب تغطية القيمة التراكمية.
- `isTop` — `true` لأعلى، `false` لأدنى.
- `itemCount` — الـ N في أعلى N؛ وحدته تعتمد على `type`.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	wss, _ := workbook.GetWorksheets()
	worksheet, _ := wss.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// For a percentage-based filter instead, keep the top 30 percent of the items:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
إعدادات AutoShow و`FilterTop10` ميزتان منفصلتان. يكتب AutoShow سمة `autoShow` الكلاسيكية على حقل Pivot ويُعترف بها جميع إصدارات Excel منذ Excel 97. يكتب `FilterTop10` إدخال `PivotFilter` حديث، يتطلب Excel 2007 أو أحدث. عند فتح مصنف في إصدار Excel أسبق، يُظهر جدول Pivot يستخدم الفلتر الحديث جميع العناصر. للمستندات التي يجب أن تمر عبر أدوات قديمة، يُفضَّل `Top10AutoShow`؛ للمصنفات الحديثة، يُفضَّل `FilterTop10` لأنه يتناغم مع مرشحات القيمة الأخرى.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول Pivot في جدول محوري](/cells/ar/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}