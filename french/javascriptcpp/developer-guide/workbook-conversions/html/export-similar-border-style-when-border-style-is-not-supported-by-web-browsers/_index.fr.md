---
title: Exporter un style de bordure similaire lorsque le style de bordure n’est pas supporté par les navigateurs web avec JavaScript via C++  
linktitle: Exporter un style de bordure similaire lorsque le style de bordure n est pas pris en charge par les navigateurs Web  
type: docs  
weight: 70  
url: /fr/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Apprenez comment exporter les bordures non supportées par les navigateurs web lors de la conversion de fichiers Excel en HTML en utilisant Aspose.Cells for JavaScript via C++.  
---  

## **Scénarios d'utilisation possibles**  

Microsoft Excel supporte certains types de bordures en pointillé qui ne sont pas supportés par les navigateurs web. Lorsque vous convertissez un tel fichier Excel en HTML en utilisant Aspose.Cells for JavaScript via C++, ces bordures sont supprimées. Cependant, Aspose.Cells peut également supporter l’affichage de telles bordures avec la propriété [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--). Veuillez définir sa valeur à **true** et ces bordures non supportées seront également exportées dans le fichier HTML.  

## **Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web**  

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716806.xlsx) contenant certains bordures non prises en charge comme indiqué dans la capture d'écran suivante. La capture montre aussi l'effet de la propriété [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) dans le [HTML de sortie](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options - Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
