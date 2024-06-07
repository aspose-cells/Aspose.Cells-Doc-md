---
title: 应用小计和在详细信息下方更改大纲摘要行的方向
type: docs
weight: 100
url: /zh/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: 学习如何使用 Aspose.Cells for .NET API 应用小计并更改大纲摘要行下的详细信息方向。
keywords: 应用小计，添加小计，更改大纲摘要行下的详细信息方向，更改大纲摘要列右侧的详细信息方向，创建小计并更改大纲摘要行下的详细信息方向
---

{{% alert color="primary" %}}

本文将解释如何将小计应用于数据并更改详细信息下方的大纲摘要行的方向。

您可以使用 [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) 方法对数据应用小计。它接受以下参数。

- **CellArea** - 要应用小计的范围
- **GroupBy** - 按照哪个字段分组，作为从零开始的整数偏移量
- **Function** - 小计函数
- **TotalList** - 一个从零开始的字段偏移量数组，指示添加小计的字段
- **Replace** - 指示是否替换当前小计
- **PageBreaks** - 指示是否在组之间添加分页符
- **SummaryBelowData** - 指示是否在数据下方添加汇总

此外，还可以控制大纲中 **具有详细信息下方的摘要行** 的方向，如下截图所示，使用 Worksheet.Outline.SummaryRowBelow 属性。您可以在 Microsoft Excel 中使用 **数据 > 大纲 > 设置** 打开此设置

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 源文件和输出文件的图像

以下截图显示了示例代码中使用的源Excel文件，其中在A和B列中包含一些数据。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

以下截图显示了示例代码生成的输出 Excel 文件。正如您所见，已对 A2:B11 范围应用了小计，并且大纲的方向是摘要行在详细信息下方。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## 用于应用小计和更改大纲摘要行的方向的 C# 代码

以下是实现上述输出的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
