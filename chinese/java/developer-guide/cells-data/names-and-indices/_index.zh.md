---
title: 单元格名称和行/列索引之间的转换
linktitle: 单元格名称和索引转换
type: docs
weight: 5
url: /zh/java/names-and-indices/
description: 学习如何使用 Aspose.Cells for Java API 获取单元格名称和行/列索引之间的转换结果。
keywords: Java 将单元格索引转换为名称，使用 Java API 将单元格名称转换为行/列索引，如何使用 Java 从行和列索引获取单元格名称，Java 如何从单元格名称获取行和列索引。
---

## **如何从行和列索引获取单元格名称**
可以通过给定行和列索引来查找单元格的名称。 本文解释了如何操作。

Aspose.Cells提供了[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-)方法，可以让开发者通过行列索引获取单元格的名称。

{{% alert color="primary" %}} 

Microsoft Excel从1开始计数行和列的索引。不同于Microsoft Excel，Aspose.Cells从0开始计数行和列的索引。

{{% /alert %}} 

以下示例代码演示如何使用[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) 根据已知的行列索引获取单元格名称。代码输出如下：

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **如何从单元格名称获取行和列索引**
可以从单元格名称中找到单元格的行和列索引。 本文解释了如何操作。

Aspose.Cells提供了[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-)方法，可以从单元格名称获取对应的行列索引。

{{% alert color="primary" %}} 

Microsoft Excel从1开始计数行和列的索引。不同于Microsoft Excel，Aspose.Cells从0开始计数行和列的索引。

{{% /alert %}} 

以下示例代码演示如何使用 [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) 从单元格名称获取行和列索引。该代码生成如下输出。

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **如何创建安全的工作表名称**
有时需要在运行时分配工作表名称。在这种情况下，可能存在包含一些额外字符（如<>+（?的工作表名称。需要替换任何不允许作为工作表名称的字符，使用用户提供的预设字符。同样，长度可能会增加到超过31个字符，需要截断。Apache POI提供了创建安全名称的某些功能，因此Aspose.Cells提供了类似的功能以处理所有这些问题。以下示例代码演示了这一特性：



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**控制台输出**

这是第一个名字，它是特别私人的

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
