---
title: XLSB revizyonunu JavaScript ile C++ kullanarak XLSM’ye dönüştür
linktitle: XLSB Revizyonunu XLSM ye Dönüştür
type: docs
weight: 290
url: /tr/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Aspose.Cells for JavaScript kullanarak XLSB dosyalarının revizyonlarını tamamen XLSM formatına dönüştürmeyi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells artık XLSB dosyalarının revizyonlarını tamamen XLSM dosyalarına dönüştürmeyi destekler. Revizyonlar \xl\revisions yolu içinde bulunur. Bunları görmek için XLSB dosya uzantınızı ZIP'e değiştirin. \xl\revisions yolu, .bin uzantılı dosyaları içerir.

Aspose.Cells kullanarak XLSB dosyanızı XLSM formatına dönüştürdüğünüzde, bu .bin dosyaları başarıyla .xml dosyalarına dönüşür; bu iki ekran görüntüsünde gösterilmektedir.

{{% /alert %}}

 Aşağıdaki kod örneği, Aspose.Cells for JavaScript ile C++ kullanarak XLSB dosyasını XLSM formatına nasıl dönüştüreceğinizi gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
        <button id="runExample">Run Example</button>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
