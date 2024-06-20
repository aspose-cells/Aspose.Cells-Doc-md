---
title: Convertir texto en columnas usando Aspose.Cells
type: docs
weight: 70
url: /es/java/convert-text-to-columns-using-aspose-cells/
---

## **Escenarios de uso posibles**
Puedes convertir tu Texto en Columnas usando Microsoft Excel. Esta función está disponible en *Herramientas de Datos* bajo la pestaña *Datos*. Para dividir el contenido de una columna en varias columnas, los datos deben contener un delimitador específico como una coma (o cualquier otro carácter) según el cual Microsoft Excel divide el contenido de una celda en varias celdas. Aspose.Cells también proporciona esta función a través del método [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)).
## **Convertir Texto en Columnas usando Aspose.Cells**
El siguiente código de ejemplo explica el uso del método [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)). El código primero agrega algunos nombres de personas en la columna A de la primera hoja de cálculo. El nombre y apellido están separados por un espacio. Luego aplica el método [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) en la columna A y lo guarda como archivo Excel de salida. Si abres el [archivo Excel de salida](25395230.xlsx), verás que los nombres están en la columna A mientras que los apellidos están en la columna B como se muestra en esta captura de pantalla.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
