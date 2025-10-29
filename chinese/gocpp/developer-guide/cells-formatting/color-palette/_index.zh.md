---
title: 如何在 C++ 中使用颜色调色板
linktitle: 如何使用颜色调色板
type: docs
weight: 80
url: /zh/go-cpp/excel-color-palette/
description: 用C++代码向调色板添加自定义颜色，并使用带有Aspose.Cells for C++ API的Excel颜色调色板。
keywords: C++向调色板添加自定义颜色，C++程序化操作Excel颜色调色板，程序化如何在工作簿中使用颜色调色板，C++中如何在Excel中使用颜色调色板
---

## **颜色和调色板**

调色板是在创建图像时可用的颜色数量。在演示文稿中使用标准调色板可以让用户创建一致的外观。每个Microsoft Excel（97-2003）文件都有一个包含可应用于单元格、字体、网格线、图形对象、填充和图表中的线条的56种颜色的调色板。

使用 Aspose.Cells 不仅可以使用调色板的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，首先将其添加到调色板中。

本主题讨论如何向调色板中添加自定义颜色。

## **向调色板添加自定义颜色**

Aspose.Cells 支持 Microsoft Excel 的 56 种颜色调色板。要使用在调色板中未定义的自定义颜色，需要将颜色添加到调色板中。

Aspose.Cells 提供了一个名为 [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) 的类，用于表示 Microsoft Excel 文件。 [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) 类提供了一个 [**ChangePalette**](https://reference.aspose.com/cells/go-cpp/workbook/changepalette/) 方法，接受以下参数来添加自定义颜色以修改调色板：

- Custom Color，要添加的自定义颜色。
- Index，自定义颜色在调色板中的索引，将替换指定的颜色。应该在 0-55 之间。

下面的示例在应用于字体之前向调色板中添加了自定义颜色（兰花紫）。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ColorPalette.go" >}}
{{% alert color="primary" %}}

调色板只能容纳 56 种颜色。当向调色板中添加自定义颜色时，调色板会改变，文件中用先前颜色格式化的任何元素也会发生变化。因此，在更改调色板时，请务必小心。此外，在 XLS（Excel 97 - 2003）文件格式中，这是唯一的限制，XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式则没有这种限制。

{{% /alert %}}
