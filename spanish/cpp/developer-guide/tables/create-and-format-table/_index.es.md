---
title: Crear y dar formato a la tabla
type: docs
weight: 10
url: /es/cpp/create-and-format-table/
---
## **Crear mesa**
Una de las ventajas de las hojas de cálculo es que te permiten crear diferentes tipos de listas, por ejemplo, listas de teléfonos, listas de tareas, listas de transacciones, activos o pasivos. Varios usuarios pueden trabajar juntos para usar, crear y mantener varias listas.

Aspose.Cells admite la creación y gestión de listas.
### **Ventajas de un objeto de lista**
Hay bastantes ventajas cuando convierte una lista de datos en un objeto de lista real

- Las nuevas filas y columnas se incluyen automáticamente.
- Se puede agregar fácilmente una fila total al final de su lista para mostrar SUMA, PROMEDIO, CONTEO, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente al objeto Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos con nombre asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.
### **Creación de un objeto de lista usando Microsoft Excel**

|**Selección del rango de datos para crear el objeto Lista**|
|:- |
|![todo:imagen_alternativa_texto](jHcNq4o.png)|
Esto muestra el cuadro de diálogo Crear lista.

|**Cuadro de diálogo Crear lista**|
|:- |
|![todo:imagen_alternativa_texto](kJmukRF.png)|
 Implementar el objeto Lista para los datos y especificar la fila total (Seleccionar**Datos** , después**Lista** , seguido por**fila total**).

|**Creación de un objeto de lista**|
|:- |
|![todo:imagen_alternativa_texto](ECSGVdR.png)|
### **Usando Aspose.Cells API**
 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. Él[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[IHojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Él[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class proporciona una amplia gama de métodos para administrar una hoja de cálculo. Para crear un[IListObject](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object) en una hoja de trabajo, utilice el[ObtenerIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705) método de recolección de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Cada `[IListObject]` es, de hecho, un objeto de la[IListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection) clase, que proporciona además la[Agregar](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)método para agregar un objeto `[IListObject]` y especificar un rango de celdas para la lista.

 De acuerdo con el rango de celdas especificado, el objeto `[IListObject]` es creado por Aspose.Cells. Use atributos (por ejemplo[MostrarTotales](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2) y[ListaColumnas](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)etc.) de la clase `[IListObject]` para controlar la lista.

En el ejemplo que se muestra a continuación, hemos creado el mismo `[IListObject]` usando Aspose.Cells API que creamos usando Microsoft Excel en la sección anterior.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **Dar formato a una tabla**
Para administrar y analizar un grupo de datos relacionados, es posible convertir un rango de celdas en un objeto de lista (también conocido como tabla de Excel). Una tabla es una serie de filas y columnas que contienen datos relacionados administrados independientemente de los datos de otras filas y columnas. De manera predeterminada, cada columna de la tabla tiene habilitado el filtrado en la fila del encabezado para que pueda filtrar u ordenar rápidamente los datos de su objeto de lista. Puede agregar una fila de totales (una fila especial en una lista que proporciona una selección de funciones de agregado útiles para trabajar con datos numéricos) al objeto de lista que proporciona una lista desplegable de funciones de agregado para cada celda de fila de totales. Aspose.Cells proporciona opciones para crear y administrar listas (o tablas).
### **Dar formato a un objeto de lista**
 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. Él[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[IHojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Él[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) La clase proporciona una amplia gama de métodos para administrar hojas de trabajo. Para crear un*ListObject*en una hoja de cálculo, use `IListObjectCollection`. Cada `[IListObject]` es, de hecho, un objeto de la clase `IListObjectCollection`, que además proporciona la[Agregar](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)método para agregar un objeto `[IListObject]` y especificar el rango de celdas que debe abarcar. De acuerdo con el rango especificado de celdas, un*ListObject* se crea en la hoja de trabajo por Aspose.Cells. Use atributos (por ejemplo,[TableStyleType](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)) de la clase `[IListObject]` para formatear la tabla según sus requisitos.

El siguiente ejemplo agrega datos de muestra a una hoja de trabajo, agrega un `[IListObject]` y le aplica estilos predeterminados. Los estilos `[IListObject]` son compatibles con Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}
