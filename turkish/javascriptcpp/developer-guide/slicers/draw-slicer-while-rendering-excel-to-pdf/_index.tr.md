---
title: Excel i PDF ye dönüştürürken Dilimleyici Çizer
type: docs
weight: 60
url: /tr/javascript-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **Excel dosyasına bir dilimleyici uygulanmışsa ve bu dilimleyicinin ayarlarını içeren bir Excel dosyasını PDF olarak dışa aktarmak istiyorsanız, Aspose.Cells bunu artık varsayılan olarak destekler. Sadece Excel dosyasını dilimleyici ile birlikte PDF olarak dışa aktarırsınız, oluşturulan PDF uygulanan dilimleyiciyi gösterecektir.**
 Slicer uygulanan bir Excel dosyanız varsa ve bu ayarlarla birlikte PDF'ye dışa aktarmak istiyorsanız, Aspose.Cells for JavaScript ile C++ artık bunu varsayılan olarak destekler. Sadece Slicer ile Excel dosyasını PDF'ye dışa aktarın, oluşturulan PDF'de Slicer uygulanmış şekilde gösterilecektir.

Aşağıdaki örnek kod önceden var olan bir dilimleyici içeren [örnek Excel dosyasını](94044165.xlsx) yükler. Daha sonra, çalışma kitabını [çıkış PDF dosyası](94044166.pdf) olarak kaydeder. Aşağıdaki ekran görüntüsü kaynak Excel dosyasını ve oluşturulan PDF dosyasını karşılaştırır.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **Örnek Kod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as PDF</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleSlicerChart.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
