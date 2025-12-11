---
title: Create a Slicer for a Pivot Table
type: docs
weight: 10
url: /java/create-slicer-to-a-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
The slicer is used to filter data quickly. It can be used to filter data in either a table or a pivot table. Microsoft Excel allows you to create a slicer by selecting a table or pivot table and then clicking the *Insert > Slicer*. Aspose.Cells also allows you to create a slicer using the [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.PivotTable-int-int-com.aspose.cells.PivotField-) method.

## **Create a Slicer for a Pivot Table**
See the following sample code. It loads the [sample Excel file](67338498.xlsx) that contains the pivot table. It then creates the slicer based on the first base pivot field. Finally, it saves the workbook in the [output XLSX](67338497.xlsx) and [output XLSB](67338496.xlsb) formats. The following screenshot shows the slicer created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
