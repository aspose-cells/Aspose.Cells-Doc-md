---
title: Группировка полей сводной таблицы с помощью Golang через C++
linktitle: Группировка полей сводной таблицы с помощью Golang через C++
description: Узнайте, как группировать поля строк и столбцов сводной таблицы по таким периодам времени, как месяцы и кварталы, а также по числовым диапазонам, используя PivotField.Group и PivotFieldGroupOptions в Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, сводная таблица, поле сводной таблицы, группировка полей сводной таблицы, Group, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, группировка дат, числовой диапазон, Go
type: docs
weight: 80
url: /ru/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
- Группировка полей сводной таблицы полезна, когда поле строки или столбца сводной таблицы содержит множество различных элементов, например поле дат с сотнями дат или числовое поле со множеством разрозненных значений. Группировка объединяет эти элементы в смысловые категории: даты — в месяцы, кварталы и годы, а числа — в диапазоны, например 0-1, 2-3, 4-5. Это делает большую сводную таблицу компактной и более удобной для анализа. Aspose.Cells предоставляет эту возможность с помощью перегрузок `PivotField.Group()` (автоматическая группировка по типу данных) и `PivotField.Group(PivotFieldGroupOptions)` (настраиваемые параметры группировки).
- Группировка дат объединяет отдельные даты в более крупные периоды, например дни, месяцы, кварталы и годы, и создает иерархию времени (например, «Годы», «Кварталы», «Месяцы»). Динамика изменений во времени становится видна сразу, а каждый уровень периода становится отдельным полем сводной таблицы в области строк или столбцов.
- Группировка доступна только для полей, размещенных в области ROW или COLUMN сводной таблицы. Поле данных (значений) нельзя сгруппировать напрямую. Чтобы сгруппировать такое поле, сначала добавьте его в область строк или столбцов сводной таблицы.

## **Автоматическая группировка полей сводной таблицы**
Перегрузка `PivotField.Group()` без параметров анализирует тип данных поля и автоматически группирует его. Поле, содержащее только даты (и пустые значения), группируется по месяцам. Поле, содержащее только числа (и пустые значения), группируется по числовым диапазонам с использованием автоматического интервала.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the first row field automatically by its data type
	rowFields, _ := pivotTable.GetRowFields()
	field, _ := rowFields.Get_Int(0)
	field.Group()
	pivotTable.CalculateData()
	workbook.Save_String("outputAutoGroupPivotField.xlsx")
}
```

## **Группировка полей сводной таблицы с настраиваемыми параметрами**
Класс `PivotFieldGroupOptions` позволяет настроить параметры группировки. Для полей дат задайте `StartDate`, `EndDate` и `GroupTypes` (даты передаются как значения Go `time.Time`). Для числовых полей задайте `StartNumber`, `EndNumber` и `Interval`. От поведения `newPivotField` зависит, создает ли группировка новые поля сводной таблицы рядом с исходным (см. раздел «Примечание» в конце статьи).

### **Группировка поля дат по месяцам и кварталам**
В следующем примере поле даты, размещенное в области строк сводной таблицы из примера, группируется по месяцам и кварталам в пределах заданного диапазона дат. Код загружает [пример файла Excel](sampleGroupPivotFieldsInPivotTable.xlsx), выполняет группировку, вычисляет данные сводной таблицы и сохраняет сгруппированный результат. На снимке экрана показан результат группировки: поле даты в области строк теперь сгруппировано по кварталам и месяцам.
Обратите внимание, что порядок значений в `GroupTypes` игнорируется. Независимо от порядка, в котором перечислены типы группировки, сгруппированные поля всегда отображаются от наибольшего периода к наименьшему: годы, кварталы, месяцы, дни, часы, минуты, секунды. В этом примере в `GroupTypes` месяцы перечислены перед кварталами, однако кварталы отображаются как внешний уровень, а месяцы — как внутренний.

```go
package main
import (
	"time"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the date row field by months and quarters between the given dates
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartDate(time.Date(2008, 1, 1, 0, 0, 0, 0, time.UTC))
	options.SetEndDate(time.Date(2008, 9, 5, 0, 0, 0, 0, time.UTC))
	options.SetGroupTypes([]PivotGroupByType{PivotGroupByType_Months, PivotGroupByType_Quarters})
	rowFields, _ := pivotTable.GetRowFields()
	dateField, _ := rowFields.Get_Int(0)
	dateField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputGroupPivotFieldsInPivotTable.xlsx")
}
```

![Сводная таблица, сгруппированная по месяцам и кварталам](group-pivot-fields-in-the-pivot-table_1.png)

### **Группировка числового поля по диапазонам**
`FieldTwo` в примере сводной таблицы изначально является полем данных (значений). Поскольку группировать можно только поля строк или столбцов, код сначала вызывает `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")`, чтобы переместить `FieldTwo` в область строк, обновляет сводную таблицу, а затем группирует числовое поле по диапазонам 0-1, 2-3 и 4-5 с помощью `StartNumber = 0`, `EndNumber = 5` и `Interval = 2`.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// FieldTwo is a data field: move it to the row area first,
	// because only row/column fields can be grouped
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "FieldTwo")
	pivotTable.CalculateData()
	// Group the numeric field into the ranges 0-1, 2-3, 4-5
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartNumber(0)
	options.SetEndNumber(5)
	options.SetInterval(2)
	rowFields, _ := pivotTable.GetRowFields()
	numericField, _ := rowFields.Get_Int(1)
	numericField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputNumberGroupPivotField.xlsx")
}
```

## **Примечание**

{{% alert color="primary" %}}
- Перегрузки метода `PivotField.GroupBy()` устарели и удалены из состава API. Их заменяют `PivotField.Group()` и `PivotField.Group(PivotFieldGroupOptions)`.
- В Microsoft Excel при группировке числового поля исходное поле сводной таблицы ЗАМЕНЯЕТСЯ диапазонами группировки, тогда как группировка поля дат создает НОВЫЕ поля сводной таблицы (по одному для каждого уровня группировки, например «Кварталы» и «Месяцы») рядом с исходным полем. Начиная с версии Aspose.Cells 26.10 методы `PivotField.Group()` следуют тому же поведению, что и Excel.
- Свойство `PivotFieldGroupOptions.Interval` действует только при группировке числовых полей, а также дат по дням (например, при группировке дат в семидневные периоды); при группировке дат по месяцам, кварталам или годам оно игнорируется.
{{% /alert %}}

## **Связанные статьи**
- [Отображение 10 лучших значений или фильтрация в сводной таблице](/cells/ru/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [«Отображать значения как» в сводной таблице](/cells/ru/go-cpp/show-values-as-in-pivot-table/)
- [Форматирование части сводной таблицы](/cells/ru/go-cpp/format-part-of-pivot-table/)
- [Добавление условного форматирования к сводной таблице](/cells/ru/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}