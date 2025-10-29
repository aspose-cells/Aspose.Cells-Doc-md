---
title: Проверьте пользовательский формат чисел при установке Style.Custom свойства
linktitle: Проверьте пользовательский формат чисел при установке Style.Custom свойства
description: Aspose.Cells — это библиотека JavaScript для работы с файлами таблиц, которая поддерживает проверку пользовательских форматов чисел при стилизации. В этой статье вы узнаете, как использовать библиотеку Aspose.Cells для проверки пользовательских форматов чисел, чтобы убедиться, что стилизация выполнена правильно.
keywords: Aspose.Cells, библиотеки JavaScript, таблицы, стилизация, пользовательское форматирование чисел, проверка, валидация
type: docs
weight: 170
url: /ru/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Возможные сценарии использования**

Если вы присвоите неверный пользовательский формат числа свойству [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-), то Aspose.Cells for JavaScript через C++ не выбросит исключение. Но если вы хотите, чтобы Aspose.Cells проверил, действителен ли присвоенный пользовательский формат числа, установите свойство [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) в **true**.

## **Проверка пользовательского формата числа при установке свойства Style.custom**

Следующий пример кода присваивает неверный пользовательский формат числа свойству [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-). Так как мы уже установили свойство [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) в **true**, возникает исключение, например, неправильный формат числа. Обратите внимание на комментарии внутри кода для получения дополнительной помощи.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
