---
title: Чтение и запись запросов таблицы рабочего листа
type: docs
weight: 40
url: /ru/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET предоставляет коллекцию Worksheet.QueryTables, которая возвращает объект типа QueryTable по индексу. Он имеет следующие два свойства

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Оба этих значения являются логическими. Вы можете просмотреть их в Microsoft Excel через Данные > Подключения > Свойства.

{{% /alert %}}

## Чтение и запись запросов таблицы рабочего листа

Следующий образец кода считывает первую таблицу запросов первого рабочего листа и затем выводит оба свойства таблицы запросов. Затем устанавливает QueryTable.PreserveFormatting в true.

Вы можете загрузить исходный файл Excel, используемый в этом коде, и выходной файл Excel, созданный кодом, по следующим ссылкам.

- [Исходный файл Excel](5115533.xlsx)
- [Выходной файл Excel](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### Вывод в консоли

Вот вывод консоли из приведенного выше примера кода

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Получение диапазона результатов запроса таблицы

Aspose.Cells для Python via .NET предоставляет возможность читать адрес, то есть диапазон результатов ячеек для таблицы запроса. Следующий код демонстрирует эту функцию, считывая адрес диапазона результатов для таблицы запроса. Образец файла можно скачать [здесь](72417290.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

