---
title: Cacher l affichage des valeurs zéro dans la feuille de calcul avec JavaScript via C++
linktitle: Masquer l affichage des valeurs zéro dans la feuille de calcul
type: docs
weight: 50
url: /fr/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Cet article vous montrera un exemple de code expliquant comment masquer de manière programmatique les valeurs zéro dans une feuille Excel en utilisant la bibliothèque JavaScript via C++.
keywords: masquer les valeurs zéro de la feuille Excel en JavaScript via C++
---

{{% alert color="primary" %}} 

Parfois, vous devez masquer les valeurs zéro dans une feuille de calcul. Cela peut être une préférence personnelle ou une norme de formatage.

{{% /alert %}} 

Pour masquer les valeurs zéro dans une feuille de calcul dans Microsoft Excel (par exemple Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**, puis sélectionnez l'onglet **Affichage**.
1. Désélectionnez l'option **Zéro**.
1. Cliquez sur **OK**.

Veuillez consulter le code d'exemple ci-dessous qui démontre comment masquer les zéros en utilisant Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
