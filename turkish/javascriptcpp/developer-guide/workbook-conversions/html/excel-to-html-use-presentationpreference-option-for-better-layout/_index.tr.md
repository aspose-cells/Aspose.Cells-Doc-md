---
title: Excel den HTML ye  Daha İyi Yerleşim İçin PresentationPreference Seçeneğini Kullanma, JavaScript ile C++
linktitle: Excel den HTML ye  Daha İyi Düzen İçin Presentasyon Tercihi Seçeneğini Kullanın
type: docs
weight: 220
url: /tr/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel dosyasını HTML veya MHT formatına kaydederken daha iyi düzen sağlayan görünüm tercihi özelliği olan HtmlSaveOptions.presentationPreference'ı geliştiricilere sunar. Özelliğin varsayılan değeri yanlıştır. Daha çekici bir Sunum almak için bu özelliği **true** yapmanızı öneririz.

{{% /alert %}} 

Aşağıdaki örnek kod, PresentationPreference açıkken bir Excel raporundan HTML dosyası nasıl render edileceğini gösterir.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Excel to HTML with Presentation Preference</h1>
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

            // Instantiate the Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions object
            const options = new HtmlSaveOptions();
            // Set the Presentation preference option (converted from setPresentationPreference)
            options.presentationPreference = true;

            // Save the Excel file to HTML with specified option
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPresentationlayout1.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
