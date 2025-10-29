---
title: Définir la largeur de colonne en unités évolutives telles que em ou pourcentage avec JavaScript via C++
linktitle: Définir la largeur de la colonne en unité évolutive comme em ou pourcentage
type: docs
weight: 130
url: /fr/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Apprenez comment définir la largeur des colonnes en unités évolutives comme em ou pourcentage dans Aspose.Cells for JavaScript via C++. Améliorez la présentation des tableaux HTML générés.
---

Générer un fichier HTML à partir d'une feuille de calcul est très courant. La taille des colonnes est définie en "pt," ce qui fonctionne dans de nombreux cas. Cependant, il peut arriver que cette taille fixe ne soit pas souhaitée. Par exemple, si la largeur du panneau conteneur est de 600px, où cette page HTML s’affiche, vous pouvez obtenir une barre de défilement horizontale si la largeur du tableau généré est plus grande. Il était nécessaire que cette taille fixe soit remplacée par une unité évolutive comme em ou pourcentage pour une meilleure présentation. Le code d'exemple suivant peut être utilisé où [**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--) est défini à **true** pour créer une largeur évolutive.

Le fichier source d'exemple et les fichiers de sortie peuvent être téléchargés à partir des liens suivants:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
