---
title: JavaScript ile C++ kullanarak çalışma sayfasında Hücreleri Aralıkla Taşıma
linktitle: Çalışma Sayfasında Hücre Aralığını Taşıma
type: docs
weight: 370
url: /tr/javascript-cpp/move-range-of-cells-in-a-worksheet/
description: C++ kullanarak çalışma sayfasında bir aralık hücreleri nasıl taşınır öğrenin.
---

{{% alert color="primary" %}}
Bu makale, bir çalışma sayfasında hücrelerin bir aralığını nasıl taşıyacağını gösterir.
{{% /alert %}}

## **Çalışma Sayfasında Hücre Aralığını Taşıma**
Örnek kod, görevi göstermek için bir şablon dosyası kullanır.

**Giriş dosyası**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Lütfen A1:B5 aralığındaki hücreleri C1:D5'e taşıyan oluşturulan dosyayı inceleyin.

**Çıkış dosyası**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiate the workbook object. Open the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const cells = workbook.worksheets.get(0).cells;

            const range = cells.createRange("A1", "B5");
            // move the range to right.
            range.moveTo(0, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Range moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
