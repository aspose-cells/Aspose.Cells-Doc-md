---
title: 添加二色比例和三色比例条件格式
description: 如何使用Aspose.Cells for Python via .NET库添加两色比例和三色比例的条件格式。调整这些条件，可以更好地控制单元格的外观。
keywords: Aspose.Cells for Python via .NET，条件格式，Python颜色比例，两色比例，三色比例
type: docs
weight: 20
url: /zh/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

二色比例和三色比例条件格式的添加方式相同，只是它们由 [**FormatCondition.color_scale.is_3_color_scale**](https://reference.aspose.com/cells/python-net/aspose.cells/colorscale/is_3_color_scale) 属性区分。此属性对于二色比例条件格式为 false，对于三色比例条件格式为 true。

{{% /alert %}}

以下示例代码添加了二色比例和三色比例条件格式。它生成了 [输出 Excel 文件](5115058.xlsx)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-AddColorScales.py" >}}

{{< app/cells/assistant language="python-net" >}}
