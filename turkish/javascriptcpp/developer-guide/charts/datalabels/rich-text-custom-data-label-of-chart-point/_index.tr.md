---
title: JavaScript ile C++ üzerinden Grafik Noktasının Zengin Metin Özel Veri Etiketleri
description: Kılavuzumuzda, C++ üzerinden Aspose.Cells for JavaScript kullanarak grafik noktalarına zengin metin özel veri etiketleri eklemeyi öğreneceksiniz. Rehberimiz, etiketleri farklı yazı tipleri, renkler ve hizalama seçenekleriyle biçimlendirmeyi göstererek grafiklerinizin görünümünü ve okunabilirliğini artıracaktır.
keywords: Aspose.Cells for JavaScript ile C++, grafik çizimi, zengin metin, özel veri etiketleri, yazı tipleri, renkler, hizalama, görünüm, okunabilirlik.
type: docs
weight: 10
url: /tr/javascript-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak çizelge noktaları için zengin metinli özel veri etiketleri oluşturabilirsiniz. Aspose.Cells, [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#characters-number-number-) metodunu sağlar, bu da [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) nesnesini döndürür ve bu nesne, metnin renk, kalınlık gibi yazı tipi özelliklerini ayarlamak için kullanılabilir.

{{% /alert %}}

## Grafiğin Noktasının Zengin Metin Özel Veri Etiketi

Aşağıdaki kod, ilk serinin ilk grafik noktasına erişir, metnini ayarlar ve ardından ilk 10 karakterin fontunu kırmızıya ayarlar ve kalınlığı **true** yapar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = worksheet.charts.get(0);

            // Access the data label of first series first point
            const dlbls = chart.nSeries.get(0).points.get(0).dataLabels;

            // Set data label text
            dlbls.text = "Rich Text Label";

            // Set the font setting of the first 10 characters
            const fntSetting = dlbls.characters(0, 10);
            const font = fntSetting.font;
            font.color = AsposeCells.Color.Red;
            font.isBold = true;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
