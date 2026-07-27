---
title: Добавить поля фильтров в сводную таблицу в Aspose.Cells для .NET
linktitle: Добавить поля фильтров
description: Узнайте, как добавлять и настраивать поля фильтра в сводных таблицах с помощью Aspose.Cells for Node.js via C++, включая добавление полей фильтра, фильтрацию с одиночным выбором и фильтрацию с множественным выбором.
keywords: Aspose.Cells, Node.js via C++, сводная таблица, поле фильтра, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, фильтр
type: docs
weight: 250
url: /ru/nodejs-cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает полный жизненный цикл полей фильтра в сводных таблицах. Вы можете добавить поле фильтра через высокоуровневый удобный API или через низкоуровневую коллекцию `PageFields`, управлять фильтром страниц в режиме одиночного выбора, очищать его для отображения всех элементов страницы или переключать поле в режим множественного выбора, чтобы пользователи могли выбирать несколько элементов страницы одновременно через интерфейс с флажками в Excel.
{{% /alert %}}

## **Введение**

поле фильтра — это поле сводной таблицы, которое управляет *тем, какое подмножество* исходных данных отображается в теле сводной таблицы. Конечные пользователи видят его как раскрывающийся список в верхней части отображённой сводной таблицы в Excel, и выбор одного из доступных элементов страницы перестраивает тело сводной таблицы так, чтобы суммировались только записи, принадлежащие этому элементу страницы. Поле сводной таблицы становится полем страницы, когда оно зарегистрировано как `PivotFieldType.Page`, а не как `PivotFieldType.Row`, `PivotFieldType.Column` или `PivotFieldType.Data`.

поле фильтра может работать в двух режимах. В режиме **одиночного выбора** по умолчанию одновременно виден только один элемент страницы, поэтому тело сводной таблицы суммирует ровно одно подмножество. В режиме **множественного выбора** поле отображает список с флажками, и тело сводной таблицы суммирует объединение всех отмеченных элементов страницы. Одно и то же исходное поле можно переключать между этими режимами, изменяя значение одного свойства.

Aspose.Cells for Node.js via C++ предоставляет два эквивалентных способа регистрации поля фильтраы. Высокоуровневый API — это `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, который принимает имя исходного столбца и добавляет поле одним вызовом. Низкоуровневый API — это `PivotTable.pageFields.add(PivotField)`, который используется, когда у вас уже есть ссылка на `PivotField` и вы хотите добавить тот же экземпляр поля в область фильтраы. Оба API в итоге заполняют одну и ту же коллекцию `PageFields`, и далее в этой статье показано, как выбирать между ними и как управлять каждым режимом фильтрации.

## **Добавление поля фильтраы**

Существует два способа зарегистрировать поле сводной таблицы в области страницы. Высокоуровневый вызов принимает имя исходного столбца в виде строки и является наиболее распространённым путём. Низкоуровневый вызов принимает существующий экземпляр `PivotField` и удобен, когда тот же объект поля должен использоваться в нескольких областях сводной таблицы. Оба вызова помещают поле в `PivotTable.pageFields`, после чего оно появляется как раскрывающийся список страницы в верхней части отображённой сводной таблицы.

### Добавление поля фильтраы с помощью addFieldToArea

Следующий пример создаёт небольшой набор данных Fruit / Year / Amount, размещает сводную таблицу в ячейке E3 с `Fruit` в области строк, `Amount` в области данных и `Year` в области страницы, обновляет сводную таблицу и сохраняет рабочую книгу.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Настраиваем строку заголовка
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Заполняем 9 строк образцами данных: Фрукт, Год, Количество
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

// Добавляем поля в области: Fruit как строка, Amount как данные, Year как поле страницы
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Обновляем и вычисляем данные сводной таблицы
pivotTable.refreshData();
pivotTable.calculateData();

// Сохраняем книгу
workbook.save("pageFieldSample.xlsx");
```

### Добавление поля фильтраы с помощью pageFields.add

Когда вы уже работаете с экземпляром `PivotField`, вы можете передать его напрямую в `PivotTable.pageFields.add`. Сводная таблица и поле фильтра создаются точно так же, как в предыдущем сценарии; только последняя регистрация в области страницы заменяется вызовом низкоуровневого API.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Заголовки
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Пример данных (9 строк)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Добавить сводную таблицу в E3, охватывающую A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Строка, Amount -> Данные (Year будет добавлен в область Страница ниже)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Низкоуровневый подход: получить существующее PivotField Year из BaseFields
// и зарегистрировать его в области Страница через PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Обновить, чтобы новое поле страницы отразилось в сохранённой книге
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Фильтрация с одиночным выбором (отображение одного элемента страницы)**

В режиме одиночного выбора по умолчанию поле фильтра отображается как один раскрывающийся список, и целочисленное значение `PivotField.currentPageItem` выбирает, какой элемент страницы управляет телом сводной таблицы. Присвоение конкретного индекса выбирает этот один элемент; присвоение специального значения `0x7FFD` (десятичное 32765) снимает фильтр, так что все элементы страницы суммируются одновременно. Одиночный выбор используется по умолчанию; вам не нужно включать его явно.

