---
title: Create Slicer to a Pivot Table
type: docs
weight: 10
url: /net/create-slicer-to-a-pivot-table/
---

## **Possible Usage Scenarios**
A slicer is used to filter data quickly. It can be used to filter data both in a table or pivot table. Microsoft Excel allows you to create slicer by selecting a table or pivot table and then clicking the *Insert > Slicer*. Aspose.Cells also allows you to create slicer using the [Worksheet.Slicers.Add()](https://apireference.aspose.com/net/cells/aspose.cells.slicers/slicercollection/methods/add/index) method.
## **Create Slicer to a Pivot Table**
Please see the following sample code. It loads the [sample Excel file](attachments/66948306/67338470.xlsx) that contains the pivot table. It then creates the slicer based on the first base pivot field. Finally, it saves the workbook in [output XLSX](attachments/66948306/67338471.xlsx) and [output XLSB](attachments/66948306/67338472.xlsb) format. The following screenshot shows the slicer created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Slicers-CreateSlicerToPivotTable.cs" >}}
