---
title: Creación de una tabla
type: docs
weight: 40
url: /es/java/creating-a-list-object/
---

{{% alert color="primary" %}}

Una de las ventajas de las hojas de cálculo es que te permiten crear diferentes tipos de listas, por ejemplo, listas de teléfonos, listas de tareas, listas de transacciones, activos o pasivos. Varios usuarios pueden colaborar para usar, crear y mantener varias listas.

Aspose.Cells soporta la creación y gestión de listas.

{{% /alert %}}

## **Ventajas de una tabla**

Existen varias ventajas al convertir una lista de datos en un objeto de lista real:

- Se incluyen automáticamente nuevas filas y columnas.
- Se puede agregar fácilmente una fila total en la parte inferior de tu lista para mostrar SUMA, PROMEDIO, CONTAR, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente en el Objeto de Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos nombrados asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.

## **Creación de una tabla usando Microsoft Excel**

**Seleccionar el rango de datos para crear un objeto de lista** 

![todo:image_alt_text](creating-a-list-object_1.png)

Esto muestra el cuadro de diálogo Crear lista.

**Cuadro de diálogo Crear lista** 

![todo:image_alt_text](creating-a-list-object_2.png)

Implementación del objeto Lista y especificación de una Fila Total (Selecciona **Datos**, luego **Lista**, seguido de **Fila Total**).

**Creación de un objeto de lista** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Creación de una tabla utilizando la API de Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para crear un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) en una hoja de cálculo, utilice la propiedad de la colección [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) de la clase Hoja de cálculo. Cada [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) es, de hecho, un objeto de la clase [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), que proporciona el método add para agregar un objeto Lista y especificar un rango de celdas para la lista.

Según el rango de celdas especificado, se crea un objeto Lista en la hoja de cálculo por medio de Aspose.Cells. Utilice atributos (por ejemplo, MostrarTotales, ColumnasLista, etc.) de la clase [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) para controlar la lista.

En el ejemplo que se muestra a continuación, hemos creado la misma [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) utilizando la API de Aspose.Cells como la que creamos utilizando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
{{< app/cells/assistant language="java" >}}
