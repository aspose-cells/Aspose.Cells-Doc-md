---
title: Чтение и запись запросов таблицы рабочего листа
type: docs
weight: 560
url: /ru/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет коллекцию [Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables), которая возвращает [QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection). Чтобы получить конкретную [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable), используйте свойство [QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\)) и передайте индекс QueryTable. Класс [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) имеет следующие два свойства для настройки QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Оба значения являются логическими. Вы можете просматривать их в Microsoft Excel через Data > Connections > Properties.

{{% /alert %}} 
## **Чтение и запись запроса таблицы листа**
Следующий образец кода считывает первую [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) первого рабочего листа и затем печатает оба свойства [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). Затем устанавливает [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) в **true**.

Следующий снимок экрана показывает [исходный файл Excel](5472578.xlsx), используемый в коде и его свойства, показывающие оба значения [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable).

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

Следующий снимок экрана показывает [выходной файл Excel](5472574.xlsx), сгенерированный кодом и его свойства, показывающие оба значения [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). Как видите, флажок Сохранить форматирование теперь установлен.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Вывод в консоль**
Вот вывод консоли из приведенного выше примера кода

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **Извлечение диапазона результата запроса таблицы**
Aspose.Cells предоставляет возможность чтения адреса, то есть диапазона результатов ячеек для запроса таблицы. Следующий код демонстрирует эту функцию, читая адрес диапазона результатов для таблицы запросов. Пример файла можно загрузить [здесь](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
