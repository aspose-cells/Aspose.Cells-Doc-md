---
title: Форматирование части сводной таблицы
linktitle: Форматирование части сводной таблицы
description: Форматировать часть сводной таблицы в Aspose.Cells for Go via C++ путем применения стилей к семантическим регионам PivotArea или прямоугольникам CellArea через PivotTable.Format, при этом форматы сохраняются в PivotTable.PivotFormats и остаются при обновлении сводной таблицы.
keywords: Aspose.Cells for Go via C++, сводная таблица, форматирование, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /ru/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
`PivotTable.FormatAll` применяет один стиль к всей сводной таблице и описан на родительской странице. Он не различает метки, значения, итоги или отдельные регионы отчёта.  
На практике обычно только часть сводной таблицы требует выделения. Частыми целями являются метки, принадлежащие одному полю строки, ячейки значений, полученные от одного поля, строка итогов или произвольный прямоугольник, например первые две строки элементов.  
Применение стиля непосредственно к ячейкам рабочего листа сводной таблицы не эквивалентно. Excel сохраняет форматирование сводных таблиц как семантические регионы `PivotArea`, а не как обычные записи стилей ячеек. Формат `PivotArea` остаётся привязанным к региону, например к меткам поля или значениям данных, и переразрешается при пересчёте, обновлении или расширении сводной таблицы. Стиль, записанный напрямую в ячейку, принадлежит конкретному положению ячейки и не отслеживается моделью сводной таблицы.  
`Aspose.Cells` предоставляет полный набор перегрузок `PivotTable.Format`, поэтому доступны оба типа форматирования:
- `Format(PivotArea, Style)` привязывает стиль к семантическому региону, построенному с помощью `PivotArea.Select` или `PivotArea.SelectField`.
- `Format(CellArea, Style)` привязывает стиль к прямоугольнику рабочего листа внутри сводной таблицы.
- `Format(int row, int column, Style)` нацеливается на одну ячейку.
- `FormatAll(Style)` форматирует всю сводную таблицу.

## **Форматировать область PivotArea**
Семантический подход рекомендуется, когда выделение должно следовать за полем или регионом отчёта.  
1. Создайте объект `PivotArea` с помощью `NewPivotArea(pivotTable)`. Объект описывает семантический регион, принадлежащий данной сводной таблице.  
2. Выберите поле по нулевой позиции на заданной оси с помощью `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DataAndLabel` выбирает как метки, так и данные поля.  
   - `PivotTableSelectionType.LabelOnly` выбирает только метки поля.  
   - `PivotTableSelectionType.DataOnly` выбирает только ячейки данных поля.  
3. Выберите поле по имени с помощью `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. При выборе поля строки по имени регион разрешается в ячейки значений, полученные от элементов этого поля.  
4. Создайте объект `Style` через `Workbook.CreateStyle()`, настройте шрифт, цвет переднего плана и сплошной фон, затем передайте стиль в `PivotTable.Format(area, style)`.  
5. Каждый вызов перегрузки `PivotArea` добавляет одну запись `PivotTableFormat` в `PivotTable.PivotFormats`.  
6. Форматы, привязанные к полям, применяются при вычислении данных сводной таблицы. Поэтому после применения форматов вызовите `PivotTable.CalculateData()`, чтобы стили стали видимыми.  
Следующий пример создаёт небольшую сводную таблицу продаж фруктов, применяет стиль к меткам строк `Fruit` с помощью `PivotArea.Select` и `PivotTableSelectionType.LabelOnly`, стилизует ячейки значений того же поля с помощью `PivotArea.SelectField`, а затем пересчитывает сводную таблицу, чтобы оба стиля отобразились.

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

## **Форматировать область CellArea в сводной таблице**
Используйте `PivotTable.Format(CellArea, Style)`, когда интересующий регион представляет собой простой прямоугольник рабочего листа, а не семантическую область сводной таблицы.  
`CellArea` описывается значениями `StartRow`, `EndRow`, `StartColumn` и `EndColumn`, задаваемыми через соответствующие аксессоры `Set_StartRow` и т.п. Значения задаются нулевыми координатами листа, а конечные координаты указывают последнюю включённую строку и столбец, поэтому область охватывает ячейки от начального до конечного положения включительно.  
В отличие от формата, привязанного к полю, формат `CellArea` применяется к ячейкам сразу. Дополнительный вызов `CalculateData()` не требуется для отображения стиля.  
Прямоугольник `CellArea` может содержать как ячейки меток, так и ячейки значений одновременно. Следующий раздел объясняет, как `Aspose.Cells` и Excel представляют этот прямоугольник внутри.  
Следующий пример форматирует прямоугольник `E4:F5` сводной таблицы курсивным светло‑голубым стилем и сохраняет рабочую книгу без дальнейшего пересчёта.

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

## **Как соотносятся PivotArea и CellArea**
Excel сохраняет форматирование сводных таблиц как записи `pivotArea`, а не как обычные записи стилей ячеек. Такая же модель используется в `Aspose.Cells`, поэтому запрос на форматирование преобразуется в pivot‑области при его записи.  
Соотношение между пользовательским `CellArea` и внутренними pivot‑областями является многими‑ко‑многим в обоих направлениях.  
- Один `CellArea` может породить несколько pivot‑областей. Если прямоугольник охватывает как метки, так и данные, он разбивается на отдельные правила для меток и данных, поскольку модель сводной таблицы обрабатывает их независимо.  
- Одна pivot‑область может разрешаться в несколько непересекающихся `CellArea`. Семантический регион, такой как строка итогов, или поле, элементы которого не смежны, может покрывать несколько прямоугольников. Поэтому `PivotArea.GetCellAreas()` возвращает коллекцию, а не один прямоугольник.  
Каждая операция форматирования через `PivotTable.Format` фиксируется в `PivotTable.PivotFormats`. Каждая запись `PivotTableFormat` раскрывает связанный `PivotArea` и применённый к нему `Style`. Перегрузка `PivotArea` добавляет ровно одну запись за вызов, тогда как `CellArea`, содержащий разные семантические регионы, может добавить несколько записей.  
Чтобы различать сохранённые регионы, каждый `PivotArea` раскрывает флаги `OnlyLabel` и `OnlyData`. Пример ниже форматирует один прямоугольник, охватывающий как метки, так и значения, инспектирует `PivotTable.PivotFormats` и выводит координаты `CellArea`, к которым каждый сохранённый pivot‑регион разрешается.

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
Поскольку форматы сохраняются как pivot‑области, а не как обычные стили ячеек, они сохраняются при пересчёте и обновлении. Когда сводная таблица обновляется с помощью `PivotTable.RefreshData`, пересчитывается через `CalculateData` или сохраняется и повторно загружается, каждая сохранённая pivot‑область переопределяется к текущему положению своего региона, и её стиль применяется снова.
{{% /alert %}}

Используйте `PivotArea`, построенный с помощью `Select` или `SelectField`, когда выделение должно оставаться привязанным к полю или семантическому региону при обновлениях, и используйте `CellArea`, когда достаточно отформатировать фиксированный прямоугольник в текущем макете сводной таблицы. Перегрузка `Format(int row, int column, Style)` для одной ячейки нацеливается на отдельную ячейку. Применяйте `FormatAll`, описанный на родительской странице, когда необходимо переоформить всю сводную таблицу сразу.

{{< app/cells/assistant language="go" >}}