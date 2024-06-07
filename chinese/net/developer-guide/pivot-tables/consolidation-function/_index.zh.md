---
title: 合并函数
type: docs
weight: 20
url: /zh/net/consolidation-function/
---

## **合并函数**

Aspose.Cells 可用于将合并函数应用于数据透视表的数据字段（或值字段）。在 Microsoft Excel 中，您可以右键单击值字段，然后选择**值字段设置...**选项，然后选择**通过汇总值**选项卡。从那里，您可以选择任意合并函数，例如求和、计数、平均、最大值、最小值、乘积、唯一计数等。

Aspose.Cells 提供 [**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) 枚举以支持以下合并函数。

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

### **将合并函数应用于数据透视表的数据字段**

以下代码将**平均值**合并函数应用于第一个数据字段（或值字段），并将**唯一计数**合并函数应用于第二个数据字段（或值字段）。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

**唯一计数**合并函数仅受 Microsoft Excel 2013 支持。

{{% /alert %}}
