---
title: 添加2色比例和3色比例条件格式
description: 如何在C#中使用Aspose.Cells库为两种颜色比例和三种颜色比例添加条件格式。通过调整这些条件，您可以更好地控制单元格外观。
keywords: Aspose.Cells, 条件格式, C#,颜色比例, 两色比例, 三色比例
type: docs
weight: 20
url: /zh/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

2色标尺和3色标尺条件格式的添加方式相同，唯一区别在于[**FormatCondition.ColorScale.Is3ColorScale**](https://reference.aspose.com/cells/net/aspose.cells/colorscale/properties/is3colorscale)属性。对于2色标尺设置为**false**，对于3色标尺条件格式设置为**true**。

{{% /alert %}}

以下示例代码可添加2色和3色标尺条件格式。它将生成[输出的Excel文件](5115058.xlsx)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-AddColorScales-AddColorScales.cs" >}}
