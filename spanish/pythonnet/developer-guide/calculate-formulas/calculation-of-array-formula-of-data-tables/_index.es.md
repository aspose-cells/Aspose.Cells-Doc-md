---
title: Cálculo de fórmulas de matrices en tablas de datos con Python.NET
linktitle: Cálculo de la fórmula de arreglo de tablas de datos
type: docs
weight: 70
url: /es/python-net/calculation-of-array-formula-of-data-tables/
description: Aprenda a calcular fórmulas de matriz para tablas de datos de Excel usando Aspose.Cells para la API Python via .NET. Modifique y guarde hojas de cálculo programáticamente.
keywords: Tablas de datos en Excel con Python, fórmulas de matriz en Python, Aspose.Cells Python, calificación de tablas de datos en Python, automatización de Excel en Python
---

{{% alert color="primary" %}}

Puede crear una tabla de datos en Microsoft Excel usando Datos > Análisis de hipótesis > Tabla de datos.... Aspose.Cells para Python via .NET le permite calcular la fórmula de matriz de una tabla de datos. Use [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) como en caso normal para calcular cualquier tipo de fórmula.

{{% /alert %}}

En el siguiente ejemplo, usamos el [archivo de Excel fuente](5115535.xlsx). Si cambia el valor de la celda B1 a 100, los valores de la Tabla de Datos (destacados en amarillo) se actualizarán a 120 como se muestra en las capturas de pantalla abajo. El código en Python genera este [PDF de salida](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

A continuación, se presenta la implementación en Python que demuestra cómo generar el [PDF de salida](5115538.pdf) a partir del [archivo de Excel fuente](5115535.xlsx):

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook from source excel file
workbook = Workbook(os.path.join(data_dir, "DataTable.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.cells.get("B1").put_value(100)

# Calculate formula, now it also calculates Data Table array formula
workbook.calculate_formula()

# Save the workbook in pdf format
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```

**Explicación del código Python:**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
