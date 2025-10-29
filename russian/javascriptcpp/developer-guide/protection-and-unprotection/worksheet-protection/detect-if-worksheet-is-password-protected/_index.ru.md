---
title: Обнаружение, защищена ли рабочая книга паролем, с помощью JavaScript и C++
linktitle: Определить, защищен ли рабочий лист паролем
type: docs
weight: 360
url: /ru/javascript-cpp/detect-if-worksheet-is-password-protected/
description: Узнайте, как определить, защищена ли рабочая книга паролем, с помощью Aspose.Cells for JavaScript и C++. 
keywords: Обнаружение защиты паролем рабочего листа с помощью JavaScript и C++, проверка, защищен ли рабочий лист паролем с помощью JavaScript и C++, Aspose.Cells for JavaScript через C++
---

{{% alert color="primary" %}}

Возможно защищать рабочие книги и листы отдельно. Например, таблица может содержать один или несколько листов, защищенных паролем, однако сама таблица может быть защищена или нет. API Aspose.Cells предоставляет средства для обнаружения, защищен ли конкретный лист паролем. В этой статье демонстрируется использование Aspose.Cells for JavaScript через API C++ для достижения этой цели.

{{% /alert %}}

Aspose.Cells for JavaScript через C++ предоставил свойство [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) для обнаружения, защищен ли лист паролем. Булевое свойство типа [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) возвращает **true**, если [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) защищен паролем, и **false** в противном случае.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an instance of Workbook and load a spreadsheet
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the protected Worksheet
            const sheet = book.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                resultDiv.innerHTML = '<p>Worksheet is password protected</p>';
                console.log("Worksheet is password protected");
            } else {
                resultDiv.innerHTML = '<p>Worksheet is not password protected</p>';
                console.log("Worksheet is not password protected");
            }
        });
    </script>
</html>
```
