---
title: Microsoft Excel gibi otomatik Eksen Birimlerini JavaScript ile C++ kullanarak yönetme
linktitle: Microsoft Excel gibi Grafik Ekseni Otomatik Birimleri ile Başa Çık
description: Aspose.Cells for JavaScript kullanarak C++ ile çizelge eksenlerinde otomatik birimleri nasıl yöneteceğinizi öğrenin. Rehberimiz, otomatik birimleri yapılandırma ve özelleştirme, bilimsel gösterim ve ölçek ayarlama dahil olmak üzere, ekrandaki gösterim ve ayarlama konularında size yol gösterecektir.
keywords: Aspose.Cells for JavaScript kullanarak C++, çizelge eksenleri, otomatik birimler, Microsoft Excel, yapılandırma, özelleştirme, bilimsel gösterim, ölçeklandırma.
type: docs
weight: 120
url: /tr/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Olası Kullanım Senaryoları**  
 Aspose.Cells for JavaScript kullanarak C++ ile otomatik eksen birimleri düzgün şekilde işlenememişti, özellikle de çizelge görseli veya PDF'e dönüştürülürken. Şimdi, Aspose.Cells for JavaScript C++ otomatik eksen birimlerinin işlenmesini destekliyor. Kod değişikliği yok. Sadece çizelgenizi bir görsele veya PDF'e dönüştürün, ve çizelge ekseni Microsoft Excel gibi render edilecektir.  

## **Grafik Ekseni Otomatik Birimleri ile Başa Çık**  
Aşağıdaki örnek kod, [örnek Excel dosyasını](61767755.xlsx) yükler ve [çıktı PDF çizelgesi](61767752.pdf) üretir. Ekran görüntüsü, çizelge ekseninin otomatik birimlerini kırmızı dikdörtgenlerde gösterirken, örnek Excel dosyasındaki çizelge ile çıktı PDF'sini karşılaştırır. Her ikisi de tam olarak aynıdır.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Örnek Kod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
