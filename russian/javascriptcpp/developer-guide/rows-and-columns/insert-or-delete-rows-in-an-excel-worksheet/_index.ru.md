---
title: Вставка или удаление строк в листе Excel с помощью JavaScript через C++
linktitle: Вставка или удаление строк в рабочем листе Excel
type: docs
weight: 20
url: /ru/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Эта статья содержит JavaScript код с использованием C++, чтобы вставлять и удалять строки в листе Excel.
keywords: JavaScript вставка или удаление строк в листе Excel, JavaScript вставка или удаление строк в Excel, JavaScript вставка строк в Excel, JavaScript удаление строк в Excel, вставка или удаление строк в листе Excel с помощью JavaScript, вставка или удаление строк в Excel с помощью JavaScript, вставка строк в Excel с JavaScript, удаление строк в Excel с JavaScript
---

{{% alert color="primary" %}}  

Когда создаёте новый рабочий лист или работаете с существующим, вам может понадобиться добавить дополнительные строки или столбцы для размещения данных. В других случаях, необходимо удалить строки или столбцы из указанных позиций в рабочем листе.  

{{% /alert %}}  

Aspose.Cells for JavaScript через C++ предлагает два метода для вставки и удаления строк: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) и [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-). Эти методы оптимизированы для производительности и очень быстры.  

Для вставки или удаления определённого количества строк рекомендуется всегда использовать методы [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) и [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-), а не в цикле методы [**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) или [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-).  

Aspose.Cells работает так же, как и Microsoft Excel. При добавлении строк или столбцов содержимое рабочего листа сдвигается вниз и вправо. При удалении строк или столбцов содержимое рабочего листа сдвигается вверх или влево. Ссылки в других рабочих листах и ячейках обновляются при добавлении или удалении строк.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
