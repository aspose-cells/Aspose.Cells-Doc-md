---
title: Создавайте доступ и копируйте именованные диапазоны с помощью JavaScript через C++
linktitle: Создание доступа и копирование именованных диапазонов
type: docs
weight: 200
url: /ru/javascript-cpp/create-access-and-copy-named-ranges/
description: Узнайте, как создавать, получать доступ и копировать именованные диапазоны в Excel с помощью Script через C++.
---

## **Введение**  

Обычно метки столбцов и строк используются для ссылки на отдельные ячейки. Можно создавать описательные имена для представления ячеек, диапазонов ячеек, формул или постоянных значений. слово **имя** может относиться к строке символов, которая представляет ячейку, диапазон ячеек, формулу или постоянное значение. Назначение имени диапазону означает, что этот диапазон ячеек можно ссылаться по имени. Используйте легкие для понимания имена, такие как Products, чтобы обозначать сложные диапазоны, такие как Sales!C20:C30. Метки можно использовать в формулах, ссылающихся на данные на той же рабочей странице; если хотите представить диапазон на другой странице, можно использовать имя. *Именованные диапазоны — одна из самых мощных функций Microsoft Excel, особенно при использовании в качестве исходных диапазонов для списков, сводных таблиц, графиков и т. д.*  

## **Работа с именованным диапазоном с помощью Microsoft Excel**  

### **Создание именованных диапазонов**  

Следующие шаги описывают, как назвать ячейку или диапазон ячеек с помощью **MS Excel**. Этот метод применяется к **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** и **2002**.  

1. Выберите ячейку или диапазон ячеек, которые хотите назвать.  
2. Нажмите **Пакетное имя** слева на строке формул.  
3. Введите название для ячеек.  
4. Нажмите ENTER.  

{{% alert color="primary" %}}  
Вы не можете называть ячейку, когда вы изменяете содержимое ячейки.  
{{% /alert %}}  

## **Работа с именованным диапазоном с использованием Aspose.Cells**  

Здесь мы используем API Aspose.Cells для выполнения этой задачи.  
Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).  

### **Создание именованного диапазона**  

Можно создать именованный диапазон, вызвав перегруженный метод [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) коллекции [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Типичная версия метода [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) принимает следующие параметры:  

- Имя верхней левой ячейки, имя верхней левой ячейки в диапазоне.  
- Имя нижней правой ячейки, имя нижней правой ячейки в диапазоне.  

Когда вызывается метод [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-), он возвращает только что созданный диапазон в виде экземпляра класса [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). Используйте этот объект [**Range**](https://reference.aspose.com/cells/javascript-cpp/range), чтобы настроить именованный диапазон. Например, установите имя диапазона, используя свойство [**name**](https://reference.aspose.com/cells/javascript-cpp/range/#name--). В следующем примере показано, как создать именованный диапазон ячеек, который простирается от B4:G14.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Creating a named range
            const range = worksheet.cells.createRange("B4", "G14");

            // Setting the name of the named range
            range.name = "TestRange";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Ввод данных в ячейки именованного диапазона**  

Можно вставить данные в отдельные ячейки диапазона, следуя образцу  

- **JavaScript**: Диапазон[строка, столбец]  

Предположим, у вас есть именованный диапазон ячеек, который охватывает A1:C4. Матрица состоит из 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].  

Используйте следующие свойства для определения ячеек в диапазоне:  

- firstRow возвращает индекс первой строки в именованном диапазоне.  
- firstColumn возвращает индекс первого столбца в именованном диапазоне.  
- rowCount возвращает общее количество строк в именованном диапазоне.  
- columnCount возвращает общее количество столбцов в именованном диапазоне.  

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = workbook.worksheets.get(0);

            // Create a range of cells based on H1:J4.
            const range = worksheet1.cells.createRange("H1", "J4");

            // Name the range.
            range.name = "MyRange";

            // Input some data into cells in the range.
            range.get(0, 0).value = "USA";
            range.get(0, 1).value = "SA";
            range.get(0, 2).value = "Israel";
            range.get(1, 0).value = "UK";
            range.get(1, 1).value = "AUS";
            range.get(1, 2).value = "Canada";
            range.get(2, 0).value = "France";
            range.get(2, 1).value = "India";
            range.get(2, 2).value = "Egypt";
            range.get(3, 0).value = "China";
            range.get(3, 1).value = "Philipine";
            range.get(3, 2).value = "Brazil";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rangecells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range populated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **Определение ячеек в именованном диапазоне**  

Вы можете вставить данные в отдельные ячейки диапазона, следуя шаблону:  

- **JavaScript**: Диапазон[строка, столбец]  

Если у вас есть именованный диапазон, который охватывает A1:C4. Матрица делает 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].  

