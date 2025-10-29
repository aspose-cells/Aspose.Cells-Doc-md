---
title: Копировать данные диапазона со стилем
type: docs
weight: 610
url: /ru/python-net/copy-range-data-with-style/
description: Эта статья описывает, как скопировать данные диапазона со стилем с использованием библиотеки Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, Python Как скопировать диапазон данных со стилем, Python Как скопировать диапазон данных со стилем с использованием библиотеки excel для python.
---

{{% alert color="primary" %}}

[Копировать только данные диапазона](/cells/ru/python-net/copy-range-data-only/) объясняет, как скопировать данные из диапазона ячеек в другой диапазон. В частности, процесс применяет новый набор стилей к скопированным ячейкам. Aspose.Cells для Python via .NET также может копировать диапазон с форматированием. В этой статье объясняется, как это сделать.

{{% /alert %}}

Aspose.Cells для Python via .NET предоставляет ряд классов и методов для работы с диапазонами, например, [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) и [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag).

Этот пример:

1. Создает рабочую книгу.
1. Заполняет ряд ячеек на первом листе данных.
1. Создайте объект [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) с указанными атрибутами форматирования.
1. Создайте объект [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) с указанными атрибутами форматирования.
1. Примените стиль к диапазону данных.
1. Создайте второй диапазон ячеек.
1. Скопируйте данные с форматированием из первого диапазона во второй диапазон.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
