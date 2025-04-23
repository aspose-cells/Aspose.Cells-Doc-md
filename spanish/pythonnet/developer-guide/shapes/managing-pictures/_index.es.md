---
title: Gestión de imágenes
type: docs
weight: 10
url: /es/python-net/managing-pictures/
---

Aspose.Cells para Python via .NET permite a los desarrolladores agregar imágenes a las hojas de cálculo en tiempo de ejecución. Además, la posición de estas imágenes puede controlarse en tiempo de ejecución, que se discute con más detalle en las siguientes secciones.

Este artículo explica cómo agregar imágenes e insertar una imagen que muestre el contenido de ciertas celdas.

## **Añadir imágenes**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código:
Simplemente llame al método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) de la colección [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). El método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) toma los siguientes parámetros:

- **Índice de fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **Posicionamiento de imágenes**

Hay dos formas posibles de controlar la posición de las imágenes usando Aspose.Cells para Python via .NET:

- Posicionamiento proporcional: define una posición proporcional a la altura y ancho de la fila.
- Posicionamiento absoluto: define la posición exacta en la página donde se insertará la imagen, por ejemplo, 40 píxeles a la izquierda y 20 píxeles debajo del borde de la celda.

### **Posicionamiento proporcional**

Los desarrolladores pueden posicionar las imágenes proporcionalmente a la altura de la fila y al ancho de la columna utilizando las propiedades [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x) y [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y) del objeto [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). Un objeto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) se puede obtener de la colección [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) pasando su índice de imagen. Este ejemplo coloca una imagen en la celda F6.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **Posicionamiento absoluto**

Los desarrolladores también pueden posicionar las imágenes de forma absoluta utilizando las propiedades [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) y [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) del objeto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). Este ejemplo coloca una imagen en la celda F6, a 60 píxeles a la izquierda y 10 píxeles arriba de la celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **Insertar una imagen basada en referencia de celda**

Aspose.Cells para Python via .NET permite mostrar el contenido de una celda en una forma de imagen. Puedes vincular la imagen a la celda que contiene los datos que deseas mostrar. Debido a que la celda o rango de celdas está vinculado al objeto gráfico, los cambios que hagas en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico.

Añadir una imagen a la hoja de cálculo llamando al método [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Especifica el rango de celdas utilizando el atributo [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) del objeto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **Temas avanzados**
- [Agregar Iconos Condicionales Establecidos con el Texto de la Celda](/cells/es/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Insertar una imagen vinculada desde una dirección web](/cells/es/python-net/insert-a-linked-picture-from-web-address/)
- [Insertar una imagen basada en la referencia de la celda](/cells/es/python-net/insert-a-picture-based-on-cell-reference/)
- [Cargar una imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

