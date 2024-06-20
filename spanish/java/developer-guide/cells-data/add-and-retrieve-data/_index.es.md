---
title: Agregar y recuperar datos
type: docs
weight: 20
url: /es/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

En [Acceso a celdas de una hoja de cálculo](/cells/es/java/accessing-cells-of-a-worksheet/), se discutieron enfoques básicos para acceder a las celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a las celdas.

{{% /alert %}} 
## **Añadir datos a las celdas**
Aspose.Cells proporciona una clase, [Libro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Microsoft Excel. La clase [Libro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [Colección de Hojas de Cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Hoja de Cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Hoja de Cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección de [Celdas](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Cada elemento en la colección de [Celdas](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) representa un objeto de la clase [Celda](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).

Aspose.Cells permite a los desarrolladores agregar datos a las celdas en hojas de cálculo llamando a la propiedad [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) de la clase [Celda](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Utilizando la propiedad [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value), es posible agregar valores booleanos, de cadena, dobles, enteros o de fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Mejorando la eficiencia**
{{% alert color="primary" %}} 

Si utiliza la propiedad [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) para agregar una gran cantidad de datos a una hoja de cálculo, debe agregar valores a las celdas, primero por filas y luego por columnas. Este enfoque mejora considerablemente la eficiencia de sus aplicaciones.

{{% /alert %}} 

Mientras se trabaja en hojas de cálculo, los usuarios pueden agregar diferentes tipos de datos en las celdas. Estos elementos de datos pueden incluir valores booleanos, enteros, de punto flotante, de texto o de fecha/hora. Puede obtener los valores apropiados de las celdas de acuerdo con sus tipos de datos utilizando Aspose.Cells.
## **Recuperación de datos de celdas**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Cada elemento en la colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) representa un objeto de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

La clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) proporciona varias propiedades que permiten a los desarrolladores recuperar valores de las celdas de acuerdo a sus tipos de datos. Estas propiedades incluyen:

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), el valor de cadena de la celda.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), devuelve el valor doble de la celda.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), el valor booleano de la celda.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), el valor de fecha/hora de la celda.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), el valor de tipo float de la celda.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), el valor entero de la celda.

Además, el tipo de datos contenido en una celda también se puede consultar usando la propiedad [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). De hecho, la propiedad [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell) de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) está basada en la enumeración [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType) cuyos valores predefinidos se enumeran a continuación:

|**Tipos de Valor de Celda**|**Descripción**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Especifica que el valor de la celda es Booleano.|
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Especifica que el valor de la celda es fecha/hora.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Representa que la celda contiene un valor de error|
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Representa una celda en blanco.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Especifica que el valor de la celda es numérico.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Especifica que el valor de la celda es una cadena.|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Especifica que el valor de la celda es desconocido.|
También puedes usar los tipos de valor predefinidos de celda anteriores para comparar con el tipo de datos presente en cada celda.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
