---
title: Чтение и запись таблицы запросов листа с помощью Node.js через C++
linktitle: Чтение и запись запросов таблицы рабочего листа
type: docs
weight: 40
url: /ru/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет коллекцию Worksheet.QueryTables, которая возвращает объект типа QueryTable по индексу. У него есть два следующих свойства

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

Оба этих значения являются логическими. Вы можете просмотреть их в Microsoft Excel через Данные > Подключения > Свойства.

{{% /alert %}}

## Чтение и запись запросов таблицы рабочего листа

Следующий пример кода читает первую QueryTable первого листа и выводит оба свойства QueryTable. Затем он устанавливает свойство QueryTable.preserveFormatting в значение true.

Вы можете загрузить исходный файл Excel, используемый в этом коде, и выходной файл Excel, созданный кодом, по следующим ссылкам.

- [Исходный файл Excel](5115533.xlsx)
- [Выходной файл Excel](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### Вывод в консоли

Вот вывод консоли из приведенного выше примера кода

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Получение диапазона результатов запроса таблицы

Aspose.Cells предоставляет возможность чтения адреса, то есть диапазона результатов ячеек для таблицы запросов. Следующий код демонстрирует эту функцию, считывая адрес диапазона результатов для таблицы запросов. Образец файла можно скачать [здесь](72417290.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
