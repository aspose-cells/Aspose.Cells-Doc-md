---
title: Создание областей с именами, ограниченных рабочей книгой и листом, с помощью JavaScript через C++
linktitle: Именованный диапазон
type: docs
weight: 40
url: /ru/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Узнайте, как создавать области с именами, ограниченные рабочей книгой и листом, с помощью Script через C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям определить именованные диапазоны с двумя различными областями: книга (также известная как глобальная область) и лист.

- Именованные диапазоны с глобальной областью могут быть доступны с любого листа внутри этой книги, просто используя его имя.
- Именованные диапазоны с областью листа доступны с помощью ссылки на конкретный лист, на котором он был создан.

Script через C++ предоставляет такую же функциональность, как Microsoft Excel, для добавления областей с именами, ограниченными рабочей книгой и листом. При создании области с именем, ограниченной листом, следует использовать ссылку на лист в области с именем для указания ее как области, ограниченной листом.

{{% /alert %}} 
## **Добавление именованного диапазона с областью видимости рабочей книги**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>WorkbookScope Named Range Example</title>
    </head>
    <body>
        <h1>WorkbookScope Named Range Example</h1>
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

            // If a file is provided, load it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells from Cell A1 to C10
            const workbookScope = cells.createRange("A1", "C10");

            // Assign the name to workbook scope named range
            workbookScope.name = "workbookScope";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookScope.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range "workbookScope" created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
## **Добавление Именованного Диапазона с Областью Листа**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Assign Range Name Example</h1>
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

            // Create new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells
            const localRange = cells.createRange("A1", "C10");

            // Assign name to range with sheet reference
            localRange.name = "Sheet1!local";

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Создание доступа и копирование именованных диапазонов](/cells/ru/javascript-cpp/create-access-and-copy-named-ranges/)
- [Форматирование и изменение именованных диапазонов](/cells/ru/javascript-cpp/format-and-modify-named-ranges/)
- [Получить диапазон с внешними ссылками](/cells/ru/javascript-cpp/get-range-with-external-links/)
- [Реализация не последовательных диапазонов](/cells/ru/javascript-cpp/implementing-non-sequential-ranges/)
