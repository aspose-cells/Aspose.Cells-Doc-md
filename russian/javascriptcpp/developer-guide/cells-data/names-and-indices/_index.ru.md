---
title: Преобразование между именем ячейки и индексом строки/столбца
linktitle: Преобразование имени ячейки и индекса
type: docs
weight: 10
url: /ru/javascript-cpp/names-and-indices/
description: Научитесь получать преобразование между именем ячейки и индексами строки/столбца через скрипт Aspose.Cells for Java на C++ API.
keywords: JavaScript через C++ получить имя ячейки по индексам строки и столбца, получить индексы строки и столбца по имени ячейки, создавать безопасные имена рабочих листов, добавлять безопасные имена рабочих листов
---

## **Получить имя ячейки по индексам строки и столбца**
Возможно определить имя ячейки по индексам строки и столбца. В этой статье объясняется как это сделать.
Aspose.Cells for JavaScript через C++ предоставляет метод CellsHelper.cellIndexToName, который позволяет разработчикам получить имя ячейки, указав индекс строки и столбца.

{{% alert color="primary" %}} 

Microsoft Excel начинает нумерацию индексов строк и столбцов с 1. В отличие от Microsoft Excel, Aspose.Cells for JavaScript через C++ начинает нумерацию индексов строк и столбцов с 0.

{{% /alert %}} 

Следующий пример кода демонстрирует, как использовать CellsHelper.cellIndexToName для получения имени ячейки по заданным индексам строки и столбца. Код выводит следующий результат.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **Получить индексы строки и столбца из имени ячейки**
Возможно определить индекс строки и столбца ячейки по ее имени. В этой статье объясняется как это сделать.
Aspose.Cells for JavaScript через C++ предоставляет метод CellsHelper.cellNameToIndex, который позволяет разработчикам получить индекс строки и столбца по имени ячейки.

{{% alert color="primary" %}} 

Microsoft Excel начинает нумерацию индексов строк и столбцов с 1. В отличие от Microsoft Excel, Aspose.Cells for JavaScript через C++ начинает нумерацию индексов строк и столбцов с 0.

{{% /alert %}} 

Следующий пример кода показывает, как использовать CellsHelper.cellNameToIndex для получения индекса строки и столбца из имени ячейки. Код выводит следующий результат.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **Создать безопасные имена листов**
Иногда возникает необходимость задания имени листа во время выполнения. В этом сценарии могут встречаться имена листов, содержащие дополнительные символы, такие как <>+(?”. Необходимо заменить любые такие недопустимые символы на заранее заданный символ, предоставленный пользователем. Аналогично может потребоваться обрезка длины имени листа, если она превышает 31 символ. Apache POI обеспечивает создание безопасных имен, поэтому аналогичная функция реализована в Aspose.Cells for JavaScript через C++, для обработки всех этих случаев. Ниже приведён пример кода, демонстрирующий эту функцию:



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

Вывод:

это первое имя, которое создано

` `< > + (adj.Private _"Частный"
