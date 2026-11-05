---
title: Добавление условного форматирования к сводной таблице
linktitle: Добавление условного форматирования к сводной таблице
description: Добавьте условное форматирование к сводной таблице в Aspose.Cells for Go через C++, привяжите правило к области данных с помощью ApplyTo и области PivotConditionFormatScopeType, либо задайте цель с помощью AddCellArea и PivotAreas, затем присоедините правила и стили через FormatConditions.AddCondition.
keywords: Aspose.Cells, сводная таблица, условное форматирование, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /ru/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Стили, описанные на родительской странице и на странице‑сиблинге, являются статическими — область `PivotArea` или `CellArea` окрашивается один раз и сохраняет свой стиль независимо от значений. Условное форматирование — это правило‑ориентированный аналог: выделить каждую сумму выше 200, затенить средние пятьдесят процентов или пометить элементы с самым низким рейтингом — и выделение будет следовать за значениями каждый раз, когда сводная таблица пересчитывается или обновляется.  
В Aspose.Cells условное форматирование сводной таблицы находится в коллекции `PivotTable.ConditionalFormats`. Каждая запись — это `PivotConditionalFormat`, который независимо отвечает на два вопроса:
- **Где применяется правило?** Целевая область определяется либо через `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, что имитирует выбор области в пользовательском интерфейсе Excel, либо через `AddCellArea(CellArea)` и коллекцию `PivotAreas`, которые задают область явно.  
- **Что проверяет правило?** Одна или несколько условий добавляются в `FormatConditions` с помощью `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, и каждое условие имеет собственный `Style`.

{{% alert color="primary" %}}
Не вызывайте `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` или `FormatConditionCollection.AddArea(CellArea)` у объекта `FormatConditions` условного форматирования сводной таблицы. Эти две перегрузки унаследованы от обычного API условного форматирования листа и не работают со сводными таблицами — область ячеек никогда не преобразуется в область сводной таблицы, поэтому запрос беззвучно игнорируется. Всегда задавайте область непосредственно у `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` или `PivotAreas`) и добавляйте правило одной из перегрузок `AddCondition`.
{{% /alert %}}

## **Применить правило с областью (как в интерфейсе Excel)**
Первый способ позиционирует правило так же, как делает это пользовательский интерфейс Excel. Ячейка сводной таблицы определяется её координатами на рабочем листе, начиная с нуля, а значение `PivotConditionFormatScopeType` указывает Aspose.Cells, насколько далеко правило должно распространяться от этой ячейки:
- `PivotConditionFormatScopeType.Data` — все ячейки‑значения, которые генерирует сводная таблица, включая итоги.
- `PivotConditionFormatScopeType.Field` — ячейки‑значения, принадлежащие полю, которое идентифицирует ячейка, исключая общие итоги. Ячейка должна быть ячейкой поля, например меткой строки‑поля; передача ячейки‑значения вызовет исключение.
- `PivotConditionFormatScopeType.Selection` — только те ячейки‑значения, которые находятся на пересечении, выбранном ячейкой, обычно одна ячейка‑значение.
Ниже приведён пример, в котором создаётся сводная таблица продаж фруктов с левым верхним углом в **E3**, привязывается условный формат к ячейке **F4** (строка 3, столбец 5) с областью `Data` и выделяется каждая сумма, превышающая 200, полужирным белым шрифтом на красном фоне. При значениях **Apple 220**, **Banana 330**, **Cherry 200** и общей сумме 750 правило закрасит **F4**, **F5** и **F7** — разрешённая область охватывает весь столбец данных **F4:F7**, и только ячейки, прошедшие проверку, подсвечиваются.

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

Привязка того же правила к метке строки‑поля **E4** (строка 3, столбец 4) с областью `Field` приводит к диапазону **F4:F6** — тот же столбец данных без строки общего итога, поскольку область теперь описывает поле `Fruit`, а не всю область значений. Область `Selection`, привязанная к **F4**, ограничивается лишь ячейкой **F4**.

## **Определить область вручную**
Второй способ пропускает выбор области и задаёт её явно у `PivotConditionalFormat`.

### **Прямоугольник рабочего листа с AddCellArea**
`AddCellArea(CellArea)` фиксирует заданный прямоугольник как цель правила. Координаты — нулевые координаты листа, и область точно соответствует указанному прямоугольнику — без расширения до столбца данных и без логики общих итогов. Используйте этот метод, когда интересующие ячейки находятся в известном фиксированном прямоугольнике текущего макета сводной таблицы.

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

### **Семантическая область сводной таблицы с PivotAreas**
`PivotAreas` — тот же семантический региональный подход, который используется на странице‑сиблинге для статических стилей. Создайте `PivotArea`, выберите поле или область с помощью `Select` или `SelectField` и добавьте её через `PivotAreas.AddPivotArea(PivotArea)`. Семантическая область остаётся привязанной к своему полю, поэтому условный формат следует за полем при обновлении сводной таблицы и смещении макета. Перегрузка `PivotAreas.Add(PivotArea)` всё ещё компилируется, но помечена как устаревшая — предпочтительнее использовать `AddPivotArea`.

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

## **Где хранятся правила и как они переживают перезагрузку**
Каждый вызов `ConditionalFormats.Add()` добавляет один `PivotConditionalFormat` в сводную таблицу. Условия, их формулы и стили сохраняются вместе с рабочей книгой — при повторном открытии файла в примере ниже отображаются то же правило с его типом, оператором и формулой неизменными, а `GetCellAreas()` сообщает те же области. Записи, которым никогда не было присвоено условие, отбрасываются при сохранении рабочей книги, так же как Excel удаляет условный формат без правил.

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

## **Related Articles**
- [Форматировать часть сводной таблицы](/cells/ru/go-cpp/format-part-of-pivot-table/)
- [Топ‑10 отображения или фильтрации в сводной таблице](/cells/ru/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}