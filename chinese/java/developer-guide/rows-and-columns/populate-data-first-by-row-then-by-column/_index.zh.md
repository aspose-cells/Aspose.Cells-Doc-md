---
title: 首先按行然后按列填充数据
type: docs
weight: 10
url: /zh/java/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}}

首先按行然后再按列填充电子表格中的数据可以提高整体性能。

{{% /alert %}}

## 首先按行然后按列填充数据

将数据放入A1，B1，A2，B2顺序要比A1，A2，B1，B2更快。如果工作表中有许多单元格且按照第二个顺序进行，则是，即逐行填充数据，这个提示可以使程序运行速度加快。

## Java代码先按行填充数据，然后按列填充

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
