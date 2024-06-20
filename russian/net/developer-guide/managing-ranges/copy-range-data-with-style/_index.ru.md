---
title: Копировать данные диапазона со стилем
type: docs
weight: 610
url: /ru/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Копирование только данных диапазона](/cells/ru/net/copy-range-data-only/) объясняет, как скопировать данные из диапазона ячеек в другой диапазон. А именно, он применяет новый набор стилей к скопированным ячейкам. Aspose.Cells также может копировать диапазон полностью с форматированием. В этой статье объясняется как.

{{% /alert %}}

Aspose.Cells предоставляет ряд классов и методов для работы с диапазонами, например, [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) и [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Этот пример:

1. Создает рабочую книгу.
1. Заполняет ряд ячеек на первом листе данных.
1. Создайте объект [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) с указанными атрибутами форматирования.
1. Создайте объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) с указанными атрибутами форматирования.
1. Примените стиль к диапазону данных.
1. Создайте второй диапазон ячеек.
1. Скопируйте данные с форматированием из первого диапазона во второй диапазон.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
