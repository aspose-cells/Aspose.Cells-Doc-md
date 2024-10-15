---
title: Detecting Circular Reference
description: This article introduces how to use the Aspose.Cells library to detect circular references in Microsoft Excel. By loading an existing Excel file or creating a new one, we can use the method provided by Aspose.Cells to detect circular references and get the results. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /net/detecting-circular-reference/
---

## **Introduction**

Workbooks can have circular references and sometimes there is a need to detect if circular references are there or not.

## **Concept behind detecting the circular reference**

Circular references can only be detected when the formula is calculated because the references of one formula commonly depend on the calculated result of other parts or other formulas. So we provide new APIs for this requirement(to gather cells with circular references) in the process of formula calculation:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Represents the calculation of relevant data about one cell being calculated

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): will be invoked by formula calculation engine when encounter circular references, the element in the enumerator is [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) objects which represent all cells in one circle. The returned value denotes whether the formula engine needs to calculate those cells in circular after this call.

User may gather those circular references in the implementation of [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) method.

The source sample file can be downloaded from the following link:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definition of *CircularMonitor* class which is derived from [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) class is as follows:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}