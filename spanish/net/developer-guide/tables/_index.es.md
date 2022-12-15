---
title: Cree y administre tablas de Microsoft archivos de Excel.
linktitle: Mesas
type: docs
weight: 150
url: /es/net/create-and-format-table/
description: Inserte, cambie el tamaño, edite, elimine, formatee la tabla de archivos de Excel usando la biblioteca Aspose.Cells.
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

- Seleccionar rango de datos para crear un objeto de Lista
- Esto muestra el cuadro de diálogo Crear lista.
-  Implemente el objeto Lista para los datos y especifique la fila total (Seleccione**Datos** , después**Lista** , seguido por**fila total**).

### **Usando Aspose.Cells API**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de trabajo. Para crear un[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) en una hoja de trabajo, utilice el[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) colección propiedad de la[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Cada[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) es, de hecho, un objeto de la[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) clase, que proporciona además la[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)método para agregar un objeto List y especificar un rango de celdas para la lista.

De acuerdo con el rango de celdas especificado, el objeto Lista es creado por Aspose.Cells. Use atributos (por ejemplo,[**MostrarTotales**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListaColumnas**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) , etc) de la[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)clase para controlar la lista.

 En el ejemplo dado a continuación, hemos creado el mismo[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)usando Aspose.Cells API como creamos usando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Dar formato a una tabla**

Para administrar y analizar un grupo de datos relacionados, es posible convertir un rango de celdas en un objeto de lista (también conocido como tabla de Excel). Una tabla es una serie de filas y columnas que contienen datos relacionados administrados independientemente de los datos de otras filas y columnas. De manera predeterminada, cada columna de la tabla tiene habilitado el filtrado en la fila del encabezado para que pueda filtrar u ordenar rápidamente los datos de su objeto de lista. Puede agregar una fila total (una fila especial en una lista que proporciona una selección de funciones agregadas útiles para trabajar con datos numéricos) al objeto de lista que proporciona una lista desplegable de funciones agregadas para cada celda de fila total. Aspose.Cells proporciona opciones para crear y administrar listas (o tablas).

### **Dar formato a un objeto de lista**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para crear un[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) en una hoja de trabajo, utilice[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) colección propiedad de la[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Cada[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) es, de hecho, un objeto de la[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) clase, que proporciona además la[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) para agregar un objeto List y especificar el rango de celdas que debe abarcar. De acuerdo con el rango especificado de celdas, un[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)se crea en la hoja de trabajo por Aspose.Cells. Use atributos (por ejemplo,[**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) ) del[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)class para formatear la tabla según sus necesidades.

 El siguiente ejemplo agrega datos de muestra a una hoja de trabajo, agrega un[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) y aplicarle estilos predeterminados.[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)los estilos son compatibles con Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Temas avanzados**
- [Convertir tabla a ODS](/cells/es/net/convert-table-to-ods/)
- [Encuentre tablas de consulta y objetos de lista relacionados con conexiones de datos externas](/cells/es/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Tabla de lectura y escritura con fuente de datos de tabla de consulta](/cells/es/net/read-and-write-table-with-query-table-data-source/)
- [Establezca el comentario de la tabla o el objeto de lista dentro de la hoja de trabajo](/cells/es/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tablas y Rangos](/cells/es/net/tables-and-ranges/)

