---
title : "Direct calculation of custom function without writing it in a worksheet" 
description : "" 
weight : 12532 
toc : false
type: docs
url: /java/developerguide/technicalarticles/direct+calculation+of+custom+function+without+writing+it+in+a+worksheet/
---

# Aspose.Cells for Java : Direct calculation of custom function without writing it in a worksheet


This article explains how you can directly calculate your custom functions without first writing them in a worksheet. Please use the [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) method for this purpose.

#### Direct calculation of custom function without writing it in a worksheet

Please see the following sample code that illustrates the usage of this method. We have used a custom function named *MyCompany.CustomFunction()* and we calculate its value as "Aspose.Cells." by ourselves and then this value is automatically concatenated with the value of cell A1 which is "Welcome to " by the calculation engine and the final calculated value returns as "Welcome to Aspose.Cells.". As you can see in a code that we have not written our custom function anywhere in a worksheet and it is calculated directly by our own custom logic.


#### Console Output

Below is the console output of the above sample code.

{{< code lang="cs" >}}
Calculated Value: Welcome to Aspose.Cells.
{{< /code >}}

#### Related Article

*   [Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/implement+custom+calculation+engine+to+extend+the+default+calculation+engine+of+aspose.cells)

