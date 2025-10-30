---
title: JavaScript ile C++ kullanarak Excel ı PDF olarak render ederken Zaman Çizelgesi Çizin
linktitle: Excel i PDF ye dönüştürürken Zaman Çizelgesi çizin
type: docs
weight: 60
url: /tr/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: JavaScript ile C++ kullanarak Excel dosyalarının zaman çizelgelerini yönetin.
keywords: Office 2013, Office 2016, Office 2019 ve Office 365 olmadan zaman çizelgesini PDF ye render etme (JavaScript ile C++)
---

## **Excel'i PDF'ye dönüştürürken Zaman Çizelgesi çizin**
Excel dosyanızda bir zaman çizelgesi uygulandıysa ve Excel'i zaman çizelgesi ayarlarıyla PDF'ye aktarmak istiyorsanız, JavaScript ile C++ kullanarak bu artık yerleşik olarak desteklenmektedir. Sadece Excel dosyasını zaman çizelgesiyle birlikte PDF'ye aktarın, ve oluşturulan PDF zaman çizelgesini gösterecektir.

Aşağıdaki örnek kod, var olan bir zaman çizelgesi içeren [örnek Excel dosyasını](input.xlsx) yükler. Ardından, çalışma kitabını [çıktı PDF dosyası](out.pdf) olarak kaydeder. Aşağıdaki ekran görüntüsü, kaynak Excel dosyasını ve oluşturulan PDF dosyasını karşılaştırır.

<img src="out.png" width="60%">

## **Örnek Kod**
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
