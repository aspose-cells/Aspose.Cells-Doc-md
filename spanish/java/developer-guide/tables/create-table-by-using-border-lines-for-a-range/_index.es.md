---
title: Crear Tabla usando Líneas de Borde para un Rango
type: docs
weight: 50
url: /es/java/create-table-by-using-border-lines-for-a-range/
description: Cómo crear una tabla con un rango usando líneas de borde. Aspose.Cells for Java proporciona una API simple de usar que se puede usar para agregar bordes a un rango.
keywords: crear tabla, rango a tabla, rango a tabla excel, rango a tabla con bordes, cómo crear tabla a partir de rango, convertir rango a tabla, excel convertir rango a tabla, excel crear tabla, rango a tabla java 
---

{{% alert color="primary" %}}

A veces, desea crear una tabla agregando líneas de borde para un **Rango**/**Área de celdas** basado en la dirección de las celdas que tiene. Puede utilizar el método [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) para crear un rango de celdas. El método [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) retorna un objeto [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range). Puede crear un objeto [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) y especificar las opciones de bordes (superior, izquierdo, inferior, derecho) en consecuencia. Más tarde, puede obtener las celdas del [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) y aplicar el formato deseado a las celdas.

{{% /alert %}}

El siguiente ejemplo muestra cómo crear un [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) y especificar las líneas de borde para las celdas del rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Después de ejecutar el código anterior, podemos tener el archivo de Excel generado que contiene la tabla formateada; aquí está la captura de pantalla del archivo.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
{{< app/cells/assistant language="java" >}}
