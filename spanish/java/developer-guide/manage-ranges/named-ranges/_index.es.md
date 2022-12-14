---
title: Rangos con nombre
type: docs
weight: 40
url: /es/java/named-ranges/
---
{{% alert color="primary" %}} 

Normalmente, las etiquetas de columna y fila se utilizan para hacer referencia a celdas individuales. Es posible crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra**nombre** puede hacer referencia a una cadena de caracteres que representa una celda, un rango de celdas, una fórmula o un valor constante. Asignar un nombre a un rango significa que se puede hacer referencia a ese rango de celdas por su nombre. Utilice nombres fáciles de entender, como Productos, para hacer referencia a rangos difíciles de entender, como Ventas!C20:C30. Las etiquetas se pueden usar en fórmulas que se refieren a datos en la misma hoja de trabajo; si desea representar un rango en otra hoja de trabajo, puede usar un nombre. *Los rangos con nombre se encuentran entre las características más poderosas de Microsoft Excel, especialmente cuando se usan como rango de origen para controles de lista, tablas dinámicas, gráficos, etc.

{{% /alert %}} 
## **Creación de un rango con nombre**
### **Usando Microsoft Excel**
Los siguientes pasos describen cómo nombrar una celda o rango de celdas usando Microsoft Excel. Este método se aplica a Microsoft Office Excel 2003, Microsoft Excel 97, 2000 y 2002.

1. Seleccione la celda, rango de celdas que desea nombrar.
1. Haga clic en el Cuadro de nombre en el extremo izquierdo de la barra de fórmulas.
1. Escriba el nombre de las celdas.
1. Presione ENTRAR.

{{% alert color="primary" %}} 

No puede nombrar una celda mientras está cambiando el contenido de la celda.

{{% /alert %}} 
### **Usando Aspose.Cells**
Aquí, usamos el Aspose.Cells API para hacer la tarea.

 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)recopilación.

 Es posible crear un rango con nombre llamando al sobrecargado[crearRango](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. Una versión típica de la[crearRango](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) método toma los siguientes parámetros:

- Nombre de la celda superior izquierda, el nombre de la celda superior izquierda en el rango.
- Nombre de la celda inferior derecha, el nombre de la celda inferior derecha en el rango.

 Cuando el[crearRango](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) se llama al método, devuelve el rango con nombre recién creado como una instancia de[Rango](https://reference.aspose.com/cells/java/com.aspose.cells/range) clase.

El siguiente ejemplo muestra cómo crear un rango de celdas con nombre que se extiende sobre B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Acceso a todos los rangos con nombre en una hoja de cálculo**
 Llama a[obtenerRangosNombrados](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) método de la[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) para obtener todos los rangos con nombre en una hoja de cálculo. los[obtenerRangosNombrados](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) devuelve una matriz de todos los rangos con nombre en el[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

El siguiente ejemplo muestra cómo acceder a todos los rangos con nombre en un libro de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Acceder a un rango con nombre específico**
 Llama a[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) colección[obtenerRangoPorNombre](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) método para obtener un rango específico por nombre. un tipico[obtenerRangoPorNombre](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) toma el nombre del rango con nombre y devuelve el rango con nombre especificado como una instancia del[Rango](https://reference.aspose.com/cells/java/com.aspose.cells/range)clase.

El siguiente ejemplo muestra cómo acceder a un rango específico por su nombre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identificar Cells en un rango con nombre**
Usando Aspose.Cells, puede insertar datos en las celdas individuales de un rango. Supongamos que tiene un rango de celdas con nombre, es decir, A1: C4. Entonces, la matriz haría 4 * 3 = 12 celdas y las celdas de rango individuales se organizan secuencialmente. Aspose.Cells le proporciona algunas propiedades útiles de la clase [Rango](https://reference.aspose.com/cells/java/com.aspose.cells/range) para acceder a las celdas individuales del rango. Puede usar los siguientes métodos para identificar las celdas en el rango:

- [obtenerPrimeraFila](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) devuelve el índice de la primera fila en el rango con nombre.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)devuelve el índice de la primera columna en el rango con nombre.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango específico.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Ingrese datos en el Cells en el rango con nombre**
Usando Aspose.Cells, puede insertar datos en las celdas individuales de un rango. Suponga que tiene un rango de celdas con nombre, es decir, H1:J4. Entonces, la matriz haría 4 * 3 = 12 celdas y las celdas de rango individuales se organizan secuencialmente. Aspose.Cells le proporciona algunas propiedades útiles de la clase [Rango](https://reference.aspose.com/cells/java/com.aspose.cells/range) para acceder a las celdas individuales del rango. Puede usar las siguientes propiedades para identificar las celdas en el rango:

- [obtenerPrimeraFila](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)devuelve el índice de la primera fila en el rango con nombre.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)devuelve el índice de la primera columna en el rango con nombre.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango específico.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Rangos de formato... Establecimiento de atributos de fuente y color de fondo en un rango con nombre**
 Para aplicar formato, defina un[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) objeto para especificar la configuración de estilo y aplicarlo al[Rango](https://reference.aspose.com/cells/java/com.aspose.cells/range)objeto.

El siguiente ejemplo muestra cómo establecer un color de relleno sólido (color de sombreado) con configuración de fuente en un rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Rangos de formato... Adición de bordes a un rango con nombre**
 Es posible agregar bordes a un rango de celdas en lugar de a una sola celda. los[Rango](https://reference.aspose.com/cells/java/com.aspose.cells/range) objeto proporciona un[establecerEsquemaFronteras](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)método que toma los siguientes parámetros para agregar un borde al rango de celdas:

-  borderStyle: el tipo de borde, seleccionado de la[Tipo de borde de celda](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)enumeración.
-  borderColor: el color de la línea del borde, seleccionado de la[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) enumeración.

El siguiente ejemplo muestra cómo establecer un borde de contorno en un rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


 El siguiente resultado se generaría después de ejecutar el código anterior:

![todo:imagen_alternativa_texto](named-ranges_1.png)
#### **Aplicar estilo a las celdas en un Rango**
A veces, desea crear aplicar un estilo a las celdas en un[Rango](https://reference.aspose.com/cells/java/com.aspose.cells/range) . Para esto, puede iterar sobre las celdas en el rango y usar el[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) para aplicar el estilo a la celda.

El siguiente ejemplo muestra cómo aplicar estilos a las celdas de un rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Eliminar un rango con nombre**
 Aspose.Cells proporciona el[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) para borrar el nombre del rango. Para borrar el contenido del rango, utilice[Cells.ClearRango()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) método.
El siguiente ejemplo muestra cómo eliminar un rango con nombre con su contenido.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


bordecolores
