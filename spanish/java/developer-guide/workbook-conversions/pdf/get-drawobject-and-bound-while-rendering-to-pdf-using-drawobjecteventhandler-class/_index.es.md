---
title: Obtener DrawObject y Bound al representar a PDF usando la clase DrawObjectEventHandler
type: docs
weight: 60
url: /es/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona una clase abstracta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) que tiene un método [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-). El usuario puede implementar [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) y utilizar el método [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) para obtener el [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) y **Bound** al renderizar Excel a PDF o imagen. Aquí hay una breve descripción de los parámetros del método [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) se inicializará y devolverá al renderizar

- x: Izquierda de [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Arriba de [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- width: Ancho de [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- height: Altura de [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Si está renderizando un archivo de Excel a PDF, entonces puede utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) con [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Del mismo modo, si está renderizando un archivo de Excel a imagen, puede utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) con [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Obtener DrawObject y Bound al representar a PDF utilizando la clase DrawObjectEventHandler**

Consulte el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](64716843.xlsx) y lo guarda como [PDF de salida](64716842.pdf). Al renderizar a PDF, utiliza la propiedad [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) y captura el [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) y **Bound** de celdas existentes y objetos, como imágenes, etc. Si el tipo de drawObject es Cell, imprime su Bound y StringValue. Y si el tipo de drawObject es Image, imprime su Bound y Nombre de forma. Consulte la salida de la consola del código de muestra a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Salida de la consola**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
