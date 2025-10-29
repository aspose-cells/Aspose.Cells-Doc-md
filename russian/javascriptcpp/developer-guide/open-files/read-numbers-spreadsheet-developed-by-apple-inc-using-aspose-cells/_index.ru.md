---
title: Чтение таблиц Numbers, разработанных компанией Apple Inc., с помощью Aspose.Cells for JavaScript через C++
linktitle: Чтение Numbers Spreadsheet разработанный Apple Inc. с использованием Aspose.Cells
type: docs
weight: 140
url: /ru/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Узнайте, как читать таблицы Numbers, разработанные Apple Inc., с помощью Aspose.Cells for JavaScript через C++. 
---

## **Возможные сценарии использования**

Numbers — это приложение для работы с таблицами, разработанное Apple Inc. Aspose.Cells может читать таблицы Numbers, но не поддерживает запись в них. Оно может читать данные, стили и формулы таблиц Numbers.

## **Чтение таблицы Numbers, разработанной Apple Inc., с помощью Aspose.Cells for JavaScript через C++**

Следующий пример кода загружает [Пример таблицы Numbers](sampleNumbersByAppleInc.numbers) и конвертирует его в [Выходной PDF формат](outputNumbersByAppleInc.pdf). Для успешной загрузки необходимо использовать класс [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) и указать [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) в качестве параметра в его конструкторе. Скачать оба файла можно по предоставленным ссылкам. Можно попробовать код с любой таблицей Numbers. Также рекомендуется ознакомиться с комментариями к коду для получения дополнительной информации.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
