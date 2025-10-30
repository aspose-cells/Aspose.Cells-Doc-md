---
title: Configuración de bordes
description: Cómo usar la biblioteca Aspose.Cells para Python via .NET en Python para establecer el estilo y color del borde de las celdas. Al ajustar el ancho, estilo y color del borde, tendrás más control sobre la apariencia de las celdas.
keywords: Aspose.Cells para Python via .NET, Configuración del borde de la celda, Ancho del borde en Python, Estilo de borde, Color de borde
type: docs
weight: 40
url: /es/python-net/cells-border-settings/
---

## **Añadiendo Bordes a las Celdas**

Microsoft Excel permite a los usuarios formatear celdas agregando bordes. El tipo de borde depende de dónde se agrega. Por ejemplo, un borde superior es aquel agregado a la posición superior de una celda. Los usuarios también pueden modificar el estilo de línea y el color de los bordes.

Con Aspose.Cells para Python via .NET, los desarrolladores pueden agregar bordes y personalizarlos de la misma manera flexible que en Microsoft Excel.

### **Añadiendo Bordes a las Celdas**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells para Python via .NET proporciona el método [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) en la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). El método [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) se usa para establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) proporciona propiedades para agregar bordes a las celdas.

#### **Añadir bordes a una celda**

Los desarrolladores pueden añadir bordes a una celda utilizando la colección [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). El tipo de borde se pasa como un índice a la colección [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders). Todos los tipos de bordes están predefinidos en la enumeración [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).

**Enumeración de Bordes**

|**Tipos de Bordes**|**Descripción**|
| :- | :- |
|BORDER_INFERIOR|Una línea de borde inferior|
|DIAGONAL_ABAJO|Una línea diagonal de arriba a la izquierda a la derecha abajo|
|DIAGONAL_ARRIBA|Una línea diagonal de abajo a la izquierda a la parte superior derecha|
|BORDER_IZQUIERDO|Una línea de borde izquierda|
|BORDER_DERECHO|Una línea de borde derecha|
|BORDER_SUPERIOR|Una línea de borde superior|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

Para establecer el color de la línea de un borde, seleccione un color usando la enumeración Color (parte del Framework .NET) y asígnele la propiedad Color del objeto Border.

El estilo de línea del borde se establece seleccionando un estilo de línea de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)

**Enumeración de Tipo de Bordes de Celda**

|**Estilos de Línea**|**Descripción**|
| :- | :- |
|DASH_DOT|Línea delgada con puntos y guiones|
|DASH_DOT_DOT|Línea delgada con puntos, guiones y puntos|
|ESTAMPADO|Línea a trazos|
|PUNTOS|Línea punteada|
|DOBLE|Línea doble|
|PELO|Línea delgada|
|MEDIO_DASH_DOT|Línea medio guion-dot|
|MEDIO_DASH_DOT_DOT|Línea medio guion-dot-dotted|
|MEDIO_DASHED|Línea medio guion|
|NINGUNO|Sin línea|
|MEDIO|Línea media|
|DASH_DOT_INCLINADO|Línea medio guion-dot inclinada|
|GRUESO|Línea gruesa|
|DELGADO|Línea delgada|
Selecciona uno de los estilos de línea y luego asígnalo a la propiedad [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) del objeto [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

Debes configurar tanto el estilo como el color de la línea al mismo tiempo. Las dos líneas diagonales de borde deben tener el mismo estilo y color.

{{% /alert %}}

#### **Agregar bordes a un rango de celdas**

También es posible agregar bordes a un rango de celdas en lugar de solo a una celda. Para hacerlo, primero crea un rango de celdas llamando al método [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Toma los siguientes parámetros:

- Primera fila, la primera fila del rango.
- Primera columna, representa la primera columna del rango.
- Número de filas, el número de filas en el rango.
- Número de columnas, el número de columnas en el rango.

El método [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) devuelve un objeto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range), que contiene el rango de celdas especificado. El objeto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) proporciona un método [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border) que toma los siguientes parámetros para agregar un borde al rango de celdas:

- **Tipo de borde**, el tipo de borde, seleccionado de la enumeración [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) .
- **Estilo de línea**, el estilo de línea de borde, seleccionado de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) .
- **Color**, el color de línea, seleccionado de la enumeración Color.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
