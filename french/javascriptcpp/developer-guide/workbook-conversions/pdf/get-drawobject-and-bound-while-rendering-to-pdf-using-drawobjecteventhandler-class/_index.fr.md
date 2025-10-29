---
title: Obtenir DrawObject et Bound lors du rendu en PDF en utilisant la classe DrawObjectEventHandler avec JavaScript via C++
linktitle: Obtenez DrawObject et Bound lors du rendu au format PDF en utilisant la classe DrawObjectEventHandler
type: docs
weight: 70
url: /fr/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit une classe abstraite [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) qui dispose d'une méthode [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). L'utilisateur peut implémenter [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) et utiliser la méthode [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) pour obtenir le [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) et la limite lors du rendu d'Excel en PDF ou en image. Voici une brève description des paramètres de la méthode [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject : [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) sera initialisé et renvoyé lors du rendu.

- x : Gauche de [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- y : Haut de [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- width : Largeur de [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- height : Hauteur de [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

Si vous convertissez un fichier Excel en PDF, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) avec la propriété [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--). De même, si vous convertissez un fichier Excel en image, vous pouvez utiliser la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) avec la propriété [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--).

## **Obtenir DrawObject et Bound lors du rendu au format PDF en utilisant la classe DrawObjectEventHandler**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](64716821.xlsx) et le sauvegarde en tant que [PDF de sortie](64716822.pdf). Lors du rendu en PDF, il utilise la propriété [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) et capture le [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) et la limite des cellules et objets existants, par exemple des images, etc. Si le type [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) est Cell, il affiche sa limite et sa valeur en chaîne. Et si le type [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) est Image, il affiche sa limite et le nom de sa forme. Veuillez consulter la sortie console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Get Draw Object and Bound Using DrawObjectEventHandler</title>
    </head>
    <body>
        <h1>Get Draw Object and Bound Using DrawObjectEventHandler</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, DrawObjectEventHandler, DrawObjectEnum } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        class ClsDrawObjectEventHandler extends DrawObjectEventHandler {
            draw(drawObject, x, y, width, height) {
                console.log("");

                // Print the coordinates and the value of Cell object
                if (drawObject.type === DrawObjectEnum.Cell) {
                    console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Cell Value]: ${drawObject.cell.stringValue}`);
                }

                // Print the coordinates and the shape name of Image object
                if (drawObject.type === DrawObjectEnum.Image) {
                    console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Shape Name]: ${drawObject.shape.name}`);
                }

                console.log("----------------------");
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Pdf save options
            const opts = new PdfSaveOptions();

            // Assign the instance of DrawObjectEventHandler class
            opts.drawObjectEventHandler = new ClsDrawObjectEventHandler();

            // Save to Pdf format with Pdf save options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **Sortie console**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
