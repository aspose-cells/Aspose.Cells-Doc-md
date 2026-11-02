---
title: Отображение или фильтрация топ-10 в сводной таблице
linktitle: Отображение или фильтрация топ-10 в сводной таблице
description: Узнайте, как отображать только элементы с наивысшим или наименьшим рейтингом поля сводной таблицы в Aspose.Cells for Go via C++. В этой статье рассматриваются параметры AutoShow Excel 97-2003 (SetIsAutoShow и аналогичные методы), чтение этих параметров и фильтр топ-10 Excel 2007-365 с помощью FilterTop10.
keywords: Aspose.Cells, Go via C++, сводная таблица, топ-10, автопоказ, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /ru/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица, перечисляющая все элементы поля строки, может быть неудобной для чтения, если поле содержит десятки элементов. Отчёт «топ-10» оставляет только элементы с наивысшим или наименьшим рейтингом, что как раз необходимо для ранжирующих отчётов, например «5 лидирующих товаров по выручке» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **AutoShow в Excel 97-2003** — четыре метода установки `PivotField`: `SetIsAutoShow`, `SetIsAscendShow`, `SetAutoShowCount` и `SetAutoShowField`. Это классический параметр «Показать верхние/нижние N элементов», который хранится непосредственно в поле сводной таблицы. Он работает во всех версиях Excel, поскольку является частью исходного формата сводных таблиц.
- **Фильтр топ-10 в Excel 2007-365** — метод `PivotField.FilterTop10()`. Это современный фильтр значений топ-10, доступный в разделе «Фильтры значений» меню поля. Он хранится как объект `PivotFilter`, связанный с полем, и поддерживает ранжирование по количеству элементов и проценту.

## **Отображение топ-10 в Excel 97-2003 (AutoShow)**
Классический AutoShow настраивается четырьмя вызовами методов установки `PivotField`:
- `SetIsAutoShow(bool)` — включает или отключает параметр AutoShow для поля.
- `SetIsAscendShow(bool)` — значение `false` сохраняет элементы с наивысшим рейтингом (верхние), а `true` — элементы с наименьшим рейтингом (нижние).
- `SetAutoShowCount(int32)` — количество сохраняемых элементов, например 10 для классического отчёта «топ-10».
- `SetAutoShowField(int32)` — индекс (с нуля) **поля данных**, значения которого определяют рейтинг элементов. Передайте -1, чтобы ранжировать элементы по самому полю.
Рейтинг может определяться полем значений или самим полем. Ниже показаны два естественных варианта.

### **Ранжирование по полю значений**
Ранжируйте элементы поля строки по обычному полю значений, например по полю «Сумма продаж». В следующем примере создаётся сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображаются 2 лучших вида спорта по продажам. Значение `rankBy` равно 0, поскольку «Сумма продаж» — поле данных с индексом 0.

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
	// Показать 2 верхних элемента с рейтингом по "Sum of Sales" (индекс поля данных 0)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Ранжирование по самому полю**
Поле также можно ранжировать по самому себе: передайте -1 в `SetAutoShowField`. Для этого варианта не требуется дополнительное поле данных; поле должно находиться только в области строк или столбцов. В следующем примере показаны 3 вида спорта с наименьшим рейтингом, упорядоченные по самому полю. После сохранения этого параметра атрибут `rankBy` отсутствует в XML сводной таблицы, поскольку -1 является значением по умолчанию для этого формата, а `GetAutoShowField()` считывает значение -1.

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
	// Показать 3 нижних элемента, ранжированных по самому полю (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Чтение текущих параметров AutoShow**
Методы чтения `PivotField` — `IsAutoShow()`, `IsAscendShow()`, `GetAutoShowCount()` и `GetAutoShowField()` — предоставляют параметры AutoShow, которые в настоящее время хранятся в поле. Используйте их, чтобы проверить, как существующая рабочая книга или только что настроенная сводная таблица будет представлять свои элементы, включая рабочие книги, загруженные из файла.

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

Четыре свойства соответствуют классическим атрибутам AutoShow, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому считанные значения будут учтены всеми версиями Excel.

## **Примечание**

{{% alert color="primary" %}}
- После изменения любого метода установки AutoShow повторно вызовите `PivotTable.CalculateData()` — параметры применяются к отображаемому макету только при следующем пересчёте.
- Параметры AutoShow работают с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя ранжировать таким способом, поскольку его элементы не размещаются в основной части сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр топ-10 (FilterTop10)**
Современные версии Excel предоставляют функцию «Топ-10» как фильтр значений в меню поля («Фильтры значений», «Топ-10...»). В Aspose.Cells она реализована методом `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, который возвращает созданный объект `PivotFilter`:
- `valueFieldIndex` — индекс (с нуля) поля данных, агрегированные значения которого определяют рейтинг элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.Count` сохраняет фиксированное количество элементов (параметр «Элементы» в диалоговом окне). `PivotFilterType.Percent` сохраняет процент элементов, поэтому `itemCount` сам является процентом: значение 30 сохраняет верхние 30 процентов. `PivotFilterType.Sum` ранжирует по накопленному покрытию значений.
- `isTop` — значение `true` для верхних элементов, `false` для нижних.
- `itemCount` — число N в выражении «Топ N»; его единица измерения зависит от `type`.

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
	// Фильтр «Топ-10» — оставить 2 лучших элемента по «Сумме продаж» (индекс поля данных 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// Для фильтра на основе процентов вместо этого оставить 30% элементов:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Параметры AutoShow и `FilterTop10` — это две отдельные функции. AutoShow записывает классический набор атрибутов `autoShow` для поля сводной таблицы и поддерживается всеми версиями Excel, начиная с Excel 97. `FilterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. Если рабочая книга открывается в более старой версии Excel, сводная таблица с современным фильтром переходит к отображению всех элементов. Для документов, которые должны проходить через устаревшие инструменты с сохранением структуры и функциональности, предпочтительны методы установки AutoShow; для современных рабочих книг предпочтителен `FilterTop10`, поскольку он сочетается с другими фильтрами значений.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей в сводной таблице](/cells/ru/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}