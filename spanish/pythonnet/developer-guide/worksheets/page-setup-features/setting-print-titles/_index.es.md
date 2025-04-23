---
title: Establecer títulos de impresión con Python.NET
linktitle: Establecer títulos de impresión
type: docs
weight: 200
url: /es/python-net/how-to-set-print-titles/
description: Aprende cómo configurar encabezados de fila/columna repetidos en las páginas impresas usando Aspose.Cells para Python via .NET.
keywords: Encabezados de impresión repetidos en Python, configurar títulos de impresión en Python, limpiar títulos de impresión en Python, configuración de página en Excel Python, impresión de hojas de cálculo con Python.NET
---

## **Escenarios de uso posibles**

Configurar títulos de impresión en Excel asegura que filas o columnas específicas se repitan en cada página impresa, lo cual es especialmente útil para hojas de cálculo grandes que abarcan varias páginas. Aquí tienes algunas razones para establecer títulos de impresión:

1. Mejor legibilidad: Los títulos de impresión ayudan a los lectores a entender los datos manteniendo los encabezados visibles en todas las páginas, facilitando la interpretación de la información sin tener que volver a la primera página.

1. Presentación profesional: Mostrar consistentemente encabezados o etiquetas en cada página crea una apariencia más pulida y profesional en los documentos impresos.

1. Mejor navegación: Para documentos con datos extensos, repetir los encabezados en cada página permite una navegación y referencia más rápida, reduciendo la necesidad de volver a pasar entre páginas.

1. Reducción de errores: Cuando los encabezados están presentes en cada página, se minimizan las oportunidades de malentendidos o errores de entrada de datos, ya que los usuarios pueden ver fácilmente el contexto de los datos.

1. Consistencia: Asegurar que información importante, como encabezados de columnas o etiquetas de filas, siempre sea visible mantiene la consistencia y claridad en todo el documento.

## **Cómo establecer títulos de impresión en Excel**

Para establecer títulos de impresión en Excel, sigue estos pasos:

1. Abrir la pestaña de Diseño de página: Haz clic en la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.
1. Acceder a Títulos de impresión: En el grupo "Configurar página", haz clic en "Títulos de impresión".
1. Configurar filas para repetir: En el cuadro de diálogo "Configurar página", ve a la pestaña "Hoja". En la sección "Títulos de impresión", especifica las filas a repetir en la parte superior haciendo clic en el cuadro junto a "Filas para repetir en la parte superior" y seleccionando la(s) fila(s) que deseas repetir.
1. Configurar columnas para repetir (si es necesario): De manera similar, puedes especificar las columnas para repetir en la izquierda haciendo clic en el cuadro junto a "Columnas para repetir en la izquierda" y seleccionando la(s) columna(s) que deseas repetir.
<br>
<img src="3.png" width=60% />

1. Confirmar y imprimir: Haz clic en "Aceptar" para aplicar la configuración. Cuando imprimas la hoja, las filas o columnas especificadas aparecerán en cada página impresa.

## **Cómo borrar títulos de impresión en Excel**

Para borrar títulos de impresión en Excel, necesitas eliminar las filas o columnas que están configuradas para repetirse en cada página impresa. Aquí te decimos cómo hacerlo:

1. Abrir la pestaña de Diseño de página: Haz clic en la pestaña "Diseño de página" en la cinta en la parte superior de la ventana de Excel.
1. Acceder a Títulos de impresión: En el grupo "Configurar página", haz clic en "Títulos de impresión".
1. Borrar títulos de impresión: En el cuadro de diálogo "Configurar página", ve a la pestaña "Hoja". Borra el contenido de los cuadros "Filas para repetir en la parte superior" y "Columnas para repetir en la izquierda" eliminando cualquier contenido dentro de ellos.
<br>
<img src="4.png" width=60% />

1. Confirmar y cerrar: Haz clic en "Aceptar" para aplicar los cambios.

## **Cómo establecer títulos de impresión usando Aspose.Cells**

Para establecer títulos de impresión en una hoja de cálculo específica: Primero, carga el [archivo de ejemplo](input.xlsx), luego modifica las propiedades [**Worksheet.page_setup.print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows/) y [**Worksheet.page_setup.print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) del objeto [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/). Configurar estas propiedades con una cadena de rango configurará los títulos de impresión.

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set row 1 as repeating header
worksheet.page_setup.print_title_rows = "$1:$1"

# Save modified workbook
workbook.save("output.xlsx")
```

El resultado de la salida:
<br>
<img src="1.png" width=60% />

## **Cómo borrar títulos de impresión usando Aspose.Cells**

Para borrar títulos de impresión, establece las propiedades de título de impresión a cadenas vacías:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear existing print titles
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save modified workbook
workbook.save("output.xlsx")
```

El resultado de la salida:
<br>
<img src="2.png" width=60% />

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.page_setup.print_title_rows = "$1:$2"

# Set columns to repeat at the left (e.g., columns A and B)
worksheet.page_setup.print_title_columns = "$A:$B"

# Save the workbook
workbook.save("set_print_titles.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the rows and columns set to repeat
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save the workbook
workbook.save("clear_print_titles.pdf")
```
