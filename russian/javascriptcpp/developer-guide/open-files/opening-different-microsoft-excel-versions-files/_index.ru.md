---
title: Открытие файлов разных версий Microsoft Excel с помощью JavaScript через C++
linktitle: Открыть файлы разных версий Microsoft Excel
type: docs
weight: 20
url: /ru/javascript-cpp/opening-different-microsoft-excel-versions-files/
description: В этой статье объясняется, как открывать файлы различных версий Excel с помощью Aspose.Cells for JavaScript через C++.
keywords: JavaScript Открытие разных файлов Microsoft Excel через C++, как открыть зашифрованные файлы Excel с помощью JavaScript через C++
---

{{% alert color="primary" %}}

Aspose.Cells может открывать файлы разных версий Microsoft Excel, такие как Microsoft Excel 95/97 - 2003, SpreadsheetML, открытие файлов Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX или зашифрованных файлов Excel.

{{% /alert %}}

## **Как открыть файлы разных версий Microsoft Excel**

Приложение часто должно уметь открывать файлы Microsoft Excel, созданные в разных версиях, например, Microsoft Excel 95, 97 или Microsoft Excel 2007/2010/2013/2016/2019 и Office 365. Возможно, вам нужно загрузить файл в любом из нескольких форматов, включая XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited или TSV, CSV, ODS и другие. Используйте конструктор или укажите атрибут [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) класса с типом [**fileFormat**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fileFormat--), который определяет формат с помощью перечисления [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype).

Перечисление [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype) содержит множество предопределенных форматов файлов, некоторые из которых приведены ниже.

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|Csv|Представляет файл CSV|
|Excel97To2003|Представляет файл Excel 97 - 2003|
|Xlsx|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSX|
|Xlsm|Представляет файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSM|
|Xltx|Представляет файл шаблон Excel 2007/2010/2013/2016/2019 и Office 365 XLTX|
|Xltm|Представляет макрос-возможный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLTM|
|Xlsb|Представляет бинарный файл Excel 2007/2010/2013/2016/2019 и Office 365 XLSB|
|SpreadsheetML|Представляет файл SpreadsheetML|
|Tsv|Представляет файл со значениями, разделенными знаком табуляции|
|TabDelimited|Представляет файл текста с табуляцией|
|Ods|Представляет файл ODS|
|Html|Представляет файл HTML|
|Mhtml|Представляет файл MHTML|

### **Открыть файлы Microsoft Excel 95/5.0**

Чтобы открыть файл Microsoft Excel 95/5.0, используйте [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) для загружаемого файла шаблона. Пример файла для тестирования этой функции можно скачать по следующей ссылке:

[Файл Excel95](Excel95.xls)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel95_5.0.xls Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions1 = new LoadOptions(LoadFormat.Auto);

            // Create a Workbook object and opening the file from the stream
            const wbExcel95 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);
            console.log("Microsoft Excel 95/5.0 workbook opened successfully!");

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 95/5.0 workbook opened successfully!</p>';
        });
    </script>
</html>
```

### **Открыть файлы Microsoft Excel 97 - 2003**

Чтобы открыть файл Microsoft Excel 97 - 2003, используйте [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) и установите соответствующий атрибут для класса [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) для загружаемого файла шаблона.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel 97-2003 Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel 97-2003 (.xls) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions1 = new LoadOptions(LoadFormat.Excel97To2003);
            const wbExcel97 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 97 - 2003 workbook opened successfully!</p>';

            const outputData = wbExcel97.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

### **Открыть файлы Microsoft Excel 2007/2010/2013/2016/2019 и Office 365 XLSX**

Для открытия файла в форматах Microsoft Excel 2007/2010/2013/2016/2019 и Office 365, то есть XLSX или XLSB, укажите путь к файлу. Также можно использовать [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) и установить соответствующие атрибуты/опции класса [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) для загружаемого шаблона файла.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Open Excel 2007 Xlsx Example</title>
    </head>
    <body>
        <h1>Open Excel 2007 Xlsx Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel .xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 2007 - Office365 workbook opened successfully!</p>';

            // Save the workbook back to a downloadable file (unchanged content)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book_Excel2007_output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';
        });
    </script>
</html>
```

### **Открыть зашифрованные файлы Excel**

Возможна создание зашифрованных файлов Excel с помощью Microsoft Excel. Для открытия зашифрованного файла используйте [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) и укажите его атрибуты и опции (например, задайте пароль) для загружаемого файла шаблона.
Образец файла для тестирования этой функции может быть загружен по следующей ссылке:

[Encrypted Excel](EncryptedExcel.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Encrypted Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions
            const loadOptions = new LoadOptions();

            // Specify the password (converted from setPassword to property assignment)
            loadOptions.password = "1234";

            // Create a Workbook object opening the file from the uploaded bytes with loadOptions
            const wbEncrypted = new Workbook(new Uint8Array(arrayBuffer), loadOptions);
            console.log("Encrypted excel file opened successfully!");

            // Save the workbook so user can download it (using Excel97To2003 format for .xls)
            const outputData = wbEncrypted.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            // Use original name with a prefix to indicate it's been opened
            const originalName = file.name || 'output.xls';
            downloadLink.download = 'opened_' + originalName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Encrypted Excel file opened successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Aspose.Cells также поддерживает открытие защищенных паролем файлов Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365.
