---
title: Удаление именованных диапазонов с помощью JavaScript через C++
linktitle: Удалить именованные диапазоны
type: docs
weight: 90
url: /ru/javascript-cpp/Delete-named-ranges/
description: Вы можете узнать, как удалять определенные имена или именованные диапазоны из файлов Excel или OpenOffice с помощью Script через C++.
---

## **Введение**
Если в файлах Excel слишком много определенных имен или именованных диапазонов, некоторые из них придется очистить, чтобы они больше не использовались.

## **Удалить именованный диапазон в MS Excel**

Для удаления именованного диапазона из Excel следуйте этим шагам:
1. Откройте Microsoft Excel и откройте книгу, которая содержит именованный диапазон.
2. Перейдите на вкладку "Формулы" на ленте Excel.
3. Нажмите кнопку "Менеджер имен" в группе "Определенные имена". Это откроет диалоговое окно Менеджер имен.
4. В диалоговом окне Менеджер имен выберите именованный диапазон, который вы хотите удалить.
5. Нажмите кнопку "Удалить". Подтвердите удаление по запросу.
6. Нажмите кнопку "Закрыть", чтобы закрыть диалоговое окно Менеджер имен.
7. Сохраните книгу, чтобы сохранить внесенные изменения.

## **Удаление именованного диапазона с помощью Script через C++**
С помощью Script через C++ вы можете удалять именованные диапазоны или определенные имена по [тексту](https://reference.aspose.com/cells/javascript-cpp/namecollection/#remove-string-) или [индексу](https://reference.aspose.com/cells/javascript-cpp/namecollection/#removeAt-number-) из списка.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Named Ranges Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted a named range by text.
            worksheets.names.remove("NamedRange");

            // Deleted a defined name by index. Ensure to check the count before removal.
            if (worksheets.names.count > 0) {
                worksheets.names.removeAt(0);
            }

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Примечание: если определенное имя используется в формулах, его невозможно удалить. Мы можем удалить только формулу определенного имени.

## **Удаляет несколько именованных диапазонов**
При удалении определенного имени нужно проверить, используется ли оно во всех формулах в файле.
Для повышения производительности удаления именованных диапазонов, мы можем удалять некоторые их сразу вместе.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Named Ranges Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Delete some defined names.
            worksheets.names.remove(["NamedRange1", "NamedRange2"]);

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Удаление дублированных определенных имен**
Некоторые файлы Excel повреждаются, потому что некоторые определенные имена дублируются. Поэтому мы можем удалить эти дублирующиеся имена для восстановления файла.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Duplicate Defined Names</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted some defined names.
            worksheets.names.removeDuplicateNames();

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Duplicate defined names removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
