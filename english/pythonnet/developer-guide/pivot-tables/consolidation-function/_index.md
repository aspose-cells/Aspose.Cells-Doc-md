---
title: Consolidation Function
type: docs
weight: 20
url: /python-net/consolidation-function/
description: How to apply ConsolidationFunction to Data Fields of Pivot Table with Aspose.Cells for Python via .NET.
keywords: ConsolidationFunction to Data Fields of Pivot Table.
---

## **Consolidation function**

Aspose.Cells for Python via .NET can be used to apply ConsolidationFunction to data fields (or value fields) of the pivot table. In Microsoft Excel, you can right-click the value field and then select **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice like Sum, Count, Average, Max, Min, Product, Distinct Count, etc.

Aspose.Cells for Python via .NET provides [**ConsolidationFunction**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) enumeration to support the following consolidation functions.

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

### **Applying ConsolidationFunction to Data Fields of Pivot Table**

The following code applies **AVERAGE** consolidation function to the first data field (or value field) and **DISTINCT_COUNT** consolidation function to the second data field (or value field).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

DISTINCT_COUNT consolidation function is supported by Microsoft Excel 2013 only.

{{% /alert %}}
