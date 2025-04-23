---
title: 通过指定数据范围和 Sparkline 组的位置来复制 Sparkline
type: docs
weight: 300
url: /zh/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel允许您通过指定火花线组的数据范围和位置来复制火花线。Aspose.Cells支持此功能。

{{% /alert %}}

在Microsoft Excel中复制火花线到其他单元格：

1. 选择包含火花线的单元格。
1. 从**设计**选项卡的**火花线**部分选择**编辑数据**。
1. 选择**编辑组位置和数据**。
1. 指定数据范围和位置。
1. 点击**确定**。

Aspose.Cells提供了SparklineCollection.Add(dataRange, row, column)方法用于指定火花线组的数据范围和位置。以下示例代码加载了上述屏幕截图中显示的源Excel文件，然后访问第一个火花线组，添加了数据范围和位置，并最终将输出Excel文件写入磁盘，屏幕截图也显示了这一过程。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
