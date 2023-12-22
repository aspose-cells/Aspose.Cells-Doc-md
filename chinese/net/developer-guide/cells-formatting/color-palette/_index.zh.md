---
title: 如何使用调色板
type: docs
weight: 80
url: /zh/net/excel-color-palette/
description: C# 将自定义颜色添加到调色板并使用 Excel 调色板的代码 Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **颜色和调色板**

调色板是可用于创建图像的颜色数量。在演示文稿中使用标准化调色板允许用户创建一致的外观。每个 Microsoft Excel (97-2003) 文件都有一个 56 种颜色的调色板，可应用于图表中的单元格、字体、网格线、图形对象、填充和线条。

使用 Aspose.Cells，不仅可以使用调色板的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，请先将其添加到调色板中。

本主题讨论如何将自定义颜色添加到调色板。

##  **将自定义颜色添加到调色板**

Aspose.Cells 支持 Microsoft Excel 的 56 种调色板。要使用调色板中未定义的自定义颜色，请将该颜色添加到调色板。

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了一个[**更改调色板**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette)方法采用以下参数添加自定义颜色来修改调色板：

- Custom Color，要添加的自定义颜色。
- 索引，调色板中自定义颜色将替换的颜色的索引。应在 0-55 之间。

下面的示例将自定义颜色（兰花色）添加到调色板，然后再将其应用到字体上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

调色板仅包含 56 种颜色。当您将自定义颜色添加到调色板时，调色板会发生更改，并且使用先前颜色格式化的文件中的任何元素都会发生更改。所以，当你更换调色板时，请务必小心。此外，这只是 XLS (Excel 97 - 2003) 文件格式的限制，因为 XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式没有此类限制。

{{% /alert %}}