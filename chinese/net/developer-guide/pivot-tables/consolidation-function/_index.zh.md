---
title: 整合功能
type: docs
weight: 20
url: /zh/net/consolidation-function/
---
## **整合功能**

Aspose.Cells 可用于将 ConsolidationFunction 应用于数据透视表的数据字段（或值字段）。在Microsoft Excel中，您可以右键单击值字段，然后选择**值字段设置...**选项，然后选择选项卡**值汇总依据**.从那里，您可以选择您选择的任何 ConsolidationFunction，例如 Sum、Count、Average、Max、Min、Product、Distinct Count 等。

Aspose.Cells提供[**整合功能**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction)支持以下合并功能的枚举。

- 整合函数.平均
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums 函数
- ConsolidationFunction.DistinctCount
- 合并函数.Max
- 合并函数.Min
- 合并函数.产品
- 合并函数.StdDev
- 合并函数.StdDevp
- 合并函数.Sum
- 合并函数.Var
- 合并函数.Varp

### **将 ConsolidationFunction 应用于数据透视表的数据字段**

以下代码适用**平均**合并功能到第一个数据字段（或值字段）和**非重复计数**合并功能到第二个数据字段（或值字段）。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

Microsoft 仅 Excel 2013 支持 DistinctCount 合并函数。

{{% /alert %}}
