---
title: 仅复制范围数据和样式
type: docs
weight: 340
url: /zh/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[仅复制范围数据](/cells/zh/java/copy-range-data-only/)解释了如何将数据从一个单元格范围复制到另一个范围。Aspose.Cells还可以复制带有格式的范围。本文介绍了如何实现这一点。

{{% /alert %}} 
## **复制具有样式的区域数据**
Aspose.Cells 提供了一系列用于处理范围的类和方法，例如 [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\))，[StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)，[applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\))，等等。

此示例：

1. 创建一个工作簿。
1. 在第一个工作表中填充多个单元格的数据。
1. 创建一个范围。
1. 创建具有指定格式属性的样式对象。
1. 将样式应用到数据范围。
1. 创建第二个单元格范围。
1. 将第一个范围的带有格式的数据复制到第二个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

