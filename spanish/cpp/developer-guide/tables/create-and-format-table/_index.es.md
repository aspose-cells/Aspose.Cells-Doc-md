---
title: Crear y formatear tabla
type: docs
weight: 10
url: /es/cpp/create-and-format-table/
---
##  **Crear mesa**
Una de las ventajas de las hojas de cálculo es que permiten crear diferentes tipos de listas, por ejemplo, listas de teléfonos, listas de tareas, listas de transacciones, activos o pasivos. Varios usuarios pueden trabajar juntos para utilizar, crear y mantener varias listas.

Aspose.Cells admite la creación y gestión de listas.
###  **Ventajas de un objeto de lista**
Hay bastantes ventajas al convertir una lista de datos en un objeto de lista real.

- Las nuevas filas y columnas se incluyen automáticamente.
- Se puede agregar fácilmente una fila de total al final de su lista para mostrar SUMA, PROMEDIO, RECUENTO, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente al objeto Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos con nombre asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.
###  **Crear un objeto de lista usando Microsoft Excel**

|**Seleccionar rango de datos para crear un objeto de lista**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Esto muestra el cuadro de diálogo Crear lista.

|**Crear cuadro de diálogo de lista**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Implementar el objeto Lista para los datos y especificar la fila total (Seleccione *Datos**, luego *Lista**, seguido de *Fila total**).

|**Creando un objeto de lista**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
###  **Usando Aspose.Cells API**
 Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)colección que permite el acceso a cada hoja de cálculo en un archivo Excel.

Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La clase proporciona una amplia gama de métodos para administrar una hoja de trabajo. para crear un[Lista de objetos](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) en una hoja de trabajo, use el[Obtener objetos de lista](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) método de recolección de[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. Cada `[ListObject]` es, de hecho, un objeto del[ColecciónListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) clase, que además proporciona la[Agregar](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)Método para agregar un objeto `[ListObject]` y especificar un rango de celdas para la lista.

 Según el rango de celdas especificado, el objeto `[ListObject]` es creado por Aspose.Cells. Utilice atributos (por ejemplo[EstablecerMostrarTotales](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) y[Obtener columnas de lista](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)etc.) de la clase `[ListObject]` para controlar la lista.

En el ejemplo que se muestra a continuación, hemos creado el mismo `[ListObject]` usando Aspose.Cells API que creamos usando Microsoft Excel en la sección anterior.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **Dar formato a una tabla**
Para gestionar y analizar un grupo de datos relacionados, es posible convertir un rango de celdas en un objeto de lista (también conocido como tabla de Excel). Una tabla es una serie de filas y columnas que contienen datos relacionados administrados independientemente de los datos de otras filas y columnas. De forma predeterminada, cada columna de la tabla tiene habilitado el filtrado en la fila del encabezado para que pueda filtrar u ordenar los datos de los objetos de su lista rápidamente. Puede agregar una fila de total (una fila especial en una lista que proporciona una selección de funciones agregadas útiles para trabajar con datos numéricos) al objeto de lista que proporciona una lista desplegable de funciones agregadas para cada celda de la fila de totales. Aspose.Cells proporciona opciones para crear y administrar listas (o tablas).
###  **Formatear un objeto de lista**
 Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)colección que permite el acceso a cada hoja de cálculo en un archivo Excel.

Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La clase proporciona una amplia gama de métodos para administrar hojas de trabajo. Para crear un*Lista de objetos*en una hoja de trabajo, utilice `ListObjectCollection`. Cada `[ListObject]` es, de hecho, un objeto de la clase `ListObjectCollection`, que además proporciona la[Agregar](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)método para agregar un objeto `[ListObject]` y especificar el rango de celdas que debe abarcar. Según el rango de celdas especificado, una*Lista de objetos* se crea en la hoja de trabajo por Aspose.Cells. Utilice atributos (por ejemplo,[Establecer tipo de estilo de tabla](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) de la clase `[ListObject]` para formatear la tabla según sus requisitos.

El siguiente ejemplo agrega datos de muestra a una hoja de trabajo, agrega un `[ListObject]` y le aplica estilos predeterminados. `[ListObject]` estilos son compatibles con Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
