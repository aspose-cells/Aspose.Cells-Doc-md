---
title: Obtenga DrawObject y Bound mientras renderiza a PDF usando la clase DrawObjectEventHandler
type: docs
weight: 70
url: /es/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Posibles escenarios de uso**

 Aspose.Cells proporciona una clase abstracta[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) que tiene un[**Dibujar()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)método. El usuario puede implementar[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) y utilizar el[**Dibujar()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) método para obtener el[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)y Encuadernado al renderizar Excel a PDF o Imagen. Aquí hay una breve descripción de los parámetros del[**Dibujar()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)método.

-  dibujarObjeto:[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) se inicializará y devolverá al renderizar

- x: A la izquierda de[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Parte superior de[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- ancho: Ancho de[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- altura: Altura de[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Si está procesando un archivo de Excel a PDF, entonces puede utilizar[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)clase con[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) . Del mismo modo, si está procesando un archivo de Excel en una imagen, puede utilizar[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)clase con[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Obtenga DrawObject y Bound mientras renderiza a Pdf usando la clase DrawObjectEventHandler**

 Consulte el siguiente código de ejemplo. carga el[ejemplo de archivo de Excel](64716821.xlsx) y lo guarda como[PDF de salida](64716822.pdf). Mientras se renderiza a PDF, utiliza[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)propiedad y captura la[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) y Límite de celdas y objetos existentes, por ejemplo, imágenes, etc. Si el[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) el tipo es Cell, imprime su Bound y StringValue. y si el[**DibujarObjeto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)tipo es Imagen, imprime su Encuadernado y Nombre de forma. Consulte la salida de la consola del código de muestra que se proporciona a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
