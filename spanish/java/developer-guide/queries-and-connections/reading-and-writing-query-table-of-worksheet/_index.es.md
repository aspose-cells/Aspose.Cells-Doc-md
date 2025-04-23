---
title: Leer y Escribir Tabla de Consulta de Hoja de Cálculo
type: docs
weight: 560
url: /es/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells proporciona la colección [Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) que devuelve la [QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection). Para obtener una [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) específica, use la propiedad [QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20-int-) y pase el índice de la QueryTable. La clase [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) tiene las siguientes dos propiedades para ajustar la QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Ambos son valores booleanos. Puede verlos en Microsoft Excel a través de Datos > Conexiones > Propiedades.

{{% /alert %}} 
## **Leer y Escribir Tabla de Consulta de Hoja de Cálculo**
El siguiente código de ejemplo lee la primera [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) de la primera hoja de cálculo e imprime ambas propiedades de [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). Luego establece [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) en **true**.

La siguiente captura de pantalla muestra el [archivo de Excel fuente](5472578.xlsx) utilizado en el código y sus propiedades que muestran ambos valores de [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable).

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

La siguiente captura de pantalla muestra el [archivo de Excel de salida](5472574.xlsx) generado por el código y sus propiedades que muestran ambos valores de [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). Como puede ver, la casilla de verificación de Formato Preservado ahora está marcada.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Salida de la consola**
Aquí está la salida de la consola del código de ejemplo anterior

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **Recuperar rango de resultado de la tabla de consulta**
Aspose.Cells proporciona la opción de leer la dirección, es decir, el rango de resultados de celdas para una tabla de consulta. El siguiente código demuestra esta característica leyendo la dirección del rango de resultados para una tabla de consulta. El archivo de ejemplo se puede descargar [aquí](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
{{< app/cells/assistant language="java" >}}
