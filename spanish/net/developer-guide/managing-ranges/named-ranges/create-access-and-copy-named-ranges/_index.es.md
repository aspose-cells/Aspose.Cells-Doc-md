---
title: Crear y copiar rangos con nombre
type: docs
weight: 200
url: /es/net/create-access-and-copy-named-ranges/
---

## **Introducción**

Normalmente, las etiquetas de columna y fila se utilizan para referirse a celdas individuales. Es posible crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra **nombre** puede referirse a una cadena de caracteres que representa una celda, rango de celdas, fórmula o valor constante. Asignar un nombre a un rango significa que ese rango de celdas puede ser referido por su nombre. Utilice nombres fáciles de entender, como Productos, para referirse a rangos difíciles de comprender, como Ventas!C20:C30. Las etiquetas se pueden utilizar en fórmulas que hacen referencia a datos en la misma hoja de cálculo; si desea representar un rango en otra hoja de cálculo, puede usar un nombre. *Los rangos con nombre son una de las características más potentes de Microsoft Excel, especialmente cuando se usan como el rango de origen para controles de lista, tablas dinámicas, gráficos, etc.*

## **Trabajar con Rangos con Nombre Usando Microsoft Excel**

### **Crear Rangos con Nombre**

Los siguientes pasos describen cómo nombrar una celda o un rango de celdas usando **MS Excel**. Este método se aplica a **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** y **2002**.

1. Selecciona la celda o rango de celdas que deseas nombrar.
1. Haga clic en la **Caja de Nombre** en el extremo izquierdo de la barra de fórmulas.
1. Escribe el nombre para las celdas.
1. Presiona ENTER.

{{% alert color="primary" %}}

No puedes nombrar una celda mientras estás cambiando el contenido de la celda.

{{% /alert %}}

## **Trabajar con Rangos con Nombre Usando Aspose.Cells**

Aquí, usamos la API de Aspose.Cells para realizar la tarea.
Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite el acceso a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

### **Crear Rango con Nombre**

Es posible crear un rango con nombre llamando al método sobrecargado [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Una versión típica del método [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) toma los siguientes parámetros:

- Nombre de la celda superior izquierda, el nombre de la celda superior izquierda en el rango.
- Nombre de la celda inferior derecha, el nombre de la celda inferior derecha en el rango.

Cuando se llama al método [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3), devuelve el rango recién creado como una instancia de la clase [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Utilice este objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) para configurar el rango con nombre. Por ejemplo, establezca el nombre del rango utilizando la propiedad [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name). El siguiente ejemplo muestra cómo crear un rango con nombre de celdas que se extiende sobre B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Ingresar Datos en las Celdas en el Rango Nombrado**

Puede insertar datos en las celdas individuales de un rango siguiendo el patrón

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Supongamos que tienes un rango de celdas que abarca de A1 a C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales están dispuestas secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

Utiliza las siguientes propiedades para identificar las celdas en el rango:

- FirstRow devuelve el índice de la primera fila en el rango con nombre.
- FirstColumn devuelve el índice de la primera columna en el rango con nombre.
- RowCount devuelve el número total de filas en el rango con nombre.
- ColumnCount devuelve el número total de columnas en el rango con nombre.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango especificado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identificar Celdas en el Rango con Nombre**

Puedes insertar datos en las celdas individuales de un rango siguiendo el patrón:

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Si tienes un rango con nombre que abarca de A1 a C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales están dispuestas secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].

Utiliza las siguientes propiedades para identificar las celdas en el rango:

- FirstRow devuelve el índice de la primera fila en el rango con nombre.
- FirstColumn devuelve el índice de la primera columna en el rango con nombre.
- RowCount devuelve el número total de filas en el rango con nombre.
- ColumnCount devuelve el número total de columnas en el rango con nombre.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango especificado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Acceder a rangos con nombres**

#### **Acceder a un Rango Nombrado Específico**

Llame al método [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) de la colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) para obtener un rango por el nombre especificado. Un método [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) típico toma el nombre del rango con nombre y devuelve el rango con nombre especificado como una instancia de la clase [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). El siguiente ejemplo muestra cómo acceder a un rango especificado por su nombre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Acceder a todos los rangos con nombres en una hoja de cálculo**

Llame al método [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) de la colección [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) para obtener todos los rangos con nombres en una hoja de cálculo. El método [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) devuelve un array de todos los rangos con nombres en la colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)

El siguiente ejemplo muestra cómo acceder a todos los rangos nombrados en un libro de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Copiar rangos con nombres**

Aspose.Cells proporciona el método [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) para copiar un rango de celdas con formato en otro rango.

El siguiente ejemplo muestra cómo copiar un rango de celdas fuente en otro rango con nombre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
