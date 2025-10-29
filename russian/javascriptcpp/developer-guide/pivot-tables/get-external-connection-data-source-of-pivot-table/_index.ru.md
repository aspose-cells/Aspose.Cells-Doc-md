---
title: Получить внешний источник подключения сводной таблицы
type: docs
weight: 150
url: /ru/javascript-cpp/get-external-connection-data-source-of-pivot-table/
description: Как получить внешний источник данных для сводной таблицы с помощью Aspose.Cells for JavaScript для C++.
keywords: Aspose.Cells for JavaScript для Excel, библиотека Excel JavaScript, Получить внешний источник данных сводной таблицы с помощью Aspose.Cells for JavaScript для C++.
---

## **Как получить источник данных внешнего подключения сводной таблицы**

Aspose.Cells for JavaScript для C++ позволяет получать внешний источник данных сводной таблицы. Для этого API предоставляет свойство [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) класса [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/). Свойство [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) возвращает объект [**ExternalConnection**](https://reference.aspose.com/cells/javascript-cpp/externalconnection/). Следующий пример демонстрирует использование свойства [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) для получения внешнего источника данных сводной таблицы.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Pivot Table External Connection Example</title>
    </head>
    <body>
        <h1>Pivot Table External Connection Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get the pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // Get external connection data source
            const externalConnection = pivotTable.externalConnectionDataSource;

            const name = externalConnection.name;
            const type = externalConnection.type;

            console.log("External Connection Data Source");
            console.log("Name: " + name);
            console.log("Type: " + type);

            resultDiv.innerHTML = `<p style="color: green;">External Connection Data Source</p>
                                   <p>Name: ${name}</p>
                                   <p>Type: ${type}</p>`;
        });
    </script>
</html>
```

Исходный файл, использованный во фрагменте кода, прикреплен для справки.

[Исходный файл](104398862.xlsx)
