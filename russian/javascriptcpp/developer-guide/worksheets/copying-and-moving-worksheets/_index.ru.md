---
title: Копирование и перемещение листов с помощью JavaScript через C++
linktitle: Копирование и перемещение рабочих листов
type: docs
weight: 10
url: /ru/javascript-cpp/copying-and-moving-worksheets/
description: Эта статья включает пример кода и описывает, как программно копировать и перемещать листы внутри рабочей книги Excel и между рабочими книгами Excel с помощью API JavaScript через C++.
keywords: копировать лист JavaScript, перемещать лист JavaScript
---

{{% alert color="primary" %}}

Иногда вам действительно нужно несколько рабочих листов с общим форматированием и данными. Например, если вы работаете с квартальными бюджетами, вам может потребоваться создать книгу с листами, содержащими одинаковые заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создав один лист, а затем скопировав его.

Aspose.Cells for JavaScript через C++ поддерживает копирование и перемещение листов внутри или между книгами. Лист, содержащий данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты, копируется с максимальной точностью.

{{% /alert %}}

## **Перемещение или копирование листов с использованием Microsoft Excel**

Ниже приведены шаги для копирования и перемещения листов внутри или между книгами в Microsoft Excel.

1. Чтобы переместить или скопировать листы в другую рабочую книгу, откройте рабочую книгу, которая будет получать листы.
1. Переключитесь на рабочую книгу, которая содержит листы, которые вы хотите переместить или скопировать, а затем выберите листы.
1. На меню **Правка** щелкните **Переместить или скопировать лист**.
1. В диалоговом окне **В книгу** щелкните книгу, которая получит листы.
1. Чтобы переместить или скопировать выбранные листы в новую книгу, щелкните **Новая книга**.
1. В поле **Перед листом** щелкните лист, перед которым вы хотите вставить перемещенные или скопированные листы.
1. Чтобы скопировать листы вместо их перемещения, выберите флажок **Создать копию**.

### **Копирование листов внутри рабочей книги с помощью Aspose.Cells for JavaScript через C++**

Aspose.Cells предоставляет перегруженный метод [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#addCopy-number-), который используется для добавления листа в коллекцию и копирования данных с существующего листа. Одна версия метода принимает индекс исходного листа в качестве параметра. Другая версия принимает имя исходного листа.

В следующем примере показано, как скопировать существующий лист в рамках рабочей книги.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Sheet Within Workbook</title>
    </head>
    <body>
        <h1>Copy Sheet Within Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Open an existing Excel file.
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = wb.worksheets;

            // Copy data to a new sheet from an existing sheet within the Workbook.
            sheets.addCopy("Sheet1");

            // Save the Excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWithinWorkbook_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Sheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Копировать листы между рабочими книгами**

Aspose.Cells предоставляет метод, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-), используемый для копирования данных и форматирования из исходного листа в другой лист внутри или между рабочими книгами. Метод принимает объект исходного листа в качестве параметра.

В следующем примере показано, как скопировать лист из одной рабочей книги в другую рабочую книгу.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheets Between Workbooks</title>
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
        <p>Select the source Excel file (book1.xls) to copy its first worksheet into a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (book1.xls).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook from the uploaded file (source workbook)
            const excelWorkbook0 = new Workbook(new Uint8Array(arrayBuffer));

            // Create another Workbook (destination workbook)
            const excelWorkbook1 = new Workbook();

            // Copy the first sheet of the first book into second book.
            excelWorkbook1.worksheets.get(0).copy(excelWorkbook0.worksheets.get(0));

            // Save the file as Excel 97-2003 (.xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Copied Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

В следующем примере показано, как скопировать лист из одной рабочей книги в другую рабочую книгу.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Between Workbooks Example</h1>
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
            // Create a new Workbook.
            const excelWorkbook0 = new Workbook();

            // Get the first worksheet in the book.
            const ws0 = excelWorkbook0.worksheets.get(0);

            // Put some data into header rows (A1:A4)
            for (let i = 0; i < 5; i++) {
                ws0.cells.get(i, 0).value = `Header Row ${i}`;
            }

            // Put some detail data (A5:A999)
            for (let i = 5; i < 1000; i++) {
                ws0.cells.get(i, 0).value = `Detail Row ${i}`;
            }

            // Define a pagesetup object based on the first worksheet.
            const pagesetup = ws0.pageSetup;

            // The first five rows are repeated in each page...
            // It can be seen in print preview.
            pagesetup.printTitleRows = "$1:$5";

            // Create another Workbook.
            const excelWorkbook1 = new Workbook();

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Name the worksheet.
            ws1.name = "MySheet";

            // Copy data from the first worksheet of the first workbook into the
            // first worksheet of the second workbook.
            ws1.copy(ws0);

            // Saving the modified Excel file
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetFromWorkbookToOther_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and worksheet copied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Перемещение листов в рамках рабочей книги**

Aspose.Cells предоставляет метод [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#moveto-number-), используемый для перемещения листа в другое место в той же таблице. Метод принимает индекс целевого листа в качестве параметра.

В следующем примере показано, как переместить лист в другое место внутри рабочей книги.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheet Example</h1>
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
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = wb.worksheets;

            // Get the first worksheet
            const worksheet = sheets.get(0);

            // Move the first sheet to the third position (index 2)
            worksheet.moveTo(2);

            // Save the modified workbook in Excel97-2003 format
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MoveWorksheet_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
