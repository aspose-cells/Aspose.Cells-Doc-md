---
title: 填充设置
description: Aspose.Cells 是一个用于处理电子表格文件的 Python 库。它支持设置单元格的填充设置，允许用户自定义单元格的背景和样式。本文将介绍如何使用 Aspose.Cells for Python via .NET 库设置单元格填充设置。
keywords: Aspose.Cells for Python via .NET，单元格，填充设置，背景，样式
type: docs
weight: 50
url: /zh/python-net/cells-fill-settings/
---

## **颜色和背景图案**

Microsoft Excel可以设置单元格的前景（轮廓）和背景（填充）颜色以及背景图案。

Aspose.Cells for Python via .NET 还能以灵活的方式支持这些功能。在本主题中，我们学习如何使用这些功能。

### **设置颜色和背景图案**

Aspose.Cells for Python via .NET提供了[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供一个[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合，集合中的每个项目代表一个[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的对象。

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 具有用于获取和设置单元格格式的 [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) 和 [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) 方法。[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 类提供属性，用于设置单元格的前景色和背景色。Aspose.Cells for Python via .NET 提供一个 [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) 枚举，包含一组预定义的背景图案类型，详见如下内容。

|**背景图案**|**描述**|
| :- | :- |
|DIAGONAL_CROSSHATCH| 表示对角线交叉图案|
|DIAGONAL_STRIPE| 表示对角线条纹图案|
|GRAY6| 表示 6.25% 灰色图案|
|GRAY12| 表示 12.5% 灰色图案|
|GRAY25| 表示 25% 灰色图案|
|GRAY50| 表示 50% 灰色图案|
|GRAY75| 表示 75% 灰色图案|
|HORIZONTAL_STRIPE| 表示水平条纹图案|
|NONE| 表示无背景|
|REVERSE_DIAGONAL_STRIPE| 表示反向对角线条纹图案|
|SOLID| 表示纯色图案|
|THICK_DIAGONAL_CROSSHATCH| 表示粗对角线交叉图案|
|THIN_DIAGONAL_CROSSHATCH| 表示细对角线交叉图案|
|THIN_DIAGONAL_STRIPE| 表示细对角线条纹图案|
|THIN_HORIZONTAL_CROSSHATCH| 表示细水平交叉图案|
|THIN_HORIZONTAL_STRIPE| 表示细水平条纹图案|
|THIN_REVERSE_DIAGONAL_STRIPE|代表细线反斜线条纹样式|
|THIN_VERTICAL_STRIPE|代表细竖条纹样式|
|VERTICAL_STRIPE|代表竖条纹样式|

在下面的示例中，A1单元格的前景色已设置，但A2配置为具有前景色和背景色的垂直条纹背景模式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **重要知识**

{{% alert color="primary" %}}

- 若要设置单元格的前景色或背景色，请使用 [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 对象的 [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) 或 [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) 属性。只有当 [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 对象的 [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) 属性配置好时，这两个属性才会生效。
- [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) 属性设置单元格的阴影颜色。
  属性 [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) 指定用于前景色或背景色的背景图案类型。Aspose.Cells for Python via .NET 提供了一个枚举 [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype)，其中包含一组预定义的背景图案类型。
- 如果从 [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) 枚举中选择 *BackgroundType.None* 值，则不会应用前景色。
  同样，如果选择 *BackgroundType.None* 或 *BackgroundType.Solid* 值，则不会应用背景色。
- 在检索单元格的阴影/填充颜色时，如果 [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) 是 *BackgroundType.None*，[**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) 将返回 *Color.Empty*。

{{% /alert %}}

### **应用梯度填充效果**

要将期望的渐变填充效果应用于单元格，相应地使用 [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) 对象的 [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) 方法。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **颜色和调色板**

调色板是在创建图像时可用的颜色数量。在演示文稿中使用标准调色板可以让用户创建一致的外观。每个Microsoft Excel（97-2003）文件都有一个包含可应用于单元格、字体、网格线、图形对象、填充和图表中的线条的56种颜色的调色板。

使用 Aspose.Cells for Python via .NET，不仅可以使用调色板中的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，首先将其添加到调色板中。

本主题讨论如何向调色板中添加自定义颜色。

### **向调色板中添加自定义颜色**

Aspose.Cells for Python via .NET 支持微软 Excel 的 56 种调色板。若要使用调色板中未定义的自定义颜色，请将其添加到调色板中。

Aspose.Cells for Python via .NET 提供了一个类 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，表示微软 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类提供了一个 [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette) 方法，带有以下参数，用于添加自定义颜色以修改调色板：

- Custom Color，要添加的自定义颜色。
- Index，自定义颜色在调色板中的索引，将替换指定的颜色。应该在 0-55 之间。

下面的示例在应用于字体之前向调色板中添加了自定义颜色（兰花紫）。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

调色板只能容纳 56 种颜色。当向调色板中添加自定义颜色时，调色板会改变，文件中用先前颜色格式化的任何元素也会发生变化。因此，在更改调色板时，请务必小心。此外，在 XLS（Excel 97 - 2003）文件格式中，这是唯一的限制，XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式则没有这种限制。

{{% /alert %}}

