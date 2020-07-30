---
title : "Decrease the Calculation Time of Cell.Calculate method" 
description : "" 
weight : 12553 
toc : false
type: docs
url: /java/developerguide/technicalarticles/decrease+the+calculation+time+of+cell.calculate+method/
---

# Aspose.Cells for Java : Decrease the Calculation Time of Cell.Calculate method


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Decrease the Calculation Time of Cell.Calculate() method](#decrease-the-calculation-time-of-cell.calculate()-method)method)
*   2 [Console Output](#console-output)
{{< /panel >}}
 

 

  
Possible Usage Scenarios

Normally, we recommend users to call [Workbook.CalculateFormula()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#calculateFormula()) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate entire workbook. They just want to calculate a single cell. Aspose.Cells provides [CalculationOptions.Recursive](https://apireference.aspose.com/java/cells/com.aspose.cells/calculationoptions#Recursive) property which you can set **false **and it will decrease the calculation time of individual cell significantly. Because when the recursive property is set to **true**, then all the dependents of cells are recalculated on each call. But when the recursive property is set to **false**, then dependent cells are calculated only once and are not calculated again on subsequent calls.

## Decrease the Calculation Time of Cell.Calculate() method

The following sample code illustrates the usage of [CalculationOptions.Recursive](https://apireference.aspose.com/java/cells/com.aspose.cells/calculationoptions#Recursive) property. Please execute this code with the given [sample excel file](https://docs2.aspose.com/cells/java/attachments/5275717/5472288.xlsx) and check its console output. You will find that setting the recursive property to **false **has decreased the calculation time significantly. Please also read the comments for a better understanding of this property.

## Console Output

This is the console output of the above sample code when executed with the given [sample excel file](https://docs2.aspose.com/cells/java/attachments/5275717/5472288.xlsx) on our machine. Please note, your output may differ but the elapsed time after setting the recursive property to **false **will always be less than setting it to **true**.

{{< code lang="cs" >}}
Recursive true: 51 seconds
Recursive false: 16 seconds
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sample.xlsx](https://docs2.aspose.com/cells/java/attachments/5275717/5472288.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

