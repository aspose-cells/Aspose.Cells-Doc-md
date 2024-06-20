---
title: Чтение и запись запросов таблицы рабочего листа
type: docs
weight: 40
url: /ru/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет коллекцию Worksheet.QueryTables, которая возвращает объект типа QueryTable по индексу. У него есть два следующих свойства

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Оба этих значения являются логическими. Вы можете просмотреть их в Microsoft Excel через Данные > Подключения > Свойства.

{{% /alert %}}

## Чтение и запись запросов таблицы рабочего листа

Следующий образец кода считывает первую таблицу запросов первого рабочего листа и затем выводит оба свойства таблицы запросов. Затем устанавливает QueryTable.PreserveFormatting в true.

Вы можете загрузить исходный файл Excel, используемый в этом коде, и выходной файл Excel, созданный кодом, по следующим ссылкам.

- [Исходный файл Excel](5115533.xlsx)
- [Выходной файл Excel](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Вывод в консоли

Вот вывод консоли из приведенного выше примера кода

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Получение диапазона результатов запроса таблицы

Aspose.Cells предоставляет возможность чтения адреса, то есть диапазона результатов ячеек для таблицы запросов. Следующий код демонстрирует эту функцию, считывая адрес диапазона результатов для таблицы запросов. Образец файла можно скачать [здесь](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
