---
title: Управление комментариями и заметками с помощью JavaScript через C++
linktitle: Комментарии и заметки
type: docs
weight: 128
url: /ru/javascript-cpp/comments-and-notes/
description: Вставляйте и управляйте комментариями или заметками с помощью Aspose.Cells for JavaScript через C++.
keywords: вставка комментариев, вставка заметок JavaScript через C++
---

## **Введение**

Комментарии используются для добавления дополнительной информации в ячейки. Aspose.Cells for JavaScript через C++ предоставляет два метода добавления комментариев в ячейки. Первый — создание комментариев вручную в дизайнерском файле. Эти комментарии затем импортируются с помощью Aspose.Cells. Второй — добавление комментариев в режиме выполнения через API Aspose.Cells. Эта тема посвящена добавлению комментариев к ячейкам с помощью API Aspose.Cells. Также будет объяснено форматирование комментариев.

## **Добавление комментария**

Добавьте комментарий к ячейке, вызвав метод [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#add-number-number-) коллекции [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection) (инкапсулированный в объект [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Новый объект [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment) можно получить из коллекции [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection), передав индекс комментария. После получения объекта [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment) настройте заметку комментария с помощью свойства [**note**](https://reference.aspose.com/cells/javascript-cpp/comment/#note--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Форматирование комментариев**

Также возможно форматировать внешний вид комментариев, настроив их высоту, ширину и параметры шрифта.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Setting the font size of a comment to 14
            comment.font.size = 14;

            // Setting the font of a comment to bold
            comment.font.isBold = true;

            // Setting the height of the font to 10
            comment.heightCM = 10;

            // Setting the width of the font to 2
            comment.widthCM = 2;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Добавить изображение в комментарий**

С помощью Microsoft Excel 2007 также возможно иметь изображение в качестве фона комментария к ячейке. В Excel 2007 это можно сделать, выполнив следующие шаги. (Предполагается, что вы уже добавили комментарий к ячейке.)

1. Щелкните правой кнопкой мыши ячейку, содержащую комментарий.
1. Выберите **Показать/скрыть комментарии** и очистите любой текст из комментария.
1. Щелкните по границе комментария, чтобы выбрать его.
1. Выберите **Формат**, затем **Комментарий**.
1. На вкладке **Цвета и линии** разверните список **Цвет**.
1. Нажмите **Изменение заливки**.
1. На вкладке **Изображение** нажмите **Выбрать изображение**.
1. Найдите и выберите изображение.
1. Нажмите **ОК**, пока все диалоговые окна не закроются.

Aspose.Cells также предоставляет эту функцию. Ниже приведен пример кода, который создает файл XLSX с нуля, добавляя комментарий в ячейку "A1" с установленным изображением в качестве его фона.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment with Image</title>
    </head>
    <body>
        <h1>Add Comment with Image Example</h1>
        <p>
            Select an existing Excel file to modify (optional). If no file is selected, a new workbook will be created.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image file to attach to the comment (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
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
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            const fileInput = document.getElementById('fileInput');
            const imageInput = document.getElementById('imageInput');

            if (!imageInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an image file for the comment.</p>';
                return;
            }

            // Load or create workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get a reference of comments collection with the first sheet
            const comments = workbook.worksheets.get(0).comments;

            // Add a comment to cell A1
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set the comment note and font name (converted from set/get to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load image file data
            const imgFile = imageInput.files[0];
            const imgArrayBuffer = await imgFile.arrayBuffer();
            const imgUint8 = new Uint8Array(imgArrayBuffer);

            // Set image data to the shape associated with the comment
            comment.commentShape.fill.imageData = imgUint8;

            // Save the workbook to browser-downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = '<p style="color: green;">Comment added with image successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Изменение направления текста комментария](/cells/ru/javascript-cpp/change-text-direction-of-the-comment/)
- [Как изменить цвет шрифта комментария](/cells/ru/javascript-cpp/how-to-change-the-comment-font-color/)
- [Как установить фон комментария](/cells/ru/javascript-cpp/how-to-set-comment-background/)
- [Комментарии с цепочкой](/cells/ru/javascript-cpp/threaded-comments/)
