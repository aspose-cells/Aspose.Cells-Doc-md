---
title: Excel 2016 MINIFS ve MAXIFS fonksiyonlarının JavaScript aracılığıyla C++ ile hesaplanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel 2016 da MINIFS ve MAXIFS fonksiyonlarını JavaScript aracılığıyla C++ ile nasıl hesaplayacağınızı gösterir. Varolan bir Excel dosyasını yükleyin veya yeni bir tane oluşturun, ardından bu fonksiyonları hesaplamak için Aspose.Cells yöntemlerini kullanın ve sonuçları diske kaydedin.
keywords: Aspose.Cells, Excel, 2016, MINIFS fonksiyonu, MAXIFS fonksiyonu, hesaplama JavaScript aracılığıyla C++
type: docs
weight: 300
url: /tr/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel 2016, MINIFS ve MAXIFS fonksiyonlarını destekler. Bu fonksiyonlar Excel 2013 veya daha eski sürümlerde desteklenmez. C++ aracılığıyla Aspose.Cells for JavaScript bu fonksiyonların hesaplanmasını da destekler. Aşağıdaki ekran görüntüsü bu fonksiyonların kullanımını göstermektedir. Bu fonksiyonların nasıl çalıştığını anlamak için ekran görüntüsündeki kırmızı yorumları lütfen okuyunuz.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması**
Aşağıdaki örnek kod, [örnek excel dosyasını](5115149.xlsx) yükler ve [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) yöntemini çağırarak formül hesaplamasını Aspose.Cells for JavaScript ile C++ üzerinden gerçekleştirir ve ardından sonucu [çıktı PDF'sine](5115154.pdf) kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
