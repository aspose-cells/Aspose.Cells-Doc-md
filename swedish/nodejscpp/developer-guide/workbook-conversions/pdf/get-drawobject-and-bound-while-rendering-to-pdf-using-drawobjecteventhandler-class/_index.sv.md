---
title: Hämta DrawObject och Bound vid rendering till PDF med hjälp av DrawObjectEventHandler klass med Node.js via C++
linktitle: Hämta DrawObject och Bound vid rendering till PDF med hjälp av DrawObjectEventHandler klassen
type: docs
weight: 70
url: /sv/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller en abstrakt klass [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) som har en [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) metod. Användaren kan implementera [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) och använda [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) metoden för att få [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) och Bound under rendering av Excel till PDF eller Bild. Här är en kort beskrivning av parametrarna för [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) metoden.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) kommer att initialiseras och returneras vid rendering.

- x: Vänster om [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- y: Toppen av [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- width: Bredden på [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- height: Höjden på [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

Om du renderar Excel-fil till PDF kan du använda [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) klassen med [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--). På samma sätt, om du renderar Excel-fil till Bild, kan du använda [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) klassen med [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--).

## **Hämta DrawObject och gräns vid rendering till PDF med hjälp av DrawObjectEventHandler-klassen**

Se följande exempel på kod. Den laddar [exempel Excel-fil](64716821.xlsx) och sparar den som [utdata PDF](64716822.pdf). Vid rendering till PDF använder den [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) egenskapen och fångar [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) och Bound av befintliga celler och objekt, t.ex. bilder. Om [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)-typen är Cell, skriver den ut dess Bound och StringValue. Om [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)-typen är Image, skriver den ut dess Bound och Shapes namn. Se konsolutdata för exemplet nedan för mer hjälp.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
