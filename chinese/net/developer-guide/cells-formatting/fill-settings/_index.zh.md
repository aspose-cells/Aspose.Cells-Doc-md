---
title: 填充设置
description: Aspose.Cells是一个用于处理电子表格文件的.NET库。它支持设置单元格的填充设置，允许用户自定义单元格的背景和样式。本文将介绍如何使用Aspose.Cells库设置单元格填充设置。
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /zh/net/cells-fill-settings/
---

## **颜色和背景图案**

Microsoft Excel可以设定单元格的前景（轮廓）和背景（填充）颜色以及背景图案。

Aspose.Cells还以灵活的方式支持这些功能。在这个主题中，我们将学习如何使用Aspose.Cells使用这些功能。

### **设置颜色和背景模式**

Aspose.Cells提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合中的每个项目表示一个[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)具有[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)和[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)方法，用于获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)类为设置单元格的前景色和背景色提供属性。Aspose.Cells提供了一个包含一组预定义的背景模式类型的[**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)枚举。

|**背景模式**|**描述**|
| :- | :- |
|DiagonalCrosshatch|表示对角线纹理|
|DiagonalStripe|表示对角条纹纹理|
|Gray6|表示6.25%灰度纹理|
|Gray12|表示12.5%灰度纹理|
|Gray25|表示25%灰度纹理|
|Gray50|表示50%灰度纹理|
|Gray75|表示75%灰度纹理|
|HorizontalStripe|表示水平条纹纹理|
|None|表示无背景|
|ReverseDiagonalStripe|表示反对角线条纹纹理|
|Solid|表示实线纹理|
|ThickDiagonalCrosshatch|表示厚斜交叉阴影图案|
|ThinDiagonalCrosshatch|表示细斜交叉阴影图案|
|ThinDiagonalStripe|表示细斜线条纹图案|
|ThinHorizontalCrosshatch|表示细水平交叉阴影图案|
|ThinHorizontalStripe|表示细水平条纹图案|
|ThinReverseDiagonalStripe|表示细逆斜线条纹图案|
|ThinVerticalStripe|表示细垂直条纹图案|
|VerticalStripe|表示垂直条纹图案|

在下面的示例中，设置了A1单元格的前景色，而A2配置为具有前景色和背景色，背景模式为垂直条纹。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **重要知识**

{{% alert color="primary" %}}

- 要设置单元格的前景色或背景色，请使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)或[**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor)属性。只有在配置了[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)属性时，这两个属性才会生效。
- [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)属性设置单元格的阴影颜色。
  [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)属性指定用于前景或背景色的背景模式类型。Aspose.Cells提供了一个枚举，[**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)。包含一组预定义的背景模式类型。
- 如果从[**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)枚举中选择了*BackgroundType.None*值，则不会应用前景色。
  同样，如果选择了*BackgroundType.None*或*BackgroundType.Solid*值，则不会应用背景色。
- 在检索单元格的底纹/填充颜色时，如果[**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)是*BackgroundType.None*，[**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)将返回*Color.Empty*。

{{% /alert %}}

### **应用渐变填充效果**

要将所需的渐变填充效果应用到单元格中，请相应地使用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **颜色和调色板**

调色板是用于创建图像的可用颜色数量。在演示文稿中使用标准化的调色板允许用户创建一致的外观。每个微软 Excel (97-2003) 文件有一个包含 56 种颜色的调色板，可应用于单元格、字体、网格线、图形对象、填充和图表中的线条。

使用 Aspose.Cells 不仅可以使用调色板中的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，先将其添加到调色板中。

本主题讨论如何将自定义颜色添加到调色板。

### **将自定义颜色添加到调色板**

Aspose.Cells 支持微软 Excel 的 56 种颜色调色板。要使用不在调色板中定义的自定义颜色，请将颜色添加到调色板中。

Aspose.Cells 提供一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个微软 Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类提供一个 [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) 方法，接受以下参数以添加自定义颜色来修改调色板：

- 自定义颜色，要添加的自定义颜色。
- 索引，将自定义颜色替换为调色板中颜色的索引。应在 0 到 55 之间。

下面的示例将 Orchid 添加到调色板，然后应用到字体上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

调色板只有 56 种颜色。当将自定义颜色添加到调色板时，调色板会更改，并且文件中使用之前颜色格式化的任何元素都会更改。因此，在更改调色板时请非常小心。此外，这仅适用于 XLS（Excel 97-2003）文件格式，而适用于 XLSX 或其他先进的 MS Excel（2007/2010或2013）文件格式则没有此限制。

{{% /alert %}}
