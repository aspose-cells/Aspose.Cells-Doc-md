---
title: Exporter le CSS des feuilles de calcul séparément dans le HTML de sortie avec JavaScript via C++
linktitle: Exporter la feuille de calcul CSS séparément dans le HTML de sortie
type: docs
weight: 80
url: /fr/javascript-cpp/export-worksheet-css-separately-in-output/
description: Apprenez comment exporter le CSS de la feuille de calcul séparément lors de la conversion d’un fichier Excel en HTML en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells for JavaScript via C++ offre la fonction d’exportation du CSS des feuilles de calcul séparément lors de la conversion d’un fichier Excel en HTML. Veuillez utiliser la propriété [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--) à cette fin et la définir sur **true** pendant la sauvegarde du fichier Excel en format HTML.

## **Exporter la feuille de calcul CSS séparément dans le HTML de sortie**

Le code d'exemple suivant crée un fichier Excel, ajoute du texte dans la cellule **B5** en couleur **Rouge**, puis le sauvegarde au format HTML en utilisant la propriété [**HtmlSaveOptions.exportWorksheetCSSSeparately**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetCSSSeparately--). Consultez le [HTML de sortie](60489766.zip) généré par le code pour référence. Vous y trouverez **stylesheet.css** comme résultat du code d'exemple.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet CSS Separately Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color, Utils } = AsposeCells;

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
            // Create a new workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - export worksheet css separately
            const opts = new HtmlSaveOptions();
            opts.exportWorksheetCSSSeparately = true;

            // Save the workbook in html 
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportWorksheetCSSSeparately.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Exporter un classeur à feuille unique en HTML**

Lorsqu’un classeur contenant plusieurs feuilles est converti en HTML en utilisant Aspose.Cells for JavaScript via C++, il crée un fichier HTML ainsi qu’un dossier contenant le CSS et plusieurs fichiers HTML. En ouvrant ce fichier HTML dans un navigateur, les onglets sont visibles. Le même comportement est requis pour un classeur avec une seule feuille lorsqu'il est converti en HTML. Auparavant, aucun dossier séparé n’était créé pour les classeurs à une seule feuille, et seul un fichier HTML était généré. Un tel fichier HTML ne montre pas d’onglets lors de son ouverture dans le navigateur. MS Excel crée également un dossier correct et un HTML pour une seule feuille, et c’est pourquoi le même comportement est implémenté en utilisant les API d’Aspose.Cells. Le fichier d’échantillon peut être téléchargé depuis le lien suivant à utiliser dans le code d’exemple ci-dessous :

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, EncodingType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML save options
            const options = new HtmlSaveOptions();

            // Set optional settings (converted from setters to properties)
            options.encoding = EncodingType.UTF8;
            options.exportImagesAsBase64 = true;
            options.exportGridLines = true;
            options.exportSimilarBorderStyle = true;
            options.exportBogusRowData = true;
            options.excludeUnusedStyles = true;
            options.exportHiddenWorksheet = true;

            // Save the workbook in HTML format with specified HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSampleSingleSheet.htm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to HTML. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
