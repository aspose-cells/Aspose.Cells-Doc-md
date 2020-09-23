---
title: Consolidation Function
type: docs
weight: 20
url: /net/consolidation-function/
---

## **Consolidation function**

Aspose.Cells can be used to apply ConsolidationFunction to data fields (or value fields) of the pivot table. In Microsoft Excel, you can right-click the value field and then select **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice like Sum, Count, Average, Max, Min, Product, Distinct Count, etc.

Aspose.Cells provides [**ConsolidationFunction**](https://apireference.aspose.com/cells/net/aspose.cells/consolidationfunction) enumeration to support the following consolidation functions.

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

### **Applying ConsolidationFunction to Data Fields of Pivot Table**

The following code applies **Average** consolidation function to the first data field (or value field) and **DistinctCount** consolidation function to the second data field (or value field).

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

DistinctCount consolidation function is supported by Microsoft Excel 2013 only.

{{% /alert %}}
