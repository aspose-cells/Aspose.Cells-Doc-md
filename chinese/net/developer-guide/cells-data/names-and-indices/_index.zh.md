---
title: 单元格名称与行/列索引之间的转换
linktitle: Cell 名称和索引转换
type: docs
weight: 10
url: /zh/net/names-and-indices/
description: 了解如何通过 Aspose.Cells for .NET API 获取单元格名称与行/列索引之间的转换。
keywords: Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
---
##  **从行索引和列索引中获取 Cell 名称**
给定行和列索引可以找到单元格的名称。本文解释了如何操作。
Aspose.Cells 提供了 CellsHelper.CellIndexToName 方法，允许开发人员在提供行和列索引的情况下获取单元格的名称。

{{% alert color="primary" %}} 

与 Microsoft Excel 的行索引和列索引从 1 开始不同，Aspose.Cells 从 0 开始计算行索引和列索引。

{{% /alert %}} 

以下示例代码说明了如何使用 CellsHelper.CellIndexToName 来访问给定已知行和列索引的单元格名称。该代码生成以下输出。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
##  **从 Cell 名称获取行索引和列索引**
可以从单元格的名称中找到单元格的行索引和列索引。本文解释了如何操作。
Aspose.Cells 提供了 CellsHelper.CellNameToIndex 方法，允许开发人员从单元格名称获取行和列索引。

{{% alert color="primary" %}} 

与 Microsoft Excel 的行索引和列索引从 1 开始不同，Aspose.Cells 从 0 开始计算行索引和列索引。

{{% /alert %}} 

以下示例代码说明了如何使用 CellsHelper.CellNameToIndex 从单元格名称获取行索引和列索引。该代码生成以下输出。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
##  **创建安全工作表名称**
有时需要在运行时分配工作表名称。在这种情况下，工作表名称可能包含一些附加字符，例如<>+(?”。需要替换任何此类字符，这是不允许用用户提供的某些预设字符作为工作表名称的。同样，长度可能会增加到超过 31 个字符，需要被截断。Apache POI 提供创建安全名称的某些功能，因此 Aspose.Cells 提供了类似的功能来处理所有这些问题。以下示例代码演示了此功能：



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

输出：

这是名字，cre

` `<> + (adj.私人_“私人”
