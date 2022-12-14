---
title: Преобразование таблицы Excel в диапазон данных
type: docs
weight: 10
url: /ru/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

Иногда вы создаете таблицу в Microsoft Excel и не хотите продолжать работать с ее функциональностью. Вместо этого вам нужно что-то похожее на стол. Чтобы сохранить данные в таблице без потери форматирования, преобразуйте таблицу в обычный диапазон данных.

Aspose.Cells поддерживает эту функцию Microsoft Excel для таблиц и объектов-списков.

{{% /alert %}}

## **Использование Microsoft Excel**

 Использовать**Преобразовать в диапазон** функция быстрого преобразования таблицы в диапазон без потери форматирования. В Microsoft Excel 2007/2010:

1. Щелкните в любом месте таблицы, чтобы убедиться, что активная ячейка находится в столбце таблицы.

![дело:изображение_альтернативный_текст](convert-an-excel-table-to-a-range-of-data_1.gif)

1.  На**Дизайн** вкладка, в**Инструменты** группа, нажмите**Преобразовать в диапазон**.

![дело:изображение_альтернативный_текст](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Функции таблицы больше не доступны после преобразования таблицы в диапазон. Например, заголовки строк больше не включают стрелки сортировки и фильтрации, а структурированные ссылки (ссылки, использующие имена таблиц), которые использовались в формулах, превращаются в обычные ссылки на ячейки.

{{% /alert %}}

## **Использование Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Преобразование таблицы в диапазон с параметрами**

Aspose.Cells предоставляет дополнительные параметры при преобразовании таблицы в диапазон с помощью[**Таблетторангеоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)учебный класс.[**Таблетторангеоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)класс предоставляет[**Последняя строка**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)свойство, которое позволяет вам установить последний индекс строки таблицы. Форматирование таблицы будет сохранено до указанного индекса строки, а остальное форматирование будет удалено.

Пример кода, приведенный ниже, демонстрирует использование[**Таблетторангеоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)учебный класс.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
