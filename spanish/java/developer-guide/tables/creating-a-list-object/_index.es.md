---
title: Crear una tabla
type: docs
weight: 40
url: /es/java/creating-a-list-object/
---
{{% alert color="primary" %}}

Una de las ventajas de las hojas de cálculo es que te permiten crear diferentes tipos de listas, por ejemplo, listas de teléfonos, listas de tareas, listas de transacciones, activos o pasivos. Varios usuarios pueden trabajar juntos para usar, crear y mantener varias listas.

Aspose.Cells admite la creación y gestión de listas.

{{% /alert %}}

## **ventajas de una mesa**

Hay bastantes ventajas cuando convierte una lista de datos en un objeto de lista real:

- Las nuevas filas y columnas se incluyen automáticamente.
- Se puede agregar fácilmente una fila total al final de su lista para mostrar SUMA, PROMEDIO, CONTEO, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente al objeto Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos con nombre asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.

## **Creando una tabla usando Microsoft Excel**

**Seleccionar rango de datos para crear un objeto de lista** 

![todo:imagen_alternativa_texto](creating-a-list-object_1.png)

Esto muestra el cuadro de diálogo Crear lista.

**Cuadro de diálogo Crear lista** 

![todo:imagen_alternativa_texto](creating-a-list-object_2.png)

 Implementando el objeto List y especificando Total Row (Select**Datos** , después**Lista** , seguido por**fila total**).

**Creación de un objeto de lista** 

![todo:imagen_alternativa_texto](creating-a-list-object_3.png)

## **Creando una tabla usando Usando Aspose.Cells API**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Para crear un[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) en una hoja de trabajo, use[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) propiedad de colección de la clase Worksheet. Cada[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) es, de hecho, un objeto de la[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class, que además proporciona el método add para agregar un objeto List y especificar un rango de celdas para la lista.

De acuerdo con el rango de celdas especificado, el objeto List se crea en la hoja de trabajo por Aspose.Cells. Use atributos (por ejemplo, ShowTotals, ListColumns, etc.) del[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)clase para controlar la lista.

 En el ejemplo dado a continuación, hemos creado el mismo[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)usando Aspose.Cells API como creamos usando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
