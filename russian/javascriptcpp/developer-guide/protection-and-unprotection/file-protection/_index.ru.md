---
title: Шифрование и дешифрование файлов Excel с помощью JavaScript через C++
linktitle: Шифрование и дешифрование файлов Excel
type: docs
weight: 10
url: /ru/javascript-cpp/encrypt-and-decrypt-excel-files/
description: Как шифровать и дешифровать файлы Excel с помощью JavaScript через C++. Блокировка и разблокировка файлов Excel.
---

{{% alert color="primary" %}}  
Microsoft Excel (с 97 по 365) позволяет шифровать и защищать паролем ваши электронные таблицы. Для этого используются алгоритмы, предоставляемые поставщиком криптографических услуг, или CSP - набор криптографических алгоритмов с различными свойствами. CSP по умолчанию - 'Office 97/2000 Compatible' или 'Weak Encryption (XOR)'. Важно выбрать соответствующую длину ключа шифрования. Некоторые CSP не поддерживают более 40 или 56 бит. Это считается слабым шифрованием. Для сильного шифрования требуется минимальная длина ключа 128 бит. Microsoft Windows содержит CSP, которые также предлагают сильные типы шифрования, например, 'Microsoft Strong Cryptographic Provider'. Для примера, 128-битное шифрование используется банками для шифрования соединения с их системами Интернет-банкинга.  

Aspose.Cells позволяет шифровать и защищать паролем файлы Microsoft Excel с выбранным вами типом шифрования.  
{{% /alert %}}  

## **Использование Microsoft Excel**  

Для установки параметров шифрования файла в Microsoft Excel (например, Microsoft Excel 2003):  

1. Из меню **Инструменты** выберите **Параметры**. Появится диалоговое окно.  
2. Выберите вкладку **Безопасность**.  
3. Введите пароль и нажмите **Дополнительно**  
4. Выберите тип шифрования и подтвердите пароль.  

## **Шифрование файла Excel с помощью Aspose.Cells for JavaScript через C++**  

Следующий пример показывает, как зашифровать и установить пароль на файл Excel с помощью API Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Encrypt Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiate a Workbook object by opening the uploaded excel file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify XOR encryption type.
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.XOR, keyLength: 40 };

            // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.StrongCryptographicProvider, keyLength: 128 };

            // Password protect the file.
            workbook.settings.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook encrypted and ready for download.</p>';
        });
    </script>
</html>
```  

### **Указание опции пароля для изменений**  

В следующем примере показано, как установить опцию 'Пароль на изменение' для существующего файла Microsoft Excel с помощью API Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Password To Modify Example</h1>
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

            // Set the password for modification.
            workbook.settings.writeProtection.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyPasswordToModifyOption.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password-to-modify set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


## **Дешифрование файла Excel с помощью Aspose.Cells for JavaScript через C++**  
Очень легко открыть защищенный паролем файл Excel и расшифровать его, используя API Aspose.Cells, как показано в следующем коде:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Excel and Remove Password</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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

            // Prepare load options with password to open encrypted file
            const loadOptions = new LoadOptions();
            loadOptions.password = "password";

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Remove password from workbook settings
            workbook.settings.password = null;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            // Use original filename with suffix to indicate password removed
            const originalName = file.name || 'output.xlsx';
            const baseName = originalName.replace(/(\.xls[xm]?|\.csv)$/i, '') || 'output';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unlocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unlocked Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password removed successfully! Click the download link to get the unlocked file.</p>';
        });
    </script>
</html>
```  


## **Продвинутые темы**  
- [Шифрование и дешифрование файлов ODS](/cells/ru/javascript-cpp/encrypt-and-decrypt-ods-files/)  
- [Установка сильного типа шифрования](/cells/ru/javascript-cpp/setting-strong-encryption-type/)  
- [Укажите автора при защите от записи книги](/cells/ru/javascript-cpp/specify-author-while-write-protecting-workbook/)  
- [Проверка пароля зашифрованных файлов](/cells/ru/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/)
