---
title: Detecting Circular Reference
type: docs
weight: 70
url: /java/detecting-circular-reference/
---

## **Introduction**

Workbooks can have circular references and sometimes there is a need to detect if circular references are there or not.

## **Concept behind detecting the circular reference**

Circular references can only be detected when the formula is calculated because the references of one formula commonly depend on the calculated result of other parts or other formulas. So we provide new APIs for this requirement(to gather cells with circular references) in the process of formula calculation:

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Represents the calculation of relevant data about one cell being calculated

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-): will be invoked by formula calculation engine when encounter circular references, the element in the enumerator is [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) objects which represent all cells in one circle. The returned value denotes whether the formula engine needs to calculate those cells in circular after this call.

User may gather those circular references in the implementation of [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-) method.

The source sample file can be downloaded from the following link:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Definition of *CircularMonitor* class which is derived from [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) class is as follows:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
{{< app/cells/assistant language="java" >}}