---
title: 单元格名称和行/列索引之间的转换
linktitle: 单元格名称和索引转换
type: docs
weight: 5
url: /zh/java/names-and-indices/
description: 学习如何使用Aspose.Cells for Java API在单元格名称和行/列索引之间获取转换结果。
keywords: Java将单元索引转换为名称，使用java api将单元名称转换为行/列索引，Java如何从行和列索引获取单元名称。
---

## **如何从行和列索引获取单元名称**
可以根据行和列索引找到单元格的名称。本文解释了如何执行此操作。

Aspose.Cells提供了CellsHelper.cellIndexToName方法，允许开发人员在提供行和列索引时获取单元格名称。

{{% alert color="primary" %}} 

与Microsoft Excel不同，其中行和列索引从1开始，Aspose.Cells从0开始计算行和列索引。

{{% /alert %}} 

以下示例代码说明了如何使用CellsHelper.cellIndexToName访问已知行和列索引的单元格名称。代码生成以下输出。



[0,0]处的单元格名称：A1

[4,0]处的单元格名称：A5

[0,4]处的单元格名称：E1

[2,2]处的单元格名称：C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **如何从单元格名称获取行和列索引**
可以从单元格的名称找到行和列索引。本文解释了如何执行此操作。

Aspose.Cells提供了CellsHelper.cellNameToIndex方法，允许开发人员从单元格名称获取行和列索引。

{{% alert color="primary" %}} 

与Microsoft Excel不同，其中行和列索引从1开始，Aspose.Cells从0开始计算行和列索引。

{{% /alert %}} 

以下示例代码说明了如何使用CellsHelper.cellNameToIndex从单元格名称获取行和列索引。代码生成以下输出。



单元格C6的行索引: 5

单元格C6的列索引: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **如何创建安全的工作表名称**
有时需要在运行时指定工作表名称。在这种情况下，工作表名称可能包含一些额外的字符，如<>+(？”。需要用用户提供的预设字符替换任何不允许作为工作表名称的字符。同样，长度可能增加到超过31个字符，需要被截断。Apache POI提供了创建安全名称的某些特性，因此Aspose.Cells提供了类似的功能来处理所有这些问题。以下示例代码演示了这个特性：



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**控制台输出**

这是第一个名字，它是创建

` `<> + (adj.Private _ " Private"
