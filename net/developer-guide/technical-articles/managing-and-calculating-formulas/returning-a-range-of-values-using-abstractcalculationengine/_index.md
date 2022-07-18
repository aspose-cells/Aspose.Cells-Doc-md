---
title: Returning a Range of Values using AbstractCalculationEngine
type: docs
weight: 55
url: /net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells provides [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) class which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

This article will explain how to return the range of values from [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

The following code demonstrates the use of the [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) class and returns the range of values via its method.

Create a class with a function *CalculateCustomFunction*. This class implements [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Now use above function into your program

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
