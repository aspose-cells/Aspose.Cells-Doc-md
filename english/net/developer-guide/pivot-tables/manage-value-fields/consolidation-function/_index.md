---
title: Consolidation Function
type: docs
weight: 20
url: /net/consolidation-function/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Consolidation function**

Aspose.Cells can be used to apply a **ConsolidationFunction** to data fields (or value fields) of a pivot table. In Microsoft Excel, you can right‑click the value field, select the **Value Field Settings...** option, and then choose the **Summarize Values By** tab. From there, you can select any **ConsolidationFunction** of your choice, such as Sum, Count, Average, Max, Min, Product, Distinct Count, etc.

Aspose.Cells provides the [**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) enumeration to support the following consolidation functions.

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

The following code applies the **Average** consolidation function to the first data field (or value field) and the **DistinctCount** consolidation function to the second data field (or value field).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}
DistinctCount consolidation function is supported by Microsoft Excel 2013 only.
{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
