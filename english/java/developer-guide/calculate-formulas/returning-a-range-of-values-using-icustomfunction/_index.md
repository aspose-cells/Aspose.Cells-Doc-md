---
title: Returning a Range of Values using ICustomFunction
type: docs
weight: 270
url: /java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

The [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) is deprecated since the release of Aspose.Cells for Java 20.8. Please use the [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) class. The use of the [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) class is described in the following article.

[Returning a Range of Values using AbstractCalculationEngine](/cells/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells provides [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) interface which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

Mostly when you implement the [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) interface method, you need to return a single cell value. But sometimes, you need to return a range of values. This article will explain how to return the range of values from [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Returning a Range of Values using ICustomFunction**

The following code implements [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) and returns the range of values via its method. Please check the [output excel file](5472922.xlsx) and [pdf](5472925.pdf) generated with the code for your reference.

Create a class with a function *CalculateCustomFunction*. This class implements [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Now use the above function into your program.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
{{< app/cells/assistant language="java" >}}