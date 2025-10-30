---
title: Uso de la función FormulaText en Aspose.Cells con Python.NET
linktitle: Uso de la función FormulaText
type: docs
weight: 60
url: /es/python-net/using-formulatext-function-in-aspose-cells/
description: Aprenda cómo trabajar con la función FORMULATEXT de Excel usando Aspose.Cells para Python via .NET. Obtenga y configure las fórmulas de las celdas programáticamente mientras mantiene la integridad de la hoja de cálculo.
keywords: Aspose.Cells, Python, Excel, FORMULATEXT, manejo de fórmulas, automatización de hojas de cálculo
---

{{% alert color="primary" %}} 

FORMULATEXT es una función de Excel 2013 y versiones posteriores. No es compatible con versiones anteriores como Excel 2010 o 2007, etc. Como su nombre indica, muestra el texto de la fórmula contenida en una celda especificada. Este artículo demuestra cómo usar esta función con Aspose.Cells para Python via .NET.

{{% /alert %}} 

El siguiente ejemplo de código demuestra el uso de FORMULATEXT con Aspose.Cells. El código primero escribe una fórmula en la celda A1 y luego muestra el texto de la fórmula usando FORMULATEXT en la celda A2.

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put some formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2, It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **Salida de la consola**
Aquí está la salida de la consola del código de ejemplo anterior:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
