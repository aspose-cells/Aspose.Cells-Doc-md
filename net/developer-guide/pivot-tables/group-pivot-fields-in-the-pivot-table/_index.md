---
title: Group Pivot Fields in the Pivot Table
type: docs
weight: 80
url: /net/group-pivot-fields-in-the-pivot-table/
---

## **Possible Usage Scenarios**
Microsoft Excel allows you to group pivot fields of the pivot table. When there is a large amount of data related to a pivot field, it is often useful to group them into sections. Aspose.Cells also provides this feature using the [PivotTable.SetManualGroupField()](https://apireference.aspose.com/net/cells/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index) method. 
## **Group Pivot Fields in the Pivot Table**
The following sample code loads the [sample Excel file](64716818.xlsx) and performs grouping on the first pivot field using the [PivotTable.SetManualGroupField()](https://apireference.aspose.com/net/cells/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index) method. It then refreshes and calculates data of the pivot table and saves the workbook as [output Excel file](64716817.xlsx). The screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the first pivot field is now grouped by months and quarters.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
