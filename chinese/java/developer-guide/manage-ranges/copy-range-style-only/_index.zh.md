---
title: 仅复制范围样式
type: docs
weight: 350
url: /zh/java/copy-range-style-only/
---

{{% alert color="primary" %}} 

[仅复制范围数据](/cells/zh/java/copy-range-data-only/) 和 [复制范围数据与样式](/cells/zh/java/copy-range-data-with-style/) 解释了如何复制范围的数据到另一个范围，并且可以选择是否保留格式。还可以仅复制范围的格式。本文介绍了如何实现。

{{% /alert %}} 
## **仅复制区域样式**
此示例创建一个工作簿，填充数据并仅复制范围的样式。

1. 创建一个范围。
1. 创建具有指定格式属性的样式对象。
1. 将样式格式应用于范围。
1. 创建第二个单元格范围。
1. 将第一个范围的格式复制到第二个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeStyleOnly-CopyRangeStyleOnly.java" >}}
