---
title: Creación de un objeto de lista
type: docs
weight: 20
url: /es/python-java/creating-a-list-object/
---
El uso de hojas de trabajo hace que sea fácil trabajar con diferentes tipos de listas, por ejemplo. listas de teléfonos, listas de tareas. etc. Aspose.Cells admite la creación y gestión de listas.

## **Ventajas de un objeto de lista**

Hay bastantes ventajas cuando convierte una lista de datos en un objeto de lista real:

- Las nuevas filas y columnas se incluyen automáticamente.
- Se puede agregar fácilmente una fila total al final de su lista para mostrar SUMA, PROMEDIO, CONTEO, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente al objeto Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos con nombre asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.

## **Creación de un objeto de lista usando Microsoft Excel**

**Seleccionar rango de datos para crear un objeto de lista** 

![todo:imagen_alternativa_texto](picture1.png)

Esto muestra el cuadro de diálogo Crear lista.

**Cuadro de diálogo Crear lista** 

![todo:imagen_alternativa_texto](picture2.png)

Implementando el objeto List y especificando Total Row (Select**Datos**, después**Lista**seguido por**fila total**).

**Creación de un objeto de lista** 

![todo:imagen_alternativa_texto](picture3.png)

## **Creación de un objeto de lista usando Aspose.Cells API**

Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Para crear un[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)en una hoja de trabajo, use[**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)colección propiedad de la[**Hoja de cálculo**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)clase. Cada[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)es, de hecho, un objeto de la[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)clase, que proporciona además la[**agregar**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) método para agregar un objeto List y especificar un rango de celdas para la lista.

De acuerdo con el rango de celdas especificado, el objeto List se crea en la hoja de trabajo por Aspose.Cells. Use atributos (por ejemplo, ShowTotals, ListColumns, etc.) del[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)clase para controlar la lista.

En el ejemplo dado a continuación, hemos creado el mismo[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)usando Aspose.Cells for Python via Java API como creamos usando Microsoft Excel en la sección anterior.

## Código fuente

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
