---
title: Доступ к ячейкам листа
type: docs
weight: 10
url: /ru/javascript-cpp/accessing-cells-of-a-worksheet/
description: В этой статье показано, как получить максимальный диапазон отображения листа и доступ к ячейкам через API Aspose.Cells for JavaScript через C++.
keywords: Получить объект ячейки, доступ к ячейкам, получить максимальный диапазон отображения листа. 
---

{{% alert color="primary" %}}

Мы знаем, что все листы могут содержать данные, по сути хранящиеся в ячейках (из которых состоит лист). Ячейка — это базовая часть листа, используемая для создания всего листа как последовательности строк и столбцов. Прежде чем пытаться получить доступ к данным листа, нам нужно получить доступ к его ячейкам. В этой теме мы обсудим некоторые основные подходы к доступу к ячейкам листа во время выполнения с помощью Aspose.Cells for JavaScript через C++.

{{% /alert %}}

## **Как получить доступ к ячейкам**

Aspose.Cells for JavaScript через C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), позволяющий получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), которая отображает все ячейки в листе.

Мы можем использовать коллекцию [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) для доступа к ячейкам на листе. Aspose.Cells for JavaScript через C++ предоставляет три основных подхода к доступу к ячейкам листа:

1. Использование имени ячейки.
2. Использование индекса строки и столбца ячейки.
1. Использование индекса ячейки в коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)

 Мы отметили, что 3-й подход является самым быстрым, а 1-й подход является самым медленным. Разница в производительности между подходами очень невелика, поэтому не беспокойтесь о снижении производительности, какой бы подход вы ни использовали.

### **Как получить объект Ячейки по имени ячейки**

Разработчики могут получить доступ к любой конкретной ячейке, передав её имя в коллекцию [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) в качестве индекса.

Если вы создаете пустой лист в начале, количество коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) равно нулю. Используя этот подход для доступа к ячейке, он проверит, существует ли такая ячейка в коллекции. Если да, он возвращает объект ячейки из коллекции, иначе создает новый объект [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), добавляет его в коллекцию [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), и затем возвращает объект. Этот подход — самый простой для тех, кто знаком с Microsoft Excel, однако он самый медленный по сравнению с другими подходами.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Как получить объект Ячейки по индексу строки и столбца ячейки**

Разработчики могут получить доступ к любой конкретной ячейке, передав индексы её строки и столбца в коллекцию [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

Этот подход работает так же, как и первый подход.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **Как получить объект Ячейки по индексу ячейки в коллекции ячеек**

Ячейка также может быть получена путем передачи её числового индекса в коллекцию [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

Если использовать этот подход для доступа к ячейкам, может возникнуть исключение, если числовой индекс ячейки выходит за диапазон. Этот подход — самый быстрый для доступа к ячейкам, но важно знать, что при использовании этого способа объект ячейки может измениться после добавления новых ячеек в коллекцию [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Объекты ячеек в коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) сортированы по индексам строк и столбцов внутри.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **Как получить максимальный диапазон отображения листа**

Aspose.Cells for JavaScript через C++ позволяет разработчикам получать доступ к максимальному диапазону отображения листа. Максимальный диапазон отображения — диапазон ячеек между первой и последней содержашейся ячейкой — полезен при необходимости копировать, выбирать или отображать все содержимое листа на изображении.

Вы можете получить максимальный диапазон отображения листа, используя [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--). Следующий пример кода показывает, как получить свойство [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```
