---
title: Formato de un Objeto Lista  Tabla
type: docs
weight: 50
url: /es/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

Para gestionar y analizar un grupo de datos relacionados, es posible convertir un rango de celdas en un objeto de lista (también conocido como una tabla de Excel). Una tabla es una serie de filas y columnas que contienen datos relacionados administrados de forma independiente de los datos en otras filas y columnas. Por defecto, cada columna en la tabla tiene activada la filtración en la fila de encabezado para que puedas filtrar o ordenar tus datos de objeto de lista rápidamente. Puedes agregar una fila total (una fila especial en una lista que proporciona una selección de funciones de agregación útiles para trabajar con datos numéricos) al objeto de lista que ofrece una lista desplegable de funciones de agregación para cada celda de fila total. Aspose.Cells proporciona opciones para crear y gestionar listas (o tablas).

{{% /alert %}}

## **Formateando un Objeto de Lista**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) ofrece una amplia gama de propiedades y métodos para administrar hojas de cálculo. Para crear un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) en una hoja de cálculo, usa la propiedad de colección [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Cada [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) es, en realidad, un objeto de la clase [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), que además proporciona el método add para agregar un objeto List y especificar el rango de celdas que debe abarcar. Según el rango de celdas especificado, se crea un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) en la hoja de cálculo por Aspose.Cells. Usa atributos (por ejemplo, [**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType-) de la clase [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)) para formatear la tabla según tus necesidades.

El siguiente ejemplo agrega datos de ejemplo a una hoja de cálculo, agrega un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) y aplica estilos por defecto. Los estilos [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) son compatibles con Microsoft Excel 2007/2010.

La siguiente salida se genera cuando se ejecuta el código.

**Se crea una tabla formateada en la hoja de cálculo** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
{{< app/cells/assistant language="java" >}}
