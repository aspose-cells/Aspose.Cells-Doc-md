---
title: Returning a Range of Values using AbstractCalculationEngine with Golang via C++
linktitle: Returning a Range of Values using AbstractCalculationEngine
description: This article introduces an abstract calculation engine that returns a range of values in Microsoft Excel using the Aspose.Cells library with Golang via C++. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to get a range of values and return the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, an abstract calculation engine that returns a series of values
type: docs
weight: 55
url: /go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells provides **the AbstractCalculationEngine** class, which is used to implement user‑defined or custom functions that are not supported by Microsoft Excel as built‑in functions.

This article will explain how to return the range of values from **AbstractCalculationEngine**.

{{% /alert %}}

The following code demonstrates the use of the **AbstractCalculationEngine** class and returns a range of values via its method.

Create a class with a function `CalculateCustomFunction`. This class implements **AbstractCalculationEngine**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
Now use the above function in your program.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}