---
title: 如何使用颜色调色板
type: docs
weight: 80
url: /zh/net/excel-color-palette/
description: C#代码添加自定义颜色到调色板，并使用Aspose.Cells for .NET API的Excel颜色调色板
keywords: c#在调色板中添加自定义颜色，以编程方式在Excel中使用颜色调色板，以编程方式如何在工作簿中使用颜色调色板，c#如何在Excel中使用颜色调色板
---

## **颜色和调色板**

调色板是用于创建图像的可用颜色数量。在演示文稿中使用标准化的调色板允许用户创建一致的外观。每个微软 Excel (97-2003) 文件有一个包含 56 种颜色的调色板，可应用于单元格、字体、网格线、图形对象、填充和图表中的线条。

使用 Aspose.Cells 不仅可以使用调色板中的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，先将其添加到调色板中。

本主题讨论如何将自定义颜色添加到调色板。

## **在调色板中添加自定义颜色**

Aspose.Cells 支持微软 Excel 的 56 种颜色调色板。要使用不在调色板中定义的自定义颜色，请将颜色添加到调色板中。

Aspose.Cells 提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个微软 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类提供一个 [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) 方法，接受以下参数以添加自定义颜色来修改调色板：

- 自定义颜色，要添加的自定义颜色。
- 索引，将自定义颜色替换为调色板中颜色的索引。应在 0 到 55 之间。

下面的示例将 Orchid 添加到调色板，然后应用到字体上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

调色板只有 56 种颜色。当将自定义颜色添加到调色板时，调色板会更改，并且文件中使用之前颜色格式化的任何元素都会更改。因此，在更改调色板时请非常小心。此外，这仅适用于 XLS（Excel 97-2003）文件格式，而适用于 XLSX 或其他先进的 MS Excel（2007/2010或2013）文件格式则没有此限制。

{{% /alert %}}
