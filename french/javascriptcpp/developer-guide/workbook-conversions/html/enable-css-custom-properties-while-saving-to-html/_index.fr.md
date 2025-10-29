---
title: Activer les propriétés CSS personnalisées lors de l enregistrement en HTML avec JavaScript via C++
linktitle: Activer les propriétés CSS personnalisées lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/javascript-cpp/enable-css-custom-properties-while-saving-to-html/
description: Apprenez comment activer les propriétés CSS personnalisées lors de l enregistrement de fichiers Excel en HTML en utilisant Aspose.Cells for JavaScript via C++. 
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, pour le scénario où il y a plusieurs occurrences d'une image en base64, avec une propriété personnalisée, les données de l'image n'ont besoin d'être enregistrées qu'une seule fois afin d'améliorer la performance du HTML résultant. Veuillez utiliser la propriété [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--) et la définir **true** lors de l'enregistrement en HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Activer les propriétés personnalisées CSS lors de l'enregistrement en HTML**

Le code d'exemple ci-dessous montre l'utilisation de la propriété [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas réglée sur **true**. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) utilisé dans ce code et le [HTML de sortie](50528261.zip) généré pour référence.



## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Enable CSS Custom Properties Example</title>
    </head>
    <body>
        <h1>Enable CSS Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Create HtmlSaveOptions and set properties (converted from setters to property assignments)
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.exportImagesAsBase64 = true;
            opts.enableCssCustomProperties = true;

            // Save the workbook to HTML using SaveFormat.Html and provided options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEnableCssCustomProperties.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