### Отображение всех элементов

Установка `currentPageItem` на магическое значение `0x7FFD` эквивалентна снятию фильтра страницы: тело сводной таблицы суммирует все элементы страницы, как если бы фильтр не был применён.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Заполнение данных Fruit/Year/Amount
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Создание сводной таблицы в E3
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// Настройка полей сводной таблицы: Fruit→Строка, Amount→Данные, Year→Страница
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Сброс фильтра страницы, чтобы каждый элемент поля страницы был виден.
// 0x7FFD (десятичное 32765) — это специальное значение-маркер, означающее "все элементы" —
// эквивалентно выбору "(Все)" в раскрывающемся списке поля страницы Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Отображение одного конкретного элемента

Установка `currentPageItem` на реальный индекс выбирает только этот один элемент страницы. Индекс — это позиция элемента в отсортированном списке элементов поля фильтраы, поэтому, например, `1` выбирает второй элемент после сортировки.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Добавляем пример данных (Фрукт/Год/Количество)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// Добавляем сводную таблицу в ячейку E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Добавляем поля: Fruit→Строка, Amount→Данные, Year→Страница
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Операции, специфичные для поля страницы
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = второй элемент в отсортированном порядке (например, "2021")

// Обновляем и пересчитываем сводную таблицу
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Фильтрация с множественным выбором**

Фильтрация с множественным выбором превращает раскрывающийся список страницы в список с флажками и позволяет конечному пользователю выбирать несколько элементов страницы одновременно. Aspose.Cells предоставляет два свойства, которые работают вместе. `PivotField.isMultipleItemSelectionAllowed` должно быть установлено в `true`, прежде чем интерфейс множественного выбора начнёт действовать. После его включения `PivotItem.isHidden` управляет тем, какие элементы отображаются в списке с флажками, поэтому вы можете либо показать все элементы, либо включить в белый список только конкретные элементы.

Код ниже включает множественный выбор для того же поля фильтраы Year, созданного в сценарии 1a, а затем демонстрирует два шаблона: Часть A показывает все элементы страницы, оставляя `isHidden` равным `false` для каждой записи, тогда как Часть B включает в белый список только выбранные вами исходные значения и скрывает все остальные через блок `switch (pivotItems[i].getStringValue())`.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// Пример данных: Фрукт | Год | Количество
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// — Включить множественный выбор в поле страницы
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// Часть A — выбрать ВСЕ элементы (сделать каждый элемент видимым)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// Часть B — выбрать только конкретные элементы по исходному значению
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Примечание:** При использовании фильтрации с множественным выбором через `PivotItem.isHidden`, **по крайней мере один `PivotItem` должен оставаться видимым** (`isHidden == false`). Если все элементы скрыты, Excel либо аварийно завершает работу при открытии файла, либо отображает пустую сводную таблицу. Всегда проверяйте, что ваш белый список множественного выбора включает хотя бы один элемент из ваших исходных данных.

## **Какой API и какой режим следует использовать?**

Таблица ниже обобщает, когда использовать каждый API и режим, чтобы вы могли выбрать правильную комбинацию без необходимости читать каждый сценарий подробно.

| Сценарий / Вариант использования | Рекомендуемый API | Используемое свойство | Примечания |
|---|---|---|---|
| Добавить поле фильтра по имени исходного столбца (наиболее распространённый случай) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Высокоуровневый, однострочный. Используйте его, если вам не нужна ссылка на `PivotField`. |
| Добавить поле фильтра, когда у вас уже есть объект `PivotField` | `PivotTable.pageFields.add(PivotField)` | n/a | Используйте, когда объект поля был получен в другом месте или должен использоваться повторно. |
| Фильтрация до одного элемента страницы (режим по умолчанию) | `PivotField.currentPageItem` | установить на конкретный индекс | Например, `1` показывает второй элемент в отсортированном списке. |
| Показать все элементы / снять фильтр страницы | `PivotField.currentPageItem` | установить на `0x7FFD` | Магическое значение `0x7FFD` (десятичное 32765) является маркером «все элементы». |
| Включить интерфейс множественного выбора в Excel | `PivotField.isMultipleItemSelectionAllowed` | установить в `true` | Требуется до того, как любые вызовы `isHidden` вступят в силу. |
| Скрыть / показать отдельные элементы в списке множественного выбора | `PivotItem.isHidden` | устанавливается для каждого элемента | По крайней мере один элемент должен оставаться видимым (`isHidden == false`). |

{{% alert color="primary" %}}
Всегда помните об ограничении видимости при настройке фильтрации с множественным выбором. Если каждый `PivotItem` в поле фильтра с множественным выбором скрыт, Excel аварийно завершает работу при открытии или отображает пустую сводную таблицу. Создавайте свой белый список на основе исходных данных так, чтобы хотя бы один элемент оставался видимым, и ваши сохранённые рабочие книги будут надёжно открываться на любом компьютере.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}