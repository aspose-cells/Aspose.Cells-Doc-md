---
title : "Specify Maximum Rows of Shared Formula" 
description : "" 
weight : 12191 
toc : false
type: docs
url: /java/developerguide/formulas/specify+maximum+rows+of+shared+formula/
---

# Aspose.Cells for Java : Specify Maximum Rows of Shared Formula


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Specify Maximum Rows of Shared Formula](#specify-maximum-rows-of-shared-formula)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

The default maximum rows of the shared formula are 64. It could be any number e.g. it could be 1000. The performance of shared formula changes with a different number of rows. Therefore, Aspose.Cells provides the [Workbook.Settings.MaxRowsOfSharedFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) property that can be used to specify the maximum rows of the shared formula. The shared formula will be split to several shared formulae if the total rows of the shared formula are greater than it as shown in the following screenshot.

![](https://docs2.aspose.com/cells/java/attachments/61542589/61767870.png)

## Specify Maximum Rows of Shared Formula

The following sample code explains the usage of the [Workbook.Settings.MaxRowsOfSharedFormula](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) property. It sets the maximum rows of the shared formula to 5 and adds the shared formula in cell D1 for 100 rows and saves to [output Excel file](https://docs2.aspose.com/cells/java/attachments/61542589/61767869.xlsx). If you extract the contents of output Excel file and check the *sheet1.xml*, you will see the shared formula splits after every 5 rows as highlighted in the above screenshot.

## Sample Code

