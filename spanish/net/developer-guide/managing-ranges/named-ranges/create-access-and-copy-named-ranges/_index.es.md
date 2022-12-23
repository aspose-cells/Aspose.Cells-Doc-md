---
title: Crear acceso y copiar rangos con nombre
type: docs
weight: 200
url: /es/net/create-access-and-copy-named-ranges/
---
## **Introducción**

Normalmente, las etiquetas de columna y fila se utilizan para referirse a celdas individuales. Es posible crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra**nombre** puede hacer referencia a una cadena de caracteres que representa una celda, un rango de celdas, una fórmula o un valor constante. Asignar un nombre a un rango significa que se puede hacer referencia a ese rango de celdas por su nombre. Utilice nombres fáciles de entender, como Productos, para hacer referencia a rangos difíciles de entender, como Ventas!C20:C30. Las etiquetas se pueden usar en fórmulas que se refieren a datos en la misma hoja de trabajo; si desea representar un rango en otra hoja de trabajo, puede usar un nombre. *Los rangos con nombre se encuentran entre las características más poderosas de Microsoft Excel, especialmente cuando se usan como rango de origen para controles de lista, tablas dinámicas, gráficos, etc.

## **Trabajar con rango con nombre usando Microsoft Excel**

### **Crear rangos con nombre**

 Los siguientes pasos describen cómo nombrar una celda o rango de celdas usando**ms excel** . Este método se aplica a**Microsoft Oficina Excel 2003**, **Microsoft excel 97**, **2000** y**2002**.

1. Seleccione la celda, rango de celdas que desea nombrar.
1.  Haga clic en el**Nombre de Caja** en el extremo izquierdo de la barra de fórmulas.
1. Escriba el nombre de las celdas.
1. Presione ENTRAR.

{{% alert color="primary" %}}

No puede nombrar una celda mientras está cambiando el contenido de la celda.

{{% /alert %}}

## **Trabajar con rango con nombre usando Aspose.Cells**

Aquí, usamos el Aspose.Cells API para hacer la tarea.
 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación.

### **Crear rango con nombre**

 Es posible crear un rango con nombre llamando al sobrecargado[**CrearRango**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Una versión típica de[**CrearRango**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) método toma los siguientes parámetros:

- Nombre de la celda superior izquierda, el nombre de la celda superior izquierda en el rango.
- Nombre de la celda inferior derecha, el nombre de la celda inferior derecha en el rango.

 Cuando el[**CrearRango**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) se llama al método, devuelve el rango recién creado como una instancia del[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) clase. Utilizar esta[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto para configurar el rango con nombre. Por ejemplo, establezca el nombre del rango usando el[**Nombre**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) propiedad. El siguiente ejemplo muestra cómo crear un rango de celdas con nombre que se extiende sobre B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Ingrese datos en el Cells en el rango con nombre**

Puede insertar datos en las celdas individuales de un rango siguiendo el patrón

- **C#**: Rango[fila,columna]
- **VB**: Rango (fila, columna)

Supongamos que tiene un rango de celdas con nombre que abarca A1: C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales se organizan secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

Use las siguientes propiedades para identificar las celdas en el rango:

- FirstRow devuelve el índice de la primera fila en el rango con nombre.
- FirstColumn devuelve el índice de la primera columna en el rango con nombre.
- RowCount devuelve el número total de filas en el rango con nombre.
- ColumnCount devuelve el número total de columnas en el rango con nombre.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango específico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identifique Cells en el rango con nombre**

Puede insertar datos en las celdas individuales de un rango siguiendo el patrón:

- **C#**: Rango[fila,columna]
- **VB**: Rango (fila, columna)

Si tiene un rango con nombre que abarca A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales se organizan secuencialmente: Rango [0,0], Rango [0,1], Rango [0,2], Rango [1,0], Rango [1,1], Rango [1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

Use las siguientes propiedades para identificar las celdas en el rango:

- FirstRow devuelve el índice de la primera fila en el rango con nombre.
- FirstColumn devuelve el índice de la primera columna en el rango con nombre.
- RowCount devuelve el número total de filas en el rango con nombre.
- ColumnCount devuelve el número total de columnas en el rango con nombre.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango específico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Acceder a rangos con nombre**

#### **Acceder a un rango con nombre específico**

 Llama a[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) colección[**ObtenerRangoPorNombre**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) método para obtener un rango por el nombre especificado. un tipico[**ObtenerRangoPorNombre**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) El método toma el nombre del rango con nombre y devuelve el rango con nombre especificado como una instancia del[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) clase. El siguiente ejemplo muestra cómo acceder a un rango específico por su nombre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Acceda a todos los rangos con nombre en una hoja de cálculo**

 Llama a[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) colección[**ObtenerRangosNombrados**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) método para obtener todos los rangos con nombre en una hoja de cálculo. Él[**ObtenerRangosNombrados**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) método devuelve una matriz de todos los rangos de nombres en el[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) recopilación.

El siguiente ejemplo muestra cómo acceder a todos los rangos con nombre en un libro de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Copiar rangos con nombre**

 Aspose.Cells proporciona[**Rango.Copiar()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) método para copiar un rango de celdas con formato en otro rango.

El siguiente ejemplo muestra cómo copiar un rango de celdas de origen a otro rango con nombre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
