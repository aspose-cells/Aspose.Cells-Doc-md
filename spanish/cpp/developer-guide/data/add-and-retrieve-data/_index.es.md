---
title: Agregar y recuperar datos
type: docs
weight: 20
url: /es/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

En [Accediendo a Celdas de una Hoja de Cálculo](/cells/es/cpp/accediendo-a-celdas-de-una-hoja-de-calculo/), discutimos enfoques básicos para acceder a celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a celdas.

{{% /alert %}} 
## **Añadir datos a las celdas**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Excel de Microsoft. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección de [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Cada elemento en la colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representa un objeto de la clase [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)

Aspose.Cells permite a los desarrolladores agregar datos a las celdas en hojas de cálculo llamando al método [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) de la clase [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Aspose.Cells proporciona versiones sobrecargadas del método [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) que permite a los desarrolladores agregar diferentes tipos de datos a las celdas. Utilizando estas versiones sobrecargadas del método [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/), es posible agregar valores booleanos, de cadena, dobles, enteros o fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **Mejorando la eficiencia**
Si usas el método [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) para agregar una gran cantidad de datos a una hoja de cálculo, debes agregar valores a las celdas primero por filas y luego por columnas. Este enfoque mejora enormemente la eficiencia de tus aplicaciones.
## **Recuperación de datos de celdas**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección de [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a las hojas de cálculo en el archivo. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Cada elemento de la colección [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representa un objeto de la clase [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La clase [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) proporciona varios métodos que permiten a los desarrolladores recuperar valores de las celdas de acuerdo a sus tipos de datos. Estos métodos incluyen:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), devuelve el valor de cadena de la celda.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), devuelve el valor doble de la celda.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), devuelve el valor booleano de la celda.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), devuelve el valor de fecha/hora de la celda.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), devuelve el valor flotante de la celda.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/), devuelve el valor entero de la celda.

Cuando un campo no está lleno, las celdas con [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) o [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) lanzan una excepción.

El tipo de datos contenido en una celda también se puede verificar utilizando el método [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) de la clase [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). De hecho, el método [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) de la clase [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) se basa en la enumeración [CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) cuyos valores predefinidos se enumeran a continuación:

|**Tipos de Valor de Celda**|**Descripción**|
| :- | :- |
|CellValueType_IsBool|Especifica que el valor de la celda es Booleano.|
|CellValueType_IsDateTime|Especifica que el valor de la celda es fecha/hora.|
|CellValueType_IsNull|Representa una celda en blanco.|
|CellValueType_IsNumeric|Especifica que el valor de la celda es numérico.|
|CellValueType_IsString|Especifica que el valor de la celda es de cadena.|
|CellValueType_IsUnknown|Especifica que el valor de la celda es desconocido.
También puedes usar los tipos de valor de celda predefinidos anteriores para comparar con el tipo de dato presente en cada celda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
