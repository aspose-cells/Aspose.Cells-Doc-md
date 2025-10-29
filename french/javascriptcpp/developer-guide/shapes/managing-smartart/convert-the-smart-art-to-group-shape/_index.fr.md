---
title: Convertir l art intelligent en forme de groupe avec JavaScript via C++
linktitle: Convertir l Art Smart en une Forme de Groupe
type: docs
weight: 200
url: /fr/javascript-cpp/convert-the-smart-art-to-group-shape/
---

## **Scénarios d'utilisation possibles**

Vous pouvez convertir une forme d'art intelligent en forme de groupe en utilisant la méthode [**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--). Cela vous permettra de traiter la forme d'art intelligent comme une forme de groupe. Par conséquent, vous aurez accès aux parties ou formes individuelles du groupe.

## **Convertir l'Art Smart en une Forme de Groupe**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541793.xlsx) contenant une forme d'art intelligent comme illustré dans cette capture d'écran. Il convertit ensuite la forme d'art intelligent en forme de groupe et affiche la propriété Shape.isGroup. Veuillez voir la sortie de la console du code d'exemple ci-dessous.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Result Of SmartArt</title>
    </head>
    <body>
        <h1>Get Result Of SmartArt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (property access, not method)
            const isSmartArt = shape.isSmartArt;

            // Determine if shape is group shape (property access)
            const isGroup = shape.isGroup;

            // Convert smart art shape into group shape result and check if group (getResultOfSmartArt -> resultOfSmartArt property)
            const resultOfSmartArtIsGroup = shape.resultOfSmartArt.isGroup;

            const html = [
                `<p>Is Smart Art Shape: ${isSmartArt}</p>`,
                `<p>Is Group Shape: ${isGroup}</p>`,
                `<p>Result of SmartArt is Group: ${resultOfSmartArtIsGroup}</p>`
            ].join('');

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Sortie console**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
