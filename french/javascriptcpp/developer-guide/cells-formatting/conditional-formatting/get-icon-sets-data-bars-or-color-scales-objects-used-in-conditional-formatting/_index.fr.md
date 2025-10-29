---
title: Obtenir des objets d ensembles d icônes, de barres de données ou d échelles de couleurs utilisés dans la mise en forme conditionnelle
linktitle: Obtenir des objets d ensembles d icônes, de barres de données ou d échelles de couleurs utilisés dans la mise en forme conditionnelle
description: Apprenez comment utiliser Aspose.Cells for JavaScript via C++ pour récupérer les ensembles d icônes, les barres de données et les objets de dégradé de couleurs dans le cadre du formatage conditionnel à partir de fichiers de feuille de calcul.
keywords: Aspose.Cells, Formatage Conditionnel, Ensemble d Icônes, Barre de Données, Échelle de Couleurs, Feuille de Calcul, JavaScript via C++
type: docs
weight: 10
url: /fr/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}}  

Parfois, vous devez récupérer des ensembles d'icônes utilisés dans la mise en forme conditionnelle d'une cellule ou d'une plage de cellules et vous voulez créer un fichier image basé sur celui-ci. Vous pourriez avoir besoin de lire les barres de données ou les échelles de couleurs utilisées dans la mise en forme conditionnelle. Aspose.Cells prend en charge cette fonctionnalité.

{{% /alert %}}  

L'exemple de code suivant montre comment lire les ensembles d'icônes utilisés pour la mise en forme conditionnelle. Avec l'API simple d'Aspose.Cells, les données d'image de l'ensemble d'icônes sont enregistrées en tant qu'image.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Extract Conditional Formatting Icon</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const fileInput = document.getElementById('fileInput');
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon and create a downloadable blob
            const imageData = icon.imageData;
            const blob = new Blob([imageData], { type: 'image/jpeg' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Icon Image';

            resultEl.innerHTML = '<p style="color: green;">Icon image extracted. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
