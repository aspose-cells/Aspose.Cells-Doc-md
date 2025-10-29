---
title: Преобразование ревизии XLSB в XLSM с помощью JavaScript через C++
linktitle: Преобразование ревизии из XLSB в XLSM
type: docs
weight: 290
url: /ru/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Узнайте, как полноценно преобразовать ревизии файлов XLSB в формат XLSM с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}

Aspose.Cells теперь полностью поддерживает преобразование ревизий файлов XLSB в файлы XLSM. Ревизии находятся по пути \xl\revisions. Их можно просмотреть, изменив расширение файла XLSB на ZIP. Путь \xl\revisions содержит файлы с расширениями .bin.

Когда вы преобразуете файл XLSB в XLSM с помощью Aspose.Cells, эти .bin файлы успешно преобразуются в .xml файлы, как показано на двух скриншотах.

{{% /alert %}}

Следующий образец кода показывает, как преобразовать файл XLSB в формат XLSM с помощью Aspose.Cells for JavaScript через C++.

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
