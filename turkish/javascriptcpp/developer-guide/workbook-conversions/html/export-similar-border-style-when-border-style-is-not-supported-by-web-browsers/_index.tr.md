---
title: Web Tarayıcıları tarafından desteklenmeyen Kenar Stili olduğunda, JavaScript ve C++ aracılığıyla Benzer Sınır Stili dışa aktarın  
linktitle: Web Tarayıcıları tarafından Desteklenmeyen Kenar Stili Benzeri Kenar Stilini Dışa Aktar  
type: docs  
weight: 70  
url: /tr/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Excel dosyalarını HTML ye dönüştürürken, web tarayıcıları tarafından desteklenmeyen sınırları dışa aktarmayı öğrenin Aspose.Cells for JavaScript ve C++ aracılığıyla.  
---  

## **Olası Kullanım Senaryoları**  

Microsoft Excel, Web Tarayıcıları tarafından desteklenmeyen bazı türlerde kesik sınırları destekler. Böyle bir Excel dosyasını HTML'ye dönüştürdüğünüzde, bu sınırlar kaldırılır. Ancak, Aspose.Cells ayrıca [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) özelliği ile bu sınırların gösterilmesini de destekleyebilir. Lütfen değeri **true** olarak ayarlayın, böylece desteklenmeyen sınırlar da HTML dosyasına dışa aktarılır.  

## **CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle**  

Aşağıdaki örnek kod, aşağıdaki ekran görüntüsünde gösterildiği gibi bazı desteklenmeyen sınırları içeren örnek Excel dosyasını (64716806.xlsx) yükler. Ekran görüntüsü ayrıca [çıktı HTML](64716804.zip) içindeki [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) özelliğinin etkisini gösterir.  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options - Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
