---
title: 通过指定迷你图组的数据范围和位置来复制迷你图
type: docs
weight: 300
url: /zh/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft Excel 允许您通过指定迷你图组的数据范围和位置来复制迷你图。 Aspose.Cells 支持此功能。

{{% /alert %}}

要将迷你图复制到 Microsoft Excel 中的其他单元格：

1. 选择包含迷你图的单元格。
1. 选择**编辑数据**来自**迷你图**的部分**设计**标签。
1. 选择**编辑组位置和数据**.
1. 指定数据范围和位置。
1. 点击**好的**.

Aspose.Cells 提供 SparklineCollection.Add(dataRange, row, column) 方法来指定迷你图组的数据范围和位置。以下示例代码加载源 Excel 文件，如上面的屏幕截图所示，然后访问第一个迷你图组并在迷你图组中添加数据范围和位置。最后，它将输出的 Excel 文件写入磁盘，如上图所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
