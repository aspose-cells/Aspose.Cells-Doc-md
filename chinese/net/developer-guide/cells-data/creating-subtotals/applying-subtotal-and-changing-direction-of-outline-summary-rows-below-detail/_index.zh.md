---
title: 应用小计并更改大纲摘要行的方向，而不是详细信息下面的行
type: docs
weight: 100
url: /zh/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: 通过使用 Aspose.Cells for .NET API，学习如何应用小计并更改汇总行下详细信息的方向。
keywords: 应用小计，添加小计，更改详细下面概要行的方向，更改详细右边概要列的方向，创建小计并更改详细下面概要行的方向
---

{{% alert color="primary" %}}

本文将解释如何对数据应用小计并更改大纲摘要行下面的方向。

你可以使用[**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)方法对数据应用小计。它接受以下参数。

- **单元格区域** - 应用小计的范围
- **按组** - 按零为基础的整数偏移量分组
- **功能** - 小计功能。
- **TotalList** - 一个从零开始的字段偏移量数组，指示要添加小计的字段。
- **Replace** - 指示是否替换当前的小计
- **分页符** - 表示是否在组之间添加分页符
- **SummaryBelowData** - 指示是否在数据下方添加摘要。

此外，您可以使用 Worksheet.Outline.SummaryRowBelow 属性，在下图所示的 Microsoft Excel 中通过“数据 > 大纲 > 设置”来控制大纲摘要行在细节下方的方向。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 源文件和输出文件的图像

下图显示了示例代码中使用的源Excel文件，其中包含列A和B中的一些数据。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

下图显示了示例代码生成的输出Excel文件。如您所见，对范围A2:B11应用了小计，并且大纲的方向是细节下方的摘要行。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## 用于应用小计并更改详细下面概要行方向的C#代码

以下是实现上述输出的示例代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
