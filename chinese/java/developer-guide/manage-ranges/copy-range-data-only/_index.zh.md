---
title: 仅复制范围的数据
type: docs
weight: 330
url: /zh/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

有时，你需要将数据从一个范围复制到另一个范围，只复制数据本身，不复制格式。Aspose.Cells 提供了 [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-) 方法实现此功能。

{{% /alert %}} 
## **仅复制区域数据**
此示例演示如何：

1. 创建一个工作簿。
1. 在第一个工作表中的单元格中添加数据。
1. 创建一个范围。
1. 创建具有指定格式属性的样式对象。
1. 将样式格式应用于范围。
1. 创建另一个单元格范围。
1. 使用 [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-) 方法，将第一个范围的数据复制到第二个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
{{< app/cells/assistant language="java" >}}
