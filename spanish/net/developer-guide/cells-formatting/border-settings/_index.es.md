---
title: Configuración de bordes
description: Cómo usar la biblioteca Aspose.Cells en C# para establecer el estilo y color del borde de las celdas. Al ajustar el ancho, estilo y color del borde, se tiene un mayor control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Configuración de bordes de celda, C#, Ancho del borde, Estilo de borde, Color del borde
type: docs
weight: 40
url: /es/net/cells-border-settings/
---

## **Añadiendo Bordes a las Celdas**

Microsoft Excel permite a los usuarios formatear celdas agregando bordes. El tipo de borde depende de dónde se agrega. Por ejemplo, un borde superior es aquel agregado a la posición superior de una celda. Los usuarios también pueden modificar el estilo de línea y el color de los bordes.

Con Aspose.Cells, los desarrolladores pueden agregar bordes y personalizar su aspecto de la misma manera flexible que en Microsoft Excel.

### **Añadiendo Bordes a las Celdas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección de [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells proporciona el método [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) en la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). El método [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) se utiliza para establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) proporciona propiedades para añadir bordes a las celdas.

#### **Añadir bordes a una celda**

Los desarrolladores pueden añadir bordes a una celda utilizando la colección [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). El tipo de borde se pasa como un índice a la colección [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders). Todos los tipos de bordes están predefinidos en la enumeración [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).

**Enumeración de Bordes**

|**Tipos de Bordes**|**Descripción**|
| :- | :- |
|BottomBorder|Una línea de borde inferior|
|DiagonalDown|Una línea diagonal de la esquina superior izquierda a la esquina inferior derecha|
|DiagonalUp|Una línea diagonal de la esquina inferior izquierda a la esquina superior derecha|
|LeftBorder|Una línea de borde izquierda|
|RightBorder|Una línea de borde derecha|
|TopBorder|Una línea de borde superior|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

Para establecer el color de la línea de un borde, seleccione un color usando la enumeración Color (parte del Framework .NET) y asígnele la propiedad Color del objeto Border.

El estilo de línea del borde se establece seleccionando un estilo de línea de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)

**Enumeración de Tipo de Bordes de Celda**

|**Estilos de Línea**|**Descripción**|
| :- | :- |
|DashDot|Línea fina con guiones y puntos|
|DashDotDot|Línea fina con guiones y puntos y puntos|
|Dashed|Línea discontinua|
|Dotted|Línea punteada|
|Double|Línea doble|
|Hair|Línea fina|
|MediumDashDot|Línea medianamente punteada|
|MediumDashDotDot|Línea mediana punto-punteada|
|MediumDashed|Línea mediana punteada|
|None|Sin línea|
|Medium|Línea mediana|
|SlantedDashDot|Línea oblicua medianamente punteada|
|Thick|Línea gruesa|
|Thin|Línea delgada|
Selecciona uno de los estilos de línea y luego asígnalo a la propiedad [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) del objeto [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Debes configurar tanto el estilo como el color de la línea al mismo tiempo. Las dos líneas diagonales de borde deben tener el mismo estilo y color.

{{% /alert %}}

#### **Agregar bordes a un rango de celdas**

También es posible agregar bordes a un rango de celdas en lugar de solo a una celda. Para hacerlo, primero crea un rango de celdas llamando al método [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Toma los siguientes parámetros:

- Primera fila, la primera fila del rango.
- Primera columna, representa la primera columna del rango.
- Número de filas, el número de filas en el rango.
- Número de columnas, el número de columnas en el rango.

El método [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) devuelve un objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range), que contiene el rango de celdas especificado. El objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) proporciona un método [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) que toma los siguientes parámetros para agregar un borde al rango de celdas:

- **Tipo de borde**, el tipo de borde, seleccionado de la enumeración [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) .
- **Estilo de línea**, el estilo de línea de borde, seleccionado de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) .
- **Color**, el color de línea, seleccionado de la enumeración Color.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
