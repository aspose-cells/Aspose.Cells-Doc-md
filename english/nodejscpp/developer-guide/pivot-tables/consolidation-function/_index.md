---
title: Consolidation Function
type: docs
weight: 20
url: /nodejs-cpp/consolidation-function/
description: How to apply ConsolidationFunction to Data Fields of Pivot Table with Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js library, ConsolidationFunction to Data Fields of Pivot Table Using Aspose.Cells for Node.js via C++ Excel Library.
---

## **Consolidation function**

Aspose.Cells for Node.js via C++ can be used to apply ConsolidationFunction to data fields (or value fields) of the pivot table. In Microsoft Excel, you can right-click the value field and then select **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice like Sum, Count, Average, Max, Min, Product, Distinct Count, etc.

Aspose.Cells for Node.js via C++ provides [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/) enumeration to support the following consolidation functions.

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

## **How to Apply ConsolidationFunction to Data Fields of Pivot Table Using Aspose.Cells for Node.js via C++**

The following code applies **Average** consolidation function to the first data field (or value field) and **DistinctCount** consolidation function to the second data field (or value field).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

DISTINCT_COUNT consolidation function is supported by Microsoft Excel 2013 only.

{{% /alert %}}
