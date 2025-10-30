---
title: Agregar celdas a la ventana de vigilancia de fórmulas en Microsoft Excel con Python.NET
linktitle: Agregar celdas a la ventana de vigilancia de fórmulas
type: docs
weight: 60
url: /es/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Aprende cómo monitorear celdas en la ventana de vigilancia de fórmulas de Excel usando Aspose.Cells para Python via .NET. Incluye ejemplos de código y referencias API.
keywords: Python Excel, ventana de vigilancia de fórmulas, monitoreo de celdas, aspose.cells, python.net
---

## **Escenarios de uso posibles**

La ventana de vigilancia de Excel de Microsoft es una herramienta útil para monitorear valores de celdas y fórmulas de manera conveniente en una ventana dedicada. Puedes abrir la *Ventana de Vigilancia* en Excel navegando a *Fórmulas > Ventana de Vigilancia*. El botón *Agregar vigilancia* permite agregar celdas para inspección. De manera similar, puedes usar el método [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) para agregar programáticamente celdas a la ventana de vigilancia usando la API de Aspose.Cells.

## **Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel**

El siguiente código de ejemplo establece fórmulas para las celdas C1 y E1, y luego ambas se agregan a la ventana de vigilancia. Guarda el libro de trabajo como [archivo de Excel de salida](67338481.xlsx). Al abrir el archivo de salida en Excel, ambas celdas aparecerán en la ventana de vigilancia como se muestra:

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Código de muestra**

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
