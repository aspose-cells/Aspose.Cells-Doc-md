---
title: 填充设置
type: docs
weight: 50
url: /zh/net/cells-fill-settings/
---
## **颜色和背景图案**

Microsoft Excel 可以设置单元格的前景（轮廓）和背景（填充）颜色和背景图案。

Aspose.Cells 也以灵活的方式支持这些功能。在本主题中，我们通过 Aspose.Cells 学习使用这些功能。

### **设置颜色和背景图案**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

这[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)有[**获取样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)和[**设置样式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)用于获取和设置单元格格式的方法。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)类提供用于设置单元格前景色和背景色的属性。 Aspose.Cells提供了[**背景类型**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)包含一组预定义类型的背景图案的枚举，如下所示。

|**背景图案**|**描述**|
|:- |:- |
|对角线交叉影线|表示对角交叉影线图案|
|斜条纹|代表斜条纹图案|
|灰色6|代表 6.25% 灰色图案|
|灰12|代表 12.5% 灰色图案|
|灰25|代表 25% 灰色图案|
|灰色50|代表 50% 灰色图案|
|灰色75|代表75%灰色图案|
|水平条纹|代表横条纹图案|
|没有任何|代表没有背景|
|反斜条纹|表示反斜条纹图案|
|坚硬的|表示实心图案|
|粗斜线|表示粗对角交叉影线图案|
|细对角线|表示细对角线交叉影线图案|
|细斜条纹|代表细斜条纹图案|
|细水平剖面线|表示细水平交叉影线图案|
|细横条纹|代表细横条纹图案|
|细反斜条纹|代表细反斜条纹图案|
|细竖条纹|代表细竖条纹图案|
|垂直条纹|代表竖条纹图案|

在下面的示例中，设置了 A1 单元格的前景色，但 A2 配置为具有垂直条纹背景图案的前景色和背景色。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **重要须知**

{{% alert color="primary" %}}

- 要设置单元格的前景色或背景色，请使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)要么[**背景颜色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor)特性。只有当[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**图案**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)属性已配置。
- 这[**前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)属性设置单元格的阴影颜色。
这[**图案**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)属性指定用于前景色或背景色的背景图案类型。 Aspose.Cells 提供枚举，[**背景类型**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype).包含一组预定义类型的背景图案。
- 如果你选择*背景类型.无*价值来自[**背景类型**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)枚举，不应用前景色。
同样，如果您选择*背景类型.无*要么*背景类型.Solid*值。
- 检索单元格的阴影/填充颜色时，如果[**样式.图案**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)是*背景类型.无*, [**样式.前景色**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)将返回*颜色.空*.

{{% /alert %}}

### **应用渐变填充效果**

要将所需的渐变填充效果应用于单元格，请使用[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象的[**设置双色渐变**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)相应的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **颜色和调色板**

调色板是可用于创建图像的颜色数量。在演示文稿中使用标准化调色板允许用户创建一致的外观。每个 Microsoft Excel (97-2003) 文件都有一个 56 种颜色的调色板，可应用于图表中的单元格、字体、网格线、图形对象、填充和线条。

使用 Aspose.Cells 不仅可以使用调色板的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，请先将其添加到调色板中。

本主题讨论如何将自定义颜色添加到调色板。

### **将自定义颜色添加到调色板**

Aspose.Cells 支持Microsoft Excel的56色调色板。要使用未在调色板中定义的自定义颜色，请将颜色添加到调色板。

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了[**改变调色板**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette)采用以下参数添加自定义颜色以修改调色板的方法：

- Custom Color，要添加的自定义颜色。
- 索引，自定义颜色将替换的调色板中颜色的索引。应该在 0-55 之间。

下面的示例在将自定义颜色（兰花）应用于字体之前将其添加到调色板。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

调色板只有 56 种颜色。当您将自定义颜色添加到调色板时，调色板会更改，文件中使用先前颜色设置格式的任何元素也会更改。所以，当你改变调色板时，请非常小心。此外，这只是 XLS（Excel 97 - 2003）文件格式的限制，因为 XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式没有此类限制。

{{% /alert %}}
