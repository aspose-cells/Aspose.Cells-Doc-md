---
title: Защитите PDF документы с помощью JavaScript на C++
linktitle: Защищенные PDF документы
type: docs
weight: 120
url: /ru/javascript-cpp/secure-pdf-documents/
description: Узнайте, как защитить PDF документы, используя пароли владельца и пользователя, а также установить разрешения для PDF файлов с помощью Script Aspose.Cells for Java на C++.
---

{{% alert color="primary" %}}

Иногда разработчикам приходится работать с зашифрованными PDF-файлами. Например:

- Защитите документы паролями владельца и пользователя, чтобы открыть его могли не все.
- Установите ограничения или разрешения для документа после его открытия. например, ограничьте, можно ли печатать или извлекать содержимое документа.

Эта статья объясняет, как передавать параметры безопасности PDF при сохранении электронных таблиц в PDF.

{{% /alert %}}

Aspose.Cells предоставляет [**PdfSecurityOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/) для работы с безопасностью. Вы можете установить пароли владельца и пользователя при сохранении в PDF. Пароль владельца или пользователя потребуется для открытия зашифрованного PDF-документа для просмотра.

- Пароль пользователя может быть равен null или пустой строке; в этом случае пользователю не потребуется пароль при открытии PDF-документа.
- Открытие PDF-документа с правильным паролем владельца обеспечивает полный доступ (без указанных ограничений доступа) к документу.
- Открытие PDF-документа с правильным паролем пользователя (или открытие документа без пароля пользователя) дает ограниченный доступ в соответствии с установленными разрешениями.

Приведенный ниже пример кода описывает, как защищать PDF с помощью Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Secure PDF Example</title>
    </head>
    <body>
        <h1>Secure PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Create PDF save options and security options
            const saveOption = new PdfSaveOptions();
            saveOption.securityOptions = new PdfSecurityOptions();

            // Set security options (converted from getters/setters to properties)
            saveOption.securityOptions.userPassword = "user";
            saveOption.securityOptions.ownerPassword = "owner";
            saveOption.securityOptions.extractContentPermission = false;
            saveOption.securityOptions.printPermission = false;

            // Save the workbook to PDF with security options
            const outputData = workbook.save(SaveFormat.Pdf, saveOption);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'securepdf_test.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Secure PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the secured PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Если электронная таблица содержит формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) прямо перед преобразованием ее в PDF. Это гарантирует, что значения, зависящие от формул, пересчитываются верно и отображаются правильные значения в PDF.

{{% /alert %}}
