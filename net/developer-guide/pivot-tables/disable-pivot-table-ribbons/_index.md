---
title: Disable Pivot Table Ribbons
type: docs
weight: 90
url: /net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}} 

Pivot table based reports are useful but prone to error if target users do not have detailed knowledge of Excel to configure these reports. In these circumstances, organizations will want to restrict users from being able to change a pivot table based report. Common pivot table features like adding additional filters, slicers, fields, or changing the order of certain things in the report are mostly not recommended for every user. On the other hand, these users shall also be able to refresh the report and use existing filters or slicers. Aspose.Cells has provided this ability to developers for restricting users from changing these reports while creating these reports. For this purpose, Excel provides a feature to disable the pivot table ribbon and the same is provided by Aspose.Cells i.e. developer can disable the ribbon which contains controls to modify these reports.

{{% /alert %}} 
#### **Disable Pivot Table Ribbon using PivotTable.EnableWizard**
Following code demonstrates this feature by accessing a pivot table from a sheet and then setting [EnableWizard](https://apireference.aspose.com/net/cells/aspose.cells.pivot/pivottable/properties/enablewizard) to **false**. Sample pivot table file can be downloaded from this [link](https://docs-qa.aspose.com/download/attachments/71303575/pivot_table_test.xlsx?version=1&modificationDate=1536042135788&api=v2).



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "PivotTables-DisablePivotTableRibbon.cs" >}}
