---
title: Creación de un objeto de lista
type: docs
weight: 20
url: /es/python-java/creating-a-list-object/
---

El uso de hojas de cálculo facilita el trabajo con diferentes tipos de listas, por ejemplo, listas de teléfonos, listas de tareas, etc. Aspose.Cells admite la creación y gestión de listas.

## **Ventajas de un Objeto de Lista**

Existen varias ventajas al convertir una lista de datos en un objeto de lista real:

- Se incluyen automáticamente nuevas filas y columnas.
- Se puede agregar fácilmente una fila total en la parte inferior de tu lista para mostrar SUMA, PROMEDIO, CONTAR, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente en el Objeto de Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos nombrados asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.

## **Creación de un Objeto de Lista utilizando Microsoft Excel**

**Seleccionar el rango de datos para crear un objeto de lista** 

![todo:image_alt_text](picture1.png)

Esto muestra el cuadro de diálogo Crear lista.

**Cuadro de diálogo Crear lista** 

![todo:image_alt_text](picture2.png)

Implementar el objeto de lista y especificar Fila Total (Seleccionar **Datos**, luego **Lista**, seguido de **Fila Total**).

**Creación de un objeto de lista** 

![todo:image_alt_text](picture3.png)

## **Creación de un objeto de lista usando el API de Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para crear un [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) en una hoja de cálculo, use la propiedad de la colección [**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects) de la clase [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). Cada [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) es, de hecho, un objeto de la clase [**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection), que además proporciona el método [**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) para agregar un objeto de lista y especificar un rango de celdas para la lista.

Según el rango especificado de celdas, el objeto de lista se crea en la hoja de cálculo por Aspose.Cells. Utilice atributos (por ejemplo, ShowTotals, ListColumns, etc.) de la clase [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) para controlar la lista.

En el ejemplo dado a continuación, hemos creado la misma [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) usando Aspose.Cells para la API de Python via Java como la que creamos usando Microsoft Excel en la sección anterior.

## Código fuente

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
