---
title: Excel dosyasını HTML ye aktarırken sağdan sola metin genişletme, JavaScript ile C++
linktitle: Excel den HTML ye Dönüştürürken Metni Sağdan Sola Doğru Genişletme
type: docs
weight: 60
url: /tr/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}}

Aspose.Cells, Excel dosyasını HTML'e dönüştürürken metni sağdan sola doğru genişletmeyi destekler. Bu özellik, v8.9.0.0'dan itibaren uygulanmıştır. Artık kaynak Excel dosyanız sağdan sola doğru genişleyen metin içeriyorsa, Aspose.Cells bunu HTML olarak doğru bir şekilde dışa aktaracaktır.

{{% /alert %}}
## **Excel dosyasını HTML'e dönüştüren aşağıdaki örnek kod. Bu ekran görüntüsü, örnek Excel dosyasının Microsoft Excel 2013'te nasıl göründüğünü göstermektedir.**
Aşağıdaki örnek kod, [örnek excel dosyasını](5115502.xlsx) HTML'ye dönüştürür. Bu ekran görüntüsü, örnek excelin Microsoft Excel 2013'te nasıl göründüğünü göstermektedir.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Bu ekran görüntüsü, eski sürümle oluşturulan [çıktı HTML'yi](5115509) göstermektedir.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Bu ekran görüntüsü, daha yeni sürümle oluşturulan [çıktı HTML'yi](5115508) göstermektedir.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Ekran görüntülerinde görebileceğiniz gibi, yeni sürüm sağa hizalanan metni Microsoft Excel gibi doğru bir şekilde sola genişletebilmektedir.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Expand Text From Right To Left Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load source excel file inside the workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get CellsHelper version (converted from getVersion())
            const version = CellsHelper.version;

            // Save workbook in html format
            const outputData = wb.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `ExpandTextFromRightToLeft_out_${version}.html`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to HTML successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
