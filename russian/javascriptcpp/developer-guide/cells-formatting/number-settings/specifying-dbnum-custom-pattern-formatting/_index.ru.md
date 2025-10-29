---
title: Указание пользовательского шаблона форматирования с использованием DBNum
linktitle: Указание пользовательского шаблона форматирования с использованием DBNum
description: Aspose.Cells — это библиотека для JavaScript через C++, которая поддерживает форматирование дат и чисел с помощью пользовательских шаблонов форматирования. В этой статье показано, как указать пользовательский формат dbnum для лучшего контроля отображения чисел.
keywords: Aspose.Cells, JavaScript через C++, электронная таблица, шаблон пользовательского формата, форматирование, dbnum , управление отображением
type: docs
weight: 110
url: /ru/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Возможные сценарии использования**

Aspose.Cells for JavaScript через C++ поддерживает пользовательский шаблон форматирования *DBNum*. Например, если значение ячейки равно 123 и его пользовательское форматирование указано как [DBNum2][$-804]General, то оно отобразится как 壹佰贰拾叁. Пользователи могут задать пользовательское форматирование ячейки, используя методы [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) и [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-).

## **Образец кода**

Следующий пример кода показывает, как указать пользовательский шаблон *DBNum*. Пожалуйста, проверьте его [вывод PDF](43352081.pdf) для получения дополнительной помощи.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
