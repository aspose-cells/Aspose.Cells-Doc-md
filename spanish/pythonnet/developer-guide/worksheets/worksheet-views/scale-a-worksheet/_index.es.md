---
title: Cómo escalar una hoja de trabajo con Python.NET
linktitle: Cómo escalar una hoja de trabajo
type: docs
weight: 130
url: /es/python-net/how-to-scale-a-worksheet/
description: Este artículo explica cómo escalar una hoja de trabajo usando Aspose.Cells para Python.NET.
keywords: Escalar una hoja de trabajo con Python, Escalar hoja de trabajo con Python.NET, Ajustar a página en Python, Porcentaje de escalado de hoja de trabajo en Python, Aspose.Cells escalado de hoja de trabajo en Python.
---

## **Escenarios de uso posibles**
Escalar una hoja de trabajo puede ser útil por varias razones, dependiendo del contexto en el que estés trabajando. Aquí algunas razones comunes para escalar una hoja de trabajo:
1. **Ajustar a la página**: Para garantizar que todo el contenido quepa en una sola página o en un número específico de páginas al imprimir.
1. **Presentación**: Para crear hojas de trabajo organizadas y profesionales para compartir.
1. **Legibilidad**: Para ajustar tamaño de texto y elementos para mejor accesibilidad visual.
1. **Gestión del espacio**: Para optimizar el diseño de la hoja y minimizar el espacio en blanco innecesario.
1. **Visualización de datos**: Para dimensionar adecuadamente gráficos y cuadros dentro del espacio disponible.
1. **Consistencia**: Para mantener una apariencia uniforme en varias hojas de trabajo o documentos.

## **Cómo escalar una hoja de trabajo en Excel**
Escalar una hoja de trabajo en Excel ayuda a ajustar el contenido a páginas especificadas al imprimir. Sigue estos pasos:

1. Abre tu hoja de trabajo en Excel
1. Navega a **Diseño de página** > grupo **Escalar para ajustarse**
1. Ajusta **Ancho** y **Alto** para los requisitos de número de páginas
1. Establece un porcentaje de escalado personalizado si es necesario
<br>
<img src="1.png" width=60% />

## **Cómo escalar una hoja de trabajo usando Python.NET**
Aspose.Cells para Python.NET proporciona capacidades completas de escalado de hojas de trabajo. Usa estos enfoques para escalar hojas de trabajo programáticamente:

### **Ejemplo de ajuste a página**
Ajusta la configuración de impresión para que el contenido quepa en páginas especificadas:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the worksheet to fit to 1 page wide and 1 page tall
page_setup.fit_to_pages_wide = 1
page_setup.fit_to_pages_tall = 1

# Save the modified workbook
workbook.save("output_fit_to_page.xlsx")
```
<br>
<img src="3.png" width=60% />

### **Ejemplo de escala en porcentaje**
Aplica un porcentaje de escalado personalizado a los contenidos de la hoja de trabajo:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the scaling to a specific percentage (e.g., 75%)
page_setup.zoom = 75

# Save the modified workbook
workbook.save("output_scaled_percentage.xlsx")
```
<br>
<img src="2.png" width=60% />

**Referencias clave de API:**
- [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) clase
- [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) clase
- [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) configuración
{{< app/cells/assistant language="python-net" >}}
