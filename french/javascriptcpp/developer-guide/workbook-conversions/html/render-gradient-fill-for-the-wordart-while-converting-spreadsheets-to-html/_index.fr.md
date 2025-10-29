---
title: Rendre le remplissage en dégradé pour WordArt lors de la conversion de feuilles de calcul en HTML avec JavaScript via C++
linktitle: Rendu de remplissage dégradé pour le WordArt lors de la conversion des feuilles de calcul en HTML
type: docs
weight: 90
url: /fr/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Apprenez comment rendre le remplissage en dégradé pour WordArt lors de la conversion de feuilles de calcul en HTML en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  
Avant Aspose.Cells 17.1, Aspose.Cells ne rendait pas le remplissage en dégradé du WordArt lors de la conversion du fichier Excel en format HTML. Depuis la version 17.1, le remplissage en dégradé WordArt est supporté. La capture d'écran suivante compare l'effet du remplissage en dégradé lors de la conversion du fichier Excel avec Aspose.Cells 17.1 et la version plus ancienne.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Rendu de remplissage dégradé pour le WordArt lors de la conversion des feuilles de calcul en HTML**  
Le code d'exemple suivant convertit le [fichier Excel source](22774111.xlsx) en [format HTML de sortie](22774109.zip). Le fichier Excel source contient un objet WordArt avec remplissage en dégradé comme montré dans la capture d'écran ci-dessus.  

## **Code d'exemple**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
