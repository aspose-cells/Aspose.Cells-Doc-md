---
title: Чтение и запись таблицы запросов рабочего листа
type: docs
weight: 560
url: /ru/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

 Aspose.Cells предоставляет[Рабочий лист.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) коллекция, которая возвращает[QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) . Чтобы получить конкретное[таблица запросов](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) , использовать[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) и передать индекс QueryTable.[таблица запросов](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) Класс имеет следующие два свойства для настройки QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Оба значения являются логическими. Вы можете просмотреть их в Microsoft Excel через Данные > Соединения > Свойства.

{{% /alert %}} 
## **Чтение и запись таблицы запросов рабочего листа**
 Следующий пример кода считывает первый[таблица запросов](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)первого рабочего листа, а затем печатает оба[таблица запросов](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) характеристики. Затем он устанавливает[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) к**истинный**.

На следующем снимке экрана показано[исходный файл excel](5472578.xlsx) используемый в коде, и его свойства, показывающие оба[таблица запросов](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)ценности.

![дело:изображение_альтернативный_текст](reading-and-writing-query-table-of-worksheet_1.png)

На следующем снимке экрана показано[выходной файл excel](5472574.xlsx) сгенерированный кодом, и его свойства, показывающие оба[таблица запросов](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)ценности. Как видите, флажок «Сохраненное форматирование» теперь установлен.

![дело:изображение_альтернативный_текст](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Консольный вывод**
Вот консольный вывод приведенного выше примера кода

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **Получить диапазон результатов таблицы запроса**
Aspose.Cells предоставляет возможность прочитать адрес, т.е. диапазон результатов ячеек для таблицы запросов. Следующий код демонстрирует эту функцию, читая адрес диапазона результатов для таблицы запросов. Образец файла можно скачать[здесь](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
