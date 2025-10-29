---
title: Экспортировать сертификат VBA в файл или поток с помощью JavaScript через C++
linktitle: Экспорт сертификата VBA в файл или поток
type: docs
weight: 90
url: /ru/javascript-cpp/export-vba-certificate-to-file-or-stream/
description: Узнайте, как экспортировать цифровой сертификат VBA в файл или поток с помощью Aspose.Cells for JavaScript через C++. Получить необработанные данные цифровых сертификатов VBA.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать цифровой сертификат VBA в поток, такой как файл или поток памяти. Вы можете получить доступ к сырым данным цифрового сертификата VBA, используя свойство [**VbaProject.certRawData**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#certRawData--).

{{% /alert %}}

## **Экспортировать сертификат VBA в файл или поток с помощью JavaScript**

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, который сохраняет сырые данные сертификата VBA в файл. Вы можете загрузить [образец excel файла, используемого в этом коде](5115031.xlsm) по предоставленной ссылке.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract VBA Project Certificate</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve bytes data of Digital Certificate of VBA Project
            const certBytes = workbook.vbaProject.certRawData;

            // Convert to Uint8Array and create a Blob for download
            const certUint8 = Uint8Array.from(certBytes);
            const blob = new Blob([certUint8]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Cert_out_';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Certificate';

            document.getElementById('result').innerHTML = '<p style="color: green;">Certificate extracted successfully! Click the download link to save the certificate.</p>';
        });
    </script>
</html>
```
