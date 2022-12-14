---
title: Convertir Texto a Columnas usando Aspose.Cells
type: docs
weight: 30
url: /es/net/convert-text-to-columns-using-aspose-cells/
---
## **Posibles escenarios de uso**

Puede convertir su Texto a Columnas usando Microsoft Excel. Esta función está disponible desde*Herramientas de datos* bajo la*Datos* pestaña. Para dividir el contenido de una columna en varias columnas, los datos deben contener un delimitador específico como una coma (o cualquier otro carácter) basado en el cual Microsoft Excel divide el contenido de una celda en varias celdas. Aspose.Cells también ofrece esta función a través de[**Hoja de trabajo.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)método.

## **Convertir Texto a Columnas usando Aspose.Cells**

 El siguiente código de ejemplo explica el uso de[**Hoja de trabajo.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) método. El código primero agrega el nombre de algunas personas en la columna A de la primera hoja de trabajo. El nombre y el apellido están separados por un carácter de espacio. Entonces se aplica[**Hoja de trabajo.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) método en la columna A y guárdelo como archivo de salida de Excel. Si abres el[archivo de salida de Excel](25395213.xlsx), verá que los nombres están en la columna A mientras que los apellidos están en la columna B, como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](convert-text-to-columns-using-aspose-cells_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
