---
title: Désactiver les commentaires révélés par Downlevel lors de l enregistrement en HTML avec JavaScript via C++
linktitle: Désactiver les commentaires révélés de niveau inférieur lors de l enregistrement en HTML
type: docs
weight: 20
url: /fr/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Apprenez comment désactiver les commentaires révélés par Downlevel lors de l enregistrement d un fichier Excel en HTML en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, Aspose.Cells révèle les commentaires conditionnels en dessous. Ces commentaires conditionnels concernent principalement les anciennes versions d'Internet Explorer et sont inutiles pour les navigateurs modernes. Vous pouvez en savoir plus à leur sujet via le lien suivant.

- [Commentaire conditionnel - Commentaire conditionnel révélé de niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for JavaScript via C++ vous permet de supprimer ces commentaires révélés par Downlevel en réglant la propriété [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--) sur **true**.

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas réglée sur true. Veuillez télécharger le [fichier Excel d'exemple](50528257.xlsx) utilisé dans ce code et le [HTML de sortie](50528258.zip) généré par celui-ci pour référence.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Disable Downlevel Revealed Comments Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load sample workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable DisableDownlevelRevealedComments
            const opts = new HtmlSaveOptions();
            opts.disableDownlevelRevealedComments = true;

            // Save the workbook in html
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisableDownlevelRevealedComments_true.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML with DisableDownlevelRevealedComments = true. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
