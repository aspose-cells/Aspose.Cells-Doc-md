---
title: Таблицы и диапазоны
type: docs
weight: 50
url: /ru/net/tables-and-ranges/
---

## **Введение**

Иногда вы создаете таблицу в Microsoft Excel и не хотите продолжать работу с функциональностью таблицы, которая в ней есть. Вместо этого вы хотите что-то, что похоже на таблицу. Чтобы сохранить данные в таблице без потери форматирования, преобразуйте таблицу в обычный диапазон данных.
Aspose.Cells действительно поддерживает эту функцию Microsoft Excel для таблиц и объектов списка.

## **Использование Microsoft Excel**

Используйте функцию **Преобразовать в диапазон** , чтобы быстро преобразовать таблицу в диапазон без потери форматирования. В Microsoft Excel 2007/2010:

1. Щелкните в любом месте таблицы, чтобы активная ячейка находилась в столбце таблицы.
1. На вкладке **Разрботка** , в группе **Инструменты** , щелкните **Преобразовать в диапазон** .

## **Использование Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

После преобразования таблицы в диапазон функции таблицы больше не доступны. Например, заголовки строк больше не включают стрелки сортировки и фильтра, и структурированные ссылки (ссылки, использующие имена таблиц) , используемые в формулах, превращаются в обычные ссылки на ячейки.

{{% /alert %}}

## **Преобразовать таблицу в диапазон с параметрами**

Aspose.Cells предоставляет дополнительные опции при преобразовании таблицы в диапазон с помощью класса [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions).  Класс [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) предоставляет свойство [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow), которое позволяет установить последний индекс строки таблицы. Форматирование таблицы будет сохранено до указанного индекса строки, а остальное форматирование будет удалено.

Приведенный ниже примерный код демонстрирует использование класса [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
