---
title: Prendre en charge la disposition des balises DIV lors du chargement du HTML dans un classeur Excel avec JavaScript via C++
linktitle: Prise en charge de la mise en page des balises DIV lors du chargement de HTML dans un classeur Excel
type: docs
weight: 50
url: /fr/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}}
Normalement, la disposition des balises div est ignorée lors du chargement du HTML dans un objet classeur Excel. Cependant, si vous souhaitez que la disposition des balises div ne soit pas ignorée, veuillez définir la propriété [HtmlLoadOptions.supportDivTag](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#supportDivTag--) sur **true**. La valeur par défaut de cette propriété est **false**.
{{% /alert %}}

Le code d’exemple suivant illustre l’utilisation de la propriété [HtmlLoadOptions.supportDivTag](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#supportDivTag--). Veuillez télécharger le [logo Aspose](5115218.png) utilisé dans le HTML d’entrée et le [fichier Excel de sortie](5115220.xlsx) généré par le code.

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
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat, Utils } = AsposeCells;

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
            const exportHtml = `
<html>
<body>
<table>
<tr>
<td>
<div>This is some Text.</div>
<div>
<div>
<span>This is some more Text</span>
</div>
<div>
<span>abc@abc.com</span>
</div>
<div>
<span>1234567890</span>
</div>
<div>
<span>ABC DEF</span>
</div>
</div>
<div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>
</td>
<td>
<img src="ASpose_logo_100x100.png" />
</td>
</tr>
</table>
</body>
</html>`;

            // Encode HTML string to Uint8Array
            const encoder = new TextEncoder();
            const ms = encoder.encode(exportHtml);

            // Specify HTML load options, support div tag layouts
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.supportDivTag = true;

            // Create workbook object from the html using load options
            const wb = new Workbook(ms, loadOptions);

            // Auto fit rows and columns of first worksheet
            const ws = wb.worksheets.get(0);
            ws.autoFitRows();
            ws.autoFitColumns();

            // Save the workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DivTagsLayout_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
