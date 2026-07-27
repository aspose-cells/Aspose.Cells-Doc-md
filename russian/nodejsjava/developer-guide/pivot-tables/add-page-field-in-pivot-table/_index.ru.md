---
title: Добавить поля фильтров в сводную таблицу в Aspose.Cells для .NET
linktitle: Добавить поля фильтров
description: Узнайте, как добавлять и настраивать поля фильтра в сводных таблицах с помощью Aspose.Cells for Node.js via Java, включая добавление полей фильтра, фильтрацию с одиночным выбором и множественную фильтрацию.
keywords: Aspose.Cells, Node.js via Java, сводная таблица, поле фильтра, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, фильтр
type: docs
weight: 250
url: /ru/nodejs-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает полный жизненный цикл полей фильтра в сводных таблицах. Вы можете добавить поле фильтра через высокоуровневый удобный API или через низкоуровневую коллекцию `PageFields`, а также управлять фильтром страницы в режиме одиночного выбора, очищать его, чтобы отобразить все элементы страницы, или переключать поле в режим множественного выбора, чтобы пользователи могли выбирать несколько элементов страницы одновременно через интерфейс флажков в Excel.
{{% /alert %}}

## **Введение**

поле фильтра — это поле сводной таблицы, которое управляет *тем, какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его как раскрывающийся список в верхней части отображаемой сводной таблицы в Excel, и выбор одного из доступных элементов страницы перестраивает тело сводной таблицы так, чтобы суммировались только записи, принадлежащие этому элементу страницы. Поле сводной таблицы становится полем страницы, когда оно зарегистрировано как `PivotFieldType.Page`, а не как `PivotFieldType.Row`, `PivotFieldType.Column` или `PivotFieldType.Data`.

поле фильтра может работать в двух режимах. В режиме по умолчанию **одиночного выбора** одновременно виден только один элемент страницы, поэтому тело сводной таблицы суммирует ровно одно подмножество. В режиме **множественного выбора** поле отображает список флажков, и тело сводной таблицы суммирует объединение каждого отмеченного элемента страницы. То же самое исходное поле можно переключать между этими режимами, изменяя одно свойство.

Aspose.Cells for Node.js via Java предоставляет два эквивалентных способа регистрации поля фильтраы. Высокоуровневый API — это `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, который принимает имя исходного столбца и добавляет поле одним вызовом. Низкоуровневый API — это `pivotTable.getPageFields().add(PivotField)`, который используется, когда у вас уже есть ссылка на `PivotField` и вы хотите добавить тот же экземпляр поля в область фильтраы. Оба API в итоге заполняют одну и ту же коллекцию `PageFields`, и остальная часть этой статьи демонстрирует, как выбирать между ними и как управлять каждым режимом фильтрации.

## **Добавление поля фильтраы**

Существует два способа зарегистрировать поле сводной таблицы в области страницы. Высокоуровневый вызов принимает имя исходного столбца в виде строки и является наиболее распространённым путём. Низкоуровневый вызов принимает существующий экземпляр `PivotField` и удобен, когда тот же объект поля должен быть повторно использован в нескольких областях сводной таблицы. Оба вызова помещают поле в `pivotTable.getPageFields()`, после чего оно отображается как раскрывающийся список страницы в верхней части отображаемой сводной таблицы.

### Добавление поля фильтраы с помощью addFieldToArea

Следующий пример создаёт небольшой набор данных Фрукт / Год / Сумма, размещает сводную таблицу в ячейке E3 с `Fruit` в области строк, `Amount` в области данных и `Year` в области страницы, обновляет сводную таблицу и сохраняет рабочую книгу.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Настраиваем строку заголовков
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Заполняем 9 строк примерами данных: Фрукт, Год, Количество
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// Добавляем сводную таблицу с привязкой к ячейке E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Добавляем поля в области: Фрукт как строка, Количество как данные, Год как поле страницы
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Обновляем и рассчитываем данные сводной таблицы
pivotTable.refreshData();
pivotTable.calculateData();

// Сохраняем книгу
workbook.save("pageFieldSample.xlsx");
```

### Добавление поля фильтраы с помощью getPageFields().add

Если вы уже работаете с экземпляром `PivotField`, вы можете передать его напрямую в `pivotTable.getPageFields().add`. Сводная таблица и поле фильтра создаются точно так же, как в предыдущем сценарии; только финальная регистрация в области страницы заменяется вызовом низкоуровневого API.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Заголовки
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Пример данных (9 строк)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Добавить сводную таблицу в E3, охватывающую A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Строка, Amount -> Данные (Year будет добавлен в область Страница ниже)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Низкоуровневый подход: получить существующий PivotField Year из BaseFields
// и зарегистрировать его в области Страница через PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Обновить, чтобы новое поле страницы отразилось в сохранённой книге
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Фильтрация с одиночным выбором (отображение одного элемента страницы)**

В режиме одиночного выбора по умолчанию поле фильтра отображается как один раскрывающийся список, и целочисленное значение `PivotField.CurrentPageItem` выбирает, какой элемент страницы управляет телом сводной таблицы. Присвоение конкретного индекса выбирает этот один элемент; присвоение специального значения-маркера `0x7FFD` (десятичное 32765) очищает фильтр, так что все элементы страницы суммируются одновременно. Одиночный выбор используется по умолчанию; вам не нужно включать его явно.

