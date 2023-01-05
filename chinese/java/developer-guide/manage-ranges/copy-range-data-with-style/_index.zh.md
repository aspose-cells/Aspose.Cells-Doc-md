---
title: 使用样式复制范围数据
type: docs
weight: 340
url: /zh/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[仅复制范围数据](/cells/zh/java/copy-range-data-only/)解释了如何将数据从一个单元格区域复制到另一个区域。 Aspose.Cells 还可以复制带格式的范围。这篇文章解释了如何。

{{% /alert %}} 
## **使用样式复制范围数据**
Aspose.Cells 提供了一系列用于处理范围的类和方法，例如，[创建范围()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [风格旗帜](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [应用样式()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)）， ETC。

这个例子：

1. 创建工作簿。
1. 用数据填充第一个工作表中的多个单元格。
1. 创建一个范围。
1. 创建具有指定格式属性的样式对象。
1. 将样式应用于数据范围。
1. 创建第二个单元格区域。
1. 将具有格式的数据从第一个范围复制到第二个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

