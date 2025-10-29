---
title: Rendre les compléments Office lors de la conversion d Excel en PDF avec JavaScript via C++
linktitle: Rendre les Compléments Office lors de la conversion d Excel en PDF
type: docs
weight: 100
url: /fr/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells ne pouvait pas rendre les compléments Office lors de la sauvegarde d'un fichier Excel en format PDF. Maintenant, Aspose.Cells le rend correctement. Vous n'avez pas besoin d'utiliser une méthode ou propriété spéciale pour rendre les compléments Office dans le PDF de sortie. Il suffit d'enregistrer votre fichier Excel en format PDF, et il rendra les compléments Office.

## **Rendre les compléments Office lors de la conversion Excel en PDF**

Le code d'exemple suivant enregistre le [fichier Excel d'exemple](60489769.xlsx) qui contient les compléments Office. Veuillez voir le [PDF de sortie généré avec la version précédente, c’est-à-dire 17.11](60489770.pdf) et le [PDF de sortie généré avec la version plus récente, c’est-à-dire 17.12 et suivantes](60489771.pdf). Le PDF de la version précédente est vide, mais le PDF de la version plus récente montre le complément Office.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
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

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
