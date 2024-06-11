---
title: 应用小计和在详细信息下方更改大纲摘要行的方向
type: docs
weight: 100
url: /zh/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: 了解如何通过Aspose.Cells for Python通过.NET API应用小计并更改详细信息下方的大纲摘要行的方向。
keywords: Python Excel库，应用小计，添加小计，更改详细信息下方的大纲摘要行的方向，更改详细信息下方的大纲摘要列的方向，创建小计并更改详细信息下方的大纲摘要行的方向
---

{{% alert color="primary" %}}

本文将解释如何将小计应用于数据并更改详细信息下方的大纲摘要行的方向。

您可以使用 [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list-bool-bool-bool) 方法对数据应用小计。它接受以下参数。

- **ca** - 应用小计的范围
- **group_by** - 按零为基础的整数偏移来分组的字段
- **function** - 小计函数
- **total_list** - 以零为基础的字段偏移的数组，指示要添加小计的字段
- **replace** - 指示是否替换当前的小计
- **page_breaks** - 指示在组之间添加分页符
- **summary_below_data** - 指示是否在数据下方添加摘要

此外，还可以控制大纲中 **具有详细信息下方的摘要行** 的方向，如下截图所示，使用 Worksheet.Outline.SummaryRowBelow 属性。您可以在 Microsoft Excel 中使用 **数据 > 大纲 > 设置** 打开此设置

![todo:image_alt_text](1.png)

{{% /alert %}}

## **源文件和输出文件的图像**

以下截图显示了示例代码中使用的源Excel文件，其中在A和B列中包含一些数据。

![todo:image_alt_text](2.png)

以下截图显示了示例代码生成的输出 Excel 文件。正如您所见，已对 A2:B11 范围应用了小计，并且大纲的方向是摘要行在详细信息下方。

![todo:image_alt_text](3.png)

## **应用小计并更改大纲摘要行方向的Python代码**

以下是实现上述输出的示例代码。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
