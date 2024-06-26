---
title: 创建数据透视表
type: docs
weight: 10
url: /zh/python-java/create-a-pivot-table/
---

## **创建数据透视表**
Aspose.Cells for Python via Java提供了创建数据透视表的功能。要使用Aspose.Cells创建数据透视表，请按照以下步骤操作：

1. 使用[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)对象的[setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)属性向工作表单元格添加一些数据。这些数据将用作数据透视表的数据源。
1. 通过调用[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\))方法在工作表中添加一个数据透视表。
1. 通过传递[PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)索引从[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)中访问[PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)对象。
1. 使用[PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)对象中封装的任何数据透视表对象（如上所述）来管理数据透视表。

以下代码片段演示如何使用Aspose.Cells API创建数据透视表。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
