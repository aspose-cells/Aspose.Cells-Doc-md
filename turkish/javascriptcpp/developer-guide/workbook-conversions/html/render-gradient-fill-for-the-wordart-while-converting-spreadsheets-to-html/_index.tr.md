---
title: JavaScript kullanarak C++ ile WordArt için Gradyan Doldurma Çizimi
linktitle: Hücre Dizelerini HTML ye Dönüştürürken WordArt için Gradient Doldurmayı Oluşturma
type: docs
weight: 90
url: /tr/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Aspose.Cells for JavaScript kullanarak C++ ile tabloları HTML ye dönüştürürken WordArt için gradyan dolgunun nasıl render edileceğini öğrenin.
---

## **Olası Kullanım Senaryoları**  
Aspose.Cells 17.1 öncesinde, Excel dosyası HTML formatına dönüştürülürken, WordArt'ın gradient dolumu render edilmezdi. Aspose.Cells 17.1 sürümünden itibaren WordArt gradient dolumu desteklenmektedir. Aşağıdaki ekran görüntüsü, Aspose.Cells 17.1 ve eski sürüm kullanılarak Excel dosyasının dönüştürülmesiyle gradient dolumu üzerindeki etkiyi karşılaştırır.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Hücre Dizelerini HTML'ye dönüştürürken word art için gradient doldurmayı oluştur.**  
Aşağıdaki örnek kod, [kaynak excel dosyasını](22774111.xlsx) [çıktı HTML formatına](22774109.zip) dönüştürür. Kaynak excel dosyası, yukarıdaki ekran görüntüsünde gösterilen gradient dolumu olan WordArt nesnesini içerir.  

## **Örnek Kod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
