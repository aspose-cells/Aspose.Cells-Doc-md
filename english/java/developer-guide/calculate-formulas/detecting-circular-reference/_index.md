---
title: Detecting Circular Reference
type: docs
weight: 70
url: /java/detecting-circular-reference/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Workbooks can contain circular references, and sometimes there is a need to detect whether circular references are present.

## **Concept behind detecting the circular reference**

Circular references can only be detected when the formula is calculated because the references of one formula commonly depend on the calculated result of other parts or other formulas. So we provide new APIs for this requirement (to gather cells with circular references) in the process of formula calculation:

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Represents the calculation of relevant data about one cell being calculated  

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-): will be invoked by the formula calculation engine when it encounters circular references; the elements in the iterator are **CalculationCell** objects which represent all cells in a circular reference. The returned value indicates whether the formula engine should continue calculating those cells involved in the circular reference after this call.

Users may gather those circular references in the implementation of the [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-) method.

The source sample file can be downloaded from the following link:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

The definition of the *CircularMonitor* class, which derives from [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) class, is as follows:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
{{< app/cells/assistant language="java" >}}
