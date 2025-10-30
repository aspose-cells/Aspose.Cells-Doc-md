---
title: Aplicar formato condicional avanzado con Python.NET
linktitle: Aplicar Formato Condicional Avanzado
type: docs
weight: 70
url: /es/python-net/apply-advanced-conditional-formatting/
description: Aprende cómo implementar funciones avanzadas de formato condicional de Excel como barras de datos, escalas de color y conjuntos de iconos usando Aspose.Cells para Python via .NET.
keywords: Formato de Excel en Python, Formato condicional en Python, Barras de datos en Python, Escalas de color en Python, Conjuntos de iconos en Python, Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 y versiones posteriores (2010/2013/2016) ofrecen funciones avanzadas de formato condicional, incluyendo sombreado de celdas, bordes, íconos en color, flechas, banderas y formato de fuente.

{{% /alert %}} 

## **Implementar formato condicional avanzado en archivos de Excel**
Aspose.Cells para Python via .NET soporta todas las funciones de formato condicional avanzado incluyendo:

- Agregar barras de datos sombreadas para mejorar gráficamente los números subyacentes mediante la inclusión de un gráfico de barras simple en las celdas.
- Sombrear automáticamente las celdas con escalas de colores basadas en su relación con los valores en otras celdas del rango. La configuración por defecto sombrea el valor más bajo en rojo moviéndose hasta el valor más alto en verde.
- Utilizar conjuntos de iconos de forma similar a las escalas de colores, pero en lugar de sombrear las celdas, agrega pequeños iconos, como flechas y semáforos en las celdas.

Aspose.Cells admite completamente el formato condicional proporcionado por Microsoft Excel 2007 y versiones posteriores en formato XLSX en las celdas en tiempo de ejecución. Este ejemplo demuestra un ejercicio para tipos avanzados de formato condicional que incluyen conjuntos de iconos, barras de datos, escalas de colores, periodos de tiempo, top/bottom y otras reglas con diferentes conjuntos de atributos.

- [**Adding Color Scale Conditional Formattings**](/cells/es/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/es/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/es/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/es/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/es/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/es/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/es/python-net/how-to-add-top10-conditional-formatting/)



### **Calcular la selección de color en Excel para el formato de escala de color**
Este código muestra cómo determinar el color seleccionado por Excel para reglas de formato condicional con escala de color:

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}
