---
title: JavaScript ve C++ kullanarak PivotOptions ile PivotChart nasıl yönetilir
linktitle: Pivot Seçenekleri
type: docs
weight: 10
url: /tr/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: JavaScript ve C++ kullanarak PivotOptions ile PivotChart nasıl yönetilir.
keywords: C++ ile PivotChart JavaScript
---

## PivotChart Nedir

Excel'de bir PivotChart, bir PivotTable'dan oluşturulan verilerin grafiksel bir temsilidir. Kullanıcılara verileri dinamik olarak görselleştirmelerine ve analiz etmelerine olanak tanır. Veriyi özetleyerek ve bilgileri grafik formunda göstererek PivotChart'lar etkileşimlidir ve verinin farklı perspektiflerini göstermek için kolayca değiştirilebilir, bu da Excel'de veri analizi ve sunum için güçlü bir araç yapar.

## PivotOptions ile PivotChart'ı Yönetme

C++ kullanarak Aspose.Cells for JavaScript ile [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/)'i kullanarak PivotChart'ı yönetebilirsiniz.

Örnek dosya ve kod:
[Örnek Dosya](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Yukarıdaki örnek kodla sonuç dosyasını kontrol edebilir ve aşağıdaki etkiyi gösteren sonuç dosyasını inceleyebilirsiniz:

**![Çıktı](Output.png)**
