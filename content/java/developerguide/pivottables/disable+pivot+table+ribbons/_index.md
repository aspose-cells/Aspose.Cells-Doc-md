---
title : "Disable Pivot Table Ribbons" 
description : "" 
weight : 12243 
toc : false
type: docs
url: /java/developerguide/pivottables/disable+pivot+table+ribbons/
---

# Aspose.Cells for Java : Disable Pivot Table Ribbons


Pivot table based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot table based report. Common pivot table features like adding additional filters, slicers, fields, or changing the order of certain things in the report are mostly not recommended for every user. On the other hand, these users shall also be able to refresh the report and use existing filters or slicers. Aspose.Cells has provided this ability to developers for restricting users from changing these reports while creating these reports. For this purpose, Excel provides a feature to disable the pivot table ribbon and the same is provided by Aspose.Cells i.e. developer can disable the ribbon which contains controls to modify these reports.

#### Disable Pivot Table Ribbon using PivotTable.setEnableWizard

Following code demonstrates this feature by accessing a pivot table from a sheet and then calling the [setEnableWizard](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#EnableWizard) to set this flag **false**. Sample pivot table file can be downloaded from this [link](https://docs2.aspose.com/cells/java/attachments/71303575/71630876.xlsx).


## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [pivot\_table\_test.xlsx](https://docs2.aspose.com/cells/java/attachments/71303575/71630876.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

