---
title: Calcul des fonctions MINIFS et MAXIFS d Excel 2016 avec JavaScript via C++
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer les fonctions MINIFS et MAXIFS dans Microsoft Excel 2016 en utilisant JavaScript via C++. Charger un fichier Excel existant ou en créer un nouveau, puis utiliser les méthodes Aspose.Cells pour calculer ces fonctions et enregistrer les résultats sur le disque.
keywords: Aspose.Cells, Excel, 2016, fonction MINIFS, fonction MAXIFS, calcul JavaScript via C++
type: docs
weight: 300
url: /fr/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Scénarios d'utilisation possibles**
Microsoft Excel 2016 supporte les fonctions MINIFS et MAXIFS. Ces fonctions ne sont pas supportées dans Excel 2013 ou les versions antérieures. Aspose.Cells for JavaScript via C++ supporte également le calcul de ces fonctions. La capture d'écran suivante illustre l’utilisation de ces fonctions. Veuillez lire les commentaires en rouge dans la capture pour savoir comment ces fonctions fonctionnent.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcul des fonctions MINIFS et MAXIFS d'Excel 2016**
Le code d'exemple suivant charge le [fichier Excel d'exemple](5115149.xlsx) et appelle la méthode [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) pour effectuer le calcul de formule via Aspose.Cells for JavaScript via C++, puis sauvegarde les résultats dans le [fichier PDF de sortie](5115154.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
