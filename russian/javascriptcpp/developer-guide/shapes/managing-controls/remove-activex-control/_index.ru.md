---
title: Удалите элемент управления ActiveX с помощью JavaScript через C++
linktitle: Удалить элемент управления ActiveX
type: docs
weight: 1000
url: /ru/javascript-cpp/remove-activex-control/
description: Узнайте, как удалять элементы управления ActiveX из книг с помощью Aspose.Cells for JavaScript через C++.
---

## **Удалить элемент управления ActiveX**

Aspose.Cells предоставляет возможность удалять элементы ActiveX из рабочих книг. Для этого API имеет метод [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/javascript-cpp/shape/#removeActiveXControl--). Следующий код демонстрирует использование метода [**Shape.removeActiveXControl()**](https://reference.aspose.com/cells/javascript-cpp/shape/#removeActiveXControl--) для удаления элемента ActiveX.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Remove ActiveX Control Example</title>
    </head>
    <body>
        <h1>Remove ActiveX Control Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access first shape from first worksheet
            const shape = worksheet.shapes.get(0);

            // Access ActiveX ComboBox Control and update its value / remove it
            if (shape && shape.activeXControl != null) {
                // Remove Shape ActiveX Control
                shape.removeActiveXControl();
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveActiveXControl_our.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">ActiveX control removed (if present). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
