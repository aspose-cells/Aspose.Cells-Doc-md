---
title: Travailler avec l effet de lueur d une forme ou d un graphique avec JavaScript via C++
linktitle: Travailler avec l effet de lueur de la forme ou du graphique
type: docs
weight: 240
url: /fr/javascript-cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Apprenez comment travailler avec l effet de lueur des formes ou graphiques en JavaScript en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  
Aspose.Cells fournit la propriété [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) ainsi que la classe [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) pour travailler avec l'effet de lueur d'une forme ou d'un graphique. La classe [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) contient les propriétés suivantes pouvant être réglées pour obtenir différents résultats selon les besoins de l'application.  

- [GlowEffect.taille](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#size--)  
- [GlowEffect.transparence](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#transparency--)  
- [GlowEffect.couleur](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#color--)  

## **Travailler avec l'effet de lueur de la forme ou du graphique**  
 Le code d'exemple suivant charge le [fichier Excel source](5115407.xlsx), accède à la première forme dans la première feuille et configure les sous-propriétés de la propriété [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) avant d'enregistrer le classeur dans [fichier Excel de sortie](5115414.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Glow Effect</title>
    </head>
    <body>
        <h1>Apply Glow Effect to First Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Apply Glow Effect</button>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the glow effect of the shape, Set its Size and Transparency properties
            const glowEffect = shape.glow;
            glowEffect.size = 30;
            glowEffect.transparency = 0.4;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Glow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
