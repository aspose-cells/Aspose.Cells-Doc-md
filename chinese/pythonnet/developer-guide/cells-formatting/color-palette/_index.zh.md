---
title: 如何使用颜色调色板
type: docs
weight: 80
url: /zh/python-net/excel-color-palette/
description: 使用Aspose.Cells for Python via .NET API向调色板添加自定义颜色并使用Excel调色板的Python代码示例
keywords: 使用Python向调色板添加自定义颜色，Python程序化操作Excel调色板，程序化在工作簿中如何使用调色板，Python中如何在Excel中使用调色板
---

## **颜色和调色板**

调色板是在创建图像时可用的颜色数量。在演示文稿中使用标准调色板可以让用户创建一致的外观。每个Microsoft Excel（97-2003）文件都有一个包含可应用于单元格、字体、网格线、图形对象、填充和图表中的线条的56种颜色的调色板。

使用 Aspose.Cells for Python via .NET，不仅可以使用调色板中的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，首先将其添加到调色板中。

本主题讨论如何向调色板中添加自定义颜色。

## **向调色板添加自定义颜色**

Aspose.Cells for Python via .NET 支持微软 Excel 的 56 种调色板。若要使用调色板中未定义的自定义颜色，请将其添加到调色板中。

Aspose.Cells for Python via .NET 提供了一个类 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，表示微软 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类提供了一个 [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette) 方法，带有以下参数，用于添加自定义颜色以修改调色板：

- Custom Color，要添加的自定义颜色。
- Index，自定义颜色在调色板中的索引，将替换指定的颜色。应该在 0-55 之间。

下面的示例在应用于字体之前向调色板中添加了自定义颜色（兰花紫）。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

调色板只能容纳 56 种颜色。当向调色板中添加自定义颜色时，调色板会改变，文件中用先前颜色格式化的任何元素也会发生变化。因此，在更改调色板时，请务必小心。此外，在 XLS（Excel 97 - 2003）文件格式中，这是唯一的限制，XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式则没有这种限制。

{{% /alert %}}

