---
title: 合并函数
type: docs
weight: 20
url: /zh/python-net/consolidation-function/
description: 如何使用 Aspose.Cells for Python 通过 .NET 将汇总函数应用于数据透视表中的数据字段
keywords: Aspose.Cells for Python Excel，Excel Python 库，使用 Aspose.Cells for Python Excel 库将汇总函数应用于数据透视表的数据字段。
---

## **合并函数**

Aspose.Cells for Python 通过 .NET 可用于将汇总函数应用于数据透视表的数据字段（或数值字段）。在 Microsoft Excel 中，您可以右键单击数值字段，然后选择 **值字段设置...** 选项，然后选择选项卡 **通过汇总值**。从那里，您可以选择任何您喜欢的汇总函数，如求和、计数、平均、最大、最小、乘积、去重计数等。

Aspose.Cells for Python 通过 .NET 提供 [**ConsolidationFunction**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) 枚举以支持以下的汇总函数。

- ConsolidationFunction.AVERAGE
- ConsolidationFunction.COUNT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.DISTINCT_COUNT
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.SUM
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP

## **如何使用 Aspose.Cells for Python Excel 库将汇总函数应用于数据透视表中的数据字段**

以下代码将 **AVERAGE** 汇总函数应用于第一个数据字段（或数值字段），并将 **DISTINCT_COUNT** 汇总函数应用于第二个数据字段（或数值字段）。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

Microsoft Excel 2013 仅支持 DISTINCT_COUNT 汇总函数。

{{% /alert %}}
