---
title: Verileri Önce Satır, Sonra Sütun Olarak Doldur
type: docs
weight: 1000
url: /tr/javascript-cpp/populate-data-first-by-row-then-by-column/
description: İlk olarak Satır satır ve sonra Sütun ile Veri Doldurma konusunda Aspose.Cells for JavaScript C++ API sini kullanmayı öğrenin.
keywords: İpucu Veri Doldurma Satır satır ve sonra Sütun ile JavaScript C++ aracılığıyla Veri Doldurma Satır satır ve sonra Sütun ile JavaScript C++ aracılığıyla Veri Ekleme Satır satır ve sonra Sütun ile JavaScript C++ aracılığıyla Veri Ekleme Yüksek performanslı veri ekleme JavaScript C++, Yüksek performanslı veri ekleme JavaScript C++
---

{{% alert color="primary" %}}  

Bir elektronik tabloya verileri önce satır, sonra sütun olarak doldurmak genel performansı iyileştirir.  

{{% /alert %}}  

A1, B1, A2, B2 şeklinde veri yerleştirmek, A1, A2, B1, B2 şeklinde yerleştirmekten daha hızlıdır. Eğer bir çalışma sayfasında çok fazla hücre varsa ve ikinci sırayı takip ediyorsanız, yani verileri satır satır dolduruyorsanız, bu ipucu programı çok daha hızlı hale getirebilir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
