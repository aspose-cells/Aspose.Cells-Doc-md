---
title: Gestión de imágenes
type: docs
weight: 10
url: /es/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells permite a los desarrolladores agregar imágenes a hojas de cálculo en tiempo de ejecución. Además, el posicionamiento de estas imágenes se puede controlar en tiempo de ejecución, lo cual se analiza con más detalle en las próximas secciones.

Aspose.Cells for Java solo admite formatos de imagen: BMP, JPEG, PNG, GIF.

Los índices utilizados en los ejemplos comienzan desde 0.

{{% /alert %}}

## **Adición de imágenes**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo se necesitan unas pocas líneas de código.

 Simplemente llame al[**agregar**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) ) método de la[**Fotos**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) colección (encapsulada en el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objeto). Él[**agregar**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) método toma los siguientes parámetros:

- **Índice de la fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de la columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Posicionamiento de Imágenes**

Las imágenes se pueden colocar usando Aspose.Cells de la siguiente manera:

- [Posicionamiento absoluto](/cells/es/java/managing-pictures/#absolute-positioning).

### **Posicionamiento absoluto**

 Los desarrolladores pueden posicionar las imágenes absolutamente usando el[**establecerUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) y[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) métodos de la[**Fotografía**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objeto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Temas avanzados**
- [Insertar una imagen vinculada desde una dirección web](/cells/es/java/insert-a-linked-picture-from-web-address/)
- [Insertar una imagen basada en la referencia Cell](/cells/es/java/insert-a-picture-based-on-cell-reference/)
- [Insertar imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
