---
title: 添加 2 色标和 3 色标条件格式
description: 如何使用C#中的Aspose.Cells库添加两种颜色比例和三种颜色比例的条件格式。通过调整这些标准，您可以更好地控制单元格的外观和显示方式。
keywords: Aspose.Cells, Conditional Formatting, C#, Color Ratio, Two Color Scale, Three Color Scale
type: docs
weight: 20
url: /zh/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---
{{% alert color="primary" %}}

**2 色标**和**三色标度**条件格式的添加方式相同，但不同之处在于[**FormatCondition.ColorScale.Is3ColorScale**](https://reference.aspose.com/cells/net/aspose.cells/colorscale/properties/is3colorscale)财产。此属性是**错误的**对于 2 色阶和**真的**用于 3 色阶条件格式。

{{% /alert %}}

以下示例代码添加了 2 色和 3 色阶条件格式。它生成[输出Excel文件](5115058.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-AddColorScales-AddColorScales.cs" >}}
