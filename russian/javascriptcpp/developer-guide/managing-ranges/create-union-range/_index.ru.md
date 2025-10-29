---
title: Создать объединённый диапазон с помощью JavaScript через C++
linktitle: Создать объединенный диапазон
type: docs
weight: 360
url: /ru/javascript-cpp/create-union-range/
description: Узнайте, как создать объединенный диапазон, используя Aspose.Cells for JavaScript через C++.
keywords: Создать объединённый диапазон JavaScript через C++, Объединение диапазонов Aspose.Cells JavaScript через C++, Создать объединённый диапазон листа JavaScript через C++
---

## **Создать объединенный диапазон**
Aspose.Cells предоставляет возможность создавать объединённые диапазоны с помощью метода [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-). Метод [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-) принимает два параметра: адрес для создания объединённого диапазона и индекс листа. Метод возвращает объект [UnionRange](https://reference.aspose.com/cells/javascript-cpp/unionrange).  

' Следующий код демонстрирует создание объединенного диапазона с помощью метода [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-). Созданный кодом файл прикреплен для ознакомления.  

- [Выходной файл](106364952.xlsx)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Union Range Example</title>
    </head>
    <body>
        <h1>Create Union Range Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create union range
            const unionRange = workbook.worksheets.createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

            // Put value "ABCD" in the range (converted setter to property)
            unionRange.value = "ABCD";

            // Save the output workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CreateUnionRange_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Union range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
