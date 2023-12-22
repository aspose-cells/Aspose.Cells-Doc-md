---
title: Configuración de borde
description: Cómo utilizar la biblioteca Aspose.Cells en C# para establecer el estilo del borde y el color de las celdas. Al ajustar el ancho, el estilo y el color del borde, tiene más control sobre el aspecto y la apariencia de las celdas.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /es/net/cells-border-settings/
---
##  **Agregar bordes a Cells**

Microsoft Excel permite a los usuarios formatear celdas agregando bordes. El tipo de borde depende de dónde se agregue. Por ejemplo, un borde superior es aquel que se agrega a la posición superior de una celda. Los usuarios también pueden modificar el estilo y el color de las líneas de los bordes.

Con Aspose.Cells, los desarrolladores pueden agregar bordes y personalizar su apariencia de la misma manera flexible que en Microsoft Excel.

###  **Agregar bordes a Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Cada elemento en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Aspose.Cells proporciona la[**Obtener estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)método en el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase. El[**Establecer estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)El método se utiliza para establecer el estilo de formato de una celda. El[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona propiedades para agregar bordes a las celdas.

####  **Agregar bordes a un Cell**

Los desarrolladores pueden agregar bordes a una celda usando el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Fronteras**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) recopilación. El tipo de borde se pasa como índice del[**Fronteras**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) recopilación. Todos los tipos de borde están predefinidos en el[**Tipo de borde**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) enumeración.

**Enumeración de fronteras**

|**Tipos de borde**|**Descripción**|
| :- | :- |
|Borde inferior|Una línea fronteriza inferior|
|DiagonalAbajo|Una línea diagonal desde la parte superior izquierda hasta la parte inferior derecha.|
|DiagonalArriba|Una línea diagonal desde la parte inferior izquierda hasta la parte superior derecha.|
|Borde izquierdo|Una línea fronteriza izquierda|
|borde derecho|Una línea fronteriza derecha|
|Borde superior|Una línea fronteriza superior|

El[**Fronteras**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)La colección almacena todas las fronteras. Cada frontera en el[**Fronteras**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) colección está representada por un[**Borde**](https://reference.aspose.com/cells/net/aspose.cells/border) objeto que proporciona dos propiedades,[**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) y[**Estilo de línea**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)para establecer el color y el estilo de la línea de un borde respectivamente.

Para establecer el color de la línea de un borde, seleccione un color usando la enumeración Color (parte del marco .NET) y asígnelo a la propiedad Color del objeto Borde.

 El estilo de línea del borde se establece seleccionando un estilo de línea del menú[**Tipo de borde de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumeración.

**Enumeración CellBorderType**

|**Estilos de línea**|**Descripción**|
| :- | :- |
|Guion punto|Línea fina de puntos y trazos|
|DashPuntoPunto|Línea fina de guiones, puntos y puntos|
|discontinuo|Linea discontinua|
|Punteado|Linea punteada|
|Doble|Doble linea|
|Cabello|Línea de pelo|
|Punto de guión medio|Línea media de puntos y trazos|
|MedioDashPuntoPunto|Línea mediana de guiones, puntos y puntos|
|Medio discontinuo|Línea discontinua media|
|Ninguno|No hay línea|
|Medio|linea media|
|InclinadoDashDot|Línea de puntos y trazos medianos inclinados|
|Grueso|linea gruesa|
|Delgado|Linea fina|
Seleccione uno de los estilos de línea y luego asígnelo al[**Borde**](https://reference.aspose.com/cells/net/aspose.cells/border) objetos[**Estilo de línea**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Debes configurar tanto el estilo como el color de la línea al mismo tiempo. Las dos líneas de borde diagonales deben tener el mismo estilo y color de línea.

{{% /alert %}}

####  **Agregar bordes a un rango de Cells**

 También es posible agregar bordes a un rango de celdas en lugar de solo una celda. Para hacerlo, primero, cree un rango de celdas llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**Crear rango**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) método. Toma los siguientes parámetros:

- Primera fila, la primera fila del rango.
- Primera columna, representa la primera columna del rango.
- Número de filas, el número de filas del rango.
- Número de columnas, el número de columnas en el rango.

 El[**Crear rango**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) El método devuelve un[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto, que contiene el rango de celdas especificado. El[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto proporciona un[**Establecer ContornoBorde**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) Método que toma los siguientes parámetros para agregar un borde al rango de celdas:

-  *Tipo de borde**, el tipo de borde, seleccionado del menú[**Tipo de borde**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)enumeración.
-  *Estilo de línea**, el estilo de línea del borde, seleccionado del menú[**Tipo de borde de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumeración.
- *Color**, el color de la línea, seleccionado de la enumeración Color.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
