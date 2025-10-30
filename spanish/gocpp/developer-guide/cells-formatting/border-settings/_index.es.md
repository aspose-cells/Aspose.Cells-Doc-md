---
title: Configuración de borde con Golang a través de C++
linktitle: Configuración de bordes
description: Cómo usar la biblioteca Aspose.Cells en C++ para establecer el estilo y color del borde de las celdas. Ajustando el grosor, estilo y color del borde, tienes mayor control sobre cómo lucen y aparecen las celdas.
keywords: Aspose.Cells, Configuración del borde de la celda, C++, Ancho del borde, Estilo del borde, Color del borde
type: docs
weight: 40
url: /es/go-cpp/cells-border-settings/
---

## **Añadiendo Bordes a las Celdas**

Microsoft Excel permite a los usuarios dar formato a las celdas agregando bordes. El tipo de borde depende de en qué posición se añada. Por ejemplo, un borde superior se añade en la posición superior de una celda. Los usuarios también pueden modificar el estilo de línea y el color de los bordes.

Con Aspose.Cells, los desarrolladores pueden agregar bordes y personalizar su aspecto de la misma manera flexible que en Microsoft Excel.

### **Añadiendo Bordes a las Celdas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells ofrece el método [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) en la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). El método [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) se usa para establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) proporciona propiedades para agregar bordes a las celdas.

#### **Añadir bordes a una celda**

Los desarrolladores pueden agregar bordes a una celda usando la colección [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) del objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/). El tipo de borde se pasa como índice a la colección [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/). Todos los tipos de borde están predefinidos en la enumeración [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).

**Enumeración de Bordes**

| **Tipos de Bordes** | **Descripción** |
|------------------|-----------------|
| BordeInferior   | Línea de borde inferior |
| DiagonalAbajo   | Línea diagonal de la esquina superior izquierda a la inferior derecha |
| DiagonalArriba  | Línea diagonal de la esquina inferior izquierda a la superior derecha |
| BordeIzquierdo | Línea de borde izquierda |
| BordeDerecho   | Línea de borde derecha |
| BordeSuperior  | Línea de borde superior |

La colección [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) almacena todos los bordes. Cada borde en la colección [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) está representado por un objeto [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) que proporciona dos propiedades, [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) y [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) para establecer el color de línea del borde y su estilo respectivamente.

Para establecer el color de línea de un borde, selecciona un color usando la enumeración Color y asígnalo a la propiedad Color del objeto Borde.

El estilo de línea del borde se establece seleccionando un estilo de línea de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).

**Enumeración de Tipo de Bordes de Celda**

| **Estilos de líneas** | **Descripción** |
|------------------------|-------------------------------|
| DashDot | Línea delgada de puntos y guiones |
| DashDotDot | Línea delgada de puntos, guiones y puntos |
| Dashed | Línea discontinuada |
| Dotted | Línea punteada |
| Double | Línea doble |
| Hair | Línea muy delgada |
| MediumDashDot | Línea de puntos y guiones de grosor medio |
| MediumDashDotDot | Línea de puntos, guiones y puntos de grosor medio |
| MediumDashed | Línea discontinuada de grosor medio |
| None | Sin línea |
| Medium | Línea de grosor medio |
| SlantedDashDot | Línea inclinada de puntos y guiones de grosor medio |
| Thick | Línea gruesa |
| Thin | Línea fina |

Seleccione uno de los estilos de línea y luego asignarlo a la propiedad [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/) del objeto [**Border**](https://reference.aspose.com/cells/go-cpp/border/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

Debe configurar tanto el estilo de línea como el color al mismo tiempo. Las dos líneas diagonales del borde deben tener el mismo estilo y color.

{{% /alert %}}

#### **Agregar bordes a un rango de celdas**

También es posible agregar bordes a un rango de celdas en lugar de solo a una celda. Para ello, primero cree un rango de celdas llamando al método [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/) de la colección [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/). Toma los siguientes parámetros:

- Primera fila, la primera fila del rango.
- Primera columna, representa la primera columna del rango.
- Número de filas, el número de filas en el rango.
- Número de columnas, el número de columnas en el rango.

El método [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/) devuelve un objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/), que contiene el rango de celdas especificado. El objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) proporciona un método [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) que toma los siguientes parámetros para agregar un borde al rango de celdas:

- **Tipo de borde**, el tipo de borde, seleccionado de la enumeración [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/).
- **Estilo de línea**, el estilo de línea del borde, seleccionado de la enumeración [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).
- **Color**, el color de línea, seleccionado de la enumeración Color.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
