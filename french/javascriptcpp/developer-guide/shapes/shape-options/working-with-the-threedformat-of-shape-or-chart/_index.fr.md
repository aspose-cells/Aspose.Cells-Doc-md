---
title: Travailler avec le ThreeDFormat de Shape ou Chart avec JavaScript via C++
linktitle: Travailler avec le ThreeDFormat de la forme ou du graphique
type: docs
weight: 250
url: /fr/javascript-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells for JavaScript via C++ fournit la propriété [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) ainsi que la classe [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) pour travailler avec le format 3D d'une forme ou d'un graphique. La classe [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) contient différentes propriétés qui peuvent être définies pour obtenir différents résultats selon les besoins de l’application.

## **Travailler avec le ThreeDFormat de la forme ou du graphique**
Le code d’échantillon suivant charge le [fichier Excel source](5115419.xlsx) et accède à la première forme dans la première feuille de calcul, puis règle les sous-propriétés de la propriété [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) et enregistre ensuite le classeur dans le [fichier Excel de sortie](5115410.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Apply 3D Format Example</title>
    </head>
    <body>
        <h1>Apply 3D Format to Shape</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const ws = workbook.worksheets.get(0);

            const sh = ws.shapes.get(0);

            const n3df = sh.threeDFormat;
            n3df.contourWidth = 17;
            n3df.extrusionHeight = 32;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">3D formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
