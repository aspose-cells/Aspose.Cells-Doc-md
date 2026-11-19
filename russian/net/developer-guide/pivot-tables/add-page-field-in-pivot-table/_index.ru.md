---
title: Добавить поля фильтров в сводную таблицу в Aspose.Cells для .NET
description: Узнайте, как добавлять и настраивать поля фильтра в сводных таблицах с помощью Aspose.Cells for .NET, включая добавление полей фильтра, фильтрацию с одиночным выбором и фильтрацию с множественным выбором.
linktitle: Добавить поля фильтров
keywords: Aspose.Cells, .NET, сводная таблица, поле фильтра, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, фильтр
type: docs
weight: 250
url: /ru/net/add-page-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает полный жизненный цикл полей фильтра в сводных таблицах. Вы можете добавить поле фильтра через высокоуровневый удобный API или через низкоуровневую коллекцию `PageFields`, а также управлять фильтром страницы в режиме одиночного выбора, очищать его, чтобы отобразить все элементы страницы, или переключать поле в режим множественного выбора, чтобы пользователи могли выбирать несколько элементов страницы одновременно через интерфейс флажков в Excel.
{{% /alert %}}

## **Введение**
поле фильтра — это поле сводной таблицы, которое управляет *тем, какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его как раскрывающийся список в верхней части отображаемой сводной таблицы в Excel, и при выборе одного из доступных элементов страницы тело сводной таблицы перестраивается таким образом, чтобы суммировались только записи, принадлежащие этому элементу страницы. Поле сводной таблицы становится полем страницы, когда оно зарегистрировано как `PivotFieldType.Page`, а не как `PivotFieldType.Row`, `PivotFieldType.Column` или `PivotFieldType.Data`.
поле фильтра может работать в двух режимах. В режиме **одиночного выбора** по умолчанию одновременно виден только один элемент страницы, поэтому тело сводной таблицы суммирует ровно одно подмножество. В режиме **множественного выбора** поле отображает список флажков, и тело сводной таблицы суммирует объединение всех отмеченных элементов страницы. Одно и то же исходное поле можно переключать между этими режимами, изменяя значение одного свойства.
Aspose.Cells for .NET предоставляет два эквивалентных способа регистрации поля фильтраы. Высокоуровневый API — `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, который принимает имя исходного столбца и добавляет поле одним вызовом. Низкоуровневый API — `PivotTable.PageFields.Add(PivotField)`, который используется, когда у вас уже есть ссылка на `PivotField` и вы хотите добавить тот же экземпляр поля в область фильтраы. Оба API в итоге заполняют одну и ту же коллекцию `PageFields`, и далее в этой статье показано, как выбирать между ними и как управлять каждым режимом фильтрации.

## **Добавление поля фильтраы**
Существует два способа зарегистрировать поле сводной таблицы в области страницы. Высокоуровневый вызов принимает имя исходного столбца в виде строки и является наиболее распространённым способом. Низкоуровневый вызов принимает существующий экземпляр `PivotField` и удобен, когда тот же объект поля необходимо использовать в нескольких областях сводной таблицы. Оба вызова помещают поле в `PivotTable.PageFields`, после чего оно отображается как раскрывающийся список страницы в верхней части отображаемой сводной таблицы.

### Добавление поля фильтраы с помощью AddFieldToArea
В следующем примере создаётся небольшой набор данных Fruit / Year / Amount, сводная таблица размещается в ячейке E3 с полем `Fruit` в области строк, `Amount` в области данных и `Year` в области страницы, после чего сводная таблица обновляется и сохраняется книга.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Create a new workbook
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
// Set up the header row
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}
// Add a pivot table anchored at cell E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Refresh and calculate the pivot table data
pivotTable.CalculateData();
// Save the workbook
workbook.Save("pageFieldSample.xlsx");
```

### Добавление поля фильтраы с помощью PageFields.Add
Если у вас уже есть экземпляр `PivotField`, вы можете передать его напрямую в `PivotTable.PageFields.Add`. Сводная таблица и поле фильтра создаются точно так же, как в предыдущем сценарии; только регистрация в области страницы заменяется вызовом низкоуровневого API.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add — the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
// Headers
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");
// Sample data (9 rows)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);
// Add pivot table at E3 covering A1:C10
PivotTable pivotTable = sheet.PivotTables.Add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Фильтрация с одиночным выбором (отображение одного элемента страницы)**
В режиме одиночного выбора по умолчанию поле фильтра отображается как одиночный раскрывающийся список, и целочисленное значение `PivotField.CurrentPageItem` выбирает, какой элемент страницы управляет телом сводной таблицы. Присвоение конкретного индекса выбирает именно этот элемент; присвоение специального значения `0x7FFD` (десятичное 32765) снимает фильтр, после чего суммируются все элементы страницы одновременно. Одиночный выбор используется по умолчанию; включать его явно не требуется.

