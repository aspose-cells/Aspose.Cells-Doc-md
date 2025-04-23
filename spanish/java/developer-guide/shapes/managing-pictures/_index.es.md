---
title: Gestión de imágenes
type: docs
weight: 10
url: /es/java/managing-pictures/
---

Aspose.Cells permite a los desarrolladores agregar imágenes a las hojas de cálculo en tiempo de ejecución. Además, la posición de estas imágenes se puede controlar en tiempo de ejecución, lo cual se discute con más detalle en las siguientes secciones.

Este artículo explica cómo agregar imágenes e insertar una imagen que muestre el contenido de ciertas celdas.

## **Añadir imágenes**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código.

Simplemente llame al método [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-) de la colección [**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). El método [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-) toma los siguientes parámetros:

- **Índice de fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Posicionamiento de imágenes**

Las imágenes se pueden posicionar usando Aspose.Cells de la siguiente manera:

- [Posicionamiento absoluto](/cells/es/java/managing-pictures/#absolute-positioning).

### **Posicionamiento absoluto**

Los desarrolladores pueden posicionar las imágenes de forma absoluta utilizando los métodos [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) y [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) del objeto [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Temas avanzados**
- [Insertar una imagen vinculada desde una dirección web](/cells/es/java/insert-a-linked-picture-from-web-address/)
- [Insertar una imagen basada en una referencia de celda](/cells/es/java/insert-a-picture-based-on-cell-reference/)
- [Insertar imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="java" >}}
