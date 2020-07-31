---
title : "Enter Cell Data of GridWeb Worksheet in Percentage Format" 
description : "" 
weight : 12568 
toc : false
type: docs
url: /java/developerguide/technicalarticles/enter+cell+data+of+gridweb+worksheet+in+percentage+format/
---

# Aspose.Cells for Java : Enter Cell Data of GridWeb Worksheet in Percentage Format


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Enter Cell Data of GridWeb Worksheet in Percentage Format](#enter-cell-data-of-gridweb-worksheet-in-percentage-format)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

 


## Possible Usage Scenarios

GridWeb now supports users to enter cell data in percentage format like 3% and the data in the cell will automatically be formatted as 3.00%. However, you will have to set the cell style to `Percentage Format` which is either `GridTableItemStyle.NumberType` a 9 or 10. The number 9 will format 3% as 3% but the number 10 will format 3% as 3.00%.

If you have not set the cell style to `Percentage Format`, then input data 3% will display as 0.03.

## Enter Cell Data of GridWeb Worksheet in Percentage Format

The following sample code sets the cell A1 `GridTableItemStyle.NumberType` as 10, therefore the input data 3% automatically be formatted as 3.00% as shown in the screenshot.

![](https://docs2.aspose.com/cells/java/attachments/5275788/5473421.png)

## Sample Code

