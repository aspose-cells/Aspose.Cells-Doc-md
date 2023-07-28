---
title: Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells
type: docs
weight: 80
url: /net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implement Custom Calculation Engine**

Aspose.Cells has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine which provides you greater power and flexibility.

The following property and classes are used in implementing this feature.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

The following code implements the Custom Calculation Engine. It implements the interface **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** which has a **[Calculate(CalculationData data)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** method. This method is called against all of your formulas. Inside this method, we capture the **TODAY** function and add one day to the system date. So if the current date is 27/07/2023, then the custom engine will calculate TODAY() as 28/07/2023.

### **Programming Sample**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Result**

Please check the console output of the above sample code, the value(date time) of A1 with custom engine should be one day later than the result without custom engine.

### **Related Article**

{{% alert color="primary" %}}

[Direct calculation of custom function without writing it in a worksheet](/cells/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
