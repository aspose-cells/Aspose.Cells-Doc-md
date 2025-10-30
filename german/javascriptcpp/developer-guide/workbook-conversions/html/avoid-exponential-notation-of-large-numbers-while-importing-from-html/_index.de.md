---
title: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML
linktitle: Verhindern Sie die Exponentialnotation großer Zahlen beim Importieren aus HTML
type: docs
weight: 10
url: /de/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Erfahren Sie, wie Sie verhindern können, dass große Zahlen in exponentielle Notation umgewandelt werden, wenn sie aus HTML importiert werden, mit Aspose.Cells for JavaScript über C++.
--- 

{{% alert color="primary" %}}  

 Manchmal enthält Ihr HTML Zahlen wie 1234567890123456, die länger als 15 Ziffern sind. Beim Import in eine Excel-Datei werden diese Zahlen in die Exponentialnotation 1.23457E+15 umgewandelt. Wenn Sie möchten, dass Ihre Zahl unverändert importiert wird, setzen Sie die Eigenschaft [**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--) auf **true** beim Laden Ihres HTML.  

{{% /alert %}}  

 Das folgende Beispiel zeigt, wie die [**HtmlLoadOptions.keepPrecision**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#keepPrecision--)-Eigenschaft verwendet wird. Die API importiert die Zahl genau so, ohne sie in Exponentialnotation umzuwandeln.  

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
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            // Sample Html containing large number with digits greater than 15
            const html = "<html><body><p>1234567890123456</p></body></html>";

            // Convert Html to byte array
            const byteArray = new TextEncoder().encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.keepPrecision = true;

            // Convert byte array into stream
            const stream = byteArray;

            // Create workbook from stream with Html load options
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAvoidExponentialNotationWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```
