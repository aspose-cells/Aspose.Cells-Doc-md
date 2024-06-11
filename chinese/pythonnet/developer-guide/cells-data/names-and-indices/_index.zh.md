---
title: 单元格名称和行/列索引之间的转换
linktitle: 单元格名称和索引转换
type: docs
weight: 10
url: /zh/python-net/names-and-indices/
description: 通过Aspose.Cells为Python通过.NET API获取单元格名称和行/列索引之间的转换。
keywords: Python Excel库，通过行和列索引获取单元格名称，通过单元格名称获取行和列索引，创建安全的工作表名称，添加安全的工作表名称
---

## **从行和列索引获取单元格名称**
可以根据行和列索引找到单元格的名称。本文解释了如何执行此操作。
Aspose.Cells for Python提供了[**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int)方法，允许开发人员根据提供的行和列索引获取单元格名称。

{{% alert color="primary" %}} 

与Microsoft Excel不同，Aspose.Cells for Python通过.NET从0开始计数行和列索引，而不是从1开始。

{{% /alert %}} 

以下示例代码演示了如何使用[**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int)来访问已知行和列索引的单元格名称。该代码生成以下输出。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **从单元格名称获取行和列索引**
可以从单元格的名称找到行和列索引。本文解释了如何执行此操作。
Aspose.Cells for Python通过.NET提供了[**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)方法，允许开发人员从单元格名称中获取行和列索引。

{{% alert color="primary" %}} 

与Microsoft Excel不同，Aspose.Cells for Python通过.NET从0开始计数行和列索引，而不是从1开始。

{{% /alert %}} 

以下示例代码演示了如何使用[**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)从单元格名称中获取行和列索引。该代码生成以下输出。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **创建安全的工作表名称**
有时需要在运行时分配工作表名称。在这种情况下，可能会有一些工作表名称包含一些额外字符，如<>+(?”. 需要替换任何不允许作为工作表名称的字符，将其替换为用户提供的预设字符。同样长度可能会增加到超过31个字符，需要截断。Apache POI提供了创建安全名称的某些特性，因此Aspose.Cells为Python通过.NET提供了相似的功能来处理所有这些问题。以下示例代码演示了此功能:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

输出：

这是第一个名字，它是创建

` <> +（adj.Private _ "私人"
