---
title: 重用样式对象
type: docs
weight: 60
url: /zh/java/reusing-style-objects/
---

{{% alert color="primary" %}}

重用样式对象可以节省内存并使程序执行更快。

{{% /alert %}}

若要对工作表中的大范围单元格应用一些格式设置：

1. 创建一个样式对象。
1. 指定属性。
1. 将样式应用于范围中的单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

上述讨论的相同流程也可以按照以下方式完成。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

因为 [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) 和 [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) 方法使用的内存较少且高效，旧的 *Cell.getStyle()* 属性消耗了大量不必要的内存，在 *Aspose.Cells 7.1.0* 发布时被移除。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
