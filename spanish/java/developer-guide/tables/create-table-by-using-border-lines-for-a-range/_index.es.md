---
title: Crear tabla usando líneas de borde para un rango
type: docs
weight: 50
url: /es/java/create-table-by-using-border-lines-for-a-range/
description: Cómo crear una tabla con rango usando líneas de borde. Aspose.Cells for Java proporciona un API fácil de usar que se puede usar para agregar bordes a un rango.
keywords: create table, range to table, range to table excel, excel range to table, range to table with borders, how to create table from range, convert range to table, excel convert range to table, excel create table, range to table java 
---
{{% alert color="primary" %}}

 A veces, desea crear una tabla agregando líneas de borde para un**Rango**/**área de celda** basado en la dirección de las celdas que tiene. Puedes usar[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) para crear un rango de celdas. los[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean) ) método devuelve un[**Rango**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objeto. Puedes crear un[**Estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objeto y especifique las opciones de los bordes (superior, izquierdo, inferior, derecho) en consecuencia. Más tarde, puede obtener las células del[**Rango**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)y aplique el formato deseado a las celdas.

{{% /alert %}}

 El siguiente ejemplo muestra cómo crear un[**Rango**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)y especifique los límites para las celdas de rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Después de ejecutar el código anterior, podemos tener el archivo de Excel generado que contiene la tabla formateada; aquí está la captura de pantalla del archivo.

![todo:imagen_alternativa_texto](create-table-by-using-border-lines-for-a-range_1.png)
