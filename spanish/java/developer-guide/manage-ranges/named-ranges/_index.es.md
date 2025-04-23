---
title: Rangos Nombrados
type: docs
weight: 40
url: /es/java/named-ranges/
---

{{% alert color="primary" %}} 

Normalmente, las etiquetas de columnas y filas se utilizan para hacer referencia a celdas individuales. Es posible crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra **nombre** puede referirse a una cadena de caracteres que representa una celda, un rango de celdas, una fórmula o un valor constante. Asignar un nombre a un rango significa que ese rango de celdas puede ser referido por su nombre. Utilice nombres fáciles de entender, como Productos, para referirse a rangos difíciles de entender, como Ventas!C20:C30. Las etiquetas pueden ser utilizadas en fórmulas que hacen referencia a datos en la misma hoja de cálculo. Si desea representar un rango en otra hoja de cálculo, puede usar un nombre. *Los rangos nombrados son una de las características más potentes de Microsoft Excel, especialmente cuando se utilizan como el rango de origen para controles de lista, tablas dinámicas, gráficos, etc.

{{% /alert %}} 
## **Creando un Rango Nombrado**
### **Usar Microsoft Excel**
Los siguientes pasos describen cómo nombrar una celda o rango de celdas utilizando Microsoft Excel. Este método se aplica a Microsoft Office Excel 2003, Microsoft Excel 97, 2000 y 2002.

1. Selecciona la celda o rango de celdas que deseas nombrar.
1. Haz clic en el Cuadro de Nombre al final izquierdo de la barra de fórmulas.
1. Escribe el nombre para las celdas.
1. Presiona ENTER.

{{% alert color="primary" %}} 

No puedes nombrar una celda mientras estás cambiando el contenido de la celda.

{{% /alert %}} 
### **Usar Aspose.Cells**
Aquí, usamos la API de Aspose.Cells para realizar la tarea.

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

Es posible crear un rango con nombre llamando al método sobrecargado [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) de la colección [Cells](https://reference.aspose.com/cells/java/com/aspose.cells/Cells). Una versión típica del método [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) acepta los siguientes parámetros:

- Nombre de la celda superior izquierda, el nombre de la celda superior izquierda en el rango.
- Nombre de la celda inferior derecha, el nombre de la celda inferior derecha en el rango.

Cuando se llama al método [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) , devuelve el rango con nombre recién creado como una instancia de la clase [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

El siguiente ejemplo muestra cómo crear un rango nombrado de celdas que se extiende sobre B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Accediendo a Todos los Rangos Nombrados en una Hoja de Cálculo**
Llame al método [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) de la [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) para obtener todos los rangos con nombre en una hoja de cálculo. El método [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) devuelve un arreglo de todos los rangos con nombre en la [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

El siguiente ejemplo muestra cómo acceder a todos los rangos nombrados en un libro de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Acceder a un Rango Nombrado Específico**
Llame al método [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) de la colección [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) para obtener un rango especificado por nombre. El método [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) típico toma el nombre del rango con nombre y devuelve el rango especificado como una instancia de la clase [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

El siguiente ejemplo muestra cómo acceder a un rango especificado por su nombre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identificar Celdas en un Rango Nombrado**
Usando Aspose.Cells, puede insertar datos en las celdas individuales de un rango. Supongamos que tiene un rango nombrado de celdas, es decir, A1:C4. Entonces, la matriz haría 4 * 3 = 12 celdas y las celdas de rango individuales se organizan secuencialmente. Aspose.Cells le proporciona algunas propiedades útiles de la clase [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) para acceder a las celdas individuales en el rango. Puede usar los siguientes métodos para identificar las celdas en el rango:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) devuelve el índice de la primera fila en el rango nombrado.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) devuelve el índice de la primera columna en el rango nombrado.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango especificado.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Ingresar Datos en las Celdas en el Rango Nombrado**
Usando Aspose.Cells, puede insertar datos en las celdas individuales de un rango. Supongamos que tiene un rango nombrado de celdas, es decir, H1:J4. Entonces, la matriz haría 4 * 3 = 12 celdas y las celdas de rango individuales se organizan secuencialmente. Aspose.Cells le proporciona algunas propiedades útiles de la clase [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) para acceder a las celdas individuales en el rango. Puede usar las siguientes propiedades para identificar las celdas en el rango:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) devuelve el índice de la primera fila en el rango nombrado.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) devuelve el índice de la primera columna en el rango nombrado.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango especificado.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Formato de Rangos...Configurar Color de Fondo y Atributos de Fuente a un Rango Nombrado**
Para aplicar formato, defina un objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) para especificar la configuración de estilo y aplíquelo al objeto [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

El siguiente ejemplo muestra cómo configurar un color de relleno sólido (color de sombreado) con ajustes de fuente a un rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Formato Rangos...Añadir Bordes a un Rango Nombrado**
Es posible agregar bordes a un rango de celdas en lugar de solo una celda. El objeto [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) proporciona un método [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) que acepta los siguientes parámetros para agregar un borde al rango de celdas:

- borderStyle: el tipo de borde, seleccionado de la enumeración [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- borderColor: el color de la línea del borde, seleccionado de la enumeración [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

El siguiente ejemplo muestra cómo establecer un borde de contorno en un rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


La siguiente salida se generaría después de ejecutar el código anterior: 

![todo:image_alt_text](named-ranges_1.png)
#### **Aplicar estilo a las celdas en un rango**
A veces, desea crear y aplicar un estilo a las celdas en un [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range). Para ello, puede iterar sobre las celdas en el rango y usar el método [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) para aplicar el estilo a la celda.

El siguiente ejemplo muestra cómo aplicar estilos a las celdas en un Rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Eliminar un Rango Nombrado**
Aspose.Cells proporciona el método [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt-int-) para eliminar el nombre del rango. Para borrar el contenido del rango, utilice el método [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange-com.aspose.cells.CellArea-) .
El siguiente ejemplo muestra cómo eliminar un rango nombrado con su contenido.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
{{< app/cells/assistant language="java" >}}
