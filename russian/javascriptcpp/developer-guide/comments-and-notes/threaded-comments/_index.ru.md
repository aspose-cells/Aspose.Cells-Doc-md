---
title: Многослойные комментарии с помощью JavaScript через C++
linktitle: Нитевые комментарии
type: docs
weight: 140
url: /ru/javascript-cpp/threaded-comments/
description: Управление многослойными комментариями в документах Excel с помощью Aspose.Cells for JavaScript через C++. Узнайте, как добавлять, читать, редактировать и удалять многослойные комментарии.
---

## **Комментарии с цепочкой**

MS Excel 365 предоставляет возможность добавлять нитевые комментарии. Эти комментарии работают как разговоры и могут использоваться для обсуждений. Теперь комментарии идут с полем Ответа, которое позволяет вести разговоры в нитевом порядке. Старые комментарии в Excel 365 называются Примечаниями. Ниже показано, как выглядят нитевые комментарии, когда они открываются в Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Нитевые комментарии показываются таким образом в старых версиях Excel. Следующие изображения были получены при открытии образцового файла в Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells также предоставляет возможность управлять нитевыми комментариями.

## **Добавить нитевые комментарии**

### **Добавить нитевой комментарий с Excel**

Чтобы добавить нитевые комментарии в Excel 365, выполните следующие шаги.

- Метод 1
  - Нажмите вкладку **Обзор**
  - Нажмите кнопку **Новый комментарий**
  - Это откроет диалог для ввода комментариев в активной ячейке.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Метод 2
  - Щелкните правой кнопкой мыши на ячейке, куда нужно вставить комментарий.
  - Нажмите на **Новый комментарий**.
  - Это откроет диалог для ввода комментариев в активной ячейке.
  - ![todo:image_alt_text](threaded-comments_5)

### **Добавить ветвистый комментарий с помощью Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) для добавления цепочечных комментариев. Метод [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) принимает три параметра.

- Имя ячейки: Имя ячейки, в которую будет вставлен комментарий.
- Текст комментария: Текст комментария.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentauthor): Автор комментария.

Следующий пример демонстрирует использование метода [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) для добавления цепочечного комментария в ячейку A1. Пожалуйста, посмотрите сгенерированный файл Excel [выходной файл](89849859.xlsx) для примера.

#### **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Threaded Comment</title>
    </head>
    <body>
        <h1>Add Threaded Comment Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Add Author
            const authorIndex = workbook.worksheets.threadedCommentAuthors.add("Aspose Test", "", "");
            const author = workbook.worksheets.threadedCommentAuthors.get(authorIndex);

            // Add Threaded Comment to cell A1 in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.comments.addThreadedComment("A1", "Test Threaded Comment", author);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddThreadedComments_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Threaded comment added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Чтение ветвистых комментариев**

### **Чтение ветвистых комментариев с помощью Excel**

Для чтения ветвистых комментариев в Excel просто наведите курсор мыши на ячейку с комментариями, чтобы просмотреть комментарии. Просмотр комментариев будет выглядеть так же, как на следующем изображении.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Чтение ветвистых комментариев с использованием Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) для извлечения ветвистых комментариев для указанного столбца. Метод [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Вы можете перебирать [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) для просмотра комментариев.

В следующем примере демонстрируется чтение комментариев из столбца A1 путем загрузки [образца Excel-файла](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.

#### **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;
            let html = '<h2>Threaded Comments</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found for A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

#### **Вывод в консоль**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Прочтите дату создания ветвящихся комментариев**

Aspose.Cells предоставляет метод [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) для получения цепочечных комментариев для указанной колонки. Метод [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) принимает название колонки и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Вы можете перебрать [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) и использовать свойство [**ThreadedComment.createdTime**](https://reference.aspose.com/cells/javascript-cpp/threadedcomment/#createdTime--).

В следующем примере демонстрируется чтение времени создания ветвистых комментариев при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.

#### **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: allow errors to propagate for testing
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;

            let html = '<h2>Threaded Comments (Cell A1)</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found in cell A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    const createdTime = comment.createdTime;

                    console.log("Comment: " + notes);
                    console.log("Author: " + authorName);
                    console.log("Created Time: " + createdTime);

                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Created:</strong> ${createdTime} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;

            // No file modifications or save in this example; hide download link
            downloadLink.style.display = 'none';
        });
    </script>
</html>
```

#### **Вывод в консоль**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Редактировать ветвящиеся комментарии**

### **Редактировать ветвящийся комментарий с помощью Excel**

Чтобы отредактировать ветвистый комментарий в Excel, щелкните ссылку **Редактировать** в комментарии, как показано на следующем изображении.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Редактирование ветвящегося комментария с использованием Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) для получения цепочечных комментариев для указанной колонки. Метод [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) принимает название колонки и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Вы можете обновить нужный комментарий в [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) и сохранить книгу.

Следующий пример демонстрирует редактирование первого многослойного комментария в столбце A1 путем загрузки [примера Excel файла](89849861.xlsx). См. [сгенерированный Excel файл](89849862.xlsx), показывающий обновленный комментарий для ознакомления.

#### **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Edit Threaded Comments Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comment from cell A1
            const comment = worksheet.comments.threadedComments("A1").get(0);

            // Update the threaded comment notes
            comment.notes = "Updated Comment";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'EditThreadedComments.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Edited Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Threaded comment updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Удалить ветвящиеся комментарии**

### **Удалить ветвящиеся комментарии с помощью Excel**

Чтобы удалить ветвистые комментарии в Excel, щелкните правой кнопкой мыши на ячейке с комментариями и выберите опцию **Удалить комментарий**, как показано на следующем изображении.

![todo:image_alt_text](threaded-comments_8.jpg)
