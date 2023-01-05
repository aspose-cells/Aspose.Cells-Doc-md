---
title: 重用样式对象
type: docs
weight: 60
url: /zh/java/reusing-style-objects/
---
{{% alert color="primary" %}}

重用样式对象可以节省内存并使程序执行得更快。

{{% /alert %}}

将某些格式应用于工作表中的大范围单元格：

1. 创建样式对象。
1. 指定属性。
1. 将样式应用于范围内的单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

与上面讨论的相同过程也可以如下完成。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

因为[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ） 和[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) 方法使用更少的内存并且效率更高，越老*Cell.getStyle()*消耗大量不必要内存的属性随着*Aspose.Cells 7.1.0*.

{{% /alert %}}
