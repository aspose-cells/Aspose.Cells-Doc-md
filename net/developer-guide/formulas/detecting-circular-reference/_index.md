---
title: Detecting Circular Reference
type: docs
weight: 20
url: /net/detecting-circular-reference/
---

## **Introduction**

Workbooks can have circular references and sometimes there is a need to detect if circular references are there or not.

## **Concept behind detecting the circular reference**

Circular references can only be detected when the formula is calculated because the references of one formula commonly depend on the calculated result of other parts or other formulas. So we provide new APIs for this requirement(to gather cells with circular references) in the process of formula calculation:

[**CalculationCell**](https://apireference.aspose.com/cells/net/aspose.cells/calculationcell): Represents the calculation of relevant data about one cell being calculated

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://apireference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): will be invoked by formula calculation engine when encounter circular references, the element in the enumerator is [**CalculationCell**](https://apireference.aspose.com/cells/net/aspose.cells/calculationcell) objects which represent all cells in one circle. The returned value denotes whether the formula engine needs to calculate those cells in circular after this call.

User may gather those circular references in the implementation of [**AbstractCalculationMonitor.OnCircular()**](https://apireference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular) method.

The source sample file can be downloaded from the following link:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Definition of *CircularMonitor* class which is derived from [**AbstractCalculationMonitor**](https://apireference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) class is as follows:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
