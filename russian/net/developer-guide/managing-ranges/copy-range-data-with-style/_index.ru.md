---
title: Копировать данные диапазона со стилем
type: docs
weight: 610
url: /ru/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[Копировать только данные диапазона](/cells/ru/net/copy-range-data-only/) объяснил, как копировать данные из диапазона ячеек в другой диапазон. В частности, он применил новый набор стилей к скопированным ячейкам. Aspose.Cells также может копировать диапазон с форматированием. В этой статье объясняется, как.

{{% /alert %}}

Aspose.Cells предоставляет ряд классов и методов для работы с диапазонами, например,[**Создатьдиапазон()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**СтильФлаг**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) а также[**ПрименитьСтиль()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Этот пример:

1. Создает рабочую книгу.
1. Заполняет ряд ячеек на первом листе данными.
1.  Создает[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  Создает[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объект с указанными атрибутами форматирования.
1. Применяет стиль к диапазону данных.
1. Создает второй диапазон ячеек.
1. Копирует данные с форматированием из первого диапазона во второй диапазон.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
