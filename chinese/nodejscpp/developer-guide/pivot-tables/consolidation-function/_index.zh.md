---
title: 合并函数
type: docs
weight: 20
url: /zh/nodejs-cpp/consolidation-function/
description: 如何将汇总函数应用于Aspose.Cells for Node.js via C++中数据透视表的数值字段。
keywords: Aspose.Cells for Node.js via C++ Excel、Excel Node.js库，使用Aspose.Cells for Node.js via C++ Excel库对数据透视表的数据字段应用汇总函数。
---

## **合并函数**

Aspose.Cells for Node.js via C++可以用于对数据透视表的数值字段（或值字段）应用汇总函数。在Microsoft Excel中，你可以右键点击数值字段，然后选择**值字段设置...**，再切换到**汇总值方式**标签，然后选择你喜欢的任何汇总函数，如求和、计数、平均值、最大值、最小值、乘积、不同计数等。

Aspose.Cells for Node.js via C++ 提供 [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/) 枚举，支持以下汇总函数。

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **如何使用Aspose.Cells for Node.js via C++将汇总函数应用于数据透视表的数值字段。**

以下代码将**平均值**整合函数应用于第一个数据字段（或数值字段），将**不重复计数**整合函数应用于第二个数据字段（或数值字段）。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

Microsoft Excel 2013仅支持DISTINCT_COUNT合并函数。

{{% /alert %}}
