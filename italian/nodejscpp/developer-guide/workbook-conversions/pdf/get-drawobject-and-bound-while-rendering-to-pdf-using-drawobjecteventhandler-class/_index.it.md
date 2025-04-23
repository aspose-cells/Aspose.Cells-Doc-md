---
title: Ottieni DrawObject e Bound durante il rendering in PDF usando la classe DrawObjectEventHandler con Node.js via C++
linktitle: Ottieni DrawObject e Bound durante la resa in PDF utilizzando la classe DrawObjectEventHandler
type: docs
weight: 70
url: /it/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce una classe astratta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) che ha un metodo [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). L'utente può implementare [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) e utilizzare il metodo [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) per ottenere l'oggetto [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) e Bound durante il rendering di Excel in PDF o immagine. Di seguito una breve descrizione dei parametri del metodo [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) verrà inizializzato e restituito durante il rendering.

- x: Sinistra di [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- y: Sopra di [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- width: Larghezza di [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- height: Altezza di [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

Se stai esportando un file Excel in PDF, puoi utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) con [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--). Analogamente, se stai esportando un file Excel in Immagine, puoi utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) con [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--).

## **Ottieni DrawObject e Bound durante il rendering in PDF utilizzando la classe DrawObjectEventHandler**

Consulta il seguente esempio di codice. Carica il [file Excel di esempio](64716821.xlsx) e lo salva come [output PDF](64716822.pdf). Durante il rendering in PDF, utilizza la proprietà [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) e cattura il [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) e il Bound delle celle ed oggetti esistenti, ad esempio immagini. Se il tipo [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) è Cell, stampa il suo Bound e StringValue. Se il tipo [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) è Immagine, stampa il suo Bound e il nome della forma. Per maggiori dettagli, consulta l'output della console dell'esempio di codice di seguito.

## **Codice di Esempio**

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

## **Output della console**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
