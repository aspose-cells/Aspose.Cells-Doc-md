+++
title = "Specify Maximum Rows of Shared Formula" 
description = "" 
weight = 12229 
+++

Aspose.Cells for .NET : Specify Maximum Rows of Shared Formula  

# Aspose.Cells for .NET : Specify Maximum Rows of Shared Formula


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#SpecifyMaximumRowsofSharedFormula-PossibleUsageScenarios)
*   2 [Specify Maximum Rows of Shared Formula](#SpecifyMaximumRowsofSharedFormula-SpecifyMaximumRowsofSharedFormula)
*   3 [Sample Code](#SpecifyMaximumRowsofSharedFormula-SampleCode)
{{< /panel >}}
 

## Possible Usage Scenarios

The default maximum rows of the shared formula are 64. It could be any number e.g. it could be 1000. The performance of shared formula changes with a different number of rows. Therefore, Aspose.Cells provides the [Workbook.Settings.MaxRowsOfSharedFormula](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) property that can be used to specify the maximum rows of the shared formula. The shared formula will be split to several shared formulae if the total rows of the shared formula are greater than it as shown in the following screenshot.

![](https://docs2.aspose.com/cells/net/attachments/61542290/61767855.png)

## Specify Maximum Rows of Shared Formula

The following sample code explains the usage of the [Workbook.Settings.MaxRowsOfSharedFormula](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) property. It sets the maximum rows of the shared formula to 5 and adds the shared formula in cell D1 for 100 rows and saves to [output Excel file](https://docs2.aspose.com/cells/net/attachments/61542290/61767856.xlsx). If you extract the contents of output Excel file and check the *sheet1.xml*, you will see the shared formula splits after every 5 rows as highlighted in the above screenshot.

## Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Specify Maximum Row Number of Shared Formula.png](https://docs2.aspose.com/cells/net/attachments/61542290/61767855.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [outputSpecifyMaximumRowsOfSharedFormula.xlsx](https://docs2.aspose.com/cells/net/attachments/61542290/61767856.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

