+++
title = "Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range" 
description = "" 
weight = 20465 
+++

Aspose.Cells for .NET : Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range  

# Aspose.Cells for .NET : Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#ChangeDataSourceoftheCharttoDestinationWorksheetwhileCopyingRowsorRange-PossibleUsageScenarios)
*   2 [Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range](#ChangeDataSourceoftheCharttoDestinationWorksheetwhileCopyingRowsorRange-ChangeDataSourceoftheCharttoDestinationWorksheetwhileCopyingRowsorRange)
{{< /panel >}}
 

 

## Possible Usage Scenarios

When you copy rows or range which contains charts to a new worksheet, then the data source of the chart does not change. For example, if the data source of chart is `=Sheet1!$A$1:$B$4`, then after copying rows or range to new worksheet, the data source will remain the same i.e `=Sheet1!$A$1:$B$4`. It still refers to old worksheet i.e. `Sheet1`. This is also the behavior in Microsoft Excel. But if you want that it to refer to the new destination worksheet, then please use the [CopyOptions.ReferToDestinationSheet](https://apireference.aspose.com/net/cells/aspose.cells/copyoptions/properties/refertodestinationsheet) property and set it to **true **while calling the [Cells.CopyRows()](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/copyrows/index) method. Now if your destination worksheet is `DestSheet`, then the data source of your chart will change from `=Sheet1!$A$1:$B$4` to `=DestSheet!$A$1:$B$4`.

## Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range

The following sample code explains the usage of [CopyOptions.ReferToDestinationSheet](https://apireference.aspose.com/net/cells/aspose.cells/copyoptions/properties/refertodestinationsheet) property while copying rows or range containing charts to a new worksheet. The code uses the [sample excel file](https://docs2.aspose.com/cells/net/attachments/5013542/5113699.xlsx) and generates the [output excel file](https://docs2.aspose.com/cells/net/attachments/5013542/5113697.xlsx).

![](https://docs2.aspose.com/cells/net/attachments/5013542/5113695.png)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [CopyOptions.ReferToDestinationSheet-effect-on-chart-data-source.png](https://docs2.aspose.com/cells/net/attachments/5013542/5113695.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [output.xlsx](https://docs2.aspose.com/cells/net/attachments/5013542/5113697.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sample.xlsx](https://docs2.aspose.com/cells/net/attachments/5013542/5113699.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

