---
title: Rotation du texte avec la forme à l’intérieur de la feuille de calcul en utilisant JavaScript via C++
linktitle: Faire pivoter le texte avec la forme à l intérieur de la feuille de calcul
type: docs
weight: 1300
url: /fr/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Apprenez comment faire pivoter le texte avec la forme à l’intérieur d’une feuille Excel en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajouter du texte à l’intérieur de toute forme en utilisant Microsoft Excel. Si vous ajoutez une forme avec l’ancienne version Microsoft Excel 2003, alors le texte ne pivotera pas avec la forme. Mais si vous ajoutez une forme en utilisant des versions plus récentes de Microsoft Excel, par exemple 2007, 2010, 2013 ou 2016, etc., alors le texte pivotera avec la forme. Vous pouvez contrôler si le texte doit pivoter avec la forme ou non en utilisant la propriété [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--). Sa valeur par défaut est **true**, ce qui signifie que le texte pivote avec la forme, mais si vous la définissez comme **false**, le texte ne pivote pas avec la forme.

## **Faire pivoter le texte avec la forme à l'intérieur de la feuille de calcul**

Le code exemple suivant charge le [fichier Excel d'exemple](64716896.xlsx) qui possède une forme triangulaire dont le texte tourne avec la forme. Si vous ouvrez le fichier Excel dans Microsoft Excel et que vous faites pivoter la forme triangulaire, le texte tournera également avec. Le code définit ensuite la propriété [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--) sur **false** et l’enregistre sous le nom de [fichier Excel de sortie](64716897.xlsx). Si vous ouvrez maintenant le fichier Excel de sortie dans Microsoft Excel et faites pivoter la forme triangulaire, le texte ne tournera plus avec. Veuillez voir la capture d'écran suivante illustrant l'effet du code sur le fichier Excel d'exemple à titre de référence.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
