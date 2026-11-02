---
title: 使用 Golang 通过 C++ 在数据透视表中对数据透视字段进行分组
linktitle: 使用 Golang 通过 C++ 在数据透视表中对数据透视字段进行分组
description: 了解如何使用 Aspose.Cells for Go via C++ 在数据透视表中对数据透视字段进行分组。
keywords: Aspose.Cells, Aspose.Cells for Go via C++, 数据透视表, 数据透视字段, 对数据透视字段进行分组, GroupBy, PivotField, 日期分组, Go
type: docs
weight: 80
url: /zh/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
Microsoft Excel 允许您在数据透视表中对数据透视字段进行**分组**。当与某个数据透视字段相关的数据量较大时，通常可将这些数据划分为若干部分进行分组。Aspose.Cells 同样通过 [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/) 方法提供此功能。

## **在数据透视表中对数据透视字段进行分组**
以下示例代码加载[示例 Excel 文件](64716818.xlsx)，并使用 [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/) 方法对第一个数据透视字段进行分组。随后，代码刷新数据透视表、重新计算数据，并将工作簿另存为[输出 Excel 文件](64716817.xlsx)。截图展示了示例代码应用于示例 Excel 文件后的效果。如截图所示，第一个数据透视字段现已按月份和季度进行了分组。
![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}