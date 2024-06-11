---
title: 合并函数
type: docs
weight: 20
url: /zh/net/consolidation-function/
---

## **合并函数**

Aspose.Cells 可用于将合并函数应用于数据透视表的数据字段（或值字段）。在 Microsoft Excel 中，您可以右键单击值字段，然后选择“值字段设置...”选项，然后选择选项卡“按以下方式汇总值”。从那里，您可以选择任何您喜欢的合并函数，如求和、计数、平均值、最大值、最小值、乘积、去重计数等。

Aspose.Cells提供[**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction)枚举以支持以下合并功能。

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

### **应用合并功能到数据字段的数据透视表**

以下代码将**平均值**整合函数应用于第一个数据字段（或数值字段），将**不重复计数**整合函数应用于第二个数据字段（或数值字段）。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

Microsoft Excel 2013仅支持去重计数合并功能。

{{% /alert %}}
