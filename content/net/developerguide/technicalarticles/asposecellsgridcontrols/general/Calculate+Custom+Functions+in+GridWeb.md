+++
title = "Calculate Custom Functions in GridWeb" 
description = "" 
weight = 20345 
+++

Aspose.Cells for .NET : Calculate Custom Functions in GridWeb  

# Aspose.Cells for .NET : Calculate Custom Functions in GridWeb


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#CalculateCustomFunctionsinGridWeb-PossibleUsageScenarios)
*   2 [Calculate Custom Functions in GridWeb](#CalculateCustomFunctionsinGridWeb-CalculateCustomFunctionsinGridWeb)
    *   2.1 [Sample Code](#CalculateCustomFunctionsinGridWeb-SampleCode)
{{< /panel >}}
 

 

## Possible Usage Scenarios

Aspose.Cells.GridWeb supports the calculation of custom functions with the `GridWeb.CustomCalculationEngine` property. This property takes the instance of `GridAbstractCalculationEngine` interface. Please implement `GridAbstractCalculationEngine` interface and calculate your custom functions with your own logic.

## Calculate Custom Functions in GridWeb

The following sample code adds a custom function named `MYTESTFUNC()` in cell B3. Then we calculate the value of this function by implementing the `GridAbstractCalculationEngine` interface. We calculate `MYTESTFUNC()` in such a way that it multiplies its parameter with 2 and returns the result. So if its parameter is 9, it will return 2\*9 = 18.

### Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [gridweb-custom-calculation.png](https://docs2.aspose.com/cells/net/attachments/5013744/5115427.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Calculate Custom Functions in GridWeb-001.png](https://docs2.aspose.com/cells/net/attachments/5013744/5115169.png) (image/png)  

