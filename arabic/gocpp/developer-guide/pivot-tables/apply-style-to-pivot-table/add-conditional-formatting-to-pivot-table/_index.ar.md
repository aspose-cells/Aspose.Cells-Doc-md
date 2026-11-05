---
title: إضافة تنسيق شرطي إلى جدول محوري
linktitle: إضافة تنسيق شرطي إلى جدول محوري
description: إضافة تنسيق شرطي إلى جدول محوري في Aspose.Cells عبر Go باستخدام C++ ، ربط قاعدة بمنطقة البيانات باستخدام ApplyTo ونطاق PivotConditionFormatScopeType ، أو تعريف الهدف باستخدام AddCellArea و PivotAreas ، ثم إرفاق القواعد والأنماط عبر FormatConditions.AddCondition
keywords: Aspose.Cells, جدول محوري, تنسيق شرطي, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /ar/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
الأنماط الموضحة في الصفحة الأصلية والصفحة الشقيقة هي أنماط ثابتة – يتم رسم منطقة `PivotArea` أو `CellArea` مرة واحدة وتحتفظ بتنسيقها بغض النظر عن القيم. التنسيق الشرطي هو المكمل القائم على القواعد – يبرز كل مبلغ فوق 200، يظلل الخمسين بالمئة الوسطى، أو يُشير إلى العناصر ذات الترتيب الأدنى – ويتبع التمييز القيم كلما تم إعادة حساب أو تحديث الجدول المحوري.

{{% alert color="primary" %}}
لا تقم باستدعاء `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` أو `FormatConditionCollection.AddArea(CellArea)` على كائن `FormatConditions` لتنسيق شرطي محوري. هاتان الدالتان المتجاوزتان موروثتان من API التنسيق الشرطي للورقة العادية ولا تعملان مع الجداول المحورية – لا يتم تحويل منطقة الخلية إلى منطقة محورية، لذا يتم تجاهل الطلب بصمت. احرص دائمًا على تعريف المنطقة على `PivotConditionalFormat` نفسه (`ApplyTo`، `AddCellArea` أو `PivotAreas`) وأضف القاعدة باستخدام أحد إصدارات `AddCondition`.
{{% /alert %}}

