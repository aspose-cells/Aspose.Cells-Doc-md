---
title: Как распечатать Excel как умещающиеся страницы по ширине и высоте с помощью JavaScript через C++
linktitle: Как напечатать Excel так, чтобы страницы были шириной и высотой, подогнанными под страницу
type: docs
weight: 200
url: /ru/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: В этой статье приводится код, объясняющий, как установить FitToPagesWide и FitToPagesTall с помощью Aspose.Cells for JavaScript через C++.
keywords: JavaScript через C++ Как установить FitToPagesWide и FitToPagesTall, как добавить FitToPagesWide и FitToPagesTall в JavaScript, как установить FitToPagesWide и FitToPagesTall в Excel, как очистить FitToPagesWide и FitToPagesTall в Excel, как распечатать Excel как умещающиеся страницы по ширине и высоте, как распечатать лист как одну страницу, как распечатать все столбцы листа на одной странице.
---

## **Введение**

Настройки FitToPagesWide и FitToPagesTall используются в приложениях для работы с таблицами (таких как Microsoft Excel), чтобы контролировать масштабирование при печати. Эти настройки помогают обеспечить, чтобы напечатанный результат поместился на указанное количество страниц, как по горизонтали, так и по вертикали. Вот разъяснение каждого из параметров:

1. FitToPagesWide: Эта настройка задает количество страниц по ширине, в которые должна поместиться распечатка. Например, установка значения в 1 означает, что содержимое масштабируется для размещения на одной странице по ширине, независимо от ширины таблицы.
2. FitToPagesTall: Эта настройка определяет количество страниц по вертикали, в которые должна поместиться распечатанная часть. Например, установка FitToPagesTall в 1 означает, что содержимое масштабируется для размещения на одной высоте страницы, независимо от количества строк.

## **Зачем использовать FitToPagesWide и FitToPagesTall**
Вот некоторые причины установки FitToPagesWide и FitToPagesTall:
1. Контроль над размещением при печати: задавая количество страниц по ширине и высоте, вы можете убедиться, что ваш печатный документ легко читаем и хорошо отформатирован, без нежелательного переноса столбцов или строк между страницами.
2. Последовательность: Если вы печатаете несколько листов или отчетов, использование этих настроек помогает поддерживать последовательный формат, что облегчает сравнение и анализ печатных документов.
3. Профессиональный вид: Правильное масштабирование и подгонка содержимого под заданное количество страниц могут сделать ваш документ более аккуратным и профессиональным.

## **Как распечатать файл по страницам по ширине и высоте в Excel**

Чтобы установить параметры FitToPagesWide и FitToPagesTall в Microsoft Excel, выполните следующие шаги:

1. Откройте рабочую книгу Excel и перейдите к листу, который хотите распечатать.
2. Перейдите на вкладку Макет страницы на ленте.
3. В группе Настройка страницы щёлкните по маленькой стрелке в правом нижнем углу, чтобы открыть диалоговое окно Настройка страницы.
4. В диалоговом окне Настройка страницы перейдите на вкладку Страница.
5. В разделе Масштабирование выберите опцию "По размеру" и укажите желаемое число страниц по ширине и высоте: Введите желаемое число страниц по ширине в первое поле (по ширине x страниц). Введите желаемое число страниц по высоте во второе поле (по высоте y страниц).
<br>
<img src="2.png" width=60% />

Нажмите OK, чтобы применить настройки.

## **Как распечатать Excel как умещающиеся страницы по ширине и высоте с помощью Aspose.Cells for JavaScript через C++**

Чтобы установить FitToPagesWide и FitToPagesTall для указанного листа: сначала загрузите [пример файла](input.xlsx), затем необходимо изменить свойства [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) и [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) объекта [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) для желаемого листа. Вот пример на JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Результат вывода:
<br>
<img src="1.png" width=60% />

## **Как напечатать лист как одну страницу с использованием Aspose.Cells for JavaScript через C++**

Для печати листа как одной страницы: сначала загрузите [пример файла](sample.xlsx), затем установите свойство [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). Вот пример на JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Результат вывода:
<br>
<img src="3.png" width=60% />

## **Как вывести все столбцы листа на одной странице с помощью Aspose.Cells for JavaScript через C++**

Чтобы вывести все столбцы листа на одной странице: сначала откройте [образец файла](sample.xlsx), затем нужно установить свойство [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). Вот пример на JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Результат вывода:
<br>
<img src="4.png" width=60% />
