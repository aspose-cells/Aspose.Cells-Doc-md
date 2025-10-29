---
title: Шифрование и расшифровка файлов ODS с помощью JavaScript через C++
linktitle: Шифрование и дешифрование файлов ODS
type: docs
weight: 10
url: /ru/javascript-cpp/encrypt-and-decrypt-ods-files/
description: Защитите паролем и зашифруйте файлы ODS с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}
OpenOffice.org — полнофункциональный офисный пакет, который поддерживает защиту паролем и шифрование файлов. Но зашифрованный файл ODS можно открыть только в OpenOffice после ввода пароля. Excel не может открыть зашифрованный файл ODS и может вывести предупреждающие сообщения. Опции шифрования не применимы к файлам ODS, в отличие от других типов файлов. 
 Aspose.Cells позволяет шифровать и дешифровать файлы ODS. Расшифрованные файлы ODS могут быть открыты как в Excel, так и в OpenOffice.
{{% /alert %}}

## **Шифровать с помощью OpenOffice Calc**
1. Выберите **Сохранить как** и установите флажок **Сохранить с паролем**.
1. Нажмите кнопку **Сохранить**.
1. Введите желаемый пароль в поля **Введите пароль для открытия** и **Подтвердите пароль** в окне установки пароля, которое откроется. 
1. Нажмите кнопку **OK**, чтобы сохранить файл.

## **Зашифруйте файл ODS с помощью Aspose.Cells for JavaScript через C++**
Для шифрования файла ODS загрузите файл и установите значение [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) в фактический пароль перед сохранением. Полученный зашифрованный файл ODS можно открыть только в OpenOffice.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect ODS File</title>
    </head>
    <body>
        <h1>Protect ODS File Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Protect and Download ODS</button>
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

            // Instantiating a Workbook object by opening the uploaded ODS file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Password protect the file (converted from getSettings().setPassword -> settings.password)
            workbook.settings.password = "1234";

            // Saving the ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEncryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File protected successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```

## **Расшифровка файла ODS с помощью Aspose.Cells for JavaScript через C++**
Для расшифровки файла ODS загрузите файл, указав пароль в [**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--). После загрузки файла установите строку [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) в null.

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

            // Open an encrypted ODS file with load options
            const loadOptions = new LoadOptions(LoadFormat.Ods);

            // Set original password
            loadOptions.password = "1234";

            // Load the encrypted ODS file with the appropriate load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Set the password to null (remove password from settings)
            workbook.settings.password = null;

            // Save the decrypted ODS file and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDecryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Decrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Decryption completed successfully! Click the download link to get the decrypted file.</p>';
        });
    </script>
</html>
```