### Отображение всех элементов
Установка `CurrentPageItem` на магическое значение `0x7FFD` эквивалентна снятию фильтра страницы: тело сводной таблицы суммирует все элементы страницы так, как если бы фильтр не применялся.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
class Program
{
    static void Main()
    {
        // Create a new workbook
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        // Populate Fruit/Year/Amount data
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");
        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };
        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }
        // Create pivot table at E3
        var pivotTables = sheet.PivotTables;
        PivotTable pivotTable = pivotTables.Add("=A1:C7", 2, 4);
        // Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
        pivotTable.CalculateData();
        // Clear the page filter so every item in the page field is visible.
        // 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
        // equivalent to selecting "(All)" in Excel's page-field dropdown.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;
        workbook.Save("output.xlsx");
    }
}
```

### Отображение одного конкретного элемента
Присвоение `CurrentPageItem` реального индекса выбирает только этот один элемент страницы. Индекс — это позиция элемента в отсортированном списке элементов поля фильтраы, поэтому, например, `1` выбирает второй элемент после сортировки.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Create workbook
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;
// Add sample data (Fruit/Year/Amount)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");
cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");
cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");
cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");
// Add pivot table at E3
var pivotTables = sheet.PivotTables;
var pivotTable = pivotTables.Add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Page-field-specific operations
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Фильтрация с множественным выбором**
Фильтрация с множественным выбором превращает раскрывающийся список страницы в список флажков и позволяет конечному пользователю выбирать несколько элементов страницы одновременно. Aspose.Cells предоставляет два свойства, которые работают совместно. `PivotField.IsMultipleItemSelectionAllowed` должно быть установлено в `true`, чтобы интерфейс множественного выбора вообще начал действовать. После его включения `PivotItem.IsHidden` управляет тем, какие элементы отображаются в списке флажков, поэтому вы можете либо показать все элементы, либо внести в белый список только определённые элементы.
В приведённом ниже коде включается множественный выбор для того же поля фильтраы Year, созданного в сценарии 1а, а затем показаны два шаблона: Часть A раскрывает все элементы страницы, оставляя для каждой записи `IsHidden` равным `false`, тогда как Часть B вносит в белый список только выбранные вами исходные значения и скрывает все остальные через блок `switch (pivotItems[i].GetStringValue())`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data, Year→Page via AddFieldToArea).
//   Below we apply multi-select filtering on the page field.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Sample data: Fruit | Year | Amount
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");
string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}
Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
PivotTable pivotTable = pivots.Add("A1:C10", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// — Enable multi-select on the page field
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;
// Part A — select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}
// Part B — select only specific items by source value
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

> **Примечание:** При использовании фильтрации с множественным выбором через `PivotItem.IsHidden` **как минимум один `PivotItem` должен оставаться видимым** (`IsHidden == false`). Если все элементы скрыты, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Всегда проверяйте, что ваш белый список множественного выбора включает хотя бы один элемент из ваших исходных данных.

## **Какой API и какой режим следует использовать?**
В таблице ниже приведена сводка, когда использовать каждый API и режим, чтобы вы могли выбрать правильную комбинацию, не читая подробно каждый сценарий.
| Сценарий / Вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавить поле фильтра по имени исходного столбца (наиболее распространённый случай) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Высокоуровневый, однострочный. Используйте его, если вам не нужна ссылка на `PivotField`. |
| Добавить поле фильтра, когда у вас уже есть объект `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/a | Используйте, когда объект поля получен из другого места или его необходимо использовать повторно. |
| Фильтрация до одного элемента страницы (режим по умолчанию) | `PivotField.CurrentPageItem` | установить конкретный индекс | Например, `1` отображает второй элемент в отсортированном списке. |
| Показать все элементы / снять фильтр страницы | `PivotField.CurrentPageItem` | установить `0x7FFD` | Магическое значение `0x7FFD` (десятичное 32765) означает "все элементы". |
| Включить интерфейс множественного выбора в Excel | `PivotField.IsMultipleItemSelectionAllowed` | установить `true` | Требуется, чтобы любые вызовы `IsHidden` вступили в силу. |
| Скрытие / отображение отдельных элементов в списке множественного выбора | `PivotItem.IsHidden` | установить для каждого элемента | Как минимум один элемент должен оставаться видимым (`IsHidden == false`). |

{{% alert color="primary" %}}
Всегда помните об ограничении видимости при настройке фильтрации с множественным выбором. Если в поле фильтра с множественным выбором скрыт каждый `PivotItem`, Excel аварийно завершает работу при открытии файла или отображает пустую сводную таблицу. Составляйте белый список на основе ваших исходных данных так, чтобы хотя бы один элемент оставался видимым, и ваши сохранённые книги будут надёжно открываться на любом компьютере.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}