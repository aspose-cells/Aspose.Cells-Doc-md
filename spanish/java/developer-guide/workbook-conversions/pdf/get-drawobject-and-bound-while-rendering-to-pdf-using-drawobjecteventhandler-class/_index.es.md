---
title: Obtenga DrawObject y Bound mientras renderiza a PDF usando la clase DrawObjectEventHandler
type: docs
weight: 60
url: /es/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Posibles escenarios de uso**

Aspose.Cells proporciona una clase abstracta[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) que tiene un[**dibujar()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) método. El usuario puede implementar[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)y utilizar el[**dibujar()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) método para obtener el[**DibujarObjeto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)y**Ligado**mientras renderiza Excel a PDF o Imagen. Aquí hay una breve descripción de los parámetros del[**dibujar()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) método.

-  dibujarObjeto:[**DibujarObjeto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)se inicializará y devolverá al renderizar

- x: A la izquierda de[**DibujarObjeto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Parte superior de[**DibujarObjeto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- ancho: Ancho de[**DibujarObjeto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- altura: Altura de[**DibujarObjeto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Si está procesando un archivo de Excel en PDF, puede utilizar[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)clase con[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Del mismo modo, si está procesando un archivo de Excel en una imagen, puede utilizar[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)clase con[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Obtenga DrawObject y Bound mientras renderiza a Pdf usando la clase DrawObjectEventHandler**

Consulte el siguiente código de ejemplo. carga el[ejemplo de archivo de Excel](64716843.xlsx)y lo guarda como[salida PDF](64716842.pdf). Mientras se renderiza a PDF, utiliza[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)propiedad y captura la[**DibujarObjeto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) y**Ligado**de celdas y objetos existentes, por ejemplo, imágenes, etc. Si el tipo drawObject es Cell, imprime su Bound y StringValue. Y si el tipo de objeto de dibujo es Imagen, imprime su Nombre de forma y límite. Consulte la salida de la consola del código de muestra que se proporciona a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
