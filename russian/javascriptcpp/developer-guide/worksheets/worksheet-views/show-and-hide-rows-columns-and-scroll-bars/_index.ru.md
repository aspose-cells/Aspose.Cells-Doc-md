---
title: Показать и скрыть строки, столбцы и полосы прокрутки с помощью JavaScript через C++
linktitle: Показать и скрыть строки, столбцы и полосы прокрутки
type: docs
weight: 20
url: /ru/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/
description: В этой статье показано, как программно отображать и скрывать строки и столбцы листа Excel с помощью JavaScript через C++. Управляйте видимостью полос прокрутки и эффективно скрывайте несколько строк и столбцов.
---

{{% alert color="primary" %}}  
Aspose.Cells предоставляет способы управления видимостью строк, столбцов и полос прокрутки листа.  
{{% /alert %}}  

## **Показ и скрытие строк и столбцов**  

Aspose.Cells for JavaScript через C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет разработчикам получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--), которая отображает все ячейки на листе. Коллекция [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) содержит несколько методов управления строками или столбцами листа. Некоторые из них рассмотрены ниже.  

### **Показать строки и столбцы**  

Разработчики могут отображать любой скрытый ряд или столбец, вызвав методы [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) и [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) соответственно. Оба метода требуют два параметра:  

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.  
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unhide Row and Column Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.unhideRow(2, 13.5);
            worksheet.cells.unhideColumn(1, 8.5);

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
При восстановлении скрытого столбца, если необходимо вернуть его к ранее назначенной ширине или к исходной ширине, пожалуйста, сделайте его неподсвеченным с отрицательной шириной. Например: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Скрыть строки и столбцы**  

Разработчики могут скрывать строки или столбцы, вызвав методы [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) и [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) соответственно. Оба метода требуют индекс строки или столбца, чтобы скрыть конкретный элемент.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Hide Row/Column Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Hide the 3rd row (index 2) and 2nd column (index 1)
            worksheet.cells.hideRow(2);
            worksheet.cells.hideColumn(1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row and column hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.  
{{% /alert %}}  

### **Скрыть несколько строк и столбцов**  

Разработчики могут скрывать несколько строк или столбцов одновременно, вызвав методы [**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-) и [**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) соответственно. Оба метода требуют начальный индекс строки или столбца и количество скрываемых строк или столбцов в качестве параметров.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Rows and Columns</title>
    </head>
    <body>
        <h1>Hide Rows and Columns Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4 and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Показывать и скрывать полосы прокрутки**  

Полосы прокрутки используются для навигации по содержимому любого файла. Обычно существует два типа полос прокрутки:  

- Вертикальные полосы прокрутки  
- Горизонтальные полосы прокрутки  

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли пролистывать содержимое листа Excel. Используя Aspose.Cells, разработчики могут контролировать видимость обоих типов полос прокрутки в файлах Excel.  

### **Управление видимостью полос прокрутки**  

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит широкий спектр свойств и методов для управления файлом Excel. Для управления видимостью полос прокрутки используйте свойства [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) и [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) и [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) — логические свойства, означающие, что эти свойства могут хранить только значения **true** или **false**.  

#### **Отображение полос прокрутки**  

Делайте полосы прокрутки видимыми, устанавливая свойства [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) или [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) в **true**.  

#### **Скрытие полос прокрутки**  

Скрыть полосы прокрутки, установив свойства [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) или [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) в **false**.  

**Пример кода**  

Ниже приведен полный код, который открывает файл Excel, book1.xls, скрывает оба ползунка прокрутки, а затем сохраняет измененный файл как output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Hide Scrollbars Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the vertical scroll bar of the Excel file
            workbook.settings.isVScrollBarVisible = false;

            // Hiding the horizontal scroll bar of the Excel file
            workbook.settings.isHScrollBarVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scrollbars hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
