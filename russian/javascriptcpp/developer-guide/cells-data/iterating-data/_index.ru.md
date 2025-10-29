---
title: Где и как использовать перечислители с помощью JavaScript для C++
linktitle: Итерация данных
type: docs
weight: 55
url: /ru/javascript-cpp/how-and-where-to-use-enumerators/
description: Научитесь использовать перечислители через скрипт Aspose.Cells for Java на C++ API.
keywords: Как использовать перечислители JavaScript через C++, перечислитель ячеек JavaScript через C++, перечислитель строк JavaScript через C++, перечислитель столбцов JavaScript через C++
---

{{% alert color="primary" %}}  

Перечислитель — это объект, который обеспечивает возможность обхода контейнера или коллекции. Перечислители можно использовать для чтения данных в коллекции, но они не могут быть использованы для изменения базовой коллекции, тогда как Array — это интерфейс, который определяет один метод `enumerator` возвращающий интерфейс `IEnumerator`, что, в свою очередь, обеспечивает только чтение коллекции.  

API Aspose.Cells предоставляет множество перечислителей, однако в данной статье обсуждаются в основном три типа, перечисленные ниже.  

1. Перечислитель ячеек  
1. Перечислитель строк  
1. Перечислитель столбцов  

{{% /alert %}}  

## **Как использовать перечислители**  

### **Перечислитель ячеек**  

Существуют различные способы доступа к перечислителю ячеек, и можно использовать любые из этих методов в зависимости от требований приложения. Вот методы, возвращающие перечислитель ячеек.  

1. [**Cells.enumerator**](https://reference.aspose.com/cells/javascript-cpp/cells/#enumerator--)  
1. [**Row.enumerator**](https://reference.aspose.com/cells/javascript-cpp/row/#enumerator--)  
1. [**Range.enumerator**](https://reference.aspose.com/cells/javascript-cpp/range/#enumerator--)  

Все вышеперечисленные методы возвращают перечислитель, который позволяет осуществлять обход коллекции ячеек, которые были инициализированы.  

{{% alert color="primary" %}}  

При обходе ячеек коллекция не должна изменяться (операции, которые приведут к созданию новой ячейки или удалению существующей). В противном случае перечислитель может не иметь возможности правильно обойти все ячейки (некоторые элементы могут быть обойдены повторно или пропущены).  

{{% /alert %}}  

Следующий пример кода демонстрирует реализацию интерфейса `IEnumerator` для коллекции ячеек.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Values</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            const resultLines = [];

            // Iterate over all cells in the worksheet
            const cellsEnumerator = worksheet.cells.getEnumerator();
            for (const cell of cellsEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over the first row's cells
            const firstRowEnumerator = worksheet.cells.rows.get(0).getEnumerator();
            for (const cell of firstRowEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over a specific range A1:B10
            const rangeEnumerator = worksheet.cells.createRange("A1:B10").getEnumerator();
            for (const cell of rangeEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            document.getElementById('result').innerHTML = `<pre>${resultLines.join('\n')}</pre>`;
        });
    </script>
</html>
```  

### **Перечислитель строк**  

Перечислитель строк можно получить при использовании метода [**RowCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/rowcollection/#enumerator--). Следующий пример кода демонстрирует реализацию интерфейса `IEnumerator` для [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - List Row Indexes</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get RowCollection and iterate using index
            const rows = workbook.worksheets.get(0).cells.rows;
            const rowCount = rows.count;

            // Traverse rows in the collection and display indexes
            let output = '<p>Row indexes:</p><ul>';
            for (let i = 0; i < rowCount; i++) {
                const row = rows.get(i);
                output += `<li>${row.index}</li>`;
                console.log(row.index);
            }
            output += '</ul>';
            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```  

### **Перечислитель столбцов**  

Перечислитель столбцов можно получить при использовании метода [**ColumnCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/columncollection). Следующий пример кода демонстрирует реализацию интерфейса `IEnumerator` для [**ColumnCollection**](https://reference.aspose.com/cells/javascript-cpp/columncollection).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Columns Indexes Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get columns collection from first worksheet
            const columns = workbook.worksheets.get(0).cells.columns;
            // Traverse columns using index
            const count = columns.count;
            let html = '<p>Columns indexes:</p><ul>';
            for (let i = 0; i < count; i++) {
                const col = columns.get(i);
                html += `<li>${col.index}</li>`;
                console.log(col.index);
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

## **Где использовать перечислители**  

Чтобы обсудить преимущества использования перечислителей, возьмем реальный пример.  

**Сценарий**  

Требование приложения — пройтись по всем ячейкам в заданном [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet), чтобы прочитать их значения. Для достижения этой цели существует несколько способов. Некоторые из них показаны ниже.  

### **Использование диапазона отображения**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Max Display Range Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Get the MaxDisplayRange
            const displayRange = cells.maxDisplayRange;

            // Loop over all cells in the MaxDisplayRange
            let outputLines = [];
            for (let row = displayRange.firstRow; row < displayRange.rowCount; row++) {
                for (let col = displayRange.firstColumn; col < displayRange.columnCount; col++) {
                    // Read the Cell value (stringValue property)
                    const cell = displayRange.get(row, col);
                    outputLines.push(cell.stringValue);
                    console.log(cell.stringValue);
                }
            }

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```  

### **Использование MaxDataRow и MaxDataColumn**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result { margin-top: 15px; max-height: 400px; overflow: auto; border: 1px solid #ddd; padding: 10px; }
            .cell-value { padding: 2px 0; border-bottom: 1px dashed #eee; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Read Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;

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

        function escapeHtml(text) {
            if (text === null || text === undefined) return '';
            return String(text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p class="error">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells2 = workbook.worksheets.get(0).cells;
            const maxDataRow = cells2.maxDataRow;
            const maxDataColumn = cells2.maxDataColumn;

            const outputLines = [];
            // Loop over all cells
            for (let row = 0; row <= maxDataRow; row++) {
                for (let col = 0; col <= maxDataColumn; col++) {
                    // Read the Cell value
                    const currentCell = cells2.checkCell(row, col);
                    if (currentCell) {
                        const cellText = currentCell.stringValue;
                        outputLines.push('<div class="cell-value">' + escapeHtml(cellText) + '</div>');
                        console.log(cellText);
                    }
                }
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p>No cell values found.</p>';
            } else {
                resultDiv.innerHTML = outputLines.join('');
            }
        });
    </script>
</html>
```  

Как видите, оба вышеупомянутых подхода используют более или менее похожую логику: цикл по всем ячейкам в коллекции для чтения значений ячеек. Это может вызвать проблемы по ряду причин, о которых рассказано ниже.  

1. API такие как [**maxRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxRow--), [**maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--), [**maxColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxColumn--), [**maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) и [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) требуют дополнительного времени для сбора соответствующей статистики. Если размер матрицы данных (строки x столбцы) велик, использование этих API может сказаться на производительности.  
1. В большинстве случаев не все ячейки в заданном диапазоне созданы. В таких ситуациях проверка каждой ячейки в матрице не так эффективна, как проверка только инициализированных ячеек.  
1. Доступ к ячейке в цикле в виде Cells row, column заставит создавать все объекты ячеек в диапазоне, что в конечном итоге может вызвать исключение OutOfMemoryException.  

## **Заключение**  

Исходя из вышеуказанных фактов, возможны следующие сценарии использования перечислителей.  

1. Требуется только чтение коллекции ячеек, то есть только проверка ячеек.  
1. Необходимо пройти большое количество ячеек.  
1. Требуется пройти только инициализированные ячейки/строки/столбцы.
