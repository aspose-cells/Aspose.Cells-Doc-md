---
title: Установка цвета вкладки листа с помощью JavaScript через C++
linktitle: Установка цвета вкладки таблицы
type: docs
weight: 120
url: /ru/javascript-cpp/set-worksheet-tab-color/
description: В этой статье приводится пример кода, который программно устанавливает цвет вкладки листа Excel с помощью JavaScript через C++.
keywords: установка цвета вкладки Excel JavaScript через C++, код для установки цвета вкладки Excel JavaScript через C++
---

{{% alert color="primary" %}}

Aspose.Cells позволяет изменять цвет отдельных вкладок таблицы, чтобы выделить их из остальных. Например, вы можете сделать вкладку Expenses красной, Sales зеленой, Assets синей и т. д.

{{% /alert %}}
## **Установка цвета вкладки таблицы в Microsoft Excel**
1. Щелкните правой кнопкой мыши на вкладке в листе внизу текущей таблицы.
1. Выберите **Цвет вкладки**.
1. Выберите цвет из палитры.
1. Нажмите **ОК**.
## **Установка цвета вкладки таблицы с помощью Aspose.Cells**
Приведенный ниже образцовый код показывает, как установить цвет вкладки с помощью Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
