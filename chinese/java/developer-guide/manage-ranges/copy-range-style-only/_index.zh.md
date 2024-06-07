---
title: 仅复制范围样式
type: docs
weight: 350
url: /zh/java/copy-range-style-only/
---

{{% alert color="primary" %}} 

[仅复制范围数据](/cells/zh/java/copy-range-data-only/)和[复制带有样式的范围数据](/cells/zh/java/copy-range-data-with-style/)解释了如何复制带有或不带有格式的范围数据。也可以仅复制范围的格式。本文展示了如何操作。

{{% /alert %}} 
## **仅复制区域样式**
本例会创建工作簿，填充数据并仅复制范围的样式。

1. 创建一个范围。
1. 使用指定的格式属性创建样式对象。
1. 应用样式格式到范围。
1. 创建第二个单元格范围。
1. 将第一个范围的格式复制到第二个范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeStyleOnly-CopyRangeStyleOnly.java" >}}
