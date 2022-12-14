---
title: Configuración de borde
type: docs
weight: 40
url: /es/net/cells-border-settings/
---
## **Adición de bordes a Cells**

Microsoft Excel permite a los usuarios formatear celdas agregando bordes. El tipo de borde depende de dónde se agregue. Por ejemplo, un borde superior es uno que se agrega a la posición superior de una celda. Los usuarios también pueden modificar el estilo y el color de las líneas de los bordes.

Con Aspose.Cells, los desarrolladores pueden agregar bordes y personalizar su apariencia de la misma forma flexible que en Microsoft Excel.

### **Adición de bordes a Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la clase proporciona la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Aspose.Cells proporciona el[**ObtenerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)método en el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase. los[**EstablecerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)El método se utiliza para establecer el estilo de formato de una celda. los[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona propiedades para agregar bordes a las celdas.

#### **Adición de bordes a un Cell**

Los desarrolladores pueden agregar bordes a una celda usando el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Fronteras**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) recopilación. El tipo de borde se pasa como un índice al[**Fronteras**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) recopilación. Todos los tipos de borde están predefinidos en el[**Tipo de borde**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) enumeración.

**enumeración de fronteras**

|**Tipos de borde**|**Descripción**|
|:- |:- |
|Borde inferior|Una línea de borde inferior|
|DiagonalAbajo|Una línea diagonal desde la parte superior izquierda hasta la parte inferior derecha|
|DiagonalArriba|Una línea diagonal desde abajo a la izquierda hasta arriba a la derecha|
|Borde izquierdo|Una línea de borde izquierda|
|borde derecho|Una línea de borde derecho|
|Borde superior|Una línea de borde superior|

los[**Fronteras**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)tiendas de colección todas las fronteras. Cada borde en el[**Fronteras**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) colección está representada por un[**Borde**](https://reference.aspose.com/cells/net/aspose.cells/border) objeto que proporciona dos propiedades,[**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) y[**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)para establecer el color y el estilo de línea de un borde, respectivamente.

Para establecer el color de línea de un borde, seleccione un color usando la enumeración Color (parte del Marco .NET) y asígnelo a la propiedad Color del objeto Borde.

 El estilo de línea del borde se establece seleccionando un estilo de línea de la[**Tipo de borde de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumeración.

**Enumeración CellBorderType**

|**Estilos de línea**|**Descripción**|
|:- |:- |
|Guion punto|Línea delgada de puntos y guiones|
|guiónpuntopunto|Línea delgada de puntos y guiones|
|punteado|Linea discontinua|
|Punteado|Linea punteada|
|Doble|Doble linea|
|Pelo|Línea de pelo|
|Medio Guión Punto|Línea de puntos y guiones medianos|
|Medio Guión Punto Punto|Línea mediana de puntos y guiones|
|medio punteado|Línea discontinua mediana|
|Ninguna|No hay línea|
|Medio|línea media|
|InclinadoGuiónPunto|Línea de puntos y guiones medianos inclinados|
|Grueso|línea gruesa|
|Delgada|Linea fina|
Seleccione uno de los estilos de línea y luego asígnelo al[**Borde**](https://reference.aspose.com/cells/net/aspose.cells/border) objetos[**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Debe configurar el estilo de línea y el color al mismo tiempo. Las dos líneas de borde diagonales deben tener el mismo estilo y color de línea.

{{% /alert %}}

#### **Adición de bordes a un rango de Cells**

También es posible agregar bordes a un rango de celdas en lugar de solo a una sola celda. Para hacerlo, primero, cree un rango de celdas llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**CrearRango**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) método. Toma los siguientes parámetros:

- Primera fila, la primera fila del rango.
- Primera columna, representa la primera columna del rango.
- Número de filas, el número de filas en el rango.
- Número de columnas, el número de columnas en el rango.

 los[**CrearRango**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) método devuelve un[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto, que contiene el rango especificado de celdas. los[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto proporciona un[**EstablecerEsquemaBorde**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) método que toma los siguientes parámetros para agregar un borde al rango de celdas:

- **Tipo de borde** , el tipo de borde, seleccionado de la[**Tipo de borde**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)enumeración.
- **Estilo de línea** , el estilo de línea de borde, seleccionado de la[**Tipo de borde de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)enumeración.
- **Color**, el color de la línea, seleccionado de la enumeración Color.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **colores y paleta**

Una paleta es el número de colores disponibles para usar en la creación de una imagen. El uso de una paleta estandarizada en una presentación le permite al usuario crear una apariencia consistente. Cada archivo Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.

Con Aspose.Cells es posible no solo usar los colores existentes de la paleta sino también colores personalizados. Antes de usar un color personalizado, agréguelo primero a la paleta.

Este tema trata sobre cómo agregar colores personalizados a la paleta.

### **Adición de colores personalizados a la paleta**

Aspose.Cells es compatible con la paleta de 56 colores de Microsoft de Excel. Para usar un color personalizado que no está definido en la paleta, agregue el color a la paleta.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase proporciona un[**CambiarPaleta**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) método que toma los siguientes parámetros para agregar un color personalizado para modificar la paleta:

- Color personalizado, el color personalizado que se agregará.
- Índice, el índice del color en la paleta que reemplazará el color personalizado. Debe estar entre 0-55.

El siguiente ejemplo agrega un color personalizado (Orquídea) a la paleta antes de aplicarlo en una fuente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Entonces, cuando cambie la paleta, tenga mucho cuidado. Además, esta es la limitación en el formato de archivo XLS (Excel 97 - 2003), ya que no existe tal limitación para XLSX u otros formatos de archivo avanzados de MS Excel (2007/2010 o 2013).

{{% /alert %}}


