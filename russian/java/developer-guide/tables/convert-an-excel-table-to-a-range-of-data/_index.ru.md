---
title: Преобразовать таблицу Excel в диапазон данных
type: docs
weight: 10
url: /ru/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

Иногда вы создаете таблицу в Microsoft Excel и не хотите продолжать работу с функциональностью таблицы, которая в ней есть. Вместо этого вы хотите что-то, что похоже на таблицу. Чтобы сохранить данные в таблице без потери форматирования, преобразуйте таблицу в обычный диапазон данных.

Aspose.Cells поддерживает эту функцию Microsoft Excel для таблиц и объектов-списков.

{{% /alert %}}

## **Использование Microsoft Excel**

Используйте функцию **Преобразовать в диапазон** , чтобы быстро преобразовать таблицу в диапазон без потери форматирования. В Microsoft Excel 2007/2010:

1. Щелкните в любом месте таблицы, чтобы активная ячейка находилась в столбце таблицы.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. На вкладке **Разрботка** , в группе **Инструменты** , щелкните **Преобразовать в диапазон** .

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

После преобразования таблицы в диапазон функции таблицы больше не доступны. Например, заголовки строк больше не включают стрелки сортировки и фильтра, и структурированные ссылки (ссылки, использующие имена таблиц) , используемые в формулах, превращаются в обычные ссылки на ячейки.

{{% /alert %}}

## **Использование Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Преобразовать таблицу в диапазон с параметрами**

Aspose.Cells предоставляет дополнительные параметры при преобразовании таблицы в диапазон через класс [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions). Класс [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) предоставляет свойство [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow), которое позволяет установить последний индекс строки таблицы. Форматирование таблицы будет сохранено до указанного индекса строки, а остальное форматирование будет удалено.

Приведенный ниже примерный код демонстрирует использование класса [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
