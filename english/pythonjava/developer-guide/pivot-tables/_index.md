---
title: Pivot Tables
linktitle: Pivot Tables
description: Create and format pivot tables of Excel spreadsheet files.
url: /python-java/create-pivot-table/
type: docs
weight: 160
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Create Pivot Table**
It is possible to use Aspose.Cells to add pivot tables to spreadsheets programmatically.

### **Pivot Table Object Model**
Aspose.Cells provides a set of classes that are used to create and control pivot tables. The building blocks are:
- `PivotField` represents a field in a `PivotTable`.
- `PivotFieldCollection` represents a collection of all the `PivotField` objects in the `PivotTable`.
- `PivotTable` represents a PivotTable on a worksheet.
- `PivotTableCollection` represents a collection of all the `PivotTable` objects on a worksheet.

### **Creating a Simple Pivot Table Using Aspose.Cells**
1. Add data to a worksheet using the cell's `putValue` method. This data will be used as the pivot table's data source.
2. Add a pivot table to the worksheet by calling the `add` method on the `PivotTables` collection, which is encapsulated in the worksheet object.
3. Access the new `PivotTable` object from the `PivotTables` collection by passing the PivotTable's index.
4. Use any of the `PivotTable` objects (explained above) to manage the pivot table.

After executing the example code, a pivot table is added to the worksheet.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

dataDir = "./"
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

cell = cells.get("A1")
cell.putValue("Sport")
cell = cells.get("B1")
cell.putValue("Quarter")
cell = cells.get("C1")
cell.putValue("Sales")

cell = cells.get("A2")
cell.putValue("Golf")
cell = cells.get("A3")
cell.putValue("Golf")
cell = cells.get("A4")
cell.putValue("Tennis")
cell = cells.get("A5")
cell.putValue("Tennis")
cell = cells.get("A6")
cell.putValue("Tennis")
cell = cells.get("A7")
cell.putValue("Tennis")
cell = cells.get("A8")
cell.putValue("Golf")

cell = cells.get("B2")
cell.putValue("Qtr3")
cell = cells.get("B3")
cell.putValue("Qtr4")
cell = cells.get("B4")
cell.putValue("Qtr3")
cell = cells.get("B5")
cell.putValue("Qtr4")
cell = cells.get("B6")
cell.putValue("Qtr3")
cell = cells.get("B7")
cell.putValue("Qtr4")
cell = cells.get("B8")
cell.putValue("Qtr3")

cell = cells.get("C2")
cell.putValue(1500)
cell = cells.get("C3")
cell.putValue(2000)
cell = cells.get("C4")
cell.putValue(600)
cell = cells.get("C5")
cell.putValue(1500)
cell = cells.get("C6")
cell.putValue(4070)
cell = cells.get("C7")
cell.putValue(5000)
cell = cells.get("C8")
cell.putValue(6430)

pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C8", "E3", "PivotTable2")
pivotTable = pivotTables.get(index)
pivotTable.setRowGrand(False)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1)
pivotTable.addFieldToArea(PivotFieldType.DATA, 2)
workbook.save(dataDir + "pivotTable_test_out.xls")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
When assigning a range of cells as the data source, the range must go from top left to bottom right. For example, "A1:C3" is valid but "C3:A1" is not.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}