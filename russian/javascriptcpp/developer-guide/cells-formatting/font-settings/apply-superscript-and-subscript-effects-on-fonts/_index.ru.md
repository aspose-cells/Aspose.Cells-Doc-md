---
title: Применение эффектов надстрочного и подстрочного индексов к шрифтам
linktitle: Применение эффектов надстрочного и подстрочного индексов к шрифтам
type: docs
weight: 80
url: /ru/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/
description: JavaScript код для применения эффектов надстрочного и подстрочного текста в Excel с помощью Script Aspose.Cells for Java через C++.
keywords: надстрочный JavaScript для Excel через C++, подстрочный JavaScript для Excel через C++, надстрочный и подстрочный JavaScript для Excel через C++, вставка подстрочного и надстрочного текста в Excel JavaScript через C++, добавление подстрочного и надстрочного в Excel JavaScript через C++, добавление надстрочного и подстрочного в Excel JavaScript через C++, добавление надстрочного в Excel JavaScript через C++, добавление подстрочного в Excel JavaScript через C++
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет возможность применять эффекты надстрочного (текст над базовой линией) и подстрочного (текст под базовой линией) к тексту.

{{% /alert %}}

## **Работа с надстрочным и подстрочным индексами**

Для применения эффекта надстрочного текста установите свойство [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-) объекта [**Font**](https://reference.aspose.com/cells/javascript-cpp/font) в значение **true**. Для применения подстрочного текста установите свойство [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-) объекта [**Font**](https://reference.aspose.com/cells/javascript-cpp/font) в значение **true**.

Приведенные ниже примеры кода показывают, как применить надстрочный и подстрочный текст.

### JavaScript код для применения эффекта надстрочного текста

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Superscript Example</title>
    </head>
    <body>
        <h1>Superscript Example</h1>
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

            // Adding a new worksheet to the Excel object
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello";

            // Setting the font Superscript
            const style = cell.style;
            style.font.isSuperscript = true;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Superscript.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### JavaScript код для применения эффекта подстрочного текста

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Subscript Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello";

            // Setting the font Subscript
            const style = cell.style;
            style.font.isSubscript = true;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Subscript.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created with subscript formatting. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
