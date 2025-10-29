---
title: Настройка параметра сводной таблицы  Показывать пустые ячейки
type: docs
weight: 40
url: /ru/javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

Вы можете настроить различные параметры сводной таблицы с помощью Aspose.Cells for JavaScript через C++. Одним из таких параметров является "Для пустых ячеек показывать". Установив этот параметр, все пустые ячейки в сводной таблице отображаются в виде заданной строки.

{{% /alert %}}

## **Установка параметров сводной таблицы в Microsoft Excel**

Чтобы найти и установить этот параметр в Microsoft Excel:

1. Выберите сводную таблицу и щелкните правой кнопкой мыши.
1. Выберите **Параметры сводной таблицы**.
1. Выберите вкладку **Макет и формат**.
1. Выберите опцию **Показывать пустые ячейки** и укажите строку.

## **Настройка параметра сводной таблицы с помощью Aspose.Cells for JavaScript через C++**

Aspose.Cells for JavaScript через C++ предоставляет свойства [**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-) и [**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-) для установки параметра "Для пустых ячеек показывать" сводной таблицы.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Update Example</title>
    </head>
    <body>
        <h1>Update PivotTable Null Display Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            await AsposeCells.onReady();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its first pivot table
            const worksheet = workbook.worksheets.get(0);
            const pt = worksheet.pivotTables.get(0);

            // Indicating if or not display the empty cell value
            pt.displayNullString = true;
            // Indicating the null string
            pt.nullString = "null";

            // Recalculate pivot table data
            pt.calculateData();

            // Do not refresh data on opening file
            pt.refreshDataOnOpeningFile = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Связанные статьи

- [Форматирование сводной таблицы](/cells/ru/javascript-cpp/formatting-pivot-table/)
