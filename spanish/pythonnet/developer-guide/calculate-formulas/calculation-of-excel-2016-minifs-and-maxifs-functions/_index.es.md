---
title: Cálculo de las funciones MINIFS y MAXIFS de Excel 2016 con Python.NET
linktitle: Cálculo de las funciones MINIFS y MAXIFS de Excel 2016
type: docs
weight: 300
url: /es/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: Aprende cómo calcular las funciones MINIFS y MAXIFS de Excel 2016 usando Aspose.Cells para Python via .NET con ejemplos de código.
keywords: python excel, minifs maxifs, cálculo de fórmulas, aspose.cells
---

## **Escenarios de uso posibles**
Microsoft Excel 2016 soporta las funciones MINIFS y MAXIFS. Estas funciones no son compatibles en Excel 2013 o versiones anteriores. Aspose.Cells también soporta el cálculo de estas funciones. La siguiente captura de pantalla muestra el uso de estas funciones. Por favor, lee los comentarios en rojo dentro de la captura para entender cómo funcionan estas funciones.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Cálculo de las funciones MINIFS y MAXIFS de Excel 2016**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](5115149.xlsx) y llama al método [workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) para realizar el cálculo de fórmulas mediante Aspose.Cells, y luego guarda los resultados en el [PDF de salida](5115154.pdf).


```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Load your source workbook containing MINIFS and MAXIFS functions
workbook = Workbook(os.path.join(source_dir, "sampleMINIFSAndMAXIFS.xlsx"))

# Perform Aspose.Cells formula calculation
workbook.calculate_formula()

# Save the calculations result in pdf format
options = PdfSaveOptions()
options.one_page_per_sheet = True

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "outputMINIFSAndMAXIFS.pdf"), options)
```
{{< app/cells/assistant language="python-net" >}}
