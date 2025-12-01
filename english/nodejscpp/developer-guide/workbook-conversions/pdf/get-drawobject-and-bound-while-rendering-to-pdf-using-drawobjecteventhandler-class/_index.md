---
title: Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class with Node.js via C++
linktitle: Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class
type: docs
weight: 70
url: /nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells provides an abstract class [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) which has a [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) method. The user can implement [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) and utilize the [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) method to get the [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) and Bound while rendering Excel to PDF or Image. Here is a brief description of the parameters of the [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) method.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) will be initialized and returned when rendering.

- x: Left of [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- y: Top of [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- width: Width of [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- height: Height of [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

If you are rendering Excel file to PDF, then you can utilize [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) class with [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--). Similarly, if you are rendering Excel file to Image, you can utilize [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) class with [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--).

## **Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class**

Please see the following sample code. It loads the [sample Excel file](64716821.xlsx) and saves it as [output PDF](64716822.pdf). While rendering to PDF, it utilizes [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) property and captures the [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) and Bound of existing cells and objects e.g. images etc. If the [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) type is Cell, it prints its Bound and StringValue. And if the [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) type is Image, it prints its Bound and Shape Name. Please see the console output of the sample code given below for more help.

## **Sample Code**

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

## **Console Output**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
