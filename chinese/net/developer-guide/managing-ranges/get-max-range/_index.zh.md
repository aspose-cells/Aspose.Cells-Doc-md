---
title: 获取工作表中的最大范围
type: docs
weight: 360
url: /zh/net/get-max-range-in-a-worksheet/
description: 本文介绍了如何使用Aspose.Cells for .Net库获取Excel文件的最大范围、最大数据范围和最大显示范围。
---

{{% alert color="primary" %}} 

在读取工作表数据时，我们需要知道最大区域。

在从工作表复制所有数据时，我们需要知道最大区域。

在将指定区域导出为html和pdf时，我们需要知道最大区域。

Aspose.Cells for .Net包含不同的方法来查找工作表中的最大范围。 


{{% /alert %}} 



## **获取最大范围**
在Aspose.Cells中，如果[**row**](https://reference.aspose.com/cells/net/aspose.cells/row)和[**column**](https://reference.aspose.com/cells/net/aspose.cells/column)对象被初始化，这些行和列将被计入最大区域，即使空行或列中没有数据也是如此。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **获取最大数据范围**
在大多数情况下，我们只需要获取包含所有数据的所有范围，即使范围外的空单元格也被格式化。
关于形状、表格和数据透视表的设置将被忽略。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **获取最大显示范围**
当我们将工作表中的所有数据导出到HTML、PDF或图像时，我们需要获取一个包含所有可见对象的区域，包括数据、样式、图形、表格和数据透视表。
以下代码展示了如何将最大显示范围呈现到html：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

这里是[源Excel文件](Book1.xlsx)。
