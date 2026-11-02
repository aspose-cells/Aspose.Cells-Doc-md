---
title: عرض أو تصفية أعلى 10 في الجدول المحوري
linktitle: عرض أو تصفية أعلى 10 في الجدول المحوري
description: تعلّم كيفية عرض أفضل 10 عناصر أو أسوأ 10 عناصر فقط من حقل في الجدول المحوري في Aspose.Cells for Go via C++. تتناول هذه المقالة إعدادات العرض التلقائي AutoShow في Excel 97-2003 (SetIsAutoShow والدوال المرتبطة بها)، وقراءة هذه الخيارات، وتصفية أعلى 10 في Excel 2007-365 عبر FilterTop10.
keywords: Aspose.Cells, Go via C++, جدول محوري, أعلى 10, العرض التلقائي, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /ar/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
قد يصعب قراءة جدول محوري يسرد جميع عناصر حقل صف إذا كان الحقل يحتوي على عشرات العناصر. لا يعرض تقرير أعلى 10 سوى العناصر الأعلى أو الأدنى تصنيفًا، وهو ما تحتاج إليه تقارير الترتيب تحديدًا — «أفضل 5 منتجات حسب الإيرادات» أو «أسفل 3 مناطق حسب عدد المبيعات». تدعم Aspose.Cells آليتين لهذا الغرض، وتتطابقان مع جيلين من إصدارات Microsoft Excel.
- **العرض التلقائي `AutoShow` في Excel 97-2003** — دوال التعيين الأربعة الموجودة في `PivotField`، وهي `SetIsAutoShow` و`SetIsAscendShow` و`SetAutoShowCount` و`SetAutoShowField`. هذا هو الإعداد الكلاسيكي «اعرض أعلى N عناصر/أسفل N عناصر»، ويُخزَّن مباشرةً في حقل الجدول المحوري. يعمل في جميع إصدارات Excel، القديمة والجديدة، لأنه جزء من تنسيق الجداول المحورية الأصلي.
- **تصفية أعلى 10 في Excel 2007-365** — طريقة `PivotField.FilterTop10()`. هذا هو مرشح القيم الحديث الموجود ضمن مرشحات القيم في قائمة الحقل. يُخزَّن في صورة كائن `PivotFilter` مرتبط بالحقل، ويوفر ترتيبًا قائمًا على عدد العناصر أو النسبة المئوية.

## **عرض أعلى 10 في Excel 97-2003 (`AutoShow`)**
يُهيأ العرض التلقائي `AutoShow` الكلاسيكي بأربعة استدعاءات لدوال التعيين في `PivotField`:
- `SetIsAutoShow(bool)` — يتيح إعداد العرض التلقائي `AutoShow` على الحقل أو يعطله.
- `SetIsAscendShow(bool)` — قيمة `false` تحتفظ بالعناصر الأعلى تصنيفًا (الأعلى)، بينما قيمة `true` تحتفظ بالعناصر الأدنى (الأسفل).
- `SetAutoShowCount(int32)` — عدد العناصر التي يجب الاحتفاظ بها، مثل 10 لتقرير أعلى 10 كلاسيكي.
- `SetAutoShowField(int32)` — الفهرس الذي يبدأ من الصفر لحقل **البيانات** الذي تُرتَّب العناصر وفق قيمه. مرِّر -1 لترتيب العناصر حسب الحقل نفسه.
يمكن أن يعتمد الترتيب على حقل قيمة أو على الحقل نفسه. وهناك خياران طبيعيان، يوضحهما المثالان أدناه.

