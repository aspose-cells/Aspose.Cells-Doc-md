---
title: Obtenez DrawObject et Bound lors du rendu en PDF en utilisant la classe DrawObjectEventHandler avec Node.js via C++
linktitle: Obtenez DrawObject et Bound lors du rendu au format PDF en utilisant la classe DrawObjectEventHandler
type: docs
weight: 70
url: /fr/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit une classe abstraite [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) qui dispose d'une méthode [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). L'utilisateur peut implémenter [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) et utiliser la méthode [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) pour obtenir le [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) et la limite lors du rendu d'Excel en PDF ou en image. Voici une brève description des paramètres de la méthode [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject : [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) sera initialisé et renvoyé lors du rendu.

- x : Gauche de [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- y : Haut de [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- width : Largeur de [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- height : Hauteur de [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

Si vous rendez un fichier Excel en PDF, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) avec [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--). De même, si vous rendez un fichier Excel en image, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) avec [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--).

## **Obtenir DrawObject et Bound lors du rendu au format PDF en utilisant la classe DrawObjectEventHandler**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](64716821.xlsx) et le sauvegarde en tant que [PDF de sortie](64716822.pdf). Lors du rendu en PDF, il utilise la propriété [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) et capture le [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) et la limite des cellules et objets existants, par exemple des images, etc. Si le type [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) est Cell, il affiche sa limite et sa valeur en chaîne. Et si le type [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) est Image, il affiche sa limite et le nom de sa forme. Veuillez consulter la sortie console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

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

## **Sortie console**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
