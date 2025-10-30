---
title: JavaScript ve C++ kullanarak Tarihleri Japon Tarihlerine dönüştürme
linktitle: Japon Tarihlerine Dönüştür
type: docs
weight: 350
url: /tr/javascript-cpp/convert-dates-to-japanese-dates/
description: C++.scripte Aspose.Cells for JavaScript kullanarak Gregoryen tarihleri Japon tarihlerine dönüştürmeyi öğrenin.
---  

{{% alert color="primary" %}}  

Japon Takviminde, yeni bir imparatorun saltanatıyla yeni bir çağ başlar. 1 Mayıs 2019'da, Heisei çağı sona erdi ve Reiwa çağı başladı.  

{{% /alert %}}  

 Aspose.Cells, Gregoriyen tarihlerini Japon tarihine dönüştürmenin bir yolunu sağlar. Bu dönüşüm sırasında, çağdaki değişiklikler de dikkate alınır. Aşağıdaki kod parçası, Gregoriyen tarihleri içeren [kaynak Excel](90112015.xlsx) dosyasını Japon tarihleriyle [çıktı PDF](90112016.pdf) haline dönüştürür, aşağıdaki görselde gösterildiği gibi.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel with Japanese Dates to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, CountryCode } = AsposeCells;

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

            // Create LoadOptions for XLSX and set language/region to Japan
            const options = new LoadOptions(LoadFormat.Xlsx);
            options.languageCode = CountryCode.Japan;
            options.region = CountryCode.Japan;

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'JapaneseDates.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
