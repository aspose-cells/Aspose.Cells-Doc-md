---
title: Beim Rendern nach PDF den DrawObject und Bound Status mit der DrawObjectEventHandler Klasse in Node.js via C++ abrufen
linktitle: Holen Sie sich DrawObject und Bound während des Renderns im PDF mit der DrawObjectEventHandler Klasse
type: docs
weight: 70
url: /de/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells stellt eine abstrakte Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) bereit, die eine [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) Methode hat. Der Benutzer kann [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) implementieren und die [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) Methode nutzen, um die [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) und Bound beim Rendern von Excel zu PDF oder Bild zu erhalten. Hier ist eine kurze Beschreibung der Parameter der [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) Methode.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) wird initialisiert und beim Rendern zurückgegeben.

- x: Linke Seite von [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- y: Obere Seite von [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- width: Breite von [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- height: Höhe von [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

Wenn Sie Excel-Dateien in PDF rendern, können Sie die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) mit [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) nutzen. Ebenso können Sie bei der Renderung von Excel in Bild die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) mit [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--) verwenden.

## **Holen Sie sich DrawObject und Bound beim Rendern in PDF mit der DrawObjectEventHandler-Klasse**

Siehe den folgenden Beispielcode. Es lädt die [Beispiel-Excel-Datei](64716821.xlsx) und speichert sie als [Ausgabe-PDF](64716822.pdf). Beim Rendern zu PDF nutzt es die [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) Eigenschaft und erfasst die [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) und Bound bestehender Zellen und Objekte, z.B. Bilder. Wenn der [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) Typ Cell ist, werden Bound und StringValue ausgegeben. Ist der [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) Typ Image, werden Bound und Shape-Name ausgegeben. Siehe den Konsolenausdruck des unten angegebenen Beispielcodes für mehr Hilfe.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
