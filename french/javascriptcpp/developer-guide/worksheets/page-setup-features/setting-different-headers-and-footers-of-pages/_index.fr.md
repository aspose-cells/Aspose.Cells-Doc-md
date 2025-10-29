---
title: Définir différents en têtes et pieds de page pour différentes pages avec JavaScript via C++
linktitle: Définir des en têtes et des pieds de page différents pour différentes pages
type: docs
weight: 35
url: /fr/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Cet article fournit un exemple de code qui montre comment définir de manière programmatique les en têtes et pieds de page de la configuration de page de la feuille Excel en utilisant Aspose.Cells for JavaScript via C++. Définir les en têtes et pieds de page pour la première, impaire et paire pages.
keywords: définir l en tête et le pied de page d Excel pour la première page JavaScript via C++, définir l en tête et le pied de page pour les pages impaires JavaScript via C++, définir l en tête et le pied de page pour les pages paires JavaScript via C++
---

{{% alert color="primary" %}}

MS Excel supporte la définition d'en-têtes et pieds de page différents pour la première page, les pages impaires et les pages paires depuis Excel 2007.
Aspose.Cells for JavaScript via C++ supporte la même fonctionnalité.

{{% /alert %}}

## **Définir des en-têtes et des pieds de page différents dans MS Excel**

**![Définir des en-têtes et des pieds de page différents](difpage.png)**

1. Cliquez sur **Mise en page > Titres et en-têtes > En-tête/pied de page**.
1. Cochez **Différentes pages impaires et paires** ou **Première page différente**.
1. Entrez des en-têtes et pieds de page différents.

## ** Définir différents en-têtes et pieds de page avec Aspose.Cells for JavaScript via C++**

Aspose.Cells se comporte de la même manière qu'Excel.
1. Définit les indicateurs [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) et [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) 
1. Entrez des en-têtes et pieds de page différents.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
