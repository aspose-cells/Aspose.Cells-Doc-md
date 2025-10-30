---
title: Excel i Tooltip ile HTML e Dönüştürme ve JavaScript kullanımı ile C++  
linktitle: Excel i HTML e dönüştür ve açıklama metni ekleyin  
type: docs  
weight: 200  
url: /tr/javascript-cpp/convert-excel-to-html-with-tooltip/  
description: Aspose.Cells for JavaScript i C++ kullanarak Excel dosyalarını tooltip ile tam metin görüntüsü sağlayacak HTML formatına dönüştürmeyi öğrenin.  
---

## **Excel'i HTML'e dönüştür ve açıklama metni ekleyin**

Oluşturulan HTML'de metnin kesildiği durumlar olabilir ve hover olayında tamamını tooltip olarak göstermek isteyebilirsiniz. Aspose.Cells for JavaScript'i C++ kullanarak bu özelliği [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--) özelliğiyle destekler. [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--) özelliğini **true** yapmanız, tam metni oluşturulan HTML'de tooltip olarak ekler.

Aşağıdaki resim, oluşturulan HTML dosyasındaki açıklama metnini göstermektedir.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Aşağıdaki kod örneği, [kaynak excel dosyasını](98107416.xlsx) yükler ve [çıktı HTML dosyasını](98107417.zip) araç ipucu ile oluşturur.

Örnek Kod

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Tooltip to HTML Example</title>
    </head>
    <body>
        <h1>Add Tooltip to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and enable tooltip text
            const options = new HtmlSaveOptions();
            options.addTooltipText = true;

            // Save workbook as HTML with the specified options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddTooltipToHtmlSample_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
