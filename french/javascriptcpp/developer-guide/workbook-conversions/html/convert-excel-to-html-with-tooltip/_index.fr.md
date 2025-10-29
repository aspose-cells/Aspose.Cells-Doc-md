---
title: Convertir Excel en HTML avec infobulle en utilisant JavaScript via C++  
linktitle: Convertir Excel en HTML avec info bulle  
type: docs  
weight: 200  
url: /fr/javascript-cpp/convert-excel-to-html-with-tooltip/  
description: Découvrez comment convertir des fichiers Excel en format HTML avec infobulles pour l affichage complet du texte en utilisant Aspose.Cells for JavaScript via C++.  
---

## **Convertir Excel en HTML avec info-bulle**

Il peut arriver que le texte soit tronqué dans le HTML généré et vous souhaitez afficher le texte complet en tant qu'infobulle lors du survol. Aspose.Cells for JavaScript via C++ prend en charge cette fonctionnalité en fournissant la propriété [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--). La définition de la propriété [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--) à **true** ajoutera le texte complet comme infobulle dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Le code d'exemple suivant charge le [fichier Excel source](98107416.xlsx) et génère le [fichier HTML de sortie](98107417.zip) avec l'infobulle.

Code d'exemple

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Tooltip to HTML Example</title>
    </head>
    <body>
        <h1>Add Tooltip to HTML Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and enable tooltip text
            const options = new HtmlSaveOptions();
            options.addTooltipText = true;

            // Save workbook as HTML with the specified options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddTooltipToHtmlSample_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
