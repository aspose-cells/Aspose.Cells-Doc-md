---
title: 填充设置
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库。它支持设置单元格的填充设置，允许用户自定义单元格的背景和样式。本文将介绍如何使用Aspose.Cells库来设置单元格填充设置。
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /zh/net/cells-fill-settings/
---
##  **颜色和背景图案**

Microsoft Excel可以设置单元格的前景色（轮廓）和背景（填充）颜色以及背景图案。

Aspose.Cells也以灵活的方式支持这些功能。在本主题中，我们通过 Aspose.Cells 学习如何使用这些功能。

###  **设置颜色和背景图案**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)代表 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

这[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)有[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)和[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)用于获取和设置单元格格式的方法。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供用于设置单元格的前景色和背景色的属性。 Aspose.Cells 提供[**背景类型**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)包含一组预定义类型的背景图案的枚举，如下所示。

|**背景图案**|**描述**|
| :- | :- |
|对角线剖面线|表示对角线剖面线图案|
|斜条纹|代表斜条纹图案|
|灰色6|代表6.25%灰度图案|
|灰色12|代表12.5%灰度图案|
|灰色25|代表25%灰度图案|
|灰色50|代表50%灰度图案|
|灰色75|代表75%灰度图案|
|横条纹|代表水平条纹图案|
|没有任何|代表无背景|
|反斜条纹|代表反向对角条纹图案|
|坚硬的|代表实体图案|
|厚对角线剖面线|表示粗对角线剖面线图案|
|细对角线剖面线|表示细对角线剖面线图案|
|细斜条纹|代表细斜条纹图案|
|细水平剖面线|代表细水平剖面线图案|
|细横条纹|代表细水平条纹图案|
|细反斜条纹|代表细反向对角条纹图案|
|细竖条纹|代表细竖条纹图案|
|竖条纹|代表竖条纹图案|

在下面的示例中，设置了 A1 单元格的前景色，但将 A2 配置为同时具有前景色和背景色以及垂直条纹背景图案。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **重要了解**

{{% alert color="primary" %}}

- 要设置单元格的前景色或背景色，请使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)或者[**背景颜色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor)特性。这两个属性只有在以下情况下才会生效[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**图案**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)属性已配置。
- 这[**前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)属性设置单元格的阴影颜色。
这[**图案**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)属性指定用于前景色或背景色的背景图案的类型。 Aspose.Cells提供了一个枚举，[**背景类型**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)。包含一组预定义类型的背景图案。
- 如果您选择*背景类型.无*值来自于[**背景类型**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)枚举时，不应用前景色。
同样，如果您选择*背景类型.无*或者*背景类型.实心*价值观。
- 当检索单元格的阴影/填充颜色时，如果[**风格.图案**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)是 *BackgroundType.None*，[**样式.前景颜色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)将返回*Color.Empty*。

{{% /alert %}}

###  **应用渐变填充效果**

要将所需的渐变填充效果应用到单元格，请使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**设置双色渐变**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)相应的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **颜色和调色板**

调色板是可用于创建图像的颜色数量。在演示文稿中使用标准化调色板允许用户创建一致的外观。每个 Microsoft Excel (97-2003) 文件都有一个 56 种颜色的调色板，可应用于图表中的单元格、字体、网格线、图形对象、填充和线条。

使用 Aspose.Cells，不仅可以使用调色板的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，请先将其添加到调色板中。

本主题讨论如何将自定义颜色添加到调色板。

###  **将自定义颜色添加到调色板**

Aspose.Cells 支持 Microsoft Excel 的 56 种调色板。要使用调色板中未定义的自定义颜色，请将该颜色添加到调色板。

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了一个[**更改调色板**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette)方法采用以下参数添加自定义颜色来修改调色板：

- Custom Color，要添加的自定义颜色。
- 索引，调色板中自定义颜色将替换的颜色的索引。应在 0-55 之间。

下面的示例将自定义颜色（兰花色）添加到调色板，然后再将其应用到字体上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

调色板仅包含 56 种颜色。当您将自定义颜色添加到调色板时，调色板会发生更改，并且使用先前颜色格式化的文件中的任何元素都会发生更改。所以，当你更换调色板时，请务必小心。此外，这只是 XLS (Excel 97 - 2003) 文件格式的限制，因为 XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式没有此类限制。

{{% /alert %}}
