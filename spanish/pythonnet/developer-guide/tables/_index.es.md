---
title: Crear y gestionar tablas de archivos de Microsoft Excel.
linktitle: Tablas
type: docs
weight: 150
url: /es/python-net/create-and-format-table/
description: Insertar, redimensionar, editar, eliminar, formatear tablas de archivos de Excel usando la biblioteca Aspose.Cells.
---

## **Crear Tabla**

Una de las ventajas de las hojas de cálculo es que te permiten crear diferentes tipos de listas, por ejemplo, listas de teléfonos, listas de tareas, listas de transacciones, activos o pasivos. Varios usuarios pueden colaborar para usar, crear y mantener varias listas.

Aspose.Cells para Python via .NET soporta la creación y gestión de Listas.

### **Ventajas de un Objeto de Lista**

Existen varias ventajas cuando conviertes una lista de datos en un Objeto de Lista real

- Se incluyen automáticamente nuevas filas y columnas.
- Se puede agregar fácilmente una fila total en la parte inferior de tu lista para mostrar SUMA, PROMEDIO, CONTAR, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente en el Objeto de Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos nombrados asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.

### **Creación de un Objeto de Lista utilizando Microsoft Excel**

- Seleccionar el rango de datos para crear un objeto de Lista
- Esto muestra el cuadro de diálogo Crear Lista.
- Implementar el Objeto de Lista para los datos y especificar la fila total (Seleccionar **Datos**, luego **Lista**, seguido de **Fila Total**).

### **Uso de la API Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia variedad de propiedades y métodos para administrar una hoja de cálculo. Para crear un [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) en una hoja de cálculo, utiliza la propiedad de colección [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Cada [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) es, de hecho, un objeto de la clase [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool), que además proporciona el método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) para agregar un objeto Lista y especificar un rango de celdas para la lista.

Según el rango de celdas especificado, el objeto Lista es creado por Aspose.Cells para Python via .NET. Use atributos (por ejemplo, [**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals), [**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns), etc.) de la clase [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) para controlar la lista.

En el ejemplo dado abajo, hemos creado la misma [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) usando la API Aspose.Cells para Python via .NET que creamos usando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **Formato de una Tabla**

Para gestionar y analizar un grupo de datos relacionados, es posible convertir un rango de celdas en un objeto lista (también conocido como tabla de Excel). Una tabla es una serie de filas y columnas que contienen datos relacionados gestionados de manera independiente de los datos en otras filas y columnas. Por defecto, cada columna en la tabla tiene habilitada la filtración en la fila de encabezado para que puedas filtrar o ordenar rápidamente los datos de tu objeto lista. Puedes agregar una fila total (una fila especial en una lista que proporciona una selección de funciones agregadas útiles para trabajar con datos numéricos) a la lista que proporciona un menú desplegable de funciones agregadas para cada celda de fila total. Aspose.Cells para Python via .NET ofrece opciones para crear y gestionar listas (o tablas).

### **Formateando un Objeto de Lista**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para crear un [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) en una hoja de cálculo, utiliza la propiedad de colección [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Cada [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) es, de hecho, un objeto de la clase [**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection), que además proporciona el método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) para agregar un objeto de Lista y especificar el rango de celdas que debe abarcar. Según el rango de celdas especificado, se crea un [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) en la hoja de cálculo mediante Aspose.Cells. Utiliza atributos (por ejemplo, [**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)) de la clase [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) para formatear la tabla según tus necesidades.

El siguiente ejemplo añade datos de muestra a una hoja de cálculo, agrega un [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) y aplica estilos predeterminados a él. Los estilos [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) son compatibles con Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **Temas avanzados**
- [Convertir Tabla a ODS](/cells/es/python-net/convert-table-to-ods/)
- [Buscar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externos](/cells/es/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Leer y Escribir Tabla con Origen de Datos de Tabla de Consulta](/cells/es/python-net/read-and-write-table-with-query-table-data-source/)
- [Establecer el Comentario de la Tabla o Objeto de Lista dentro de la Hoja de Cálculo](/cells/es/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tablas y Rangos](/cells/es/python-net/tables-and-ranges/)


