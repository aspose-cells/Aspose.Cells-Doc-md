---
title: 单元格名称与行/列索引之间的转换
linktitle: Cell 名称和索引转换
type: docs
weight: 5
url: /zh/java/names-and-indices/
---
## **从行和列索引中获取 Cell 名称**
给定行和列索引可以找到单元格的名称。这篇文章解释了如何。

Aspose.Cells 提供了[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) 方法允许开发人员在提供行和列索引的情况下获取单元格的名称。

{{% alert color="primary" %}} 

与 Microsoft Excel 的行和列索引从 1 开始不同，Aspose.Cells 从 0 开始计算行和列索引。

{{% /alert %}} 

下面的示例代码说明了如何使用[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)以访问在已知行和列索引处给出的单元格名称。该代码生成以下输出。



Cell [0, 0] 处的名称：A1

Cell [4, 0] 处的名称：A5

Cell [0, 4] 处的名称：E1

Cell [2, 2] 处的姓名：C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **从 Cell 名称获取行和列索引**
可以从单元格的名称中找到单元格的行和列索引。这篇文章解释了如何。

Aspose.Cells 提供了[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) 方法，它允许开发人员从单元格的名称中获取行和列索引。

{{% alert color="primary" %}} 

与 Microsoft Excel 的行和列索引从 1 开始不同，Aspose.Cells 从 0 开始计算行和列索引。

{{% /alert %}} 

下面的示例代码说明了如何使用[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) 从单元格名称中获取行和列索引。该代码生成以下输出。



Cell C6 的行索引：5

Cell C6的专栏索引：2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **创建安全工作表名称**
有时需要在运行时分配工作表名称。在这种情况下，工作表名称可能包含一些其他字符，例如<>+(?)。需要用用户提供的一些预设字符替换任何这样的字符，不允许作为工作表名称。同样，长度可能会增加到 31 个字符以上，需要截断。Apache POI 提供了创建安全名称的某些功能，因此 Aspose.Cells 提供了类似的功能来处理所有这些问题。以下示例代码演示了此功能：



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**控制台输出**

这是名字 cre

` `<> + (adj.Private _ "私人"
