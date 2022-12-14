---
title: Dar formato a un objeto de lista - Tabla
type: docs
weight: 50
url: /es/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

Para administrar y analizar un grupo de datos relacionados, es posible convertir un rango de celdas en un objeto de lista (también conocido como tabla de Excel). Una tabla es una serie de filas y columnas que contienen datos relacionados administrados independientemente de los datos de otras filas y columnas. De manera predeterminada, cada columna de la tabla tiene habilitado el filtrado en la fila del encabezado para que pueda filtrar u ordenar rápidamente los datos de su objeto de lista. Puede agregar una fila total (una fila especial en una lista que proporciona una selección de funciones agregadas útiles para trabajar con datos numéricos) al objeto de lista que proporciona una lista desplegable de funciones agregadas para cada celda de fila total. Aspose.Cells proporciona opciones para crear y administrar listas (o tablas).

{{% /alert %}}

## **Dar formato a un objeto de lista**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para crear un[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) en una hoja de trabajo, use[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) colección propiedad de la[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. Cada[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) es, de hecho, un objeto de la[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class, que además proporciona el método add para agregar un objeto List y especificar el rango de celdas que debe abarcar. De acuerdo con el rango especificado de celdas, un[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) se crea en la hoja de trabajo por Aspose.Cells. Use atributos (por ejemplo,[**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) ) del[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)class para formatear la tabla según sus necesidades.

 El siguiente ejemplo agrega datos de muestra a una hoja de trabajo, agrega un[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) y le aplica estilos predeterminados.[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)los estilos son compatibles con Microsoft Excel 2007/2010.

El siguiente resultado se genera cuando se ejecuta el código.

**Se crea una tabla formateada en la hoja de trabajo.** 

![todo:imagen_alternativa_texto](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
