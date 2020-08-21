---
title: Create Slicer to a Pivot Table
type: docs
weight: 10
url: /java/create-slicer-to-a-pivot-table/
---

## **Possible Usage Scenarios**
The slicer is used to filter data quickly. It can be used to filter data both in a table or pivot table. Microsoft Excel allows you to create a slicer by selecting a table or pivot table and then clicking the *Insert > Slicer*. Aspose.Cells also allows you to create slicer using the [Worksheet.getSlicers().add()](https://apireference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) method.
## **Create Slicer to a Pivot Table**
Please see the following sample code. It loads the [sample Excel file](67338498.xlsx) that contains the pivot table. It then creates the slicer based on the first base pivot field. Finally, it saves the workbook in [output XLSX](67338497.xlsx) and [output XLSB](67338496.xlsb) format. The following screenshot shows the slicer created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Slicers-CreateSlicerToPivotTable.java" >}}
