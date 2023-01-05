---
title: Tabla de consulta de lectura y escritura de la hoja de trabajo
type: docs
weight: 560
url: /es/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

 Aspose.Cells proporciona[Hoja de trabajo.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) colección que devuelve el[QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) . Para obtener un especifico[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) , utilizar el[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) y pase el índice de QueryTable. Él[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) class tiene las siguientes dos propiedades para ajustar QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Ambos son valores booleanos. Puede verlos en Microsoft Excel a través de Datos > Conexiones > Propiedades.

{{% /alert %}} 
## **Tabla de consulta de lectura y escritura de la hoja de trabajo**
 El siguiente código de ejemplo lee el primer[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) de la primera hoja de trabajo y luego imprime las dos[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) propiedades. Luego establece el[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) a**verdadero**.

La siguiente captura de pantalla muestra la[archivo fuente excel](5472578.xlsx) utilizado en el código y sus propiedades que muestran tanto el[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)valores.

![todo:imagen_alternativa_texto](reading-and-writing-query-table-of-worksheet_1.png)

La siguiente captura de pantalla muestra la[archivo de salida de Excel](5472574.xlsx) generado por el código y sus propiedades que muestran tanto el[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)valores. Como puede ver, la casilla de verificación Formato conservado está marcada ahora.

![todo:imagen_alternativa_texto](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Salida de consola**
Aquí está la salida de la consola del código de muestra anterior

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **Recuperar el rango de resultados de la tabla de consulta**
Aspose.Cells ofrece la opción de leer la dirección, es decir, el rango de resultados de las celdas de una tabla de consulta. El siguiente código demuestra esta característica al leer la dirección del rango de resultados para una tabla de consulta. El archivo de muestra se puede descargar[aquí](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
