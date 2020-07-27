+++
title = "Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells" 
description = "" 
weight = 12526 
+++

Aspose.Cells for Java : Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells  

# Aspose.Cells for Java : Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells


Aspose.Cells has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine which provides you greater power and flexibility.

The following property and classes are used in implementing this feature.

*   [CalculationOptions.CustomEngine](https://apireference.aspose.com/java/cells/com.aspose.cells/calculationoptions#CustomEngine)
*   [AbstractCalculationEngine](https://apireference.aspose.com/java/cells/com.aspose.cells/AbstractCalculationEngine)
*   [CalculationData](https://apireference.aspose.com/java/cells/com.aspose.cells/CalculationData)

#### Implement Custom Calculation Engine

The following code implements the Custom Calculation Engine. It implements the interface [AbstractCalculationEngine](https://apireference.aspose.com/java/cells/com.aspose.cells/AbstractCalculationEngine) which has only one method [calculate(CalculationData data)](https://apireference.aspose.com/java/cells/com.aspose.cells/abstractcalculationengine#calculate(com.aspose.cells.CalculationData)). This method is called against all of your formulas. Inside this method, we capture the **SUM** formula and increases its value by 30. So if the Aspose.Cells calculated value is 20, then our custom engine will make it 50 by adding 30.


#### Console Output

Here is the console output of the above sample code.

{{< code lang="cs" >}}
Without Custom Engine Value of A1: 20
With Custom Engine Value of A1: 50
{{< /code >}}

#### Related Article

*   [Direct calculation of custom function without writing it in a worksheet](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/direct+calculation+of+custom+function+without+writing+it+in+a+worksheet)

