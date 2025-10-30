---
title: Yazdırma alanı aralığını JavaScript ve C++ aracılığıyla HTML ye Dışa Aktar
linktitle: HTML ye Baskı Alanı Aralığını Dışa Aktar
type: docs
weight: 60
url: /tr/javascript-cpp/export-print-area-range-to/
---

## **Olası Kullanım Senaryoları**

Bu, yalnızca yazdırma alanı=seçili hücre aralığı, tüm sayfa yerine HTML'ye dışa aktarmamız gereken yaygın bir senaryodur. Bu özellik zaten PDF görüntüleme için mevcuttur; ancak artık bu işlemi HTML için de yapabilirsiniz. Öncelikle, sayfa ayarlarının nesnesinde yazdırma alanını ayarlayın. Daha sonra, yalnızca seçili aralığı dışa aktarmak için [**HtmlSaveOptions.exportPrintAreaOnly()**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportPrintAreaOnly--) bayrağını kullanın.

## Örnek Kod

Aşağıdaki örnek kod, bir çalışma kitabı yükler ve daha sonra baskı alanını HTML'e dışa aktarır. Bu özelliği test etmek için örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleInlineCharts.xlsx](79527946.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Print Area to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the print area.
            worksheet.pageSetup.printArea = "D2:M20";

            // Initialize HtmlSaveOptions
            const options = new AsposeCells.HtmlSaveOptions();

            // Set flag to export print area only
            options.exportPrintAreaOnly = true;

            // Save to HTML format (options specify HTML)
            const outputData = workbook.save(options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputInlineCharts.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
