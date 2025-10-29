---
title: Exclure les styles inutilisés lors de la conversion Excel vers HTML avec JavaScript via C++
linktitle: Exclure les styles inutilisés lors de la conversion d Excel en HTML
type: docs
weight: 30
url: /fr/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Apprenez comment exclure les styles inutilisés lors de la conversion d Excel en HTML en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

Les fichiers Microsoft Excel peuvent contenir de nombreux styles inutilisés. Lors de l'exportation du fichier Excel en HTML, ces styles inutilisés sont également exportés. Cela peut augmenter la taille du HTML. Vous pouvez exclure ces styles inutilisés lors de la conversion d'Excel en HTML en utilisant la propriété [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--). Lorsqu'elle est définie sur **true**, tous les styles inutilisés sont exclus du HTML de sortie. La capture d'écran suivante affiche un style inutilisé dans le HTML de sortie.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**  

Le code d'exemple ci-dessous crée un classeur et y crée un style nommé inutilisé. Comme [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) est réglé sur **true**, ce style inutilisé ne sera pas exporté vers [HTML de sortie](61767778.zip). Mais si vous le réglez sur **false**, ce style inutilisé sera présent dans le HTML de sortie, comme montré dans la capture d'écran.  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Exclude Unused Styles</title>
    </head>
    <body>
        <h1>Exclude Unused Styles from Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            if (fileInput.files.length > 0 && fileInput.files[0].size === 0) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a valid Excel file.</p>';
                return;
            }

            // Instantiate workbook from selected file or create a new one
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Create an unused named style
            const style = wb.createStyle();
            style.name = "UnusedStyle_XXXXXXXXXXXXXX";

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some value in cell C7
            const cell = ws.cells.get("C7");
            cell.value = "This is sample text.";

            // Specify html save options, we want to exclude unused styles
            const opts = new HtmlSaveOptions();
            // Comment this line to include unused styles
            opts.excludeUnusedStyles = true;

            // Save the workbook in html format
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExcludeUnusedStylesInExcelToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML generated successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
