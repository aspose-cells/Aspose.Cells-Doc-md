---
title: تنسيق جزء من جدول محوري
linktitle: تنسيق جزء من جدول محوري
description: تنسيق جزء من جدول محوري في Aspose.Cells for Go via C++ عبر تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea من خلال PivotTable.Format، مع تخزين التنسيقات في PivotTable.PivotFormats والحفاظ عليها عند تحديث الجدول المحوري.
keywords: Aspose.Cells for Go via C++, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /ar/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
`PivotTable.FormatAll` يطبق نمطًا واحدًا على كامل الجدول المحوري ويتم تغطيته في الصفحة الأم. لا يميز بين التسميات والقيم والإجماليات أو المناطق المحددة من التقرير.  
في الواقع، عادةً ما يحتاج جزء فقط من الجدول المحوري إلى التميز. تشمل الأهداف الشائعة التسميات التابعة لحقل صف واحد، خلايا القيم التي ينتجها حقل ما، صف الإجمالي الكلي، أو مستطيل عشوائي مثل صفوف العنصر الأولين.  
تطبيق نمط مباشرةً على خلايا ورقة العمل للجدول المحوري ليس مكافئًا. تخزن Excel تنسيقات الجداول المحورية كمناطق `PivotArea` دلالية بدلاً من سجلات أنماط الخلايا العادية. يبقى تنسيق منطقة PivotArea مرتبطًا بمنطقة مثل تسميات الحقل أو قيم البيانات، ويعاد حلها عندما يتم إعادة حساب أو تحديث أو توسيع الجدول المحوري. أما النمط المكتوب مباشرةً إلى خلية، فيخص تلك الخلية فقط ولا يتتبعه نموذج Pivot.  
`Aspose.Cells` يتيح عائلة التحميل الزائد الكاملة لـ `PivotTable.Format` بحيث يتوفر كلا النوعين من التنسيق:
- `Format(PivotArea, Style)` يربط نمطًا بمنطقة دلالية يتم بناؤها باستخدام `PivotArea.Select` أو `PivotArea.SelectField`.  
- `Format(CellArea, Style)` يربط نمطًا بمستطيل ورقة عمل داخل الجدول المحوري.  
- `Format(int row, int column, Style)` يستهدف خلية واحدة.  
- `FormatAll(Style)` ينسق كامل الجدول المحوري.  

## **تنسيق PivotArea**
تُعد طريقة العمل مع المنطقة الدلالية هي النهج الموصى به عندما يجب أن يتبع التمييز حقلًا أو منطقة من التقرير.
1. أنشئ كائن `PivotArea` باستخدام `NewPivotArea(pivotTable)`. يصف الكائن منطقة دلالية تتبع لهذا الجدول المحوري المحدد.  
2. حدد حقلًا وفق موقعه الصفري على المحور المطلوب باستخدام `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DataAndLabel` يختار كلًا من التسميات والبيانات الخاصة بالحقل.  
   - `PivotTableSelectionType.LabelOnly` يختار فقط تسميات الحقل.  
   - `PivotTableSelectionType.DataOnly` يختار فقط خلايا بيانات الحقل.  
3. حدد حقلًا حسب اسمه باستخدام `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. عندما يتم اختيار حقل صف بالاسم، تتحول المنطقة إلى خلايا القيم التي ينتجها عناصر ذلك الحقل.  
4. أنشئ كائن `Style` باستخدام `Workbook.CreateStyle()`، واضبط الخط واللون الأمامي ونمط الخلفية الصلبة، ثم مرر النمط إلى `PivotTable.Format(area, style)`.  
5. كل استدعاء لتحميل الزائد `PivotArea` يضيف إدخالًا واحدًا من نوع `PivotTableFormat` إلى `PivotTable.PivotFormats`.  
6. تُرسم التنسيقات المرتبطة بالحقل عندما يتم حساب بيانات Pivot. لذلك، استدعِ `PivotTable.CalculateData()` بعد تطبيق التنسيقات لتظهر الأنماط.  
المثال التالي يبني جدولًا محوريًا صغيرًا لمبيعات الفواكه، ينسق تسميات الصف `Fruit` باستخدام `PivotArea.Select` و`PivotTableSelectionType.LabelOnly`، ينسق خلايا القيم المنتجة من نفس الحقل باستخدام `PivotArea.SelectField`، ثم يعيد حساب الجدول المحوري بحيث تُرسم كلا النمطين.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	// Fruit sales data
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	a1Cell, _ := cells.Get_String("A1")
	a1Cell.PutValue_String("Fruit")
	b1Cell, _ := cells.Get_String("B1")
	b1Cell.PutValue_String("Year")
	c1Cell, _ := cells.Get_String("C1")
	c1Cell.PutValue_String("Amount")
	for i := 0; i < len(fruits); i++ {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), 0)
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), 1)
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), 2)
		amountCell.PutValue_Int(amounts[i])
	}
	// Pivot table with its top-left corner at E3 (row 2, column 4)
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Bold yellow fill on the row field's label cells
	labelStyle, _ := workbook.CreateStyle()
	labelFont, _ := labelStyle.GetFont()
	labelFont.SetIsBold(true)
	yellow, _ := Color_Yellow()
	labelStyle.SetForegroundColor(yellow)
	labelStyle.SetPattern(BackgroundType_Solid)
	labelArea, _ := NewPivotArea(pivotTable)
	labelArea.Select(PivotFieldType_Row, 0, PivotTableSelectionType_LabelOnly)
	pivotTable.Format_PivotArea_Style(labelArea, labelStyle)
	// Light green fill on the value cells the row field produces
	valueStyle, _ := workbook.CreateStyle()
	lightGreen, _ := Color_LightGreen()
	valueStyle.SetForegroundColor(lightGreen)
	valueStyle.SetPattern(BackgroundType_Solid)
	valueArea, _ := NewPivotArea(pivotTable)
	valueArea.SelectField_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.Format_PivotArea_Style(valueArea, valueStyle)
	// Field-anchored formats are painted when the data is calculated
	pivotTable.CalculateData()
	// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
	workbook.Save_String("FormatPivotArea.xlsx")
}
```

