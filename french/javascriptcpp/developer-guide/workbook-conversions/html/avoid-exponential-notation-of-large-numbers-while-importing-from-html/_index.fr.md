---
title: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML
linktitle: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML
type: docs
weight: 10
url: /fr/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Apprenez à empêcher la conversion des grands nombres en notation exponentielle lors de l importation à partir de HTML en utilisant Aspose.Cells for JavaScript via C++.
--- 

{{% alert color="primary" %}}  

Parfois, votre HTML contient des nombres comme 1234567890123456, qui font plus de 15 chiffres, et lorsque vous importez votre HTML dans un fichier Excel, ces nombres se convertissent en notation exponentielle comme 1.23457E+15. Si vous souhaitez que votre nombre soit importé tel quel et non converti en notation exponentielle, veuillez utiliser la propriété [**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--) et la définir à **true** lors du chargement de votre HTML.  

{{% /alert %}}  

Le code d'exemple suivant explique l'utilisation de la propriété [**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--). L'API importera le nombre tel quel sans le convertir en notation exponentielle.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            // Sample Html containing large number with digits greater than 15
            const html = "<html><body><p>1234567890123456</p></body></html>";

            // Convert Html to byte array
            const byteArray = new TextEncoder().encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.keepPrecision = true;

            // Convert byte array into stream
            const stream = byteArray;

            // Create workbook from stream with Html load options
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAvoidExponentialNotationWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```
