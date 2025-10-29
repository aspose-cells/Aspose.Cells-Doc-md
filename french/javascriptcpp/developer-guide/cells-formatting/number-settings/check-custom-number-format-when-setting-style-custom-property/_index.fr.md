---
title: Vérifier le format de nombre personnalisé lors du réglage de Style.Custom Property
linktitle: Vérifier le format de nombre personnalisé lors du réglage de Style.Custom Property
description: Aspose.Cells est une bibliothèque JavaScript pour travailler avec des fichiers de tableur, qui supporte la vérification des formats de nombres personnalisés lors de la mise en forme. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour vérifier les formats de nombres personnalisés afin de garantir que la mise en forme est correcte.
keywords: Aspose.Cells, bibliothèques JavaScript, feuilles de calcul, mise en forme, formatage de nombres personnalisés, vérification, validation
type: docs
weight: 170
url: /fr/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Scénarios d'utilisation possibles**

Si vous assignez un format de nombre personnalisé invalide à la propriété [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-), alors Aspose.Cells for JavaScript via C++ ne renverra aucune exception. Mais si vous voulez que Aspose.Cells vérifie si le format de nombre personnalisé assigné est valide ou non, veuillez définir la propriété [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) sur **true**.

## **Vérifier le format de nombre personnalisé lors de la définition de la propriété Style.custom**

Le code d'exemple suivant assigne un format de nombre personnalisé invalide à la propriété [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-). Étant donné que nous avons déjà défini la propriété [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) sur **true**, une exception sera levée, par exemple Format de numéro invalide. Veuillez lire les commentaires dans le code pour plus d’aide.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
