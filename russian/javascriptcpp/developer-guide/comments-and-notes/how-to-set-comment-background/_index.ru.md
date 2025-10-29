---
title: Как изменить фон комментария в Excel с помощью JavaScript через C++
linktitle: Фон комментария
type: docs
weight: 190
url: /ru/javascript-cpp/how-to-set-comment-background/
description: Как изменить цвет комментария и вставить изображение или картинку в комментарий в Excel с помощью Aspose.Cells for JavaScript через C++.
keywords: Добавление вставленного изображения, цвета комментария, фона Excel, JavaScript через C++
---

{{% alert color="primary" %}}
Комментарии добавляются к ячейкам для записи замечаний, любой информации о работе формулы, источнике данных или вопросах рецензентов. Комментарии играют важную роль при обсуждении или проверке документа несколькими людьми. Как различать комментарии разных пользователей? Да, можно установить разный фон у каждого комментария. Но при обработке большого количества документов и комментариев вручную это невозможно. К счастью, [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) предоставляет API, который позволяет делать это автоматически в коде.
{{% /alert %}}

## **Как изменить цвет комментария в Excel**

Если вам не нужен стандартный фон у комментариев, вы можете заменить его на интересующий вас цвет. Как изменить цвет фона для области комментария в Excel?

Нижеследующий код поможет вам разобраться, как использовать [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/), чтобы добавить фоновый цвет комментариев по вашему выбору.

Здесь подготовлен [пример файла](exmaple.xlsx) для вас. Этот файл используется для инициализации объекта Workbook в приведенном ниже коде.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change Comment Background Color Example</title>
    </head>
    <body>
        <h1>Change Comment Background Color Example</h1>
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

            // Initialize a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the newly added comment
            const comment = workbook.worksheets.get(0).comments.get(0);

            // change background color
            const shape = comment.commentShape;
            shape.fill.solidFill.color = AsposeCells.Color.Red;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment background color changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Выполните указанный выше код, и вы получите [выходной файл](result.xlsx).

## **Как вставить изображение в комментарий в Excel**

Microsoft Excel позволяет настраивать внешний вид таблиц практически по всему спектру. Можно даже добавить фоновое изображение к комментариям. Добавление фона может быть эстетичным выбором или способствовать укреплению бренда.

Пример ниже создает XLSX-файл с нуля с помощью API [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) и добавляет комментарий с фоновым изображением в ячейку A1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Comment with Picture Example</h1>
        <p>
            Select an existing Excel file (optional) and an image file to attach to a comment in cell A1.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert in comment (required):</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the comment.</p>';
                return;
            }

            // Instantiate or load Workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get comments collection for the first sheet
            const comments = worksheet.comments;

            // Add a comment to cell A1 (row 0, column 0)
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set comment text and font name (converted from setters to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load the selected image file and set it to the comment's shape fill imageData
            const imageFile = imageInput.files[0];
            const imgArrayBuffer = await imageFile.arrayBuffer();
            const imageData = new Uint8Array(imgArrayBuffer);

            comment.commentShape.fill.imageData = imageData;

            // Save the workbook to a blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'commentwithpicture1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Comment with picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</body>
</html>
```
