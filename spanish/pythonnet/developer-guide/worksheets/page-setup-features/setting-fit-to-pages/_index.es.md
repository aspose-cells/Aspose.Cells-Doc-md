---
title: Cómo imprimir Excel ajustado en páginas anchas y altas con Python.NET
linktitle: Cómo imprimir Excel como páginas ajustadas en ancho y alto
type: docs
weight: 200
url: /es/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Aprende a configurar las propiedades fit_to_pages_wide y fit_to_pages_tall para la impresión de Excel usando Aspose.Cells para Python API via .NET.
keywords: Impresión de Excel en Python, Configuración de ajuste a la página en Python, FitToPagesWide en Python, FitToPagesTall en Python, Imprimir hoja de cálculo como una sola página en Python, Imprimir todas las columnas en una sola página en Python
---

## **Introducción**

Las configuraciones fit_to_pages_wide y fit_to_pages_tall controlan la escala de la hoja de cálculo durante la impresión. Estas configuraciones aseguran que la salida impresa se ajuste dentro de las dimensiones de página especificadas:

1. **fit_to_pages_wide**: Especifica el recuento de páginas horizontales para la impresión
1. **fit_to_pages_tall**: Especifica el recuento de páginas verticales para la impresión

## **Por qué usar FitToPagesWide y FitToPagesTall**
Las ventajas principales incluyen:
1. Control preciso del diseño de impresión
1. Formateo coherente en varias hojas
1. Presentación profesional del documento

## **Cómo imprimir un archivo como páginas ajustadas en ancho y alto en Excel**
Para configurar en Microsoft Excel:
1. Abre el libro de trabajo y selecciona la hoja de cálculo
1. Navega a **Diseño de página** → diálogo de **Configuración de página**
1. En la pestaña **Página** bajo **Escalado**:
   - Seleccione "Ajustar a"
   - Especificar páginas de ancho (horizontal) y alto (vertical)

<br>
<img src="2.png" width=60% />

## **Cómo Imprimir Excel como Páginas Ajustadas en Ancho y Alto usando Aspose.Cells**
Para configurar programáticamente:
1. Cargar [archivo de ejemplo](input.xlsx)
1. Acceder al objeto de la hoja de trabajo [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)
1. Establecer las propiedades [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) y [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/)

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

Resultado de la salida:
<br>
<img src="1.png" width=60% />

## **Cómo Imprimir la Hoja de Trabajo como una sola página**
Para forzar la salida en una sola página:
1. Use [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Establecer la propiedad [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

Resultado de la salida:
<br>
<img src="3.png" width=60% />

## **Cómo Imprimir Todas las Columnas en Una Página**
Para consolidar columnas horizontalmente:
1. Configurar [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Habilitar la propiedad [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

Resultado de la salida:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
