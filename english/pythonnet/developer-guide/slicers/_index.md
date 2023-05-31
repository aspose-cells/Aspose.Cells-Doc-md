---
title: Insert Slicer
linktitle: Slicers
type: docs
weight: 170
url: /python-net/create-slicer/
description: Manage slicers of Excel files with Aspose.Cells.
---

## **Possible Usage Scenarios**

A slicer is used to filter data quickly. It can be used to filter data both in a table or pivot table. Microsoft Excel allows you to create slicer by selecting a table or pivot table and then clicking the *Insert > Slicer*. Aspose.Cells for Python via .NET also allows you to create slicer using the [**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField) method.

## **Create Slicer to a Pivot Table**

Please see the following sample code. It loads the [sample Excel file](67338470.xlsx) that contains the pivot table. It then creates the slicer based on the first base pivot field. Finally, it saves the workbook in [output XLSX](67338471.xlsx) and [output XLSB](67338472.xlsb) format. The following screenshot shows the slicer created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **Create Slicer to Excel Table**

Please see the following sample code. It loads the [sample Excel file](sampleCreateSlicerToExcelTable.xlsx) that contains a table. It then creates the slicer based on the first column. Finally, it saves the workbook in [output XLSX](outputCreateSlicerToExcelTable.xlsx) format.

### **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **Advance topics**
- [Change Slicer Properties](/cells/python-net/change-slicer-properties/)
- [Draw Slicer while rendering Excel to PDF](/cells/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatting Slicer](/cells/python-net/formatting-slicer/)
- [Removing Slicer](/cells/python-net/removing-slicer/)
- [Rendering Slicer](/cells/python-net/rendering-slicer/)
- [Updating Slicer](/cells/python-net/updating-slicer/)
