---
title: Agregar y recuperar datos
type: docs
weight: 20
url: /es/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 En[Acceso a Cells de una hoja de trabajo](/cells/es/java/accessing-cells-of-a-worksheet/), discutimos enfoques básicos para acceder a las celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a las celdas.

{{% /alert %}} 
## **Agregando datos al Cells**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. Cada artículo en el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección representa un objeto de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase.

 Aspose.Cells permite a los desarrolladores agregar datos a las celdas de las hojas de cálculo llamando al[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase'[valor ajustado](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)propiedad. Al usar el[valor ajustado](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)propiedad, es posible agregar valores booleanos, de cadena, dobles, enteros o de fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Mejora de la eficiencia**
{{% alert color="primary" %}} 

 Si usas el[valor ajustado](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)propiedad para agregar una gran cantidad de datos a una hoja de trabajo, debe agregar valores a las celdas, primero por filas y luego por columnas. Este enfoque mejora en gran medida la eficiencia de sus aplicaciones.

{{% /alert %}} 

Mientras trabajan en hojas de trabajo, los usuarios pueden agregar diferentes tipos de datos en las celdas. Estos elementos de datos pueden incluir valores booleanos, enteros, de coma flotante, de texto o de fecha/hora. Puede obtener los valores apropiados de las celdas según sus tipos de datos usando Aspose.Cells.
## **Recuperando datos de Cells**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Excel.[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. Cada artículo en el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección representa un objeto de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase.

 los[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)class proporciona varias propiedades que permiten a los desarrolladores recuperar valores de las celdas según sus tipos de datos. Estas propiedades incluyen:

- [Valor de cadena](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), el valor de cadena de la celda.
- [valor doble](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), devuelve el valor doble de la celda.
- [valor bool](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), el valor booleano de la celda.
- [Valor de fecha y hora](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), el valor de fecha/hora de la celda.
- [valor flotante](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), el valor flotante de la celda.
- [valorinterno](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), el valor entero de la celda.

 Además, el tipo de datos contenidos en una celda también se puede verificar usando el[Escribe](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) propiedad de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase. De hecho, el[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase'[Escribe](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) propiedad se basa en[Tipo de valor de celda](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)enumeración cuyos valores predefinidos se enumeran a continuación:

|**Cell Tipos de valor**|**Descripción**|
|:- |:- |
|[ES_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Especifica que el valor de la celda es booleano.|
|[ES_FECHA_TIEMPO](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Especifica que el valor de la celda es fecha/hora.|
|[ES_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Representa que la celda contiene un valor de error|
|[ES NULO](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Representa una celda en blanco.|
|[ES_NUMERICO](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Especifica que el valor de la celda es numérico.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Especifica que el valor de la celda es una cadena.|
|[ES DESCONOCIDO](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Especifica que el valor de la celda es desconocido.|
También puede usar los tipos de valores de celda predefinidos anteriores para comparar con el tipo de datos presentes en cada celda.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