## **تنسيق CellArea في جدول محوري**
استخدم `PivotTable.Format(CellArea, Style)` عندما تكون المنطقة المطلوبة مستطيل ورقة عمل عادي بدلاً من منطقة Pivot دلالية.  
يتم وصف `CellArea` بقيم `StartRow` و`EndRow` و`StartColumn` و`EndColumn`، وتُحدد عبر الدوال المماثلة من نمط `Set_StartRow`. القيم هي إحداثيات ورقة عمل صفرية، وتحدد الإحداثيات النهائية الصف والعمود الأخيرين المشمولين بالمستطيل، لذا يغطي النطاق الخلايا من الموضع الابتدائي إلى الموضع النهائي شاملًا.  
على عكس التنسيق المرتبط بالحقل، يُطبق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء آخر لـ `CalculateData()` لظهور النمط.  
قد يحتوي مستطيل `CellArea` على خلايا تسميات وخلايا قيم معًا. القسم التالي يوضح كيف يمثل `Aspose.Cells` وExcel ذلك المستطيل داخليًا.  
المثال التالي ينسق المستطيل `E4:F5` من الجدول المحوري بنمط مائل وأزرق فاتح، ويحفظ المصنف دون أي عملية إعادة حساب إضافية.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int{100, 150, 120, 180, 90, 110}
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Year")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Amount")
	for i := range fruits {
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(0))
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(1))
		cell.PutValue_Int(int32(years[i]))
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(int32(amounts[i]))
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Highlight the first two fruit rows (the rectangle E4:F5)
	highlightStyle, _ := workbook.CreateStyle()
	font, _ := highlightStyle.GetFont()
	font.SetIsItalic(true)
	highlightColor, _ := Color_LightBlue()
	highlightStyle.SetForegroundColor(highlightColor)
	highlightStyle.SetPattern(BackgroundType_Solid)
	rectangle, _ := NewCellArea()
	rectangle.Set_StartRow(3)
	rectangle.Set_EndRow(4)
	rectangle.Set_StartColumn(4)
	rectangle.Set_EndColumn(5)
	pivotTable.Format_CellArea_Style(rectangle, highlightStyle)
	// E4:F5 is italic on light blue immediately, no recalculation needed
	workbook.Save_String("FormatPivotCellArea.xlsx")
}
```

## **كيفية ربط Pivot Areas و Cell Areas**
تخزن Excel تنسيقات الجداول المحورية كسجلات `pivotArea` بدلاً من سجلات أنماط الخلايا العادية. يستخدم `Aspose.Cells` نفس النموذج، لذا يُترجم طلب التنسيق إلى مناطق Pivot عند تسجيله.  
العلاقة بين `CellArea` التي يقدمها المستخدم ومناطق Pivot المخزنة داخليًا هي علاقة متعدد إلى متعدد في الاتجاهين.  
- قد ينتج `CellArea` واحد عدة مناطق Pivot. إذا غطى المستطيل كلًا من خلايا التسميات والقيم، يتم تفكيكه إلى قواعد تسميات وبيانات منفصلة، لأن نموذج Pivot يعالج تنسيق التسميات وتنسيق البيانات بصورة مستقلة.  
- قد يُحل منطقة Pivot واحدة إلى عدة كائنات `CellArea` منفصلة. يمكن لمنطقة دلالية مثل صف الإجمالي الكلي أو حقل غير متتالي العناصر أن يغطي مستطيلات متعددة. لهذا السبب تُرجع `PivotArea.GetCellAreas()` مجموعة بدلاً من مستطيل واحد.  
كل عملية تنسيق تُجرى عبر `PivotTable.Format` تُسجل في `PivotTable.PivotFormats`. كل إدخال من نوع `PivotTableFormat` يُظهر الـ `PivotArea` المرتبط والنمط `Style` المطبق عليه. يضيف التحميل الزائد `PivotArea` إدخالًا واحدًا بالضبط لكل استدعاء، بينما يمكن أن يضيف `CellArea` يحتوي على مناطق دلالية مختلفة عدة إدخالات.  
للتفريق بين المناطق المخزنة، يُظهر كل `PivotArea` علمي `OnlyLabel` و`OnlyData`. المثال أدناه ينسق مستطيلًا واحدًا يغطي كلًا من التسميات والقيم، يطلع على `PivotTable.PivotFormats`، ويطبع إحداثيات `CellArea` التي تُحل كل منطقة Pivot مخزنة إليها.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Year")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Amount")
	for i := range fruits {
		cell, _ = cells.Get_Int_Int(int32(i+1), 0)
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), 1)
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), 2)
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	highlightStyle, _ := workbook.CreateStyle()
	font, _ := highlightStyle.GetFont()
	font.SetIsItalic(true)
	highlightColor, _ := Color_LightBlue()
	highlightStyle.SetForegroundColor(highlightColor)
	highlightStyle.SetPattern(BackgroundType_Solid)
	// ONE rectangle in...
	rectangle, _ := NewCellArea()
	rectangle.Set_StartRow(3)
	rectangle.Set_EndRow(4)
	rectangle.Set_StartColumn(4)
	rectangle.Set_EndColumn(5)
	pivotTable.Format_CellArea_Style(rectangle, highlightStyle)
	// ...TWO semantic pivot areas out: the label part and the data part are stored separately
	pivotFormats, _ := pivotTable.GetPivotFormats()
	formatCount, _ := pivotFormats.GetCount()
	fmt.Printf("Stored formats: %d\n", formatCount)
	for i := int32(0); i < int32(formatCount); i++ {
		pivotFormat, _ := pivotFormats.Get(i)
		storedArea, _ := pivotFormat.GetPivotArea()
		onlyLabel, _ := storedArea.GetOnlyLabel()
		onlyData, _ := storedArea.GetOnlyData()
		onlyLabelText := "False"
		if onlyLabel {
			onlyLabelText = "True"
		}
		onlyDataText := "False"
		if onlyData {
			onlyDataText = "True"
		}
		fmt.Printf("Format %d: OnlyLabel=%s, OnlyData=%s\n", i, onlyLabelText, onlyDataText)
		resolvedAreas, _ := storedArea.GetCellAreas()
		for _, resolved := range resolvedAreas {
			startRow, _ := resolved.Get_StartRow()
			endRow, _ := resolved.Get_EndRow()
			startColumn, _ := resolved.Get_StartColumn()
			endColumn, _ := resolved.Get_EndColumn()
			fmt.Printf(
				"    rows %d-%d, columns %d-%d\n",
				startRow+1,
				endRow+1,
				startColumn+1,
				endColumn+1,
			)
		}
	}
	// This prints:
	// Stored formats: 2
	// Format 0: OnlyLabel=True, OnlyData=False
	//     rows 4-5, columns 5-5        (E4:E5, the label part)
	// Format 1: OnlyLabel=False, OnlyData=True
	//     rows 4-5, columns 6-6        (F4:F5, the data part)
	workbook.Save_String("FormatPivotAreasMap.xlsx")
}
```

{{% alert color="primary" %}}
نظرًا لأن التنسيقات مخزنة كـ pivot areas بدلاً من أنماط خلايا عادية، فإنها تبقى بعد إعادة الحساب أو التحديث. عندما يُُحدَّث الجدول المحوري باستخدام `PivotTable.RefreshData`، أو يُعاد حسابه بـ `CalculateData`، أو يُحفظ ثم يُعاد تحميله، كل منطقة Pivot مخزنة تُعيد حل موقعها الحالي وتُطبق النمط مرة أخرى.
{{% /alert %}}

استخدم `PivotArea` التي تم بناؤها باستخدام `Select` أو `SelectField` عندما يجب أن يبقى التمييز مرتبطًا بحقل أو منطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عند كون تنسيق مستطيل ثابت في تخطيط الجدول المحوري الحالي كافيًا. التحميل الزائد `Format(int row, int column, Style)` يستهدف خلية فردية. استخدم `FormatAll`، كما هو مغطى في الصفحة الأم، عندما يراد إعادة تنسيق كامل الجدول المحوري دفعة واحدة.

{{< app/cells/assistant language="go" >}}