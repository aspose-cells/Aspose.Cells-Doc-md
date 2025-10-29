---
title: Шифрование файлов Excel с помощью JavaScript через C++
linktitle: Шифрование файлов Excel
type: docs
weight: 90
url: /ru/javascript-cpp/encrypting-excel-files/
description: Узнайте, как шифровать и защищать паролем файлы Excel с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Microsoft Excel (с 97 по 365) позволяет шифровать и защищать паролем ваши электронные таблицы. Для этого используются алгоритмы, предоставляемые поставщиком криптографических услуг, или CSP - набор криптографических алгоритмов с различными свойствами. CSP по умолчанию - 'Office 97/2000 Compatible' или 'Weak Encryption (XOR)'. Важно выбрать соответствующую длину ключа шифрования. Некоторые CSP не поддерживают более 40 или 56 бит. Это считается слабым шифрованием. Для сильного шифрования требуется минимальная длина ключа 128 бит. Microsoft Windows содержит CSP, которые также предлагают сильные типы шифрования, например, 'Microsoft Strong Cryptographic Provider'. Для примера, 128-битное шифрование используется банками для шифрования соединения с их системами Интернет-банкинга.

Aspose.Cells позволяет шифровать и защищать паролем файлы Microsoft Excel с выбранным вами типом шифрования.

{{% /alert %}}

## **Использование Microsoft Excel**

Для установки параметров шифрования файла в Microsoft Excel (например, Microsoft Excel 2003):

1. Из меню **Инструменты** выберите **Параметры**. Появится диалоговое окно.
1. Выберите вкладку **Безопасность**.
1. Введите пароль и нажмите **Дополнительно**.
1. Выберите тип шифрования и подтвердите пароль.

## **Шифрование с помощью Aspose.Cells for JavaScript через C++**

В следующем примере показано, как зашифровать и защитить паролем файл Excel с использованием API Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Encrypt Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, EncryptionType } = AsposeCells;

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

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify XOR encryption type.
            workbook.encryptionOptions = { type: EncryptionType.XOR, keyLength: 40 };

            // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
            workbook.encryptionOptions = { type: EncryptionType.StrongCryptographicProvider, keyLength: 128 };

            // Password protect the file.
            workbook.settings.password = "1234";

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Указание опции 'Пароль на изменение'**

В следующем примере показано, как установить опцию 'Пароль на изменение' для существующего файла Microsoft Excel с помощью API Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Password To Modify Option Example</title>
    </head>
    <body>
        <h1>Specify Password To Modify Option Example</h1>
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

            // Instantiate a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set the password for modification.
            workbook.settings.writeProtection.password = "1234";

            // Save the excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyPasswordToModifyOption.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password to modify set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Проверьте пароль зашифрованного файла**

 Чтобы проверить пароль зашифрованного файла, Aspose.Cells for JavaScript через C++ предоставляет метод [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-). Эти методы принимают два параметра: поток файла и пароль для проверки.
Следующий фрагмент кода демонстрирует использование метода [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) для проверки, является ли предоставленный пароль допустимым или нет.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Verify Password Example</title>
    </head>
    <body>
        <h1>Verify Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv,.xlsm" />
        <button id="runExample">Verify Password</button>
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
            const uint8 = new Uint8Array(arrayBuffer);

            const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(uint8, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```

## **Шифрование/дешифрование файла ODS с помощью Aspose.Cells**

Aspose.Cells позволяет шифровать и расшифровывать файлы ODS. Расшифрованный файл ODS можно открыть как в Excel, так и в OpenOffice, однако зашифрованный файл ODS может быть открыт только в OpenOffice после ввода пароля. Excel не сможет открыть зашифрованный файл ODS и может вывести предупреждающее сообщение. Параметры шифрования неприменимы к файлам ODS, в отличие от других типов файлов. Для шифрования ODS файла загрузите его и установите значение [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) равным действующему паролю перед сохранением. Финальный зашифрованный файл ODS можно открыть только в OpenOffice.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Encrypt ODS File Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Password protect the file
            workbook.settings.password = "1234";

            // Save the ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEncryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```

Для расшифровки файла ODS загрузите файл, предоставив пароль в [**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--). После загрузки файла установите строку [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) в null.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Decrypt ODS Example</title>
    </head>
    <body>
        <h1>Decrypt ODS Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options for ODS and set original password
            const loadOptions = new LoadOptions(LoadFormat.Ods);
            loadOptions.password = "1234";

            // Load the encrypted ODS file with the appropriate load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Set the password to null to remove encryption/password
            workbook.settings.password = null;

            // Save the decrypted ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDecryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Decrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File decrypted successfully! Click the download link to get the decrypted file.</p>';
        });
    </script>
</html>
```
