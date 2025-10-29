---
title: Travailler avec l effet d ombre de la forme ou du graphique avec JavaScript via C++
linktitle: Travailler avec l effet d ombre de la forme ou du graphique
type: docs
weight: 220
url: /fr/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Apprenez comment travailler avec l effet d ombre des formes ou des graphiques en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  
Aspose.Cells for JavaScript via C++ fournit la propriété [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) ainsi que la classe [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) pour travailler avec l'effet d'ombre d'une forme ou d'un graphique. La classe [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) contient les propriétés suivantes qui peuvent être définies pour obtenir différents résultats selon les besoins de l'application.  

- [ShadowEffect.angle](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [ShadowEffect.blur](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [ShadowEffect.color](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [ShadowEffect.distance](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [ShadowEffect.presetType](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [ShadowEffect.size](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [Effet d'ombre.transparence](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **Travailler avec l'effet d'ombre de la forme ou du graphique**  
Le code d’échantillon suivant charge le [fichier Excel source](5115425.xlsx) et accède à la première forme dans la première feuille de calcul, puis règle les sous-propriétés de la propriété [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) et enregistre ensuite le classeur dans le [fichier Excel de sortie](5115411.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
