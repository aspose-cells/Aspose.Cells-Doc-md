---
title: C++ ile Ribbon XML Özelleştirme ve JavaScript
linktitle: Excel Menüsünü Özelleştirme
type: docs
weight: 1500
url: /tr/javascript-cpp/customizing-the-ribbon-xml/
description: C++ ile Aspose.Cells for JavaScript kullanarak Excel de Ribbon XML yi nasıl özelleştireceğinizi öğrenin. 
---

{{% alert color="primary" %}} 

Microsoft Office, ofis 2007'den bu yana uygulama penceresinin üstünde bir Ribbon ile menüleri ve araç çubuklarını değiştirdi. Ribbon özelleştirilebilir. 
C++ ile Aspose.Cells for JavaScript size olanak tanır 

- Parse etmeden Ribbon XML'yi saklamanıza olanak tanır.
- Açılış işareti ve açılış etiketi işareti XML sınıfı kullanarak işaretleme.
- Veri ilişkilendirmesi yöntemi kullanarak XML dosyalarını aktifleştirebilme.

Eğer açılış XML’ni değiştirmek istiyorsanız, XML veri işaretleme aracıları ya da başka bir açılış XML aracı kullanarak, onu işaretleşmelisiniz.

{{% /alert %}} 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set Ribbon XML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom ribbon XML
            const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
            workbook.ribbonXml = ribbonXml;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            const outputFileName = 'output_' + (file.name || 'modified.xlsx');
            downloadLink.download = outputFileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Ribbon XML set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
