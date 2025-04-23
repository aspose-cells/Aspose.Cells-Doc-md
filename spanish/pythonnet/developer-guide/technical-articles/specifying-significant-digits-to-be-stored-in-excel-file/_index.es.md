---
title: Especificar cifras significativas que se almacenarán en el archivo de Excel con Python.NET
linktitle: Especificando Dígitos Significativos
type: docs
weight: 30
url: /es/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: Aprende cómo controlar las cifras significativas almacenadas en archivos de Excel usando la API de Aspose.Cells para Python via .NET.
---

## **Escenarios de uso posibles**

Por defecto, Aspose.Cells almacena 17 cifras significativas de valores doble dentro del archivo de Excel, a diferencia de MS-Excel que solo almacena 15 cifras significativas. Puedes cambiar este comportamiento de 17 a 15 cifras significativas usando el atributo [**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/).

## **Especificación de Dígitos Significativos a ser almacenados en un archivo de Excel**

El siguiente código de ejemplo fuerza a Aspose.Cells a usar 15 cifras significativas al almacenar valores doble. Revisa el [archivo excel de salida](22774105.xlsx) (cambia la extensión a .zip para inspeccionar los valores almacenados). La captura de pantalla a continuación muestra cómo afecta esta configuración a los valores almacenados:

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Código de muestra**

```python
from aspose.cells import Workbook, CellsHelper
import aspose.cells
import os
import pytest

# Set significant digits to 15
CellsHelper.set_significant_digits(15)

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set value with extended precision
cell = worksheet.cells.get("A1")
cell.put_value(1234567890123456.001234567890123456)

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CellsHelper

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Set significant digits to 15 like MS-Excel
CellsHelper.set_significant_digits(15)

# Create workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Access cell A1
c = worksheet.cells.get("A1")

# Put double value with 15 significant digits
c.put_value(1234567890.123451711)

# Save the workbook
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "out_SignificantDigits.xlsx"))
```
