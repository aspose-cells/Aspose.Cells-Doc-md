---
title: Zaman Çizelgesini Dönüştürme
type: docs
weight: 40
url: /tr/javascript-cpp/rendering-timeline/
description: Excel dosyalarının zaman çizelgelerini JavaScript ile C++ kullanarak yönetin.
keywords: Ofis 2013, Ofis 2016, Ofis 2019 ve Ofis 365 olmadan zaman çizelgesini dönüştürme
---

## **Olası Kullanım Senaryoları**
JavaScript ile C++ kullanarak, Office 2013, Office 2016, Office 2019 veya Office 365 kullanmadan zaman çizelgesi şeklinin render edilmesini destekler. Çalışma sayfanızı resmi dönüştürdüğünüzde veya çalışma kitabınızı PDF veya HTML formatında kaydettiğinizde, zaman çizelgelerinin doğru şekilde render edildiğini göreceksiniz.

## **Zaman Çizelgesini Dönüştürme**
Aşağıdaki örnek kod, içerisinde mevcut bir zaman çizelgesi bulunan [örnek Excel dosyasını](input.xlsx) yükler. Zaman çizelgesinin adına göre şekil nesnesini alın ve Shape.ToImage() yöntemiyle resme dönüştürün. Aşağıdaki resim, render edilmiş zaman çizelgesini gösteren [çıktı resmi](out.png)’dir. Gördüğünüz gibi, zaman çizelgesi düzgün şekilde render edilmiştir ve örnek Excel dosyasındaki ile aynıdır.

![todo:image_alt_text](out.png)
### **Örnek Kod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Timeline Shape as Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Add timeline relating to pivot table (access first timeline)
            const timeline = sheet.timelines.get(0);

            // Prepare image options
            const options = new ImageOrPrintOptions();
            options.imageType = ImageType.Png;

            // Get timeline shape object by timeline's name
            const timeLineShape = sheet.shapes.get(timeline.name);

            // Export shape to image (browser returns image bytes)
            const imageData = timeLineShape.toImage(options);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Timeline Image';

            resultDiv.innerHTML = '<p style="color: green;">Timeline image generated successfully. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
