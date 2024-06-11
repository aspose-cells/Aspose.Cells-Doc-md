---
title: 应用小计并更改大纲摘要行的方向，而不是详细信息下面的行
type: docs
weight: 100
url: /zh/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: 使用Aspose.Cells for Python via .NET API学习如何应用小计并更改大纲摘要行下面的详细信息的方向。
keywords: Python Excel库，应用小计，添加小计，更改大纲摘要下面的详细信息的方向，更改大纲摘要列的方向到详细信息的右侧，创建小计并更改大纲摘要下面的详细信息的方向
---

{{% alert color="primary" %}}

本文将解释如何对数据应用小计并更改大纲摘要行下面的方向。

你可以使用[**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list-bool-bool-bool)方法对数据应用小计。它接受以下参数。

- **ca** - 应用小计的范围
- **group_by** - 以从零开始的整数偏移量作为分组依据的字段
- **function** - 小计函数
- **total_list** - 一个从零开始的字段偏移量数组，指示添加小计的字段
- **replace** - 指示是否替换当前小计
- **page_breaks** - 指示是否在分组之间添加分页符
-**summary_below_data**- 表示是否将摘要添加在数据下方。

此外，您可以使用 Worksheet.Outline.SummaryRowBelow 属性，在下图所示的 Microsoft Excel 中通过“数据 > 大纲 > 设置”来控制大纲摘要行在细节下方的方向。

![todo:image_alt_text](1.png)

{{% /alert %}}

## **源文件和输出文件的图片**

下图显示了示例代码中使用的源Excel文件，其中包含列A和B中的一些数据。

![todo:image_alt_text](2.png)

下图显示了示例代码生成的输出Excel文件。如您所见，对范围A2:B11应用了小计，并且大纲的方向是细节下方的摘要行。

![todo:image_alt_text](3.png)

## **Python代码应用小计并改变大纲摘要行的方向**

以下是实现上述输出的示例代码。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
