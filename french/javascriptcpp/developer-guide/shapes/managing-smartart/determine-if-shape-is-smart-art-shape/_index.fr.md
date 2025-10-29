---
title: Déterminer si une forme est une forme d art intelligent avec JavaScript via C++
linktitle: Déterminer si la forme est une forme de l Art Smart
type: docs
weight: 400
url: /fr/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Apprenez comment déterminer si une forme dans Excel est une forme d art intelligent en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

Les formes d'art intelligent sont des formes spéciales dans Microsoft Excel qui permettent de créer automatiquement des diagrammes complexes. Vous pouvez vérifier si la forme est une forme d'art intelligent ou une forme normale en utilisant la propriété [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--).  

## **Déterminer si la forme est une forme de l'Art Smart**  

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541792.xlsx) contenant une forme d'art intelligent comme illustré dans cette capture d'écran. Il affiche ensuite la valeur de la propriété [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) de la première forme. Veuillez voir la sortie de la console du code d'exemple ci-dessous.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **Sortie console**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