Используйте следующие свойства для определения ячеек в диапазоне:  

- firstRow возвращает индекс первой строки в именованном диапазоне.  
- firstColumn возвращает индекс первого столбца в именованном диапазоне.  
- rowCount возвращает общее количество строк в именованном диапазоне.  
- columnCount возвращает общее количество столбцов в именованном диапазоне.  

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Named Range</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const range = workbook.worksheets.rangeByName("TestRange");

            if (!range) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
                return;
            }

            // Identify range cells and display properties
            const firstRow = range.firstRow;
            const firstColumn = range.firstColumn;
            const rowCount = range.rowCount;
            const columnCount = range.columnCount;

            const html = [
                `<p>First Row : ${firstRow}</p>`,
                `<p>First Column : ${firstColumn}</p>`,
                `<p>Row Count : ${rowCount}</p>`,
                `<p>Column Count : ${columnCount}</p>`
            ].join('');

            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

### **Доступ к именованным диапазонам**  

#### **Доступ к конкретному именованному диапазону**  

Вызовите метод [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) коллекции [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), чтобы получить диапазон по указанному имени. Типичный метод [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) принимает имя именованного диапазона и возвращает указанный именованный диапазон как экземпляр класса [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). В следующем примере показано, как получить доступ к указанному диапазону по его имени.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const worksheets = workbook.worksheets;
            const range = worksheets.rangeByName("TestRange");

            if (range !== null) {
                document.getElementById('result').innerHTML = `<p>Named Range : ${range.refersTo}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
            }
        });
    </script>
</html>
```  

#### **Доступ ко всем именованным диапазонам в электронной таблице**  

Вызовите метод [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) коллекции [**worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), чтобы получить все именованные диапазоны в электронной таблице. Метод [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) возвращает массив всех именованных диапазонов в коллекции [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection).  

В следующем примере показано, как получить доступ ко всем именованным диапазонам в книге.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Named Ranges</title>
    </head>
    <body>
        <h1>Get Named Ranges Example</h1>
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

            // Getting all named ranges
            const ranges = workbook.worksheets.namedRanges;

            if (ranges) {
                // Some collections expose 'count', others may expose 'length'
                const total = (typeof ranges.count !== 'undefined') ? ranges.count : ranges.length;
                document.getElementById('result').innerHTML = `<p style="color: green;">Total Number of Named Ranges: ${total}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No named ranges found.</p>';
            }
        });
    </script>
</html>
```  

### **Копировать именованные диапазоны**  

Aspose.Cells предоставляет метод [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-pasteoptions-) для копирования диапазона ячеек с форматированием в другой диапазон.  

В следующем примере показано, как скопировать исходный диапазон ячеек в другой именованный диапазон.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Ranges</title>
    </head>
    <body>
        <h1>Copy Ranges Example</h1>
        <p>Select an Excel file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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

            // Instantiate a new Workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = workbook.worksheets.get(0);

            // Create a range of cells.
            const range1 = worksheet.cells.createRange("E12", "I12");

            // Name the range.
            range1.name = "MyRange";

            // Set the outline border to the range.
            range1.outlineBorder = { borderType: BorderType.TopBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.BottomBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.LeftBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.RightBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };

            // Input some data with some formattings into a few cells in the range.
            range1.get(0, 0).putValue("Test");
            range1.get(0, 4).putValue("123");

            // Create another range of cells.
            const range2 = worksheet.cells.createRange("B3", "F3");

            // Name the range.
            range2.name = "testrange";

            // Copy the first range into second range.
            range2.copy(range1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyranges.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
