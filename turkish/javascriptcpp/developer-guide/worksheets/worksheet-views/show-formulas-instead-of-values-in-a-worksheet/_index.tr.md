---
title: Bir Çalışma Sayfasında Formüller Yerine Değerleri Göster veya Gizle ile JavaScript kullanımıyla ilgili
linktitle: Çalışma Sayfasında Değerler Yerine Formülleri Gösterme
type: docs
weight: 20
url: /tr/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Bu makale, JavaScript API kullanarak C++ ile Excel çalışma sayfasında veya elektronik tablolarda değerler yerine formülleri programatik olarak gösterme kodlarını içerir.
---

{{% alert color="primary" %}}

Microsoft Excel'de Formülleri Hesaplanan Değerler Yerine Gösterme işlemi, **Formüller** şeridinden **Formülleri Göster** seçeneği kullanılarak yapılabilir. Formüller göründüğünde, Microsoft Excel çalışma sayfasında formülleri gösterir. Aynı işlemi Aspose.Cells for JavaScript kullanarak yapabilirsiniz.

{{% /alert %}}

Aspose.Cells, [**Worksheet.showFormulas**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#showFormulas--) adlı bir özellik sağlar. Bu değeri **true** yaparak Microsoft Excel'e formülleri gösterecek şekilde ayarlayabilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Show Formulas Example</title>
    </head>
    <body>
        <h1>Show Formulas Example</h1>
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

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Show formulas of the worksheet
            worksheet.showFormulas = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'source.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas are now visible. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
