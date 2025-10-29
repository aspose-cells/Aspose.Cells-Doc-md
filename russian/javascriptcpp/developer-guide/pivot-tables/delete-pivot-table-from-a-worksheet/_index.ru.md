---
title: Удалить сводную таблицу из листа
type: docs
weight: 60
url: /ru/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: Код Скрипта Aspose.Cells for Java через C++, чтобы удалить сводную таблицу на рабочих листах Excel
keywords: Скрипт Aspose.Cells for Java через C++, библиотека Excel, Excel JavaScript, удаление сводной таблицы из листа, удаление сводной таблицы из Excel, как удалить сводную таблицу с помощью Скрипта Aspose.Cells for Java через C++, удаление сводной таблицы, удаление сводной таблицы из Excel, как удалить сводную таблицу, удаление сводной таблицы, Aspose.Cells for JavaScript через C++ удаляет сводную таблицу, удаление сводной таблицы, как удалить сводную таблицу
---

{{% alert color="primary" %}}

 Скрипт Aspose.Cells for Java через C++ предоставляет функцию для удаления или удаления сводной таблицы из листа. Вы можете удалить сводную таблицу, использовав объект сводной таблицы или положение сводной таблицы. Пожалуйста, используйте метод [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) для удаления сводной таблицы через объект сводной таблицы и метод [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) для удаления объекта сводной таблицы, используя его положение внутри коллекции сводных таблиц.

{{% /alert %}}

## **Как удалить сводную таблицу с листа, используя Aspose.Cells for JavaScript для C++**

В следующем примере кода удаляются две сводные таблицы с листа. Сначала удаляется сводная таблица, используя метод [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-), а затем удаляется сводная таблица, используя метод [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Table</title>
    </head>
    <body>
        <h1>Remove Pivot Table Example</h1>
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
            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table object
            const pivotTable = worksheet.pivotTables.get(0);

            // Remove pivot table using pivot table object
            worksheet.pivotTables.remove(pivotTable);
            // OR remove by index:
            // worksheet.pivotTables.removeAt(0);

            // Saving the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
