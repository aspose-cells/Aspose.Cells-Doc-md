---
title : "Decrease the Calculation Time of Cell.Calculate method" 
description : "" 
weight : 20548 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/calculationengine/decrease+the+calculation+time+of+cell.calculate+method/
---

# Aspose.Cells for .NET : Decrease the Calculation Time of Cell.Calculate method


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Decrease the Calculation Time of Cell.Calculate() method](#decrease-the-calculation-time-of-cell.calculate()-method)method)
*   3 [Console Output](#console-output)
{{< /panel >}}
 

 

## Possible Usage Scenarios

Normally, we recommend users to call [Workbook.CalculateFormula()](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/calculateformula/index) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate entire workbook. They just want to calculate a single cell. Aspose.Cells provides [CalculationOptions.Recursive](https://apireference.aspose.com/net/cells/aspose.cells/calculationoptions/properties/recursive) property which you can set to **false **and it will decrease the calculation time of individual cell significantly. Because when the recursive property is set to **true**, then all the dependents of cells are recalculated on each call. But when the recursive property is **false**, then dependent cells are calculated only once and are not calculated again on subsequent calls.

## Decrease the Calculation Time of Cell.Calculate() method

The following sample code illustrates the usage of [CalculationOptions.Recursive](https://apireference.aspose.com/net/cells/aspose.cells/calculationoptions/properties/recursive) property. Please execute this code with the given [sample excel file](https://docs2.aspose.com/cells/net/attachments/5013541/5113710.xlsx) and check its console output. You will find that setting the recursive property to **false **has decreased the calculation time significantly. Please also read the comments for a better understanding of this property.

## Console Output

This is the console output of the above sample code when executed with the given [sample excel file](https://docs2.aspose.com/cells/net/attachments/5013541/5113710.xlsx) on our machine. Please note, your output may differ but the elapsed time after setting the recursive property to **false **will always be less than setting it to **true**.

{{< code lang="cs" >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sample.xlsx](https://docs2.aspose.com/cells/net/attachments/5013541/5113710.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

