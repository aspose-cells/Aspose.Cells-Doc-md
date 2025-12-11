---
title: Returning a Range of Values using ICustomFunction
type: docs
weight: 270
url: /java/returning-a-range-of-values-using-icustomfunction/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

The **ICustomFunction** is deprecated as of the release of Aspose.Cells for Java 20.8. Please use the **AbstractCalculationEngine** class. Usage of the **AbstractCalculationEngine** class is described in the following article.

[Returning a Range of Values using AbstractCalculationEngine](/cells/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells provides the **ICustomFunction** interface, which is used to implement user‑defined or custom functions that are not supported by Microsoft Excel as built‑in functions.

Typically, when you implement the **ICustomFunction** interface method, you need to return a single cell value. But sometimes you need to return a range of values. This article explains how to return a range of values from **ICustomFunction**.

{{% /alert %}}

## **Returning a Range of Values using ICustomFunction**

The following code implements **ICustomFunction** and returns the range of values via its method. Please check the output Excel file (5472922.xlsx) and PDF (5472925.pdf) generated with the code for your reference.

Create a class with a function *CalculateCustomFunction*. This class implements the **ICustomFunction** interface.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Now use the above function in your program.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
{{< app/cells/assistant language="java" >}}
