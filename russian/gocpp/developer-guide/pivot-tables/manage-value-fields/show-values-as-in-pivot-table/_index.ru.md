---
title: Отображение значений как в сводной таблице
linktitle: Отображение значений как в сводной таблице
description: Отображайте значения полей данных сводной таблицы в виде процента от общего итога, разницы от базового элемента, скользящих итогов, рангов и прочего с Aspose.Cells for Go via C++.
keywords: Aspose.Cells for Go via C++, сводная таблица, отобразить значения как, формат отображения данных, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /ru/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Сводная таблица обычно агрегирует каждое поле данных с помощью функции агрегации, такой как `Sum` или `Count`. Функция Excel **Show Values As** заменяет каждое отображаемое значение вторичным вычислением, полученным из этой агрегированной величины — например, процент от общего итога, скользящий итог, разницу от выбранного базового элемента или ранг — что позволяет выполнять сравнительный анализ без вспомогательных формул или вычисляемых столбцов.  
Типичные применения включают анализ доли от общего итога, в том числе проценты по строке, столбцу или общему итогу; накопительную отчетность с использованием скользящего итога в поле периода; анализ отклонений от базового элемента с помощью разницы или процентной разницы; а также ранжирование значений от наименьшего к наибольшему или наоборот.  
В Aspose.Cells for Go via C++ параметр `PivotFieldDataDisplayFormat` выбирает вторичное вычисление. Метод‑аксессор `PivotField.GetShowValuesSetting()` возвращает объект `PivotShowValuesSetting`, методы `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` и `SetBaseItemIndex` которого настраивают поведение; удобный метод `PivotField.ShowValuesAs(...)` применяет те же четыре параметра одним вызовом. Примените эти настройки к полю данных или полю значений, полученному через `PivotTable.GetDataFields()`.

## **Члены перечисления PivotFieldDataDisplayFormat**
Поле данных сохраняет свою функцию агрегации, например Sum или Count, в то время как Show Values As изменяет только способ отображения агрегированного значения.  
Помимо прямого указания значений `PivotShowValuesSetting` (см. последний раздел), метод‑удобство, вызываемый один раз, применяет ту же конфигурацию:

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| Параметр | Значение | Требуется когда |
| --- | --- | --- |
| `displayFormat` | Вторичная калькуляция `PivotFieldDataDisplayFormat`, которую необходимо применить. | Всегда. |
| `baseField` | Нулевая позиция индекса базового поля среди базовых полей сводной таблицы (например, индекс строкового поля, к которому относится базовый элемент). | Только шесть базовых форматов ниже (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); игнорируется всеми остальными форматами. |
| `baseItemPositionType` | Способ выбора базового элемента относительно текущего элемента: `PivotItemPositionType.Previous`, `.Next` или `.Custom`. | Только три формата базового элемента (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); игнорируется всеми остальными форматами. |
| `baseItem` | Нулевая позиция индекса базового элемента. | Только когда `baseItemPositionType` равно `Custom` (индекс указывает точный базовый элемент); игнорируется для `Previous`/`Next` и всех форматов без базового элемента — передайте `0`. |

| Тип расчета | Поведение | Параметры базового элемента |
| --- | --- | --- |
| `Normal` | Нет вторичной калькуляции; агрегированное значение отображается как есть (по умолчанию). | — |
| `DifferenceFrom` | Отображает значение как разницу от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (только `baseItem` при `Custom`) |
| `PercentageOf` | Отображает значение как процент от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (только `baseItem` при `Custom`) |
| `PercentageDifferenceFrom` | Отображает значение как процентную разницу от значения базового элемента в базовом поле. | `baseField` + `Previous`/`Next`/`Custom` (только `baseItem` при `Custom`) |
| `RunningTotalIn` | Отображает значение как скользящий итог для последовательных элементов базового поля. | `baseField` (поле, порядок элементов которого определяет накопление) |
| `PercentageOfRow` | Отображает значение как процент от итога строки. | — |
| `PercentageOfColumn` | Отображает значение как процент от итога столбца. | — |
| `PercentageOfTotal` | Отображает значение как процент от общего итога. | — |
| `Index` | Отображает значение по формуле Excel Index ((value * grand total) / (row total * column total)). | — |
| `PercentageOfParentRowTotal` | Отображает значение как процент от итога родительской строки (для вложенных строковых полей). | — |
| `PercentageOfParentColumnTotal` | Отображает значение как процент от итога родительского столбца (для вложенных столбцовых полей). | — |
| `PercentageOfParentTotal` | Отображает значение как процент от родительского итога. | `baseField` (базовое родительское поле) |
| `PercentageOfRunningTotalIn` | Отображает значение как процент от скользящего итога в базовом поле. | `baseField` (поле накопления) |
| `RankSmallestToLargest` | Присваивает ранг от наименьшего (1) к наибольшему. | — |
| `RankLargestToSmallest` | Присваивает ранг от наибольшего (1) к наименьшему. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` записывает значения `PivotShowValuesSetting` (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) — метод и объект настроек представляют два способа конфигурировать одно и то же состояние, аналогично выборам базового поля и базового элемента в диалоговом окне Show Values As в Excel.
{{% /alert %}}

## **Отображение значений как процент от общего итога**
Вызовите метод `PivotField.ShowValuesAs` с параметром `PivotFieldDataDisplayFormat.PercentageOfTotal`, чтобы преобразовать каждую ячейку поля данных, включая общий итог, в её долю от общего итога. Отображаемые числа, таким образом, представляют собой часть полного набора результатов. Этот формат сравнивает каждое значение только с общим итогом, поэтому не требуется базовое поле или базовый элемент — завершающие аргументы (`0`, `PivotItemPositionType.Previous`, `0`) являются заполнительными и игнорируются, как указано в таблице параметров выше.

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

## **Получить и настроить PivotField.ShowValuesSetting**
Прочитайте текущую конфигурацию через `PivotField.GetShowValuesSetting()`: аксессор возвращает объект `PivotShowValuesSetting` поля, четыре метода‑геттера которого описывают активную калькуляцию Show Values As. Чтобы изменить конфигурацию, вызовите метод `PivotField.ShowValuesAs` — он записывает все четыре настройки за один вызов, поэтому необязательно задавать их по отдельности.  
Объект `PivotShowValuesSetting` раскрывает четыре значения, которые записывает `ShowValuesAs`:
- `GetCalculationType()` / `SetCalculationType()` выбирают вторичную калькуляцию `PivotFieldDataDisplayFormat`.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` указывают нулевой индекс базового поля среди полей сводной таблицы. Используется базовыми форматами.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` определяют расположение базового элемента относительно текущего и принимают `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` или `PivotItemPositionType.Custom`.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` указывают нулевой индекс базового элемента и используются, когда тип позиции равен `Custom`.  
После вызова `ShowValuesAs` снова вызовите `PivotTable.CalculateData()`, чтобы тело сводной таблицы пересчиталось и перерисовалось с обновлённой конфигурацией.

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

## **Связанные статьи**
- [Группировка полей сводной таблицы](/cells/ru/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [Отображение или фильтрация топ-10 в сводной таблице](/cells/ru/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Обновление среза](/cells/ru/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}