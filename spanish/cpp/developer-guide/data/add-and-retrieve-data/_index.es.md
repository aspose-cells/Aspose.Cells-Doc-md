---
title: Agregar y recuperar datos
type: docs
weight: 20
url: /es/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 En[Accediendo al Cells de una hoja de trabajo](/cells/es/cpp/accessing-cells-of-a-worksheet/), discutimos enfoques básicos para acceder a las celdas en una hoja de trabajo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a las celdas.

{{% /alert %}} 
##  **Agregar datos a Cells**
 Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase proporciona una[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) recopilación. Cada elemento en el[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) colección representa un objeto de la[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)clase.

 Aspose.Cells permite a los desarrolladores agregar datos a las celdas de las hojas de trabajo llamando al[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) clase[Poner valor](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) método. Aspose.Cells proporciona versiones sobrecargadas del[Poner valor](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) Método que permite a los desarrolladores agregar diferentes tipos de datos a las celdas. Usando estas versiones sobrecargadas del[Poner valor](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)método, es posible agregar valores booleanos, de cadena, dobles, enteros o de fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **Mejorando la eficiencia**
 Si utiliza[Poner valor](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)Para poner una gran cantidad de datos en una hoja de cálculo, debes agregar valores a las celdas, primero por filas y luego por columnas. Este enfoque mejora enormemente la eficiencia de sus aplicaciones.
##  **Recuperando datos de Cells**
 Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) colección que permite el acceso a las hojas de trabajo del archivo. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase proporciona un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) recopilación. Cada elemento en el[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) colección representa un objeto de la[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)clase.

 El[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)La clase proporciona varios métodos que permiten a los desarrolladores recuperar valores de las celdas según sus tipos de datos. Estos métodos incluyen:

- [Obtener valor de cadena](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), devuelve el valor de cadena de la celda.
- [ObtenerValorDoble](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), devuelve el valor doble de la celda.
- [Obtener valor bool](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), devuelve el valor booleano de la celda.
- [ObtenerFechaHoraValor](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), devuelve el valor de fecha/hora de la celda.
- [Obtener valor flotante](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), devuelve el valor flotante de la celda.
- [ObtenerValorInt](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)devuelve el valor entero de la celda.

 Cuando un campo no está lleno, las celdas con[ObtenerValorDoble](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) o[Obtener valor flotante](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)lanza una excepción.

 El tipo de datos contenidos en una celda también se puede verificar usando el[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) clase[Obtener tipo](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) método. De hecho, el[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) clase[Obtener tipo](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) método se basa en la[Tipo de valor de celda](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)enumeración cuyos valores predefinidos se enumeran a continuación:

|**Cell Tipos de valor**|**Descripción**|
| :- | :- |
|CellValueType_IsBool|Especifica que el valor de la celda es booleano.|
|CellValueType_IsDateTime|Especifica que el valor de la celda es fecha/hora.|
|CellValueType_IsNull|Representa una celda en blanco.|
|CellValueType_IsNumeric|Especifica que el valor de la celda es numérico.|
|CellValueType_IsString|Especifica que el valor de la celda es una cadena.|
|CellValueType_IsUnknown|Especifica que el valor de la celda es desconocido.|
También puede utilizar los tipos de valores de celda predefinidos anteriores para comparar con el tipo de datos presentes en cada celda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
