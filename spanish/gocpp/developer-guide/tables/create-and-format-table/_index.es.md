---
title: Crear y Formatear Tabla
type: docs
weight: 10
url: /es/go-cpp/create-and-format-table/
---

## **Crear Tabla**

Una de las ventajas de las hojas de cálculo es que te permiten crear diferentes tipos de listas, por ejemplo, listas de teléfonos, listas de tareas, listas de transacciones, activos o pasivos. Varios usuarios pueden colaborar para usar, crear y mantener varias listas.

Aspose.Cells soporta la creación y gestión de listas.

### **Ventajas de un Objeto de Lista**

Existen varias ventajas cuando conviertes una lista de datos en un Objeto de Lista real

- Se incluyen automáticamente nuevas filas y columnas.
- Se puede agregar fácilmente una fila total en la parte inferior de tu lista para mostrar SUMA, PROMEDIO, CONTAR, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente en el Objeto de Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos nombrados asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.

### **Creación de un Objeto de Lista utilizando Microsoft Excel**

|**Seleccionando el rango de datos para crear un objeto Lista**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Esto muestra el cuadro de diálogo Crear lista.

|**Diálogo Crear Lista**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Implementar el Objeto Lista para los datos y especificar fila total (Selecciona **Datos**, luego **Lista**, seguido por **Fila Total**).

|**Creando un objeto lista**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|

### **Uso de la API de Aspose.Cells**

Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) ofrece una amplia gama de métodos para gestionar una hoja de cálculo. Para crear un [ListObject](https://reference.aspose.com/cells/go-cpp/listobject/) en una hoja, usa el método [GetListObjects](https://reference.aspose.com/cells/go-cpp/worksheet/getlistobjects/) de la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Cada `[ListObject]` es, de hecho, un objeto de la clase [ListObjectCollection](https://reference.aspose.com/cells/go-cpp/listobjectcollection/), que además proporciona el método [Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add_int_int_int_int_bool/) para agregar un objeto `[ListObject]` y especificar un rango de celdas para la lista.

Según el rango de celdas especificado, Aspose.Cells crea el objeto `[ListObject]`. Usa atributos (por ejemplo, [SetShowTotals](https://reference.aspose.com/cells/go-cpp/listobject/setshowtotals/) y [GetListColumns](https://reference.aspose.com/cells/go-cpp/listobject/getlistcolumns/) etc.) de la clase `[ListObject]` para controlar la lista.

En el ejemplo dado a continuación, hemos creado el mismo `[ListObject]` utilizando la API de Aspose.Cells como lo creamos utilizando Microsoft Excel en la sección anterior.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatingListObjects.go" >}}

## **Formato de una Tabla**

Para administrar y analizar un grupo de datos relacionados, es posible convertir un rango de celdas en un objeto de lista (también conocido como una tabla de Excel). Una tabla es una serie de filas y columnas que contienen datos relacionados administrados de forma independiente de los datos en otras filas y columnas. De forma predeterminada, cada columna en la tabla tiene habilitado el filtrado en la fila del encabezado para que puedas filtrar o clasificar rápidamente tus datos del objeto de lista. Puedes agregar una fila de totales (una fila especial en una lista que proporciona una selección de funciones de agregación útiles para trabajar con datos numéricos) al objeto de lista que proporciona una lista desplegable de funciones de agregación para cada celda de la fila de totales. Aspose.Cells proporciona opciones para crear y administrar listas (o tablas).

### **Formateando un Objeto de Lista**

Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) ofrece una amplia gama de métodos para gestionar las hojas de cálculo. Para crear un *ListObject* en una hoja, usa `ListObjectCollection`. Cada `[ListObject]` es, en efecto, un objeto de la clase `ListObjectCollection`, que además proporciona el método [Add](https://reference.aspose.com/cells/go-cpp/listobjectcollection/add/) para agregar un objeto `[ListObject]` y especificar el rango de celdas que debe cubrir. Según el rango de celdas especificado, Aspose.Cells crea un *ListObject* en la hoja. Usa atributos (por ejemplo, [SetTableStyleType](https://reference.aspose.com/cells/go-cpp/listobject/settablestyletype/)) de la clase `[ListObject]` para formatear la tabla según tus requisitos.

El siguiente ejemplo agrega datos de muestra a una hoja de cálculo, agrega un `[ListObject]` y aplica estilos predeterminados. Los estilos de `[ListObject]` son compatibles con Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatTable.go" >}}
