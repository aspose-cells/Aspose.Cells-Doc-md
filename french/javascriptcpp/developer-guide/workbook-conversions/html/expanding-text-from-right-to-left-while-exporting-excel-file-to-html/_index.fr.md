---
title: Expansion du texte de droite à gauche lors de l exportation d un fichier Excel en HTML avec JavaScript via C++
linktitle: Expansion du texte de droite à gauche lors de l exportation d un fichier Excel vers HTML
type: docs
weight: 60
url: /fr/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}}

Aspose.Cells prend désormais en charge l'expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML. Cette fonctionnalité a été implémentée depuis la version 8.9.0.0. Désormais, si votre fichier excel source contient un texte qui s'étend de droite à gauche, Aspose.Cells l'exportera correctement vers HTML.

{{% /alert %}}
## **Expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML**
Le code d'exemple suivant convertit le [fichier excel d'exemple](5115502.xlsx) en HTML. Cette capture d'écran montre à quoi ressemble le fichier excel d'exemple dans Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Cette capture d'écran montre la [sortie HTML générée avec une ancienne version](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Cette capture d'écran montre la [sortie HTML générée avec une nouvelle version](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Comme vous pouvez le voir dans les captures d'écran, la nouvelle version expand le texte aligné à droite vers la gauche correctement, tout comme Microsoft Excel.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Expand Text From Right To Left Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // Load source excel file inside the workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get CellsHelper version (converted from getVersion())
            const version = CellsHelper.version;

            // Save workbook in html format
            const outputData = wb.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `ExpandTextFromRightToLeft_out_${version}.html`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to HTML successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
