---
title: Masquer le contenu superposé avec CrossHideRight lors de la sauvegarde en HTML avec JavaScript via C++
linktitle: Masquer le contenu superposé avec CrossHideRight lors de l enregistrement en HTML
type: docs
weight: 100
url: /fr/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez spécifier différents types de croisement pour les chaînes de cellules. Par défaut, Aspose.Cells génère le HTML selon Microsoft Excel, mais si vous changez le type de croisement en [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype), il cachera toutes les chaînes situées à droite de la cellule qui sont superposées ou chevauchantes avec la chaîne de la cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement en HTML**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716894.xlsx) et le sauvegarde en [HTML de sortie](64716893.zip) après avoir défini le [**HtmlSaveOptions.htmlCrossStringType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#htmlCrossStringType--) comme [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). La capture d'écran explique comment [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) influence le HTML de sortie par défaut.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hiding Overlaid Content With CrossHideRight While Saving To Html</title>
    </head>
    <body>
        <h1>Hiding Overlaid Content With CrossHideRight While Saving To Html</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.htmlCrossStringType = AsposeCells.HtmlCrossType.CrossHideRight;

            // Save to HTML with HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
