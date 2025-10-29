---
title: Установить комментарий таблицы или объекта списка внутри листа с помощью JavaScript через C++
linktitle: Установите комментарий к таблице или объекту списка внутри листа
type: docs
weight: 40
url: /ru/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Изучите, как установить комментарий таблицы или объекта списка внутри листа с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Вы можете установить комментарий для таблицы или списка внутри листа, используя свойство [**ListObject.comment**](https://reference.aspose.com/cells/javascript-cpp/listobject/#comment--). Комментарий будет отображаться внутри файла xl/tables/tableName.xml.

{{% /alert %}}

## **Установите комментарий таблицы или объекта списка внутри листа.**

Нижеприведенный образец кода загружает [исходный файл Excel](5115514.xlsx), устанавливает комментарий для первой таблицы или объекта списка на листе.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Comment of Table/ListObject</title>
    </head>
    <body>
        <h1>Set Comment of Table/ListObject</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first list object or table.
            const lstObj = worksheet.listObjects.get(0);

            // Set the comment of the list object
            lstObj.comment = "This is Aspose.Cells comment.";

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetCommentOfTableOrListObject_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
