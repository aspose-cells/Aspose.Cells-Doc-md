---
title: Чтение и запись таблицы запросов рабочего листа
type: docs
weight: 40
url: /ru/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells предоставляет коллекцию Worksheet.QueryTables, которая возвращает объект типа QueryTable по индексу. Он имеет следующие два свойства

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Оба значения являются логическими. Вы можете просмотреть их в Microsoft Excel через Данные > Соединения > Свойства.

{{% /alert %}}

## Чтение и запись таблицы запросов рабочего листа

Следующий пример кода считывает первую таблицу QueryTable первого рабочего листа, а затем печатает оба свойства QueryTable. Затем он устанавливает для QueryTable.PreserveFormatting значение true.

Вы можете загрузить исходный файл Excel, используемый в этом коде, и выходной файл Excel, сгенерированный кодом, по следующим ссылкам.

- [Исходный файл Excel](5115533.xlsx)
- [Выходной файл Excel](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Консольный вывод

Вот консольный вывод приведенного выше примера кода

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Получить диапазон результатов таблицы запроса

 Aspose.Cells предоставляет возможность прочитать адрес, т.е. диапазон результатов ячеек для таблицы запросов. Следующий код демонстрирует эту функцию, читая адрес диапазона результатов для таблицы запроса. Образец файла можно скачать[здесь](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
