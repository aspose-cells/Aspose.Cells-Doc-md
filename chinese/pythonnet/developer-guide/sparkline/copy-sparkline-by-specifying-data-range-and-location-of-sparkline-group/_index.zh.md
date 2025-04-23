---
title: 通过指定数据范围和 Sparkline 组的位置来复制 Sparkline
type: docs
weight: 300
url: /zh/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

微软Excel允许通过指定数据范围和位置复制迷你图。Aspose.Cells for Python via .NET支持此功能。

{{% /alert %}}

在Microsoft Excel中复制火花线到其他单元格：

1. 选择包含火花线的单元格。
1. 从**设计**选项卡的**火花线**部分选择**编辑数据**。
1. 选择**编辑组位置和数据**。
1. 指定数据范围和位置。
1. 点击**确定**。

Aspose.Cells for Python via .NET提供了SparklineCollection.Add(dataRange, row, column)方法，用于指定迷你图组的数据范围和位置。以下示例代码加载上方截图中的源Excel文件，然后访问第一个迷你图组，添加数据范围和位置，最后将结果Excel文件保存到磁盘。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

