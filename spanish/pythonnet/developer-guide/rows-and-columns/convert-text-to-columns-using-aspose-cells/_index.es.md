---
title: Convertir texto en columnas usando Aspose.Cells
type: docs
weight: 30
url: /es/python-net/convert-text-to-columns-using-aspose-cells/
description: Este artículo muestra cómo convertir texto a columnas mediante la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Python para Excel, Convertir texto a columnas en Python, Convertir texto a columnas en Python.
---

## **Escenarios de uso posibles**

Puede convertir su texto a columnas usando Microsoft Excel. Esta función está disponible en *Herramientas de datos* en la pestaña *Datos*. Para dividir el contenido de una columna en varias columnas, los datos deben contener un delimitador específico, como una coma (o cualquier otro carácter) en función de la cual Microsoft Excel dividirá el contenido de una celda en múltiples celdas. Aspose.Cells para Python via .NET también proporciona esta función a través del método [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/).

## **Convertir texto a columnas usando Aspose.Cells para la biblioteca de Excel de Python**

El siguiente código de muestra explica el uso del método [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/). El código primero añade algunos nombres de personas en la columna A de la primera hoja de cálculo. El nombre y apellido están separados por un espacio. Luego aplica el método [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) en la columna A y lo guarda como archivo de Excel de salida. Si abres el [archivo de Excel de salida](25395213.xlsx), verás que los nombres están en la columna A mientras que los apellidos están en la columna B como se muestra en esta captura de pantalla.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
