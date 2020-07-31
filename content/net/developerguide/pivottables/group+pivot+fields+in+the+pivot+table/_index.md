---
title : "Group Pivot Fields in the Pivot Table" 
description : "" 
weight : 12241 
toc : false
type: docs
url: /net/developerguide/pivottables/group+pivot+fields+in+the+pivot+table/
---

# Aspose.Cells for .NET : Group Pivot Fields in the Pivot Table


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Group Pivot Fields in the Pivot Table](#group-pivot-fields-in-the-pivot-table)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Microsoft Excel allows you to group pivot fields of the pivot table. When there is a large amount of data related to a pivot field, it is often useful to group them into sections. Aspose.Cells also provides this feature using the [PivotTable.SetManualGroupField()](https://apireference.aspose.com/net/cells/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index) method. 

## Group Pivot Fields in the Pivot Table

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/64454856/64716818.xlsx) and performs grouping on the first pivot field using the [PivotTable.SetManualGroupField()](https://apireference.aspose.com/net/cells/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index) method. It then refreshes and calculates data of the pivot table and saves the workbook as [output Excel file](https://docs2.aspose.com/cells/net/attachments/64454856/64716817.xlsx). The screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the first pivot field is now grouped by months and quarters.

![](https://docs2.aspose.com/cells/net/attachments/64454856/64716816.png)

## Sample Code

