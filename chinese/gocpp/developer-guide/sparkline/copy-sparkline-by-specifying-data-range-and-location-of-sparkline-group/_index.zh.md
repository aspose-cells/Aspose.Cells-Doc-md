---
title: 通过Golang via C++复制Sparkline，指定数据范围和Sparkline组的位置
linktitle: 通过指定数据区域和位置复制Sparkline
type: docs
weight: 300
url: /zh/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: 学习如何通过指定数据区域和位置使用Aspose.Cells for C++复制sparkline。
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

Aspose.Cells提供`SparklineCollection.Add(dataRange, row, column)`方法，用于指定sparkline组的数据区域和位置。以下示例加载带有示意图中的源Excel文件，然后访问第一个sparkline组，添加数据区域和位置，最后将修改后的Excel文件写入磁盘，效果如上图所示。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
