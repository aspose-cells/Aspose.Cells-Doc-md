---
title: JavaScript ile C++ kullanarak Çalışma Sayfasında Sıfır Değerlerini Gizleme
linktitle: Çalışma Taşraflarındaki Sıfır Değerlerinin Gizlenmesi
type: docs
weight: 50
url: /tr/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Bu makale, JavaScript kütüphanesi kullanılarak Excel elektronik tablosundaki sıfır değerlerini programatik olarak nasıl gizleyeceğinizi açıklayan örnek kodu gösterecek.
keywords: JavaScript ile C++ kullanarak Excel çalışma sayfasının sıfır değerlerini gizleme
---

{{% alert color="primary" %}} 

Bazen çalışma taşrasındaki sıfır değerlerini gizlemeniz gerekir. Bu kişisel tercih veya biçimlendirme standardı olabilir.

{{% /alert %}} 

Microsoft Excel'de bir çalışma taşrasındaki sıfır değerlerini gizlemek için (örneğin Microsoft Excel 2003):

1. **Araçlar** menüsünden **Seçenekler**'i seçin, ardından **Görünüm** sekmesini seçin.
1. **Sıfır değerleri** seçeneğini kaldırın.
1. **Tamam**'a tıklayın.

Lütfen aşağıdaki örnek kodu inceleyin, bu kod Aspose.Cells for JavaScript kullanılarak sıfırların nasıl gizleneceğini gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