### **الترتيب حسب حقل قيمة**
رتّب عناصر حقل الصف باستخدام حقل قيمة عادي مثل «مجموع المبيعات». ينشئ المثال التالي جدولًا محوريًا بحقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أعلى رياضتين حسب المبيعات. وتكون قيمة `rankBy` هي 0 لأن «مجموع المبيعات» هو حقل البيانات الموجود عند الفهرس 0.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// عرض أفضل عنصرين مرتبين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **الترتيب حسب الحقل نفسه**
يمكن أيضًا استخدام الحقل نفسه لترتيب عناصره — مرِّر -1 إلى `SetAutoShowField`. لا يلزم وجود حقل بيانات إضافي لهذا الخيار؛ يكفي أن يكون الحقل في منطقة الصفوف (أو الأعمدة). يعرض المثال التالي أدنى 3 رياضات مرتبة حسب الحقل نفسه. عند حفظ هذا الإعداد، لا تُدرج سمة `rankBy` في XML للجدول المحوري لأن -1 هي القيمة الافتراضية للتنسيق، وتعيد `GetAutoShowField()` إرجاع -1.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// إظهار آخر 3 عناصر مرتبة حسب الحقل نفسه (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **قراءة خيارات العرض التلقائي `AutoShow` الحالية**
تتيح دوال القراءة في `PivotField`، وهي `IsAutoShow()` و`IsAscendShow()` و`GetAutoShowCount()` و`GetAutoShowField()`، الوصول إلى خيارات العرض التلقائي `AutoShow` المخزنة حاليًا في الحقل. استخدمها لفحص طريقة عرض العناصر في مصنف موجود أو في جدول محوري قمت بتهيئته للتو، بما في ذلك المصنفات المحمّلة من الملفات.

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
	isAutoShow, _ := sportField.IsAutoShow()
	isAscendShow, _ := sportField.IsAscendShow()
	autoShowCount, _ := sportField.GetAutoShowCount()
	autoShowField, _ := sportField.GetAutoShowField()
	direction := "Bottom"
	if !isAscendShow {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", autoShowField)
}
```

تطابق دوال القراءة الأربع سمات العرض التلقائي الكلاسيكية المكتوبة في XML للجدول المحوري (`autoShow` و`topAutoShow` و`itemPageCount` و`rankBy`)، لذا تكون القيم المقروءة هي القيم التي ستدعمها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- بعد تغيير أي من دوال التعيين الخاصة بـ `AutoShow`، استدعِ `PivotTable.CalculateData()` مجددًا — لا تسري الإعدادات إلا في التخطيط المعروض عند إجراء عملية إعادة الحساب التالية.
- تعمل إعدادات العرض التلقائي `AutoShow` مع حقول الصفوف والأعمدة. لا يمكن ترتيب الحقل الموجود في منطقة الصفحات (التصفية) فقط بهذه الطريقة، لأن عناصره لا تظهر في جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: تصفية أعلى 10 (`FilterTop10`)**
تتيح إصدارات Excel الحديثة تطبيق مرشح أعلى 10 ضمن قائمة الحقل (مرشحات القيم، أعلى 10...). يمثل Aspose.Cells هذا الخيار من خلال طريقة `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`، التي تُعيد كائن `PivotFilter` الذي تم إنشاؤه:
- `valueFieldIndex` — الفهرس الذي يبدأ من الصفر لحقل البيانات الذي تُرتَّب العناصر وفق قيمه المجمّعة.
- `type` — المعنى الذي يحمله `itemCount`. تحافظ `PivotFilterType.Count` على عدد ثابت من العناصر (خيار «العناصر» في مربع الحوار). وتحافظ `PivotFilterType.Percent` على نسبة مئوية من العناصر، لذا تكون قيمة `itemCount` هي النسبة نفسها — أي أن القيمة 30 تحتفظ بأعلى 30 بالمئة. أما `PivotFilterType.Sum` فيرتب العناصر بحسب التغطية التراكمية للقيم.
- `isTop` — قيمة `true` للأعلى، وقيمة `false` للأسفل.
- `itemCount` — قيمة `N` في «أعلى N»، وتعتمد وحدتها على `type`.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// تصفية أعلى 10 — احتفظ بأعلى عنصرين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// بدلاً من ذلك، لعامل تصفية قائم على النسبة، احتفظ بأفضل 30٪ من العناصر:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
تعد إعدادات `AutoShow` و`FilterTop10` ميزتين منفصلتين. تكتب `AutoShow` سمة `autoShow` الكلاسيكية على حقل الجدول المحوري، وتحترمها جميع إصدارات Excel منذ Excel 97. أما `FilterTop10` فيكتب إدخال `PivotFilter` حديثًا يتطلب Excel 2007 أو إصدارًا أحدث. عند فتح مصنف في إصدار أقدم من Excel، يعود الجدول المحوري الذي يستخدم المرشح الحديث إلى عرض جميع العناصر. للمستندات التي يجب أن تُعالَج ذهابًا وإيابًا بواسطة أدوات قديمة، فضِّل دوال التعيين الخاصة بـ `AutoShow`؛ أما للمصنفات الحديثة، ففضِّل `FilterTop10` لأنه يتكامل مع مرشحات القيم الأخرى.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري داخل الجدول المحوري](/cells/ar/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}