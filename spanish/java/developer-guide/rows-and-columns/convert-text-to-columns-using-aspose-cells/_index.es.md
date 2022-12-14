---
title: Convertir Texto a Columnas usando Aspose.Cells
type: docs
weight: 70
url: /es/java/convert-text-to-columns-using-aspose-cells/
---
## **Posibles escenarios de uso**
Puede convertir su Texto a Columnas usando Microsoft Excel. Esta función está disponible desde*Herramientas de datos* bajo la*Datos* pestaña. Para dividir el contenido de una columna en varias columnas, los datos deben contener un delimitador específico como una coma (o cualquier otro carácter) basado en el cual Microsoft Excel divide el contenido de una celda en varias celdas. Aspose.Cells también ofrece esta función a través de[TextoAColumnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) método.
## **Convertir Texto a Columnas usando Aspose.Cells**
El siguiente código de ejemplo explica el uso de la[TextoAColumnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) método. El código primero agrega algunos nombres de personas en la columna A de la primera hoja de trabajo. El nombre y el apellido están separados por un carácter de espacio. Luego aplica el[TextoAColumnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\) ) en la columna A y lo guarda como archivo de salida de Excel. Si abres el[archivo de salida de Excel](25395230.xlsx), verá que los nombres están en la columna A mientras que los apellidos están en la columna B, como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](convert-text-to-columns-using-aspose-cells_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
