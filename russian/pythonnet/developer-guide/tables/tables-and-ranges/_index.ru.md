---
title: Таблицы и диапазоны
type: docs
weight: 50
url: /ru/python-net/tables-and-ranges/
---

## **Введение**

Иногда вы создаете таблицу в Microsoft Excel и не хотите продолжать работу с функциональностью таблицы, которая в ней есть. Вместо этого вы хотите что-то, что похоже на таблицу. Чтобы сохранить данные в таблице без потери форматирования, преобразуйте таблицу в обычный диапазон данных.
Aspose.Cells for Python via .NET поддерживает данную функцию Microsoft Excel для таблиц и списков объектов.

## **Использование Microsoft Excel**

Используйте функцию **Преобразовать в диапазон** , чтобы быстро преобразовать таблицу в диапазон без потери форматирования. В Microsoft Excel 2007/2010:

1. Щелкните в любом месте таблицы, чтобы активная ячейка находилась в столбце таблицы.
1. На вкладке **Разрботка** , в группе **Инструменты** , щелкните **Преобразовать в диапазон** .

## **Использование Aspose.Cells for Python via .NET**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

После преобразования таблицы в диапазон функции таблицы больше не доступны. Например, заголовки строк больше не включают стрелки сортировки и фильтра, и структурированные ссылки (ссылки, использующие имена таблиц) , используемые в формулах, превращаются в обычные ссылки на ячейки.

{{% /alert %}}

## **Преобразовать таблицу в диапазон с параметрами**

Aspose.Cells for Python via .NET предоставляет дополнительные опции при преобразовании таблицы в диапазон через класс [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions). Класс [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) предоставляет свойство [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/), которое позволяет установить последний индекс строки таблицы. Форматирование таблицы сохранится до указанного индекса строки, а остальное форматирование удалится.

Приведенный ниже примерный код демонстрирует использование класса [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
