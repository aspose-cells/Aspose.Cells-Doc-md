---
title: Копировать и перемещать листы внутри и между книгами с помощью JavaScript через C++
linktitle: Копирование и перемещение листов внутри и между книгами
type: docs
weight: 80
url: /ru/javascript-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Узнайте, как копировать и перемещать листы внутри и между книгами с помощью Aspose.Cells for JavaScript через C++. Эффективно управлять структурой ваших книг.
---

{{% alert color="primary" %}}

Иногда вам требуется несколько листов с общим форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вам может понадобиться создать книгу с листами, содержащими одни и те же заголовки столбцов, заголовки строк и формулы. Есть способ сделать это: создав один лист, а затем скопировав его три раза.

Aspose.Cells for JavaScript через C++ поддерживает копирование или перемещение листов внутри или между книгами. Листы, включая данные, форматирование, таблицы, матрицы, графики, изображения и другие объекты, копируются с максимальной точностью.

{{% /alert %}}

## **Копирование и перемещение листов**

### **Копирование листа внутри книги**

Начальные шаги одинаковы для всех примеров.

1. Создайте две книги с некоторыми данными в Microsoft Excel. Для целей этого примера мы создали две новые книги в Microsoft Excel и ввели некоторые данные на листах.

- FirstWorkbook.xlsx (3 листа).
- SecondWorkbook.xlsx (1 лист).

1. Скачайте и установите Aspose.Cells:
   1. [Скачать Aspose.Cells for JavaScript через C++](https://downloads.aspose.com/cells/javascript-cpp).
   1. Установите его на вашем компьютере для разработки.
      Все [Aspose](http://www.aspose.com/) компоненты при установке работают в режиме оценки. Режим оценки не имеет временных ограничений и вставляет только водяные знаки в созданные документы.
1. Создайте проект:
   1. Начните свой рабочий окружение.
   1. Создайте новое консольное приложение.
1. Добавьте ссылки:
   1. Добавьте ссылку на Aspose.Cells в проект.
      Например, добавьте ссылку на ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Скопируйте лист в книге.
   Первый пример копирует первый лист (Copy) внутри FirstWorkbook.xlsx.

При выполнении кода лист с именем Copy копируется внутри FirstWorkbook.xlsx с именем Последний лист.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheet Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Copy the first sheet of the first book within the workbook
            workbook.worksheets.get(2).copy(workbook.worksheets.get("Copy"));

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookCopied_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Перемещение листа внутри книги**

Приведенный ниже код показывает, как переместить лист с одной позиции в книге на другую. При выполнении кода лист с именем Move из индекса 1 перемещается на индекс 2 внутри FirstWorkbook.xlsx.

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Move the first sheet to index 1
            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            worksheet.moveTo(1);

            // Saving the modified Excel file and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookMoved_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Копирование листа между книгами Excel**

Выполнение кода копирует лист с именем Copy в SecondWorkbook.xlsx с именем Sheet2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
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
            // Create two workbooks
            const excelWorkbook3 = new Workbook();
            const excelWorkbook4 = new Workbook();

            // Create source worksheet
            excelWorkbook3.worksheets.add("Copy");

            // Add new worksheet into second Workbook
            excelWorkbook4.worksheets.add();

            // Copy the first sheet of the first book into second book.
            excelWorkbook4.worksheets.get(1).copy(excelWorkbook3.worksheets.get("Copy"));

            // Save the file.
            const outputData = excelWorkbook4.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheets copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Перемещение листа между книгами Excel**

При выполнении кода лист с именем Move перемещается из FirstWorkbook.xlsx в SecondWorkbook.xlsx с именем Sheet3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download First Workbook</a>
        <a id="downloadLink2" style="display: none;">Download Second Workbook</a>
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
            // Create new workbooks instead of opening existing files
            const excelWorkbook5 = new Workbook();
            const excelWorkbook6 = new Workbook();

            // Add New Worksheet
            excelWorkbook6.worksheets.add();

            // Copy the sheet from first book into second book.
            excelWorkbook6.worksheets.get(0).copy(excelWorkbook5.worksheets.get(0));

            // Remove the copied worksheet from first workbook
            excelWorkbook5.worksheets.removeAt(0);

            // Save the first workbook
            const outputData1 = excelWorkbook5.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'FirstWorkbookWithMove_out.xlsx';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download FirstWorkbookWithMove_out.xlsx';

            // Save the second workbook
            const outputData2 = excelWorkbook6.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SecondWorkbookWithMove_out.xlsx';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download SecondWorkbookWithMove_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks processed successfully. Click the download links to retrieve the files.</p>';
        });
    </script>
</html>
```
