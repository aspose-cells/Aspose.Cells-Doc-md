---  
title: Configuración de bordes
linktitle: Configuración de bordes  
description: Cómo usar la biblioteca Aspose.Cells en Node.js vía C++ para establecer el estilo y color de los bordes de las celdas. Ajustando el ancho, estilo y color del borde, tienes más control sobre la apariencia de las celdas.  
keywords: Aspose.Cells, Configuración de Borde de Celda, Node.js vía C++, Ancho del Borde, Estilo del Borde, Color del Borde  
type: docs  
weight: 40  
url: /es/nodejs-cpp/cells-border-settings/  
---  

## **Añadiendo Bordes a las Celdas**  

Microsoft Excel permite a los usuarios dar formato a las celdas agregando bordes. El tipo de borde depende de en qué posición se añada. Por ejemplo, un borde superior se añade en la posición superior de una celda. Los usuarios también pueden modificar el estilo de línea y el color de los bordes.  

Con Aspose.Cells for Node.js via C++, los desarrolladores pueden agregar bordes y personalizarlos de la misma forma flexible que en Microsoft Excel.  

### **Añadiendo Bordes a las Celdas**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona la colección [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells ofrece el método [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) en la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). El método [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) se usa para establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) proporciona propiedades para agregar bordes a las celdas.  

#### **Añadir bordes a una celda**  

Los desarrolladores pueden agregar bordes a una celda usando la colección [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). El tipo de borde se pasa como índice a la colección [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--). Todos los tipos de borde están predefinidos en la enumeración [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  

**Enumeración de Bordes**  

|**Tipos de Bordes**|**Descripción**|  
| :- | :- |  
|BottomBorder|Una línea de borde inferior|  
|DiagonalDown|Una línea diagonal de la esquina superior izquierda a la esquina inferior derecha|  
|DiagonalUp|Una línea diagonal de la esquina inferior izquierda a la esquina superior derecha|  
|LeftBorder|Una línea de borde izquierda|  
|RightBorder|Una línea de borde derecha|  
|TopBorder|Una línea de borde superior|  

La colección [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) almacena todos los bordes. Cada borde en la colección [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) está representado por un objeto [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) que proporciona dos propiedades, [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) y [**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) para establecer el color de línea del borde y su estilo respectivamente.  

Para establecer el color de línea de un borde, selecciona un color usando la enumeración Color (parte de Node.js) y asignalo a la propiedad color del objeto Border.  

El estilo de línea del borde se establece seleccionando un estilo de línea de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  

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
Seleccione uno de los estilos de línea y luego asignarlo a la propiedad [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) del objeto [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
Debe configurar tanto el estilo de línea como el color al mismo tiempo. Las dos líneas diagonales del borde deben tener el mismo estilo y color.  
{{% /alert %}}  

#### **Agregar bordes a un rango de celdas**  

También es posible agregar bordes a un rango de celdas en lugar de solo a una celda. Para ello, primero cree un rango de celdas llamando al método [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) de la colección [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Toma los siguientes parámetros:  

- Primera fila, la primera fila del rango.  
- Primera columna, representa la primera columna del rango.  
- Número de filas, el número de filas en el rango.  
- Número de columnas, el número de columnas en el rango.  

El método [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) devuelve un objeto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range), que contiene el rango de celdas especificado. El objeto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) proporciona un método [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-) que toma los siguientes parámetros para agregar un borde al rango de celdas:  

- **Tipo de borde**, el tipo de borde, seleccionado de la enumeración [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  
- **Estilo de línea**, el estilo de línea del borde, seleccionado de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  
- **Color**, el color de línea, seleccionado de la enumeración Color.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


