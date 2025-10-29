---
title: Цифровая подпись проекта VBA с помощью сертификата через JavaScript через C++
linktitle: Цифровая подпись проекта VBA с помощью сертификата
type: docs
weight: 110
url: /ru/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Узнайте, как цифрово подписать проект VBA с помощью сертификата с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Вы можете цифрово подписать ваш проект VBA с помощью Aspose.Cells и его метода [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-). Пожалуйста, следуйте этим шагам, чтобы проверить, подписан ли ваш файл Excel с помощью сертификата.

- Нажмите **Visual Basic** на вкладке **Разработчиков**, чтобы открыть **Интегрированную среду разработки Visual Basic for Applications**
- Нажмите **Сервис** > **Цифровые подписи...** в **Среде VBA**

и отобразится **Форма цифровой подписи**, показывающая, подписан ли документ цифровым сертификатом или нет.

{{% /alert %}} 

## **Цифровая подпись проекта VBA с сертификатом на JavaScript**

Следующий пример кода демонстрирует использование метода [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-). Здесь приведены входные и выходные файлы примера. Вы можете использовать любой файл Excel и любой сертификат для тестирования этого кода.

- [Исходный файл Excel](5115028.xlsm), используемый в образцовом коде.
- [Образец файла pfx](5115039.pfx) для создания цифровой подписи. Пожалуйста, установите его на ваш компьютер, чтобы запустить этот код. Пароль - 1234.
- [Файл Excel вывода](5115029.xlsm), сгенерированный образцовым кодом.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sign VBA Project with Digital Signature</h1>
        <div>
            <label for="fileInput">Select Excel Workbook (.xlsm): </label>
            <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        </div>
        <div>
            <label for="pfxInput">Select PFX Certificate (.pfx): </label>
            <input type="file" id="pfxInput" accept=".pfx" />
        </div>
        <button id="runExample">Sign VBA Project</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, DigitalSignature } = AsposeCells;

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
            const pfxInput = document.getElementById('pfxInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length || !pfxInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both the Excel workbook and the PFX certificate files.</p>';
                return;
            }

            const workbookFile = fileInput.files[0];
            const pfxFile = pfxInput.files[0];

            // Read files as ArrayBuffer
            const [wbArrayBuffer, pfxArrayBuffer] = await Promise.all([
                workbookFile.arrayBuffer(),
                pfxFile.arrayBuffer()
            ]);

            // Prepare bytes
            const wbBytes = new Uint8Array(wbArrayBuffer);
            const pfxBytes = new Uint8Array(pfxArrayBuffer);

            // Set Digital Signature parameters
            const password = "1234";
            const comment = "Signing Digital Signature using Aspose.Cells";
            const digitalSignature = new DigitalSignature(pfxBytes, password, comment, new Date());

            // Create workbook object from excel file
            const workbook = new Workbook(wbBytes);

            // Sign VBA Code Project with Digital Signature
            workbook.vbaProject.sign(digitalSignature);

            // Save the workbook as XLSM
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignVbaProjectWithCertificate.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Workbook signed successfully! Click the download link to download the signed workbook.</p>';
        });
    </script>
</html>
```
