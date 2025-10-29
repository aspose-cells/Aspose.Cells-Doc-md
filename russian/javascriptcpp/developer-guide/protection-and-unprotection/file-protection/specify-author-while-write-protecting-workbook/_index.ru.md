---
title: Укажите автора при защите паролем книги с помощью JavaScript через C++
linktitle: Укажите автора при защите от записи книги
type: docs
weight: 40
url: /ru/javascript-cpp/specify-author-while-write-protecting-workbook/
description: Укажите имя автора при защите книги паролем с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

Вы можете указать имя автора при защите вашей книги паролем с помощью API Aspose.Cells. Пожалуйста, используйте свойство [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) для этой цели.

## **Укажите автора при защите от записи книги**

Следующий пример кода объясняет использование свойства [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--). Код создает пустую книгу, защищает ее паролем, указывает имя автора и сохраняет как [выходной файл Excel](67338582.xlsx). Ниже приведен снимок экрана, иллюстрирующий эффект этого примера на выходном файле Excel для вашего ознакомления.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
