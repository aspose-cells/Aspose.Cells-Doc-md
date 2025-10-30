---
title: Grafik efsanesi giriş metninin rengini none yapacak şekilde ayarlayın, kullanarak Aspose.Cells for JavaScript ile C++
linktitle: Grafik lejant giriş dolgu metnini Aspose.Cells kullanarak hiçbir şeye ayarlayın
description: C++ kullanarak Aspose.Cells for JavaScript ile grafik efsane girişi dolgusunun hiçlik olarak ayarlanmasını öğrenin. Bu rehber, Microsoft Excel grafikleri içindeki efsane girişlerinin doldurma rengini nasıl değiştireceğinizi gösterecek ve görselleştirme ve özelleştirme amacıyla kullanılacaktır.
keywords: Aspose.Cells for JavaScript C++ ile, Grafik Efsane Girişi Doldurma, Microsoft Excel, Görselleştirme, Özelleştirme.
type: docs
weight: 320
url: /tr/javascript-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Grafik gösterge satırı içeriğinin doldurma rengini yok yapmak istiyorsanız, lütfen [**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/javascript-cpp/legendentry/#isTextNoFill--)’yi **true** olarak ayarlayın.

{{% /alert %}}

Aşağıdaki örnek kod, grafik efsanesinin ikinci giriş doldurmasını hiçbiri olarak ayarlar. Lütfen bu kodda kullanılan [örnek excel dosyasını](5115219.xlsx) ve bununla oluşturulan [çıktı excel dosyasını](5115217.xlsx) indirin.

Aşağıdaki ekran görüntüsü, bu kodun [örnek Excel dosyası](5115219.xlsx) üzerindeki etkisini vurgulamaktadır.

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Legend Entry Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = sheet.charts.get(0);

            // Set text of second legend entry fill to none
            const legendEntry = chart.legend.legendEntries.get(1);
            legendEntry.isTextNoFill = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ChartLegendEntry_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
