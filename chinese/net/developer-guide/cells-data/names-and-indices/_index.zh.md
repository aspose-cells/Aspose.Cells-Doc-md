---
title: 单元格名称和行/列索引之间的转换
linktitle: 单元格名称和索引转换
type: docs
weight: 10
url: /zh/net/names-and-indices/
description: 通过 Aspose.Cells for .NET API 学习如何在单元格名称和行/列索引之间进行转换。
keywords: 从行和列索引获取单元格名称，从单元格名称获取行和列索引，创建安全的工作表名称，添加安全的工作表名称
---

## **从行和列索引获取单元格名称**
可以通过给定行和列索引来查找单元格的名称。 本文解释了如何操作。
Aspose.Cells提供了CellsHelper.CellIndexToName方法，允许开发人员在提供行和列索引时获取单元格的名称。

{{% alert color="primary" %}} 

与Microsoft Excel不同，Aspose.Cells从0开始计算行列索引，而不是从1开始。

{{% /alert %}} 

以下示例代码说明如何使用CellsHelper.CellIndexToName来访问已知行和列索引的单元格名称。该代码生成以下输出。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **从单元格名称获取行和列索引**
可以从单元格名称中找到单元格的行和列索引。 本文解释了如何操作。
Aspose.Cells提供了CellsHelper.CellNameToIndex方法，允许开发人员从单元格的名称中获取行和列索引。

{{% alert color="primary" %}} 

与Microsoft Excel不同，Aspose.Cells从0开始计算行列索引，而不是从1开始。

{{% /alert %}} 

以下示例代码说明如何使用CellsHelper.CellNameToIndex来从单元格的名称中获取行和列索引。该代码生成以下输出。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **创建安全的工作表名称**
有时候需要在运行时指定工作表名称。在这种情况下，工作表名称可能包含一些附加字符，如<>+（？”。有必要替换不允许作为工作表名称的任何此类字符，使用用户提供的某个预设字符。同样，长度可能会增加到超过31个字符，需要截断。Apache POI提供了创建安全名称的某些功能，因此Aspose.Cells提供了类似的功能来处理所有这些问题。以下示例代码演示了此功能：



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

输出:

这是第一个名字，它是特别私人的

` ``<> + (adj.Private _ " 私有"
