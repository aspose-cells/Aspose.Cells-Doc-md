---
title: 仅复制范围样式
type: docs
weight: 350
url: /zh/java/copy-range-style-only/
---
{{% alert color="primary" %}} 

[仅复制范围数据](/cells/zh/java/copy-range-data-only/)和[使用样式复制范围数据](/cells/zh/java/copy-range-data-with-style/)解释了如何使用或不使用格式将数据从一个范围复制到另一个范围。也可以只复制范围的格式。本文展示了如何。

{{% /alert %}} 
## **仅复制范围样式**
此示例创建一个工作簿，用数据填充它并仅复制范围的样式。

1. 创建一个范围。
1. 创建具有指定格式属性的样式对象。
1. 将样式格式应用于范围。
1. 创建第二个单元格区域。
1. 将第一个范围的格式复制到第二个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeStyleOnly-CopyRangeStyleOnly.java" >}}
