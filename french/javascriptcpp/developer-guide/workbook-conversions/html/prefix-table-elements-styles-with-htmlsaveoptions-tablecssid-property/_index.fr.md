---
title: Préfixer les styles des éléments du tableau avec la propriété HtmlSaveOptions.tableCssId en JavaScript via C++
linktitle: Préfixer les styles des éléments du tableau avec la propriété HtmlSaveOptions.tableCssId
type: docs
weight: 110
url: /fr/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Apprenez à préfixer les styles des éléments de tableau dans HTML en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de préfixer les styles des éléments de tableau avec la propriété [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--). Supposons que vous définissiez cette propriété avec une valeur comme **MyTest_TableCssId**, alors vous trouverez les styles des éléments de tableau comme indiqué ci-dessous:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

La capture d'écran suivante montre l'effet de l'utilisation de la propriété [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) sur le HTML de sortie.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Préfixer les styles des éléments de tableau avec la propriété HtmlSaveOptions.tableCssId**

Le code d'exemple suivant montre comment utiliser la propriété [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--). Veuillez consulter le [HTML de sortie](60489790.zip) généré par le code comme référence.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set Cell Style and Save as HTML with Table CSS ID</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook as in original JavaScript sample
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

                // Specify html save options - specify table css id
                const opts = new HtmlSaveOptions();
                opts.tableCssId = "MyTest_TableCssId";

                // Save the workbook in html
                const outputData = wb.save(SaveFormat.Html, opts);
                const blob = new Blob([outputData], { type: 'text/html' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputTableCssId.html';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download HTML File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same changes
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - specify table css id
            const opts = new HtmlSaveOptions();
            opts.tableCssId = "MyTest_TableCssId";

            // Save the workbook in html
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTableCssId.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
