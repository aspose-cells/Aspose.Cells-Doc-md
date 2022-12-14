---
title: Gestión de imágenes
type: docs
weight: 10
url: /es/net/managing-pictures/
---
Aspose.Cells permite a los desarrolladores agregar imágenes a hojas de cálculo en tiempo de ejecución. Además, el posicionamiento de estas imágenes se puede controlar en tiempo de ejecución, lo cual se analiza con más detalle en las próximas secciones.

Este artículo explica cómo agregar imágenes y cómo insertar una imagen que muestre el contenido de ciertas celdas.

## **Adición de imágenes**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo se necesitan unas pocas líneas de código:
 Simplemente llame al[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metodo de la[**Fotos**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) colección (encapsulada en el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objeto). los[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)método toma los siguientes parámetros:

- **Índice de la fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de la columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Imágenes de posicionamiento**

Hay dos formas posibles de controlar el posicionamiento de las imágenes usando Aspose.Cells:

- Posicionamiento proporcional: defina una posición proporcional a la altura y el ancho de la fila.
- Posicionamiento absoluto: define la posición exacta en la página donde se insertará la imagen, por ejemplo, 40 píxeles a la izquierda y 20 píxeles por debajo del borde de la celda.

### **Posicionamiento proporcional**

 Los desarrolladores pueden posicionar las imágenes proporcionalmente a la altura de la fila y el ancho de la columna usando el[**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) y[**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) propiedades de la[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) objeto. A[**Imagen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) El objeto se puede obtener de la[**Fotos**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)colección pasando su índice de imágenes. Este ejemplo coloca una imagen en la celda F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Posicionamiento absoluto**

 Los desarrolladores también pueden posicionar las imágenes de forma absoluta utilizando el[**Izquierda**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) y[**Parte superior**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) propiedades de la[**Imagen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objeto. Este ejemplo coloca una imagen en la celda F6, 60 píxeles desde la izquierda y 10 píxeles desde la parte superior de la celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Insertar una imagen basada en la referencia Cell**

Aspose.Cells le permite mostrar el contenido de una celda de la hoja de cálculo en forma de imagen. Puede vincular la imagen a la celda que contiene los datos que desea mostrar. Dado que la celda o el rango de celdas está vinculado al objeto gráfico, los cambios que realice en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico.

 Agregue una imagen a la hoja de trabajo llamando al[**Añade una foto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) metodo de la[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) colección (encapsulada en el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objeto). Especifique el rango de celdas usando el[**Fórmula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) atributo de la[**Imagen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objeto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Temas avanzados**
- [Agregar conjunto de iconos condicionales con el texto Cell](/cells/es/net/add-conditional-icons-set-with-the-cell-text/)
- [Insertar una imagen vinculada desde una dirección web](/cells/es/net/insert-a-linked-picture-from-web-address/)
- [Insertar una imagen basada en la referencia Cell](/cells/es/net/insert-a-picture-based-on-cell-reference/)
- [Cargue una imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

