---
title: Create Slicer to a Pivot Table
type: docs
weight: 10
url: /pythonjava/create-slicer-to-a-pivot-table/
---

## **Possible Usage Scenarios**
Slicers are used to filter data quickly. They can be used to filter data both in a table or pivot table. Microsoft Excel allows you to create a slicer by selecting a table or pivot table and then clicking the *Insert > Slicer*. Aspose.Cells for Python via Java provides the Worksheet.getSlicers().add() method to create slicer.
## **Create Slicer to a Pivot Table**
The following code snippet loads the [sample Excel file](106364966.xlsx) that contains the pivot table. It then creates the slicer based on the first base pivot field. Finally, it saves the workbook in [output XLSX](106364967.xlsx) format. The following screenshot shows the slicer created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "f3cac13617c487b51b47cc9ae1d7c008" "Slicers-CreateSlicerToPivotTable.py" >}}
