---
title: Отправить фигуру вперёд или назад внутри листа с помощью JavaScript через C++
linktitle: Отправить форму вперед или назад внутри листа
type: docs
weight: 3400
url: /ru/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Узнайте, как отправить фигуру на передний или задний план в листе, используя Aspose.Cells for JavaScript через C++. 
---

## **Возможные сценарии использования**

Когда на одном месте расположено несколько фигур, их видимость определяется по их z-порядку. Aspose.Cells предоставляет метод [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-), который изменяет z-положение фигуры. Чтобы отправить фигуру на задний план, используйте отрицательное число, например -1, -2, -3, ..., а чтобы поднять фигуру на передний план — положительное число, например 1, 2, 3, ...

## **Отправить форму вперед или назад внутри листа**

Следующий пример кода объясняет использование метода [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-). Посмотрите [пример файла Excel](50528330.xlsx), использованный внутри кода, и [выходной файл Excel](50528331.xlsx), созданный им. Скриншот показывает эффект работы кода на образце Excel после выполнения.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Send Shapes Front or Back</title>
    </head>
    <body>
        <h1>Send Shapes to Front or Back Example</h1>
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

            // Access first and fourth shapes
            const shape1 = worksheet.shapes.get(0);
            const shape4 = worksheet.shapes.get(3);

            // Print the Z-Order position of shape1
            resultDiv.innerHTML = `<p>Z-Order Shape 1: ${shape1.zOrderPosition}</p>`;

            // Send this shape to front
            shape1.toFrontOrBack(2);

            // Print the Z-Order position of shape4
            resultDiv.innerHTML += `<p>Z-Order Shape 4: ${shape4.zOrderPosition}</p>`;

            // Send this shape to back
            shape4.toFrontOrBack(-2);

            // Saving the modified Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputToFrontOrBack.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
