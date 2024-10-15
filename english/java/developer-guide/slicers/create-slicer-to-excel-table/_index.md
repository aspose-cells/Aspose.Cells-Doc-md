---
title: Create Slicer to Excel Table
type: docs
weight: 15
url: /java/create-slicer-to-excel-table/
---

## **Possible Usage Scenarios**

A slicer is used to filter data quickly. It can be used to filter data both in a table or pivot table. Microsoft Excel allows you to create slicer by selecting a table or pivot table and then clicking the *Insert > Slicer*. Aspose.Cells also allows you to create slicer using the [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add(com.aspose.cells.ListObject,%20com.aspose.cells.ListColumn,%20int,%20int)) method.

## **Create Slicer to Excel Table**

Please see the following sample code. It loads the [sample Excel file](sampleCreateSlicerToExcelTable.xlsx) that contains a table. It then creates the slicer based on the first column. Finally, it saves the workbook in [output XLSX](outputCreateSlicerToExcelTable.xlsx) format.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
{{< app/cells/assistant language="java" >}}