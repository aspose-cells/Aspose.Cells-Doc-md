---
title: Förhindra export av dolda kalkylblads innehåll vid sparande till HTML med JavaScript via C++
linktitle: Förhindra export av dolt kalkylbladsinnehåll vid sparande till HTML
type: docs
weight: 210
url: /sv/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Lär dig hur du förhindrar export av dolda kalkylblad när du sparar Excel filer till HTML med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Du kan spara Excel-arbetsböcker till HTML. Om arbetsboken dock innehåller dolda kalkylblad exporterar Aspose.Cells som standard innehållet på de dolda kalkylbladen till HTML-utdata (_files)-mappen som innehåller filer som kalkylblad, bilder, tabstrip.htm, stylesheet.css, osv. Ibland är det inte lämpligt att exportera innehållet på de dolda kalkylbladen på detta sätt. Till exempel, om det dolda kalkylbladet innehåller bilder som inte ska exporteras till _files-mappen.

{{% /alert %}}

Aspose.Cells for JavaScript via C++ tillhandahåller [**HtmlSaveOptions.exportHiddenWorksheet**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportHiddenWorksheet--) egenskapen. Som standard är den inställd på **true** och dolda kalkylblad exporteras till HTML. Om du ställer in den på **false**, kommer Aspose.Cells inte att exportera dolt kalkylblad innehåll.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - HTML Without Hidden Content</title>
    </head>
    <body>
        <h1>Save Workbook as HTML Without Hidden Worksheet Content</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and do not export hidden worksheet contents
            const options = new HtmlSaveOptions();
            options.exportHiddenWorksheet = false;

            // Save workbook to HTML format using the options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HtmlWithoutHiddenContent_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to HTML without hidden content. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
