---
title: Agregar y recuperar datos
type: docs
weight: 20
url: /es/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 En[Acceso a Cells de una hoja de trabajo](/cells/es/cpp/accessing-cells-of-a-worksheet/), discutimos enfoques básicos para acceder a las celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a las celdas.

{{% /alert %}} 
## **Agregando datos al Cells**
 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. Él[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[IHojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Él[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la clase proporciona una[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) recopilación. Cada artículo en el[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección representa un objeto de la[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)clase.

Aspose.Cells permite a los desarrolladores agregar datos a las celdas de las hojas de trabajo llamando al[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) clase[poner valor](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) método. Aspose.Cells proporciona versiones sobrecargadas del[poner valor](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) método que permite a los desarrolladores agregar diferentes tipos de datos a las celdas. Usando estas versiones sobrecargadas del[poner valor](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)método, es posible agregar valores booleanos, de cadena, dobles, enteros o de fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **Mejora de la eficiencia**
 Si utiliza[poner valor](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)método para poner una gran cantidad de datos en una hoja de trabajo, debe agregar valores a las celdas, primero por filas y luego por columnas. Este enfoque mejora en gran medida la eficiencia de sus aplicaciones.
## **Recuperando datos de Cells**
 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. Él[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[IHojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) colección que permite el acceso a las hojas de trabajo en el archivo. Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Él[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la clase proporciona un[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) recopilación. Cada artículo en el[ICélulas](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección representa un objeto de la[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)clase.

 Él[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)class proporciona varios métodos que permiten a los desarrolladores recuperar valores de las celdas según sus tipos de datos. Estos métodos incluyen:

- [ObtenerValorDeCadena](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3), devuelve el valor de cadena de la celda.
- [ObtenerValorDoble](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a), devuelve el doble valor de la celda.
- [ObtenerValorBool](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741), devuelve el valor booleano de la celda.
- [ObtenerValorFechaHora](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61), devuelve el valor de fecha/hora de la celda.
- [Obtener valor flotante](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44), devuelve el valor flotante de la celda.
- [ObtenerValorInt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8), devuelve el valor entero de la celda.

 Cuando un campo no está lleno, las celdas con[ObtenerValorDoble](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) o[Obtener valor flotante](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)lanza una excepción.

 El tipo de datos contenidos en una celda también se puede verificar usando el[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) clase[ObtenerTipo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) método. De hecho, el[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) clase[ObtenerTipo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) método se basa en la[Tipo de valor de celda](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)enumeración cuyos valores predefinidos se enumeran a continuación:

|**Cell Tipos de valor**|**Descripción**|
|:- |:- |
|CellValueType_IsBool|Especifica que el valor de la celda es booleano.|
|CellValueType_IsDateTime|Especifica que el valor de la celda es fecha/hora.|
|CellValueType_IsNull|Representa una celda en blanco.|
|CellValueType_IsNumeric|Especifica que el valor de la celda es numérico.|
|CellValueType_IsString|Especifica que el valor de la celda es una cadena.|
|CellValueType_IsUnknown|Especifica que el valor de la celda es desconocido.|
También puede usar los tipos de valores de celda predefinidos anteriores para comparar con el Tipo de los datos presentes en cada celda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
