---
title: Obtener DrawObject y Bound al representar a PDF usando la clase DrawObjectEventHandler
type: docs
weight: 70
url: /es/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona una clase abstracta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) que tiene un método [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw). El usuario puede implementar [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) y utilizar el método [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) para obtener el [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) y Bound mientras se representa Excel a PDF o Imagen. Aquí tienes una breve descripción de los parámetros del método [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) se inicializará y se devolverá al representar

- x: Izquierda de [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Arriba de [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- width: Ancho de [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- height: Altura de [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Si estás representando un archivo de Excel a PDF, puedes utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) con [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler). De manera similar, si estás representando un archivo de Excel a Imagen, puedes utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) con [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Obtener DrawObject y Bound al representar a PDF utilizando la clase DrawObjectEventHandler**

Por favor, consulte el siguiente código de muestra. Carga el [archivo de Excel de muestra](64716821.xlsx) y lo guarda como [PDF de salida](64716822.pdf). Mientras se renderiza a PDF, utiliza la propiedad [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) y captura el [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) y Bound de las celdas y objetos existentes, por ejemplo, imágenes, etc. Si el tipo [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) es Celda, imprime su Bound y StringValue. Y si el tipo [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) es Imagen, imprime su Bound y nombre de forma. Consulte la salida de consola del código de muestra que se muestra a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
