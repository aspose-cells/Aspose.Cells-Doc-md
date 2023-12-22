---
title: 单元格名称与行/列索引之间的转换
linktitle: Cell 名称和索引转换
type: docs
weight: 5
url: /zh/java/names-and-indices/
description: 了解如何使用 Aspose.Cells for Java API 获取单元格名称与行/列索引之间的转换结果。
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---
##  **如何从行索引和列索引中获取 Cell 名称**
给定行和列索引可以找到单元格的名称。本文解释了如何操作。

 Aspose.Cells 提供[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) 方法，允许开发人员在提供行和列索引的情况下获取单元格的名称。

{{% alert color="primary" %}} 

与 Microsoft Excel 的行索引和列索引从 1 开始不同，Aspose.Cells 从 0 开始计算行索引和列索引。

{{% /alert %}} 

下面的示例代码说明了如何使用[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) 访问在已知行和列索引处给出的单元格名称。该代码生成以下输出。



Cell 名称位于 [0, 0]: A1

Cell 姓名位于 [4, 0]: A5

Cell [0, 4] 处的名称：E1

Cell 姓名 [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
##  **如何从 Cell 名称获取行索引和列索引**
可以从单元格的名称中找到单元格的行索引和列索引。本文解释了如何操作。

 Aspose.Cells 提供[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) 方法，该方法允许开发人员从单元格名称中获取行和列索引。

{{% alert color="primary" %}} 

与 Microsoft Excel 的行索引和列索引从 1 开始不同，Aspose.Cells 从 0 开始计算行索引和列索引。

{{% /alert %}} 

下面的示例代码说明了如何使用[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) 从单元格名称中获取行索引和列索引。该代码生成以下输出。



Cell C6 的行索引：5

Cell C6 的列索引：2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
##  **如何创建安全工作表名称**
有时需要在运行时分配工作表名称。在这种情况下，工作表名称可能包含一些附加字符，例如<>+(?”。需要替换任何此类字符，这是不允许用用户提供的某些预设字符作为工作表名称的。同样，长度可能会增加到超过 31 个字符，需要被截断。Apache POI提供了创建安全名称的某些功能，因此Aspose.Cells提供了类似的功能来处理所有这些问题。以下示例代码演示了此功能：



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**控制台输出**

这是名字，cre

` `<> + (adj.私人_“私人”
