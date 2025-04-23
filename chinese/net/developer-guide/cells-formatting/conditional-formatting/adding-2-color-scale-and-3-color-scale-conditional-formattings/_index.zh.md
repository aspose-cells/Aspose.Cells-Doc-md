---
title: 添加二色比例和三色比例条件格式
description: 如何在 C# 中使用 Aspose.Cells 库为两种颜色比率和三种颜色比率添加条件格式。通过调整这些条件，您可以更好地控制单元格的外观。
keywords: Aspose.Cells, 条件格式, C#, 颜色比率, 二色比例, 三色比例
type: docs
weight: 20
url: /zh/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

二色比例和三色比例条件格式的添加方式相同，只是它们由 [**FormatCondition.ColorScale.Is3ColorScale**](https://reference.aspose.com/cells/net/aspose.cells/colorscale/properties/is3colorscale) 属性区分。此属性对于二色比例条件格式为 false，对于三色比例条件格式为 true。

{{% /alert %}}

以下示例代码添加了二色比例和三色比例条件格式。它生成了 [输出 Excel 文件](5115058.xlsx)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-AddColorScales-AddColorScales.cs" >}}
{{< app/cells/assistant language="csharp" >}}
