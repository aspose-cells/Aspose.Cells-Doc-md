---
title: Функции настройки страниц с помощью JavaScript через C++
linktitle: Функции настройки страницы
type: docs
weight: 60
url: /ru/javascript-cpp/page-setup-features/
description: Изучите функции настройки страниц с помощью Aspose.Cells for JavaScript через C++. Узнайте, как настраивать размеры страниц, ориентацию и настройки.
keywords: Функции настройки страниц JavaScript через C++, настройка размеров страниц JavaScript через C++, настройки ориентации страницы JavaScript через C++
---

## **Введение**
С Aspose.Cells for JavaScript через C++ вы можете управлять различными функциями настройки страницы рабочей книги Excel. Эти функции включают установку размера страницы, ориентации, полей и многое другое. Правильная настройка этих функций обеспечивает лучшую печать и просмотр документа.

## **Установка размера и ориентации страницы**
Вы можете указать размер и ориентацию страницы рабочего листа с помощью класса `PageSetup`. Он предоставляет различные свойства для управления размерами и расположением страницы.

### **Пример кода**
Вот пример кода, демонстрирующий, как установить размер и ориентацию страницы.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Установка полей**
Вы также можете задать поля для страницы, используя тот же класс `PageSetup`. Поля можно настроить для левой, правой, верхней и нижней сторон.

### **Пример кода**
Вот как вы можете установить поля рабочего листа.
