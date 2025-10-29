---
title: Добавить подключение к сводной таблице с помощью JavaScript через C++
linktitle: Добавить связь сводной таблицы
type: docs
weight: 30
url: /ru/javascript-cpp/add-pivot-connection/
description: Узнайте, как добавить подключение к сводной таблице с помощью Aspose.Cells for JavaScript через C++.
keywords: Добавить подключение к сводной таблице без Office 2013, Office 2016, Office 2019 и Office 365 JavaScript через C++.
---

## **Возможные сценарии использования**

Если вы хотите связать срез и сводную таблицу в Excel, ПКМ по срезу и выберите пункт "Связи отчета...". В списке опций можно управлять флажками. Аналогично, для программного связывания среза и сводной таблицы через API Aspose.Cells используйте метод [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-). Он свяжет срез и сводную таблицу.

## **Ассоциировать фильтр и сводную таблицу**

Следующий пример кода загружает [образец файла Excel](add-pivot-connection.xlsx), содержащий существующий срез. Он получает доступ к срезу и затем связывает его со сводной таблицей. В конце сохраняет рабочую книгу как [выходной файл Excel](add-pivot-connection-out.xlsx).

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
