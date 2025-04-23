---
title: 单元格名称和行/列索引之间的转换
linktitle: 单元格名称和索引转换
type: docs
weight: 10
url: /zh/nodejs-cpp/names-and-indices/
description: 学习如何通过Aspose.Cells for Node.js via C++ API获取单元格名称与行/列索引之间的转换关系。
keywords: 通过C++用Node.js从行和列索引获取单元格名称，从单元格名称获取行和列索引，创建安全的工作表名称，添加安全的工作表名称。
---

## **从行和列索引获取单元格名称**
可以通过给定行和列索引来查找单元格的名称。 本文解释了如何操作。
Aspose.Cells for Node.js via C++提供CellsHelper.cellIndexToName方法，开发者在提供行和列索引后，可以获取单元格的名称。

{{% alert color="primary" %}} 

Microsoft Excel从1开始计数行和列索引。不同于Microsoft Excel，Aspose.Cells for Node.js via C++从0开始计数行和列索引。

{{% /alert %}} 

以下示例代码说明了如何使用CellsHelper.cellIndexToName在已知行和列索引的情况下访问单元格名称。代码生成以下输出。



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **从单元格名称获取行和列索引**
可以从单元格名称中找到单元格的行和列索引。 本文解释了如何操作。
Aspose.Cells for Node.js via C++提供CellsHelper.cellNameToIndex方法，允许开发者通过单元格名称获取行和列索引。

{{% alert color="primary" %}} 

Microsoft Excel从1开始计数行和列索引。不同于Microsoft Excel，Aspose.Cells for Node.js via C++从0开始计数行和列索引。

{{% /alert %}} 

以下示例代码说明了如何使用CellsHelper.cellNameToIndex根据单元格名称获取行和列索引。代码生成以下输出。



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **创建安全的工作表名称**
有时需要在运行时分配工作表名称。在这种情况下，可能存在包含一些额外字符（如<>+(?”})的工作表名称。需要将任何此类字符（不允许作为工作表名称）替换为用户提供的预设字符。同样，长度可能超过31个字符，需要截断。Apache POI提供了创建安全名称的某些功能，因此Aspose.Cells for Node.js via C++也提供类似功能来处理所有这些问题。以下示例代码展示了该功能：



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

输出:

这是第一个名字，它是特别私人的

` ``<> + (adj.Private _ " 私有"
