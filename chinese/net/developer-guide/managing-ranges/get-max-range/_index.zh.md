---
title: 获取工作表中的最大范围
type: docs
weight: 360
url: /zh/net/get-max-range-in-a-worksheet/
description: 本文介绍如何使用.Net库的Aspose.Cells获取Excel文件的最大范围、最大数据范围、最大显示范围。
---
{{% alert color="primary" %}} 

从工作表中读取数据时，我们需要知道最大面积。

当从工作表复制所有数据时，我们需要知道最大面积。

将指定区域导出为html和pdf时，我们需要知道最大区域。

 .Net 的 Aspose.Cells 包含在工作表中查找最大范围的不同方法。


{{% /alert %}} 



##  **获取最大范围**
在 Aspose.Cells 中，如果[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)和[**柱子**](https://reference.aspose.com/cells/net/aspose.cells/column)对象初始化后，这些行和列将被计入最大区域，即使空行或空列中没有数据。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

##  **获取最大数据范围**
大多数情况下，我们只需要获取包含所有数据的所有范围，即使范围外的空单元格已格式化。
并且有关形状、表格和数据透视表的设置将被忽略。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

##  **获取最大显示范围**
当我们将工作表中的所有数据导出到HTML、PDF或图像时，我们需要获得一个包含所有可见对象的区域，包括数据、样式、图形、表格和数据透视表。
以下代码展示了如何将最大显示范围渲染为 html：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

这是[源 Excel 文件](Book1.xlsx).
