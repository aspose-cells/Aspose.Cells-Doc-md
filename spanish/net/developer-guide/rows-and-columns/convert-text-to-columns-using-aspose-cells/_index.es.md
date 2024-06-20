---
title: Convertir texto en columnas usando Aspose.Cells
type: docs
weight: 30
url: /es/net/convert-text-to-columns-using-aspose-cells/
---

## **Escenarios de uso posibles**

Puedes convertir tu Texto a Columnas utilizando Microsoft Excel. Esta característica está disponible en *Herramientas de Datos* bajo la pestaña *Datos*. Para dividir el contenido de una columna en varias columnas, los datos deben contener un delimitador específico como una coma (u otro carácter) en función del cual Microsoft Excel dividirá el contenido de una celda en varias celdas. Aspose.Cells también proporciona esta característica a través del método [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns).

## **Convertir Texto en Columnas usando Aspose.Cells**

El siguiente código de muestra explica el uso del método [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns). El código primero añade algunos nombres de personas en la columna A de la primera hoja de cálculo. El nombre y apellido están separados por un espacio. Luego aplica el método [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) en la columna A y lo guarda como archivo de Excel de salida. Si abres el [archivo de Excel de salida](25395213.xlsx), verás que los nombres están en la columna A mientras que los apellidos están en la columna B como se muestra en esta captura de pantalla.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
