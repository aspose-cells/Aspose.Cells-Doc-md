---
title: Настройка различных заголовков и нижних колонтитулов для разных страниц с помощью JavaScript через C++
linktitle: Установка разных заголовков и нижних колонтитулов для разных страниц
type: docs
weight: 35
url: /ru/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: В этой статье предоставлен пример кода, показывающий, как программно установить заголовки и нижние колонтитулы страницы настройки листа Excel с помощью Aspose.Cells for JavaScript через C++. Установите заголовки и нижние колонтитулы для первых, нечетных и четных страниц.
keywords: установить заголовок и нижний колонтитул Excel для первой страницы с помощью JavaScript через C++, установить заголовок и нижний колонтитул Excel для нечетных страниц с помощью JavaScript через C++, установить заголовок и нижний колонтитул Excel для четных страниц с помощью JavaScript через C++
---

{{% alert color="primary" %}}

MS Excel поддерживает установку различных заголовков и нижних колонтитулов для первой страницы, нечетных страниц и четных страниц, начиная с Excel 2007.
Aspose.Cells for JavaScript через C++ поддерживает ту же функцию.

{{% /alert %}}

## **Установка разных заголовков и нижних колонтитулов в MS Excel**

**![Установка различных заголовков и нижних колонтитулов](difpage.png)**

1. Нажмите **Разметка страницы > Печать заголовков > Заголовок/нижний колонтитул**.
1. Установите флаги **Different Odd and Even Pages** или **Different first page**.
1. Введите разные заголовки и нижние колонтитулы.

## **Настройка различных заголовков и нижних колонтитулов с помощью Aspose.Cells for JavaScript через C++**

Aspose.Cells ведет себя так же, как Excel.
1. Устанавливает флаги [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) и [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) 
1. Введите разные заголовки и нижние колонтитулы.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
