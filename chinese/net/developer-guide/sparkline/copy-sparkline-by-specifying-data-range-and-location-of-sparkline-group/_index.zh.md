---
title: 通过指定数据范围和Sparkline组的位置复制Sparkline
type: docs
weight: 300
url: /zh/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel允许您通过指定数据范围和Sparkline组的位置来复制一个Sparkline。Aspose.Cells支持此功能。

{{% /alert %}}

要在Microsoft Excel中将Sparkline复制到其他单元格中：

1. 选择包含Sparkline的单元格。
1. 从**设计**选项卡的**Sparkline**部分中选择**编辑数据**。
1. 选择**编辑组位置和数据**。
1. 指定数据范围和位置。
1. 单击**确定**。

Aspose.Cells提供了SparklineCollection.Add(dataRange, row, column)方法来指定一个迷你图组的数据范围和位置。以下示例代码加载了上面截图中显示的源Excel文件，然后访问第一个迷你图组，并添加了数据范围和位置到迷你图组中。最后，它将输出的Excel文件写入磁盘，这也在上面的截图中显示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
