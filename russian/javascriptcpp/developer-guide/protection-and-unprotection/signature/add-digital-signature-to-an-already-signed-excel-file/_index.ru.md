---
title: Добавить цифровую подпись в уже подписанный файл Excel с помощью JavaScript через C++
linktitle: Добавить цифровую подпись к уже подписанному файлу Excel
type: docs
weight: 20
url: /ru/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Эта статья описывает, как добавить цифровую подпись в уже подписанный Excel файл с помощью JavaScript и Aspose.Cells for JavaScript через C++.
keywords: Добавление цифровой подписи в уже подписанный Excel файл, как добавить цифровую подпись в уже подписанный Excel документ с помощью JavaScript через C++.
---

## **Возможные сценарии использования**

 Aspose.Cells for JavaScript через C++ предоставляет метод [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-), который можно использовать для добавления цифровой подписи в уже подписанный Excel-файл.

{{% alert color="primary" %}}

Обратите внимание, при добавлении цифровой подписи в уже подписанный документ Excel, если исходный документ создан с помощью Aspose.Cells, он работает хорошо. Но если оригинальный документ создан другими движками (например, Microsoft Excel и др.), Aspose.Cells не сможет сохранить файл без изменений после загрузки и повторного сохранения, что сделает исходную подпись недействительной.

{{% /alert %}}

## **Как добавить цифровую подпись к уже подписанному файлу Excel**

Следующий пример кода демонстрирует, как использовать метод [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) для добавления цифровой подписи в уже подписанный файл Excel. Пожалуйста, посмотрите [пример файла Excel](50528280.xlsx), использованный в этом коде. Этот файл уже содержит цифровую подпись. Также ознакомьтесь с [выходным файлом Excel](50528281.xlsx), сгенерированным кодом. В этом примере используется демонстрационный сертификат [AsposeDemo.pfx](50528279.pfx), пароль которого **aspose**. На снимке экрана показан эффект от работы кода на примере файла Excel после выполнения.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Digital Signature Example</title>
    </head>
    <body>
        <h1>Add Digital Signature to Workbook</h1>
        <p>Select an Excel file and a PFX certificate, enter the certificate password, then click "Add Digital Signature".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <br/><br/>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <label for="certPassword">Certificate Password:</label>
        <input type="password" id="certPassword" value="aspose" />
        <br/><br/>
        <button id="runExample">Add Digital Signature</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, DigitalSignature, DigitalSignatureCollection, SaveFormat, Utils } = AsposeCells;

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
            const certInput = document.getElementById('certInput');
            const passwordInput = document.getElementById('certPassword');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            // Read files as ArrayBuffer
            const excelFile = fileInput.files[0];
            const certFile = certInput.files[0];
            const certPassword = passwordInput.value;

            const excelArrayBuffer = await excelFile.arrayBuffer();
            const certArrayBuffer = await certFile.arrayBuffer();

            // Instantiate Workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(excelArrayBuffer));

            // Create the digital signature collection
            const dsCollection = new DigitalSignatureCollection();

            // Create new digital signature and add it in digital signature collection
            // Using certificate bytes (Uint8Array), password, comment and signing date
            const signature = new DigitalSignature(new Uint8Array(certArrayBuffer), certPassword, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
            dsCollection.add(signature);

            // Add digital signature collection inside the workbook
            workbook.addDigitalSignature(dsCollection);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignedByCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Digitally Signed Excel File';

            // Dispose the workbook
            workbook.dispose();

            resultDiv.innerHTML = '<p style="color: green;">Digital signature added successfully! Click the download link to get the signed file.</p>';
        });
    </script>
</html>
```
