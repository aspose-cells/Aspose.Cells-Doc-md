---
title: Obtener DrawObject y Bound mientras se renderiza a PDF usando la clase DrawObjectEventHandler con Node.js a través de C++
linktitle: Obtener DrawObject y Bound al representar a PDF usando la clase DrawObjectEventHandler
type: docs
weight: 70
url: /es/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona una clase abstracta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) que tiene un método [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). El usuario puede implementar [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) y utilizar el método [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) para obtener el [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) y el Bound mientras renderiza Excel a PDF o Imagen. Aquí hay una breve descripción de los parámetros del método [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) será inicializado y devuelto cuando se renderice.

- x: Izquierda de [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- y: Superior de [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- ancho: Ancho de [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- altura: Altura de [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

Si está renderizando un archivo Excel a PDF, entonces puede utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) con [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--). De manera similar, si está renderizando un archivo Excel a Imagen, puede utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) con [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--).

## **Obtenga DrawObject y Bound al renderizar a PDF utilizando la clase DrawObjectEventHandler**

Por favor, vea el siguiente código de ejemplo. Carga el [archivo Excel de ejemplo](64716821.xlsx) y lo guarda como [PDF de salida](64716822.pdf). Mientras renderiza a PDF, utiliza la propiedad [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) y captura el [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) y Bound de celdas y objetos existentes, por ejemplo, imágenes, etc. Si el tipo [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) es Celda, imprime su Bound y StringValue. Y si el tipo [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) es Imagen, imprime su Bound y Nombre de Forma. Por favor, vea la salida de consola del código de ejemplo a continuación para más ayuda.

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");

class ClsDrawObjectEventHandler extends AsposeCells.DrawObjectEventHandler {
draw(drawObject, x, y, width, height) {
console.log("");

// Print the coordinates and the value of Cell object
if (drawObject.getType() === AsposeCells.DrawObjectEnum.Cell) {
console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Cell Value]: ${drawObject.getCell().getStringValue()}`);
}

// Print the coordinates and the shape name of Image object
if (drawObject.getType() === AsposeCells.DrawObjectEnum.Image) {
console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Shape Name]: ${drawObject.getShape().getName()}`);
}

console.log("----------------------");
}
}

async function run() {
// Load sample Excel file
const workbook = new AsposeCells.Workbook("sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");

// Specify Pdf save options
const opts = new AsposeCells.PdfSaveOptions();

// Assign the instance of DrawObjectEventHandler class
opts.setDrawObjectEventHandler(new ClsDrawObjectEventHandler());

// Save to Pdf format with Pdf save options
await workbook.saveAsync("outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

run();
```

## **Salida de la consola**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
