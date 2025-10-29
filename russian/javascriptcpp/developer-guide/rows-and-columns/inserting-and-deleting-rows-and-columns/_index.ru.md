---
title: Вставка и удаление строк и столбцов файлов Excel
linktitle: Вставка и удаление строк и столбцов
type: docs
weight: 70
url: /ru/javascript-cpp/inserting-and-deleting-rows-and-columns/
description: Эта статья показывает, как вставлять и удалять строки и столбцы с помощью API Aspose.Cells for JavaScript через C++.
keywords: Aspose.Cells JavaScript через C++ управляет строками и столбцами, вставляет строки и столбцы, удаляет строки и столбцы
---

## **Введение**

При создании нового листа Excel с нуля или работе с существующим листом нам может потребоваться добавить дополнительные строки или столбцы для размещения большего объема данных. Напротив, также может потребоваться удалить строки или столбцы из указанных позиций в листе. 
 Чтобы выполнить эти требования, Aspose.Cells for JavaScript через C++ предоставляет очень простые классы и методы, обсуждаемые ниже.

### **Управлять строками и столбцами**

Aspose.Cells for JavaScript через C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), которая позволяет доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--), которая представляет все клетки листа.

Коллекция [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) предоставляет несколько методов для управления строками и столбцами в листе. Некоторые из них приведены ниже.

{{% alert color="primary" %}}

При добавлении строк или столбцов содержимое листа смещается вниз или вправо, а при удалении — вверх или влево.

{{% /alert %}}


## **Вставить строки и столбцы**

### **Как вставить строку**

Вставьте строку в лист на любую позицию, вызвав метод [**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Метод [**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) принимает индекс строки, в которую будет вставлена новая строка.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert Row Example</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting a row into the worksheet at 3rd position (index 2)
            worksheet.cells.insertRow(2);

            // Saving the modified Excel file as Excel97To2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Как вставить несколько строк**

Чтобы вставить несколько строк в лист, вызовите метод [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Метод [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) принимает два параметра:

- Индекс строки, индекс строки, с которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Rows Example</title>
    </head>
    <body>
        <h1>Insert Rows Example</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting 10 rows into the worksheet starting at index 2
            worksheet.cells.insertRows(2, 10);

            // Saving the modified Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Как вставить строку с форматированием**

Для вставки строки с параметрами форматирования используйте перегрузку [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-), которая принимает [**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions) в качестве параметра. Установите свойство [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) класса [**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions) со значением [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) Enum. Перечисление [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) содержит три члена, перечисленные ниже.

- SameAsAbove: Форматирует строку так же, как и вышеуказанная.
- SameAsBelow: Форматирует строку так же, как и ниже расположенная строка.
- Очистить: Очищает форматирование.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Inserting a Row With Formatting Example</title>
    </head>
    <body>
        <h1>Inserting a Row With Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, InsertOptions, CopyFormatType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting Formatting options
            const insertOptions = new InsertOptions();
            insertOptions.copyFormatType = CopyFormatType.SameAsAbove;

            // Inserting a row into the worksheet at 3rd position
            worksheet.cells.insertRows(2, 1, insertOptions);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertingARowWithFormatting.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Как вставить столбец**

Разработчики также могут вставлять столбец в лист в любой точке, вызвав метод [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertColumn-number-boolean-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Метод [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertColumn-number-boolean-) принимает индекс столбца, в который будет вставлен новый столбец.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Insert Column Example</title>
    </head>
    <body>
        <h1>Insert Column Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting a column into the worksheet at 2nd position
            worksheet.cells.insertColumn(1);

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Удалить строки и столбцы**

### **Как удалить несколько строк**

Для удаления нескольких строк из листа вызовите метод [**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Метод [**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые нужно удалить.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Delete Rows Example</title>
    </head>
    <body>
        <h1>Delete Rows Example</h1>
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

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Deleting 10 rows from the worksheet starting from 3rd row (index 2)
            worksheet.cells.deleteRows(2, 10);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Как удалить столбец**

Чтобы удалить столбец из листа в любой точке, вызовите метод [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteColumn-number-boolean-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Метод [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteColumn-number-boolean-) принимает индекс столбца для удаления.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Column Example</title>
    </head>
    <body>
        <h1>Delete Column Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Deleting a column from the worksheet at 5th position (zero-based index 4)
            worksheet.cells.deleteColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