### Отображение всех элементов

Установка `CurrentPageItem` на магическое значение `0x7FFD` эквивалентна очистке фильтра страницы — тело сводной таблицы суммирует все элементы страницы, как если бы фильтр не применялся.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// Заполнение данных Фрукт/Год/Сумма
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Создание сводной таблицы в E3
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// Настройка полей сводной таблицы: Фрукт→Строка, Сумма→Данные, Год→Страница
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Очистка фильтра страницы, чтобы каждый элемент в поле страницы был виден.
// 0x7FFD (десятичное 32765) — это специальное значение-маркер, означающее «все элементы» —
// эквивалентно выбору «(Все)» в раскрывающемся списке поля страницы Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Отображение одного конкретного элемента

Установка `CurrentPageItem` на реальный индекс выбирает только этот один элемент страницы. Индекс — это позиция элемента в отсортированном списке элементов поля фильтраы, поэтому, например, `1` выбирает второй элемент после сортировки.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Добавление образца данных (Фрукт/Год/Сумма)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// Добавление сводной таблицы в E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Добавление полей: Фрукт→Строка, Сумма→Данные, Год→Страница
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Операции, специфичные для поля страницы
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = второй элемент в отсортированном порядке (например, "2021")

// Обновление и вычисление сводной таблицы
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Фильтрация с множественным выбором**

Фильтрация с множественным выбором превращает раскрывающийся список страницы в список флажков и позволяет конечному пользователю выбирать несколько элементов страницы одновременно. Aspose.Cells предоставляет два свойства, которые работают вместе. Свойство `PivotField.IsMultipleItemSelectionAllowed` должно быть установлено в `true`, прежде чем интерфейс множественного выбора начнёт действовать. После его включения свойство `PivotItem.IsHidden` управляет тем, какие элементы отображаются в списке флажков, поэтому вы можете либо показать все элементы, либо включить в белый список только определённые элементы.

Код ниже включает множественный выбор для того же поля фильтраы Year, созданного в Сценарии 1a, а затем показывает два шаблона. Часть A раскрывает все элементы страницы, оставляя `IsHidden` установленным в `false` для каждой записи, тогда как Часть B включает в белый список только выбранные вами исходные значения и скрывает все остальные с помощью блока `switch (pivotItems[i].getStringValue())`.

```javascript
const AsposeCells = require("aspose.cells");

// — Сводная таблица и поле страницы создаются точно так же, как в
//   Сценарии 1a (данные Fruit/Year/Amount, сводная таблица в E3, Fruit→Строка,
//   Amount→Данные, Year→Страница через AddFieldToArea).
//   Ниже мы применяем фильтрацию с множественным выбором для поля страницы.

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// Пример данных: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — Включить множественный выбор для поля страницы
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// Часть A — выбрать ВСЕ элементы (сделать каждый элемент видимым)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// Часть B — выбрать только конкретные элементы по исходному значению
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Примечание:** При использовании фильтрации с множественным выбором через `PivotItem.IsHidden` **как минимум один `PivotItem` должен оставаться видимым** (`IsHidden == false`). Если все элементы скрыты, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Всегда проверяйте, что ваш белый список множественного выбора включает как минимум один элемент из ваших исходных данных.

## **Какой API и какой режим следует использовать?**

Таблица ниже обобщает, когда использовать каждый API и режим, чтобы вы могли выбрать правильную комбинацию, не читая каждый сценарий подробно.

| Сценарий / Вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавить поле фильтра по имени исходного столбца (наиболее распространённый случай) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Высокоуровневый, однострочный. Используйте его, если вам не нужна ссылка на `PivotField`. |
| Добавить поле фильтра, когда у вас уже есть объект `PivotField` | `pivotTable.getPageFields().add(PivotField)` | n/a | Используйте, когда объект поля был получен в другом месте или должен быть повторно использован. |
| Фильтрация до одного элемента страницы (режим по умолчанию) | `PivotField.CurrentPageItem` | установить на конкретный индекс | Например, `1` показывает второй элемент в отсортированном списке. |
| Показать все элементы / очистить фильтр страницы | `PivotField.CurrentPageItem` | установить на `0x7FFD` | Магическое значение `0x7FFD` (десятичное 32765) — это маркер для «все элементы». |
| Включить интерфейс множественного выбора в Excel | `PivotField.IsMultipleItemSelectionAllowed` | установить в `true` | Требуется, чтобы любые вызовы `IsHidden` вступили в силу. |
| Скрыть / показать отдельные элементы в списке множественного выбора | `PivotItem.IsHidden` | установить для каждого элемента | Как минимум один элемент должен оставаться видимым (`IsHidden == false`). |

{{% alert color="primary" %}}
Всегда помните об ограничении видимости при настройке фильтрации с множественным выбором. Если каждый `PivotItem` в поле фильтра с множественным выбором скрыт, Excel аварийно завершает работу при открытии или отображает пустую сводную таблицу. Создавайте свой белый список на основе исходных данных так, чтобы как минимум один элемент оставался видимым, и ваши сохранённые рабочие книги будут надёжно открываться на любом компьютере.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}