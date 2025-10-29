---
title: Как масштабировать лист с помощью JavaScript через C++
linktitle: Как масштабировать лист
type: docs
weight: 130
url: /ru/javascript-cpp/how-to-scale-a-worksheet/
description: В этой статье представлен код, объясняющий, как масштабировать лист с помощью Aspose.Cells for JavaScript через C++.
keywords: Масштабирование листа с помощью JavaScript, Как масштабировать лист с помощью JavaScript через C++, Масштабировать лист с помощью JavaScript через C++.
---

## **Возможные сценарии использования**
Масштабирование листа может быть полезно по разным причинам, в зависимости от контекста работы. Вот несколько распространенных причин масштабирования листа:
1. Вписать в страницу: чтобы обеспечить умещание всего содержимого на одной странице или заданном количестве страниц при печати, облегчая чтение и управление без необходимости пролистывать несколько страниц.

1. Презентация: чтобы сделать лист более организованным и профессиональным, особенно при совместном использовании в заседаниях или отчетах.

1. Читаемость: чтобы настроить размер текста и других элементов для лучшей читаемости, особенно для людей с проблемами восприятия мелкого шрифта.

1. Управление пространством: чтобы оптимизировать использование пространства на листе, исключая ненужное пустое пространство и обеспечивая видимость всей важной информации без чрезмерной прокрутки.

1. Визуализация данных: для диаграмм и графиков масштаб может помочь сделать их более понятными, корректируя размер для соответствия доступному пространству.

1. Последовательность: чтобы поддерживать единый стиль и ощущение во многих листах или документах, что особенно важно в профессиональной и образовательной среде.

## **Как масштабировать лист в Excel**
Масштабирование листа в Excel помогает поместить содержимое на одну страницу или заданное количество страниц при печати. Вот шаги для масштабирования листа:

1. Откройте свой лист: откройте Excel-таблицу, которую хотите масштабировать.

1. Перейдите на вкладку Макет страницы: нажмите на вкладку Макет страницы в ленте.

1. Группа Масштаб для подгонки: в разделе Макет страницы найдите группу Масштаб для подгонки. Здесь есть параметры для регулировки масштабирования. Ширина: позволяет указать, сколько страниц по ширине будет занимать печатанный лист. Высота: позволяет указать, сколько страниц по высоте будет занимать печатанный лист. Масштаб: можно также установить пользовательский процент масштабирования.
<br>
<img src="1.png" width=60% />

1. Настройка ширины и высоты: задайте желаемое количество страниц по ширине и высоте. Например, оба по 1 странице, если хотите, чтобы лист помещался на одной странице.

1. Настройка процента масштабирования (при необходимости): если предпочитаете задать конкретный процент масштабирования, настройте поле Масштаб. Например, установка на 50% сделает всё в два раза меньше.


## **Как масштабировать лист с помощью JavaScript через C++**
Aspose.Cells for JavaScript через C++ — мощная библиотека для работы с файлами Excel программным способом. Чтобы масштабировать лист с помощью Aspose.Cells, необходимо выполнить следующие шаги: загрузите [пример файла](sample.xlsx) и настройте параметры печати так, чтобы содержимое помещалось на нужное количество страниц или под выбранный процент от исходного размера.

### **Пример: Подгонка под страницу**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **Пример: Масштабирование в процентное соотношение**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />
