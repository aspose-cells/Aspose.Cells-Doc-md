---
title: Gestión de imágenes
type: docs
weight: 10
url: /es/net/managing-pictures/
---

Aspose.Cells permite a los desarrolladores agregar imágenes a las hojas de cálculo en tiempo de ejecución. Además, la posición de estas imágenes se puede controlar en tiempo de ejecución, lo cual se discute con más detalle en las siguientes secciones.

Este artículo explica cómo agregar imágenes e insertar una imagen que muestre el contenido de ciertas celdas.

## **Añadir imágenes**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código:
Simplemente llame al método [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) de la colección [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). El método [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) toma los siguientes parámetros:

- **Índice de fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Posicionamiento de imágenes**

Hay dos formas posibles de controlar el posicionamiento de las imágenes usando Aspose.Cells:

- Posicionamiento proporcional: define una posición proporcional a la altura y ancho de la fila.
- Posicionamiento absoluto: define la posición exacta en la página donde se insertará la imagen, por ejemplo, 40 píxeles a la izquierda y 20 píxeles debajo del borde de la celda.

### **Posicionamiento proporcional**

Los desarrolladores pueden posicionar las imágenes proporcionalmente a la altura de la fila y al ancho de la columna utilizando las propiedades [**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) y [**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) del objeto [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). Un objeto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) se puede obtener de la colección [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) pasando su índice de imagen. Este ejemplo coloca una imagen en la celda F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Posicionamiento absoluto**

Los desarrolladores también pueden posicionar las imágenes de forma absoluta utilizando las propiedades [**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) y [**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) del objeto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). Este ejemplo coloca una imagen en la celda F6, a 60 píxeles a la izquierda y 10 píxeles arriba de la celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Insertar una imagen basada en referencia de celda**

Aspose.Cells te permite mostrar el contenido de una celda de la hoja de cálculo en una forma de imagen. Puedes vincular la imagen a la celda que contiene los datos que deseas mostrar. Dado que la celda o el rango de celdas está vinculado al objeto gráfico, los cambios que realices en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico.

Añadir una imagen a la hoja de cálculo llamando al método [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Especifica el rango de celdas utilizando el atributo [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) del objeto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Temas avanzados**
- [Agregar Iconos Condicionales Establecidos con el Texto de la Celda](/cells/es/net/add-conditional-icons-set-with-the-cell-text/)
- [Insertar una imagen vinculada desde una dirección web](/cells/es/net/insert-a-linked-picture-from-web-address/)
- [Insertar una imagen basada en la referencia de la celda](/cells/es/net/insert-a-picture-based-on-cell-reference/)
- [Cargar una imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="csharp" >}}
