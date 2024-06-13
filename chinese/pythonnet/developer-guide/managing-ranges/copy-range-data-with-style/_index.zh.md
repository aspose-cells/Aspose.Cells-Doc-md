---
title: 仅复制范围数据和样式
type: docs
weight: 610
url: /zh/python-net/copy-range-data-with-style/
description: 本文介绍了如何在Python的Aspose.Cells via .NET库中使用样式复制范围数据。
keywords: Python Excel库，Python如何复制带样式的范围数据，Python如何使用python excel库复制带样式的范围数据。
---

{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/python-net/copy-range-data-only/)解释了如何将一个单元格范围的数据复制到另一个范围。具体来说，它会为复制的单元格应用一组新样式。 Aspose.Cells for Python via .NET还可以复制带有格式的范围。本文进行了解释。

{{% /alert %}}

Aspose.Cells for Python via .NET提供了一系列用于处理范围的类和方法，例如，[**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)、[**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)和[**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag)。

此示例：

1. 创建一个工作簿。
1. 在第一个工作表中填充多个单元格的数据。
1. 创建一个 [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)。
1. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 对象。
1. 将样式应用到数据范围。
1. 创建第二个单元格范围。
1. 将第一个范围的带有格式的数据复制到第二个范围。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
