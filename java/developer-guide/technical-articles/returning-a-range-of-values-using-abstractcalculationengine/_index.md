---
title: Returning a Range of Values using AbstractCalculationEngine
type: docs
weight: 275
url: /java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells provides [**AbstractCalculationEngine**](https://apireference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) class which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

This article will explain how to return the range of values from [**AbstractCalculationEngine**](https://apireference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{% /alert %}}

The following code demonstrates the use of the [**AbstractCalculationEngine**](https://apireference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) and returns the range of values via its method.

Create a class with a function *CalculateCustomFunction*. This class extends [**AbstractCalculationEngine**](https://apireference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Now use the above function into your program.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
