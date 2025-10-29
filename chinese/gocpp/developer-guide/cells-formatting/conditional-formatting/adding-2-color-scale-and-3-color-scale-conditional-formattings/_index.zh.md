---
title: 添加双色标度和三色标度条件格式化，使用 Golang 通过 C++
linktitle: 添加二色比例和三色比例条件格式
description: 如何在C++中使用Aspose.Cells库为两个颜色比例和三个颜色比例添加条件格式。通过调整这些条件，您可以更好地控制单元格的外观和显示。
keywords: Aspose.Cells，条件格式，C++，颜色比例，双色标度，三色标度
type: docs
weight: 20
url: /zh/go-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

二色比例和三色比例条件格式的添加方式相同，只是它们由 [**FormatCondition.GetIs3ColorScale()**](https://reference.aspose.com/cells/go-cpp/colorscale/getis3colorscale/) 属性区分。此属性对于二色比例条件格式为 false，对于三色比例条件格式为 true。

{{% /alert %}}

以下示例代码添加了二色比例和三色比例条件格式。它生成了 [输出 Excel 文件](5115058.xlsx)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Adding2ColorScaleAnd3ColorScaleConditionalFormattings.go" >}}
