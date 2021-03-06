---
title: Returning a Range of Values using ICustomFunction
type: docs
weight: 50
url: /net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

The [**ICustomFunction**](https://apireference.aspose.com/cells/net/aspose.cells/icustomfunction) is deprecated since the release of Aspose.Cells for Java 20.8. Please use the [**AbstractCalculationEngine**](https://apireference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) class. The use of the [**AbstractCalculationEngine**](https://apireference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) class is described in the following article.

[Returning a Range of Values using AbstractCalculationEngine](/cells/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells provides [**ICustomFunction**](https://apireference.aspose.com/cells/net/aspose.cells/icustomfunction) interface which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

Mostly when you implement the [**ICustomFunction**](https://apireference.aspose.com/cells/net/aspose.cells/icustomfunction) interface method, you need to return a single cell value. But sometimes, you need to return a range of values. This article will explain how to return the range of values from [**ICustomFunction**](https://apireference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

The following code implements [**ICustomFunction**](https://apireference.aspose.com/cells/net/aspose.cells/icustomfunction) and returns the range of values via its method.

Create a class with a function *CalculateCustomFunction*. This class implements [**ICustomFunction**](https://apireference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Now use above function into your program

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
