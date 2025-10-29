---
title: Désactiver CSS lors de l enregistrement en HTML avec JavaScript via C++
linktitle: Désactiver le CSS lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/javascript-cpp/disable-css-while-saving-to-html/
description: Apprenez comment désactiver CSS lors de l enregistrement de fichiers Excel en HTML en utilisant Aspose.Cells for JavaScript via C++. 
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML sur une seule page, en général les éléments CSS seront intégrés dans le fichier HTML et situés dans la section HEAD. Si vous attachez ce fichier comme contenu/corps d'un email, la majorité des clients de messagerie supprimeront les éléments CSS, ce qui entraînera un rendu incorrect. La version 24.12 d'Aspose.Cells introduit une option permettant de désactiver optionnellement le CSS, permettant aux styles d'être directement appliqués dans les éléments HTML eux-mêmes. Si vous souhaitez que le HTML soit le contenu/corps de l'email, veuillez utiliser la propriété [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) et la définir sur **true**.

## **Désactiver le CSS lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--). 

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
