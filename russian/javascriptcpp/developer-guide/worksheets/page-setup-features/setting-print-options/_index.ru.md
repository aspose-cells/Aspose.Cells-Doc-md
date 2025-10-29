---
title: Настройка параметров печати с помощью JavaScript через C++
linktitle: Настройка параметров печати
type: docs
weight: 40
url: /ru/javascript-cpp/setting-print-options/
description: В этой статье показано, как программно установить параметры печати функции настройки страницы листа Excel с использованием API JavaScript и библиотеки C++. Вы можете установить область печати, названия печати и порядок страниц.
keywords: установить область печати Excel JavaScript через C++, установить названия печати Excel JavaScript через C++, установить порядок страниц Excel JavaScript через C++
---

{{% alert color="primary" %}}

Настройки страницы установки Microsoft Excel предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям контролировать порядок печати листов рабочей книги.

{{% /alert %}}

## **Установка параметров печати**

Эти параметры печати позволяют пользователям:

- Выбрать конкретную область печати на рабочем листе.
- Напечатать заголовки.
- Напечатать сетку.
- Печать верхних заголовков строк / столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.

Aspose.Cells for JavaScript через C++ поддерживает все параметры печати, предлагаемые Microsoft Excel, и разработчики могут легко настроить эти параметры для листов, используя свойства, предоставленные классом [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). Как использовать эти свойства, обсуждается ниже более подробно.

### **Установка области печати**

По умолчанию область печати включает все области листа, содержащие данные. Разработчики могут установить конкретную область печати листа.

Чтобы выбрать конкретную область печати, используйте свойство [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) класса [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). Назначьте этому свойству диапазон ячеек, определяющий область печати.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Area Example</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Specifying the cells range (from A1 cell to T35 cell) of the print area
            pageSetup.printArea = "A1:T35";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintArea_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Установка заголовков для печати**

Aspose.Cells позволяет назначить заголовки строк и столбцов для повторения на всех страницах напечатанного листа. Для этого используйте свойства [**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--) и [**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--) класса [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup).

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строки или столбца. Например, строки определяются как $1:$2, а столбцы определяются как $A:$B.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Title</title>
    </head>
    <body>
        <h1>Set Print Title Columns and Rows Example</h1>
        <p>You may optionally select an existing Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Defining column numbers A & B as title columns
            pageSetup.printTitleColumns = "$A:$B";

            // Defining row numbers 1 & 2 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintTitle_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print title columns and rows set successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **Настройка Других Опций Печати**

Класс [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) также предоставляет несколько других свойств для установки общих параметров печати следующим образом:

- [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--): логическое свойство, определяющее, следует ли печатать сетки или нет.
- [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--): логическое свойство, определяющее, следует ли печатать заголовки строк и столбцов или нет.
- [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--): логическое свойство, определяющее, следует ли печатать рабочий лист в чёрно-белом режиме или нет.
- [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--): определяет, отображать ли комментарии для печати на рабочем листе или в конце рабочего листа.
- [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--): логическое свойство, определяющее, следует ли печатать лист без графики.
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--): определяет, следует ли печатать ошибки ячейки как отображаемые, пустые, тире или N/A.

Для установки свойств [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) и [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) Aspose.Cells for JavaScript через C++ также предоставляет два перечисления, [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) и [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype), содержащие предопределённые значения, которые можно назначить свойствам [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) и [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) соответственно.

Предопределённые значения в перечислении [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) перечислены ниже с их описаниями.

|**Типы Примечаний к Печати**|**Описание**|
| :- | :- |
|PrintInPlace|Указывает на печать комментариев как отображаемых в таблице.|
|PrintNoComments|Указывает, что комментарии не нужно печатать.|
|PrintSheetEnd|Указывает на печать комментариев в конце таблицы.|

Предопределённые значения перечисления [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) перечислены ниже с их описаниями.

|**Типы Ошибок Печати**|**Описание**|
| :- | :- |
|PrintErrorsBlank|Указывает, что ошибки не нужно печатать.|
|PrintErrorsDash|Указывает на печать ошибок как "--".|
|PrintErrorsDisplayed|Указывает на печать ошибок как отображаемых.|
|PrintErrorsNA|Указывает на печать ошибок как "#N/A".|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Other Print Options</title>
    </head>
    <body>
        <h1>Other Print Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintCommentsType, PrintErrorsType } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = PrintErrorsType.PrintErrorsNA;

            // Saving the modified workbook to Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OtherPrintOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Установить порядок страниц**

Класс [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) предоставляет свойство [**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--), которое используется для сортировки нескольких страниц вашего рабочего листа для печати. Есть два варианта порядка страниц.

-  печатать все страницы снизу вверх перед печатью страниц справа.
-  печатать страницы слева направо перед печатью страниц ниже.

Aspose.Cells предоставляет перечисление [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype), которое содержит все предопределённые типы порядка.

Предопределённые значения перечисления [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) приведены ниже.

|**Типы порядка печати**|**Описание**|
| :- | :- |
|DownThenOver|Представляет порядок печати как сначала вниз, затем вправо.|
|OverThenDown|Представляет порядок печати как сначала вправо, затем вниз.|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Set Page Order Example</title>
    </head>
    <body>
        <h1>Set Page Order Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintOrderType } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;
            pageSetup.order = PrintOrderType.OverThenDown;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPageOrder_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page order set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
