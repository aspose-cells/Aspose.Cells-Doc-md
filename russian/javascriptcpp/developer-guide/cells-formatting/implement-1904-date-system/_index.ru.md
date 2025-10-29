---
title: Реализуйте систему дат 1904 с помощью JavaScript через C++
description: Aspose.Cells — это библиотека JavaScript для работы с файлами электронных таблиц. Она поддерживает реализацию системы дат 1904, позволяя пользователям выполнять вычисления и форматировать по системе дат 1 января 1904 года. Эта статья описывает, как реализовать систему дат 1904 с помощью библиотеки Aspose.Cells.
keywords: Aspose.Cells, система дат 1904, электронные таблицы, вычисления, форматирование, JavaScript через C++
type: docs
weight: 7000
url: /ru/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel поддерживает две системы дат: систему 1900 (по умолчанию в Excel для Windows) и систему 1904. Система 1904 обычно используется для обеспечения совместимости с файлами Excel для Macintosh и является системой по умолчанию, если вы используете Excel для Macintosh. Вы можете установить систему дат 1904 для файлов Excel с помощью [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/). 

{{% /alert %}} 

Для реализации системы дат 1904 в Microsoft Excel (например, Microsoft Excel 2003):

1. В меню **Инструменты** выберите **Параметры**, а затем выберите вкладку **Расчет**.
1. Выберите опцию **1904 годовая система**.
1. Нажмите **ОК**.

|**Выбор 1904-ой годовой системы в Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

См. следующий образец кода о том, как это сделать с использованием API Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
