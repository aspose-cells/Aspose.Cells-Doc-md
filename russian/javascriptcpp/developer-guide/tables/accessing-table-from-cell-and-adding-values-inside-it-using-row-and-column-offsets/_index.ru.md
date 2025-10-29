---
title: Доступ к таблице из ячейки и добавление значений внутри нее с помощью смещения строк и столбцов с помощью JavaScript через C++
linktitle: Доступ к таблице из ячейки и добавление значений в нее с использованием смещений строк и столбцов
type: docs
weight: 230
url: /ru/javascript-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}  

Обычно вы добавляете значения внутри объекта Table или List, используя метод [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-). Но иногда вам может потребоваться добавлять значения внутри объекта Table или List, используя смещения строки и столбца.  

Чтобы получить доступ к таблице или списковому объекту из ячейки, используйте свойство [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--). Чтобы добавить значения внутри нее с помощью смещения по строкам и столбцам, используйте метод [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-).  

{{% /alert %}}  

Следующий скриншот показывает исходный файл Excel, использованный внутри кода. Он содержит пустую таблицу и выделяет ячейку D5, которая находится внутри таблицы. Мы получим доступ к этой таблице из ячейки D5, используя свойство [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--), а затем добавим значения внутри нее с помощью методов [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) и [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-).  

## Пример  

### Снимки экрана сравнивают исходные и выходные файлы  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

На следующем снимке экрана показан созданный код. Как видно, ячейка D5 имеет значение, и ячейка F6, которая находится в смещении 2,2 от таблицы, имеет значение.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### JavaScript код для доступа к таблице из ячейки и добавления значений внутри нее с помощью смещения по строкам и столбцам  

Следующий примерный код загружает исходный файл Excel, как показано на снимке экрана выше, добавляет значения в таблицу и создает выходной файл Excel, как показано выше.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Accessing Table Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell D5 which lies inside the table
            const cell = worksheet.cells.get("D5");

            // Put value inside the cell D5
            cell.value = "D5 Data";

            // Access the Table from this cell
            const table = cell.table;

            // Add some value using Row and Column Offset
            table.putCellValue(2, 2, "Offset [2,2]");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
