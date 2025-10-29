---
title: Получить проверку ячейки в файлах ODS
type: docs
weight: 180
url: /ru/javascript-cpp/get-cell-validation-in-ods-files/
description: Узнайте, как получать проверку данных ячейки в файлах ODS с помощью скрипта Aspose.Cells for Java и API C++.
keywords: Получить проверку ячейки JavaScript через C++, Получить проверку ячейки JavaScript через C++
---

## **Получить проверку ячейки в файлах ODS**  

С помощью Aspose.Cells for JavaScript через C++, вы можете получить проверку, примененную к ячейке в файлах ODS. Для этого API предоставляет свойство [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) класса [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/).  

Следующий пример кода демонстрирует использование свойства [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) путём загрузки файла [исходного ODS](101089354.ods) и чтения проверки ячейки A9.  

### **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Check Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel/ODS file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the file
            const worksheet = workbook.worksheets.get(0);

            // Access cell A9
            const cell = worksheet.cells.get("A9");

            if (cell.validation !== null) {
                resultEl.innerHTML = `<p>Validation type: ${cell.validation.type}</p>`;
            } else {
                resultEl.innerHTML = '<p>No validation on A9.</p>';
            }
        });
    </script>
</html>
```