## **تطبيق قاعدة بنطاق (طريقة واجهة مستخدم Excel)**
الطريقة الأولى تضع القاعدة كما تفعل واجهة مستخدم Excel. تُسمى خلية الجدول المحوري بإحداثيات ورقة عمل ذات أساس صفري، ويخبر نطاق `PivotConditionFormatScopeType` Aspose.Cells إلى أي مدى يجب أن تمتد القاعدة من تلك الخلية:
- `PivotConditionFormatScopeType.Data` – جميع خلايا القيم التي ينتجها الجدول المحوري، بما في ذلك الإجماليات الكلية.
- `PivotConditionFormatScopeType.Field` – خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، باستثناء الإجماليات الكلية. يجب أن تكون الخلية خلية حقل مثل تسمية حقل الصف؛ تمرير خلية قيمة يسبب استثناءً.
- `PivotConditionFormatScopeType.Selection` – فقط خلايا القيم عند التقاطع التي تختارها الخلية، عادةً خلية قيمة واحدة.
المثال أدناه ينشئ جدولًا محوريًا لمبيعات الفواكه يقع ركنه العلوي الأيسر في الخلية E3، يربط تنسيقًا شرطيًا بالخلية F4 (الصف 3، العمود 5) باستخدام نطاق `Data`، ويُبرز كل مبلغ أكبر من 200 بخط عريض أبيض على خلفية حمراء. باستخدام القيم Apple 220، Banana 330، Cherry 200، والإجمالي الكلي 750، تقوم القاعدة بتلوين الخلايا F4 وF5 وF7 – المنطقة المحددة هي العمود الكامل للبيانات F4:F7، وتُضيء فقط الخلايا التي تتجاوز قيمتها القاعدة.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	a1, _ := cells.Get_String("A1")
	a1.PutValue_String("Fruit")
	b1, _ := cells.Get_String("B1")
	b1.PutValue_String("Year")
	c1, _ := cells.Get_String("C1")
	c1.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(2))
		amountCell.PutValue_Int(amounts[i])
	}
	// Pivot table with its top-left corner at E3
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	format.ApplyTo(int32(3), int32(5), PivotConditionFormatScopeType_Data)
	// Rule - highlight amounts greater than 200
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_GreaterThan,
		"200",
		"",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsBold(true)
	white, _ := Color_FromArgb(int32(-1))
	red, _ := Color_FromArgb(int32(-65536))
	font.SetColor(white)
	style.SetForegroundColor(red)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatData.xlsx")
}
```

ربط القاعدة نفسها بملصق حقل الصف E4 (الصف 3، العمود 4) باستخدام نطاق `Field` يحدِّد المنطقة إلى F4:F6 بدلاً من ذلك – أي نفس عمود البيانات دون صف الإجمالي الكلي – لأن النطاق الآن يصف حقل `Fruit` بدلاً من منطقة القيم بأكملها. النطاق `Selection` المرتبط بالخلية F4 يحدِّد الخلية F4 فقط.

## **تحديد المنطقة يدويًا**
الطريقة الثانية تتخطى اختيار النطاق وتحدِّد المنطقة صريحةً على `PivotConditionalFormat`.

### **مستطيل ورقة عمل باستخدام AddCellArea**
`AddCellArea(CellArea)` يسجل المستطيل المعطى كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة عمل ذات أساس صفري، والمنطقة هي بالضبط المستطيل المقدم – دون توسيع إلى عمود البيانات ولا منطق إجمالي شامل. استخدمها عندما تكون الخلايا ذات الاهتمام مستطيلًا ثابتًا معروفًا في تخطيط الجدول المحوري الحالي.

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
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
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
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Target the rectangle F4:F6 (the value cells without the grand total)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	area, _ := NewCellArea()
	area.Set_StartRow(3)
	area.Set_EndRow(5)
	area.Set_StartColumn(5)
	area.Set_EndColumn(5)
	format.AddCellArea(area)
	// Rule - italic on light yellow for amounts between 150 and 300
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_Between,
		"150",
		"300",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsItalic(true)
	lightYellow, _ := Color_FromArgb(int32(0xFFFFE0))
	style.SetForegroundColor(lightYellow)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatCellArea.xlsx")
}
```

### **منطقة محورية دلالية باستخدام PivotAreas**
`PivotAreas` هو نفس نموذج المنطقة الدلالية الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. أنشئ `PivotArea`، حدد حقلًا أو منطقة باستخدام `Select` أو `SelectField`، وأضفه باستخدام `PivotAreas.AddPivotArea(PivotArea)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذا يتبع التنسيق الشرطي الحقل عندما يتم تحديث الجدول المحوري ويتغير التخطيط. لا يزال الإصدار `PivotAreas.Add(PivotArea)` يُجمع ولكنّه مُعلَّم كمهمل – يفضَّل استخدام `AddPivotArea`.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Create a new workbook
	workbook, _ := NewWorkbook()
	// Get the first worksheet
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	// Get the cells collection
	cells, _ := sheet.GetCells()
	// Data arrays
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	// Write headers
	cellA1, _ := cells.Get_String("A1")
	cellA1.PutValue_String("Fruit")
	cellB1, _ := cells.Get_String("B1")
	cellB1.PutValue_String("Year")
	cellC1, _ := cells.Get_String("C1")
	cellC1.PutValue_String("Amount")
	// Write data rows
	for i := 0; i < len(fruits); i++ {
		row := int32(i + 1)
		c0, _ := cells.Get_Int_Int(row, 0)
		c0.PutValue_String(fruits[i])
		c1, _ := cells.Get_Int_Int(row, 1)
		c1.PutValue_Int(years[i])
		c2, _ := cells.Get_Int_Int(row, 2)
		c2.PutValue_Int(amounts[i])
	}
	// Create pivot table
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	// Add fields to the pivot
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Attach conditional format to the Amount data field
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	cfIdx, _ := conditionalFormats.Add()
	condFormat, _ := conditionalFormats.Get(cfIdx)
	// Define the pivot area covering the Amount data field
	area, _ := NewPivotArea(pivotTable)
	area.SelectField_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotAreas, _ := condFormat.GetPivotAreas()
	pivotAreas.AddPivotArea(area)
	// Add a condition: grey text for amounts below 150
	formatConds, _ := condFormat.GetFormatConditions()
	condIdx, _ := formatConds.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_LessThan,
		"150",
		"", // null second formula
	)
	// Create style with grey font color
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	grayColor, _ := Color_Gray()
	font.SetColor(grayColor)
	// Apply style to the condition
	cond, _ := formatConds.Get(condIdx)
	cond.SetStyle(style)
	// Save the workbook
	_ = workbook.Save_String("PivotConditionalFormatPivotArea.xlsx")
	fmt.Println("Workbook saved.")
}
```

