---
title : "Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range" 
description : "" 
weight : 12552 
toc : false
type: docs
url: /java/developerguide/technicalarticles/change+data+source+of+the+chart+to+destination+worksheet+while+copying+rows+or+range/
---

# Aspose.Cells for Java : Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range](#change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range)
{{< /panel >}}
 

 


## Possible Usage Scenarios

When you copy rows or range which contains charts to new worksheet, then data source of chart does not change. For example, if the data source of chart is `=Sheet1!$A$1:$B$4`, then after copying rows or range to new worksheet, the data source will remain the same i.e `=Sheet1!$A$1:$B$4`. It still refers to old worksheet i.e. `Sheet1`. This is also the Microsoft Excel behavior. But if you want that it refers to new destination worksheet, then please use the `CopyOptions.ReferToDestinationSheet` property and set it `true` while calling the `Cells.CopyRows()` method. Now if your destination worksheet is `DestSheet`, then the data source of your chart will change from `=Sheet1!$A$1:$B$4` to `=DestSheet!$A$1:$B$4`.

## Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range

The following sample code explains the usage of `CopyOptions.ReferToDestinationSheet` property while copying rows or range containing chart to new worksheet. The code uses the [sample excel file](https://docs2.aspose.com/cells/java/attachments/5275731/5472284.xlsx) and generates the [output excel file](https://docs2.aspose.com/cells/java/attachments/5275731/5472283.xlsx). The screenshot shows that the data source of chart in [output excel file](https://docs2.aspose.com/cells/java/attachments/5275731/5472283.xlsx) now refers to `DestSheet` instead of `Sheet1`.

![](https://docs2.aspose.com/cells/java/attachments/5275731/5472282.png)


## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [CopyOptions.ReferToDestinationSheet-effect-on-chart-data-source.png](https://docs2.aspose.com/cells/java/attachments/5275731/5472282.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [output.xlsx](https://docs2.aspose.com/cells/java/attachments/5275731/5472283.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sample.xlsx](https://docs2.aspose.com/cells/java/attachments/5275731/5472284.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

