---
title: Detecting Circular Reference
description: This article introduces how to use the Aspose.Cells library to detect circular references in Microsoft Excel. By loading an existing Excel file or creating a new one, we can use the method provided by Aspose.Cells to detect circular references and get the results. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /net/detecting-circular-reference/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Workbooks can contain circular references, and sometimes there is a need to detect whether circular references are present.

## **Concept behind detecting the circular reference**

Circular references can only be detected when the formula is calculated because the references of one formula often depend on the calculated results of other cells or formulas. Therefore, we provide new APIs for this requirement (to gather cells with circular references) in the process of formula calculation:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Represents the calculation of relevant data about one cell being calculated

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): will be invoked by the formula calculation engine when it encounters circular references; the elements in the enumerator are **CalculationCell** objects that represent all cells in a circular chain. The returned value indicates whether the formula engine should continue calculating those cells involved in the circular reference after this call.

Users may gather those circular references in the implementation of the [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) method.

The source sample file can be downloaded from the following link:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

The definition of the *CircularMonitor* class, which derives from the [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) class, is as follows:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
