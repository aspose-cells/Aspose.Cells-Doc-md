---
title: 合并函数
type: docs
weight: 20
url: /zh/python-net/consolidation-function/
description: 如何使用Aspose.Cells for Python via .NET对数据透视表的数据字段应用合并函数。
keywords: Aspose.Cells for Python Excel，Excel Python库，使用Aspose.Cells for Python Excel库对数据透视表的数据字段应用合并函数。
---

## **合并函数**

Aspose.Cells for Python via .NET可用于将合并函数应用于数据透视表的数据字段（或值字段）。在Microsoft Excel中，您可以右键单击值字段，然后选择**值字段设置...**选项，然后选择选项卡**根据汇总的值**。从那里，您可以选择您喜欢的任何合并函数，如求和、计数、平均、最大、最小、乘积、不同计数等。

Aspose.Cells for Python via .NET提供[**ConsolidationFunction**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/)枚举以支持以下合并函数。

-ConsolidationFunction.AVERAGE
-ConsolidationFunction.COUNT
-ConsolidationFunction.COUNT_NUMS
-ConsolidationFunction.DISTINCT_COUNT
-ConsolidationFunction.MAX
-ConsolidationFunction.MIN
-ConsolidationFunction.PRODUCT
-ConsolidationFunction.STD_DEV
-ConsolidationFunction.STD_DEVP
-ConsolidationFunction.SUM
-ConsolidationFunction.VAR
-ConsolidationFunction.VARP

## **如何使用Aspose.Cells for Python Excel库将ConsolidationFunction应用于数据字段的数据透视表**

以下代码将**AVERAGE**合并函数应用于第一个数据字段（或值字段），并将**DISTINCT_COUNT**合并函数应用于第二个数据字段（或值字段）。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

Microsoft Excel 2013仅支持DISTINCT_COUNT合并函数。

{{% /alert %}}
