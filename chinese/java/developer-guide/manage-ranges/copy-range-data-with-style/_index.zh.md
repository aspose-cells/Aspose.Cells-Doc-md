---
title: 带样式复制范围数据
type: docs
weight: 340
url: /zh/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[仅复制范围数据](/cells/zh/java/copy-range-data-only/)解释了如何将数据从一个单元格范围复制到另一个范围。Aspose.Cells还可以复制带有格式的范围。本文详细说明了如何操作。

{{% /alert %}} 
## **复制带样式的区域数据**
Aspose.Cells提供了一系列用于处理范围的类和方法，例如 [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\))，[StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)，[applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)) 等。

本例：

1. 创建一个工作簿。
1. 在第一个工作表中的多个单元格中填充数据。
1. 创建一个范围。
1. 使用指定的格式属性创建样式对象。
1. 将样式应用到数据范围。
1. 创建第二个单元格范围。
1. 将第一个范围的数据与格式复制到第二个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

