---
title: Add Cells to Microsoft Excel Formula Watch Window with Python.NET
linktitle: Add Cells to Formula Watch Window
type: docs
weight: 60
url: /python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Learn how to monitor cells in Excel's Formula Watch Window using Aspose.Cells for Python via .NET. Includes code examples and API references.
keywords: python excel, formula watch window, cell monitoring, aspose.cells, python.net
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Microsoft Excel Watch Window is a useful tool to monitor cell values and formulas conveniently in a dedicated window. You can open the *Watch Window* in Microsoft Excel by navigating to *Formulas > Watch Window*. The *Add Watch* button allows adding cells for inspection. Similarly, you can use the [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) method to programmatically add cells to the Watch Window using Aspose.Cells API.

## **Add Cells to Microsoft Excel Formula Watch Window**

The following sample code sets formulas for cells C1 and E1, then adds both to the Watch Window. It saves the workbook as [output Excel file](67338481.xlsx). When opening the output file in Excel, both cells will appear in the Watch Window as shown:

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Sample Code**

```python
from aspose.cells import Workbook, SaveFormat

# Create empty workbook.
wb = Workbook()

# Access first worksheet.
ws = wb.worksheets[0]

# Put some integer values in cell A1 and A2.
ws.cells.get("A1").put_value(10)
ws.cells.get("A2").put_value(30)

# Access cell C1 and set its formula.
c1 = ws.cells.get("C1")
c1.formula = "=Sum(A1,A2)"

# Add cell C1 into cell watches by name.
ws.cell_watches.add(c1.name)

# Access cell E1 and set its formula.
e1 = ws.cells.get("E1")
e1.formula = "=A2*A1"

# Add cell E1 into cell watches by its row and column indices.
ws.cell_watches.add(e1.row, e1.column)

# Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
