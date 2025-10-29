---
title: Извлечение данных темы из файла Excel
linktitle: Извлечение данных темы из файла Excel
description: Узнайте, как извлекать данные о темах из файлов Excel с помощью Script Aspose.Cells for Java через C++. Эффективно получайте информацию о стиле и форматировании.
keywords: Aspose.Cells, файл Excel, данные темы, стиль, формат, JavaScript через C++
type: docs
weight: 120
url: /ru/javascript-cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет пользователям извлекать данные, связанные с темой, из файла Excel. Например, можно извлечь название темы, примененной к книге, и цвет темы, примененный к ячейке или границам ячейки и т. д.

Вы можете применить тему к своей книге с помощью Microsoft Excel через команду Разметка страницы > Темы.

{{% /alert %}}

## Код JavaScript для извлечения данных темы из файла Excel

Следующий пример кода извлекает название темы, применённое к исходной рабочей книге, а затем извлекает цвет темы, применённый к ячейке A1, и цвет темы, применённый к нижней границе ячейки.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; }
            #result p { margin: 6px 0; }
        </style>
    </head>
    <body>
        <h1>Aspose.Cells Theme & Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Extract theme name applied to this workbook
            const themeName = workbook.theme;
            resultDiv.innerHTML += `<p>Workbook theme: ${themeName}</p>`;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Get the style object
            const style = cell.style;

            if (style.foregroundThemeColor != null) {
                // Extract theme color applied to this cell if theme has foreground theme color defined
                const fgColorType = style.foregroundThemeColor.colorType;
                resultDiv.innerHTML += `<p>Foreground theme color type: ${fgColorType}</p>`;
            } else {
                resultDiv.innerHTML += `<p>Theme has not foreground color defined.</p>`;
            }

            // Extract theme color applied to the bottom border of the cell if theme has border color defined
            const bot = style.borders.get(BorderType.BottomBorder);
            if (bot.themeColor != null) {
                const botColorType = bot.themeColor.colorType;
                resultDiv.innerHTML += `<p>Bottom border theme color type: ${botColorType}</p>`;
            } else {
                resultDiv.innerHTML += `<p>Theme has not Border color defined.</p>`;
            }

            // No file is produced here, but keep download link hidden
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            downloadLink.href = '#';
            downloadLink.textContent = '';
        });
    </script>
</html>
```
