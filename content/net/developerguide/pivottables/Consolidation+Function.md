+++
title = "Consolidation Function" 
description = "" 
weight = 12235 
+++

Aspose.Cells for .NET : Consolidation Function  

# Aspose.Cells for .NET : Consolidation Function


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Consolidation function](#ConsolidationFunction-Consolidationfunction)
    *   1.1 [Applying ConsolidationFunction to Data Fields of Pivot Table](#ConsolidationFunction-ApplyingConsolidationFunctiontoDataFieldsofPivotTable)
{{< /panel >}}
 

## Consolidation function

Aspose.Cells can be used to apply ConsolidationFunction to data fields (or value fields) of the pivot table. In Microsoft Excel, you can right-click the value field and then select **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice like Sum, Count, Average, Max, Min, Product, Distinct Count, etc.

Aspose.Cells provides [ConsolidationFunction](https://apireference.aspose.com/net/cells/aspose.cells/consolidationfunction) enumeration to support the following consolidation functions.

*   `ConsolidationFunction.Average`
*   `ConsolidationFunction.Count`
*   `ConsolidationFunction.CountNums`
*   `ConsolidationFunction.DistinctCount`
*   `ConsolidationFunction.Max`
*   `ConsolidationFunction.Min`
*   `ConsolidationFunction.Product`
*   `ConsolidationFunction.StdDev`
*   `ConsolidationFunction.StdDevp`
*   `ConsolidationFunction.Sum`
*   `ConsolidationFunction.Var`
*   `ConsolidationFunction.Varp`

### Applying ConsolidationFunction to Data Fields of Pivot Table

The following code applies **Average** consolidation function to the first data field (or value field) and **DistinctCount** consolidation function to the second data field (or value field).

DistinctCount consolidation function is supported by Microsoft Excel 2013 only.