## **أين يتم تخزين القواعد وكيفية بقاؤها بعد إعادة التحميل**
كل استدعاء لـ `ConditionalFormats.Add()` يضيف `PivotConditionalFormat` واحدًا إلى الجدول المحوري. تُحفظ الشروط وصيغها وتنسيقاتها مع المصنف – إعادة فتح الملف في المثال أدناه تُظهر القاعدة بنفس النوع والعملية والصيغة دون تغيير، وتُظهر `GetCellAreas()` نفس المناطق. تُحذف الإدخالات التي لم تتلق أي شرط عند حفظ المصنف، تمامًا كما يتجاهل Excel تنسيقًا شرطيًا لا يحتوي على قاعدة.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("PivotConditionalFormatData.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	conditionalFormatCount, _ := conditionalFormats.GetCount()
	fmt.Printf("Conditional formats: %d\n", conditionalFormatCount)
	for i := int32(0); i < conditionalFormatCount; i++ {
		format, _ := conditionalFormats.Get(i)
		formatConditions, _ := format.GetFormatConditions()
		formatConditionCount, _ := formatConditions.GetCount()
		for j := int32(0); j < formatConditionCount; j++ {
			condition, _ := formatConditions.Get(j)
			conditionType, _ := condition.GetType()
			operatorType, _ := condition.GetOperator()
			formula1, _ := condition.GetFormula1()
			conditionTypeName := fmt.Sprintf("%v", conditionType)
			if int32(conditionType) == int32(FormatConditionType_CellValue) {
				conditionTypeName = "CellValue"
			}
			operatorTypeName := fmt.Sprintf("%v", operatorType)
			if int32(operatorType) == int32(OperatorType_GreaterThan) {
				operatorTypeName = "GreaterThan"
			}
			fmt.Printf("Format %d: %s %s formula1=%s\n",
				i, conditionTypeName, operatorTypeName, formula1)
		}
		areas, _ := format.GetCellAreas()
		for _, area := range areas {
			startRow, _ := area.Get_StartRow()
			endRow, _ := area.Get_EndRow()
			startColumn, _ := area.Get_StartColumn()
			endColumn, _ := area.Get_EndColumn()
			fmt.Printf("    rows %d-%d, columns %d-%d\n",
				startRow+1, endRow+1, startColumn+1, endColumn+1)
		}
	}
	// This prints:
	// Conditional formats: 1
	// Format 0: CellValue GreaterThan formula1==200
	//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
}
```

## **مقالات ذات صلة**
- [تنسيق جزء من جدول محوري](/cells/ar/go-cpp/format-part-of-pivot-table/)
- [أعلى 10 إظهار أو تصفية في جدول محوري](/cells/ar/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}