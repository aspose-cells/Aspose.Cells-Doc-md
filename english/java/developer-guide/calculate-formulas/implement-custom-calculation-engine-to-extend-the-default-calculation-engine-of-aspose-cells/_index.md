---
title: Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells
type: docs
weight: 590
url: /java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine which provides you greater power and flexibility.

The following property and classes are used in implementing this feature.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Implement Custom Calculation Engine**
The following code implements the Custom Calculation Engine. It implements the interface [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) which has only one method [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate-com.aspose.cells.CalculationData-). This method is called against all of your formulas. Inside this method, we capture the **TODAY** function and add one day to the system date. So if the current date is 27/07/2023, then the custom engine will calculate TODAY() as 28/07/2023.

### **Programming Sample**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **Result**

Please check the console output of the above sample code, the value(date time) of A1 with custom engine should be one day later than the result without custom engine.

### **Related Article**
{{% alert color="primary" %}} 

- [Direct calculation of custom function without writing it in a worksheet](/cells/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}