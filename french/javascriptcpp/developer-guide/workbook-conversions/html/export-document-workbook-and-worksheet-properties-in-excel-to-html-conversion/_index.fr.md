---
title: Exporter les propriétés du document, du classeur et de la feuille de calcul lors de la conversion d’Excel en HTML avec JavaScript via C++
linktitle: Exporter les propriétés du classeur et des feuilles de calcul du document en Excel vers la conversion HTML
type: docs
weight: 50
url: /fr/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Apprenez comment exporter les propriétés du document, du classeur et de la feuille de calcul dans Excel vers HTML en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

Lorsque un fichier Excel de Microsoft est exporté en HTML en utilisant Microsoft Excel ou Aspose.Cells for JavaScript via C++, il exporte également divers types de propriétés de Document, Classeur et Feuille de calcul comme montré dans la capture d'écran suivante. Vous pouvez éviter d’exporter ces propriétés en réglant [**HtmlSaveOptions.exportDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportDocumentProperties--), [**HtmlSaveOptions.exportWorkbookProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorkbookProperties--) et [**HtmlSaveOptions.exportWorksheetProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetProperties--) sur **false**. La valeur par défaut de ces propriétés est **true**. La capture d'écran suivante montre à quoi ressemblent ces propriétés dans le HTML exporté.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Exporter les propriétés du Document, du Classeur et des Feuilles de calcul lors de la conversion d'Excel en HTML**  

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767776.xlsx) et le convertit en HTML sans exporter les propriétés du document, du classeur et de la feuille de calcul dans le [HTML de sortie](61767779.zip).  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export HTML without Properties</title>
    </head>
    <body>
        <h1>Export Excel to HTML (without document/workbook/worksheet properties)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Load the sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // We do not want to export document, workbook and worksheet properties
            options.exportDocumentProperties = false;
            options.exportWorkbookProperties = false;
            options.exportWorksheetProperties = false;

            // Export the Excel file to Html with Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
