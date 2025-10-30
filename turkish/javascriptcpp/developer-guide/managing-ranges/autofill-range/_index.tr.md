---
title: Excel dosyasını otomatik doldurma aralığını JavaScript ile C++ kullanarak doldurun
linktitle: Otomatik Doldurma Aralığı
type: docs
weight: 105
url: /tr/javascript-cpp/autofill-ranges/
description: Aspose.Cells for JavaScript kullanarak C++ ile bir Excel dosyasındaki belirli bir alanda otomatik doldurma işlemini nasıl yapacağınızı öğrenin.
---

## **Belirtilen aralıkta Excel'de otomatik doldurma yapın**

Excel'de, bir aralık seçin, sağ-alt köşeye geçin ve "artı" simgesini sürükleyerek otomatik doldurma yapın.

## **Aspose.Cells for JavaScript kullanarak C++ ile Otomatik Doldurma Aralıkları**

Aşağıdaki örnek, bir Aralıkta Otomatik Doldurma işleminin nasıl gerçekleştirileceğini gösterir ve 

[range_autofill.xlsx](range_autofill.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Range AutoFill Example</title>
    </head>
    <body>
        <h1>Range AutoFill Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Get Cells
            const cells = workbook.worksheets.get(0).cells;
            // Create Range
            const src = cells.createRange("C3:C4");
            const dest = cells.createRange("C5:C10");
            // AutoFill
            src.autoFill(dest, AsposeCells.AutoFillType.Series);
            // Save the Workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'range_autofill_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">AutoFill completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
