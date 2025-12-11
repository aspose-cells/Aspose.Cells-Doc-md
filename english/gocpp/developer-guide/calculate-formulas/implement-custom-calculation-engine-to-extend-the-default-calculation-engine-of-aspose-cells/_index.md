---
title: Implement Custom Calculation Engine to Extend the Default Calculation Engine of Aspose.Cells with Golang via C++
linktitle: Implement Custom Calculation Engine
description: This article describes how to extend the default calculation engine by implementing a custom calculation engine using the Aspose.Cells library with Golang via C++. By loading an existing Excel file or creating a new one, we can use the methods provided by Aspose.Cells to implement a custom calculation engine and get the results. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extend the default calculation engine, C++
type: docs
weight: 80
url: /go-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implement Custom Calculation Engine**

Aspose.Cells has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Nevertheless, it also allows you to extend the default calculation engine, which provides you greater power and flexibility.

The following property and classes are used in implementing this feature.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/go-cpp/calculationdata/)

The following code implements the custom calculation engine. It implements the interface [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) which has a [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/) method. This method is called for all of your formulas. Inside this method, we capture the **TODAY** function and add one day to the system date. So if the current date is 27/07/2023, then the custom engine will calculate TODAY() as 28/07/2023.

### **Programming Sample**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomCalculationEngineToExtendTheDefaultCalculationEngineOfAsposeCells.go" >}}

### **Result**

Please check the console output of the above sample code; the value (date/time) of A1 with the custom engine should be one day later than the result without the custom engine.

### **Related Article**

{{% alert color="primary" %}}

[Direct calculation of custom function without writing it in a worksheet](/cells/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}