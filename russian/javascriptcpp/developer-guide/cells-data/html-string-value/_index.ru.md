---
title: Добавление HTML форматированного текста внутри ячейки
linktitle: Значение HTML строки
type: docs
weight: 50
url: /ru/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: Узнайте, как добавить HTML Rich Text внутри ячейки через API Aspose.Cells for JavaScript для C++.
keywords: Добавить HTML Rich Text внутри ячейки через JavaScript для C++, Установить HTML Rich Text внутри ячейки через JavaScript для C++, Добавить HTML Rich Text в ячейку через JavaScript для C++
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование HTML, ориентированного на Microsoft Excel, в формат XLS/XLSX. Это означает, что HTML, созданный Microsoft Excel, может быть обратно преобразован в формат XLS/XLSX с помощью Aspose.Cells.

Точно так же, если есть какой-то простой HTML, Aspose.Cells может преобразовать его в HTML-строку с форматированным текстом. Aspose.Cells предоставляет свойство [**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-), которое может принять такой простой HTML и преобразовать его в отформатированный текст ячейки.

{{% /alert %}}

Приведенный ниже образец кода показывает, как добавить HTML-форматированный текст в ячейку. Пожалуйста, посмотрите скриншот выходного файла Excel.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Связанные статьи

- [Отображение маркеров путем установки значения ячейки с использованием HTML](/cells/ru/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [Получение строки HTML5 из ячейки](/cells/ru/javascript-cpp/get-html5-string-from-cell/)
