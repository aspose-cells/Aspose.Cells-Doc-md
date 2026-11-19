---
title: Показ или фильтрация топ-10 в сводной таблице
linktitle: Показ или фильтрация топ-10 в сводной таблице
description: Узнайте, как отображать только элементы с наибольшим или наименьшим рейтингом поля сводной таблицы в Aspose.Cells for Go via C++. В этой статье рассматриваются метод Top10AutoShow для Excel 97-2003, чтение параметров с помощью Top10AutoShowSettings и фильтр топ-10 для Excel 2007-365, реализуемый с помощью FilterTop10.
keywords: Aspose.Cells, Go via C++, сводная таблица, топ-10, автоматический показ, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /ru/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица, в которой перечислены все элементы поля строки, может быть сложна для восприятия, если поле содержит десятки элементов. Отчет с топ-10 оставляет только элементы с наибольшим или наименьшим рейтингом, что как раз необходимо для рейтинговых отчетов — «5 товаров с наибольшей выручкой» или «3 региона с наименьшим количеством продаж». Aspose.Cells поддерживает два механизма, соответствующих двум поколениям Microsoft Excel.
- **Excel 97-2003: AutoShow** — метод `PivotField.Top10AutoShow()`. Это классическая настройка «Показать N верхних/нижних элементов», которая хранится непосредственно в поле сводной таблицы. Она работает во всех версиях Excel, как старых, так и новых, поскольку входит в исходный формат сводных таблиц.
- **Фильтр топ-10 для Excel 2007-365** — метод `PivotField.FilterTop10()`. Это современный фильтр значений «Топ-10», доступный в меню поля в разделе «Фильтры по значениям». Он хранится в виде объекта `PivotFilter`, связанного с полем, и поддерживает ранжирование по количеству элементов и по проценту.

## **Показ топ-10 в Excel 97-2003 (Top10AutoShow)**
Классический AutoShow настраивается одним вызовом `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)`:
- `isAutoShow` — включает или отключает параметр AutoShow для поля.
- `isTop` — значение `true` оставляет элементы с наибольшим рейтингом (верхние), а `false` — элементы с наименьшим рейтингом (нижние).
- `count` — количество элементов, которые необходимо оставить, например 10 для классического отчета с топ-10.
- `rankBy` — индекс **поля данных** (с нуля), значения которого определяют ранжирование элементов. Передайте -1, чтобы ранжировать элементы по самому полю.
Ранжирование может выполняться по полю значений или по самому полю. Ниже показаны два естественных варианта.

### **Ранжирование по полю значений**
Элементы поля строки можно ранжировать по обычному полю значений, например `Sum of Sales`. В следующем примере создается сводная таблица с одним полем строки (`Sport`) и одним полем данных (`Sales`), после чего отображаются 2 вида спорта с наибольшим объемом продаж. Значение `rankBy` равно 0, поскольку `Sum of Sales` — поле данных с индексом 0.

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

### **Ранжирование по самому полю**
Поле также можно ранжировать по его собственным значениям — передайте -1 в `rankBy`. Для этого варианта не требуется дополнительное поле данных; поле должно находиться в области строк или столбцов. В следующем примере показаны 3 вида спорта с наименьшим рейтингом, ранжированные по самому полю. При сохранении этой настройки атрибут `rankBy` не включается в XML сводной таблицы, поскольку -1 является значением по умолчанию для этого формата, а `GetRankBy()` считывает -1.

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

## **Чтение текущих параметров AutoShow**
Метод `PivotField.GetTop10AutoShowSettings()` возвращает объект `PivotFieldTop10AutoShowSettings`, предоставляющий доступ к параметрам AutoShow, которые в данный момент хранятся в поле. Используйте его, чтобы проверить, как будут отображаться элементы в существующей рабочей книге или в только что настроенной сводной таблице, в том числе в рабочих книгах, загруженных из файла.

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

Параметры соответствуют классическим атрибутам AutoShow, записываемым в XML сводной таблицы (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), поэтому считанные значения будут учтены любой версией Excel.

## **Примечание**

{{% alert color="primary" %}}
- После вызова `Top10AutoShow()` снова вызовите `PivotTable.CalculateData()` — параметры вступают в силу только в отображаемом макете при следующем пересчете.
- Параметры AutoShow работают с полями строк и столбцов. Поле, находящееся только в области страницы (фильтра), нельзя таким образом ранжировать, поскольку его элементы не размещаются в основной части сводной таблицы.
{{% /alert %}}

## **Excel 2007-365: фильтр топ-10 (FilterTop10)**
Современные версии Excel предоставляют фильтр «Топ-10» как фильтр значений в меню поля («Фильтры по значениям», «Топ-10...»). В Aspose.Cells он реализован методом `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, возвращающим созданный объект `PivotFilter`:
- `valueFieldIndex` — индекс поля данных (с нуля), агрегированные значения которого определяют ранжирование элементов.
- `type` — определяет смысл `itemCount`. `PivotFilterType.Count` оставляет фиксированное количество элементов (вариант «Элементы» в диалоговом окне). `PivotFilterType.Percent` оставляет заданный процент элементов, поэтому `itemCount` само является процентом: значение 30 оставляет верхние 30 процентов. `PivotFilterType.Sum` ранжирует по совокупному объему значений.
- `isTop` — значение `true` для верхних элементов, `false` для нижних.
- `itemCount` — число N в выражении «Топ-N»; его единица измерения зависит от `type`.

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
Параметры AutoShow и `FilterTop10` — это две отдельные функции. AutoShow записывает классический атрибут `autoShow` в поле сводной таблицы и поддерживается всеми версиями Excel, начиная с Excel 97. `FilterTop10` записывает современную запись `PivotFilter`, для которой требуется Excel 2007 или более поздняя версия. При открытии рабочей книги в более старой версии Excel сводная таблица с современным фильтром отображает все элементы. Для документов, требующих сохранения и повторной загрузки с помощью устаревших инструментов, предпочтительнее использовать `Top10AutoShow`; для современных рабочих книг предпочтительнее использовать `FilterTop10`, поскольку он может применяться вместе с другими фильтрами по значениям.
{{% /alert %}}

## **Связанные статьи**
- [Группировка полей сводной таблицы](/cells/ru/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}