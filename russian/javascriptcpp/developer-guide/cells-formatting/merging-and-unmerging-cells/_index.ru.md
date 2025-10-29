---
title: Объединение и разъединение ячеек с помощью JavaScript через C++
linktitle: Объединение и разъединение ячеек
description: Aspose.Cells — это библиотека JavaScript для работы с файлами электронных таблиц, которая поддерживает объединение и разделение ячеек. В этой статье будет рассказано о том, как объединять и разбивать ячейки с помощью библиотеки Aspose.Cells, а также о настройках пользовательских стилей объединённых ячеек.
keywords: Aspose.Cells, библиотека JavaScript, таблица, объединение ячеек, разделение ячеек, настройки стилей, пользовательские стили
type: docs
weight: 190
url: /ru/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает эту функцию и также может объединять ячейки в листе. Вы также можете разъединить или разделить объединенные ячейки. Ссылка на объединенную ячейку - это ссылка на верхнюю левую ячейку в изначально выбранном диапазоне.

{{% /alert %}} 
## **Введение**
Не всегда нужно иметь одинаковое количество ячеек в каждой строке или столбце. Например, вы можете захотеть поместить заголовок в ячейку, которая охватывает несколько столбцов. Или, если создаете счет-фактуру, вам может понадобиться меньше столбцов для итоговой суммы. Чтобы объединить несколько ячеек в одну, объедините их. Microsoft Excel позволяет пользователям выбирать файлы и объединять их, чтобы структурировать электронную таблицу так, как им нужно.

{{% alert color="primary" %}} 

Обратите внимание, что при объединении ячеек сохраняются только данные в верхней левый ячейке. Если в других ячейках диапазона есть данные, эти данные удаляются. Форматирование также основывается на ссылочной ячейке, поэтому при объединении ячеек настройки форматирования верхней левой ячейки диапазона применяются к объединенной ячейке. Когда ячейки разбиваются, новые ячейки сохраняют свои исходные настройки формата.

{{% /alert %}} 
## **Объединение ячеек в листе**
### **Объединение ячеек в Microsoft Excel**
Следующие шаги описывают, как объединить ячейки в электронной таблице с использованием MS Excel.

1. Копируйте данные, которые вы хотите в верхнюю левую ячейку в пределах диапазона.
1. Выберите ячейки, которые вы хотите объединить.
1. Чтобы объединить ячейки в строке или столбце и центрировать содержимое ячейки, нажмите на значок **Объединить и центрировать** на панели инструментов **Форматирование**.

### **Объединение ячеек с помощью Aspose.Cells**
Класс Aspose.Cells.Cells содержит полезные методы для выполнения этой задачи. Например, метод `merge()` объединяет ячейки в одну в заданном диапазоне.

В следующем примере показано, как объединить ячейки (C6:E7) в электронной таблице.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Разъединение (разделение) объединенных ячеек**
### **Использование Microsoft Excel**
Следующие шаги описывают, как разделить объединенные ячейки с помощью Microsoft Excel.

1. Выберите объединенную ячейку.
   Когда ячейки были объединены, на панели инструментов **Форматирование** выбрано **Объединить и центрировать**.
1. Нажмите на **Объединить и центрировать** на панели инструментов **Форматирование**.

### **Использование Aspose.Cells**
Класс Aspose.Cells.Cells содержит метод `unmerge()`, который разбивает ячейки до их исходного состояния. Метод разъединяет ячейки, используя ссылку ячейки в диапазоне объединенных ячеек.

Приведенный ниже пример показывает, как разделить объединенные ячейки (C6). Пример использует файл, созданный в предыдущем примере, и разбивает объединенные ячейки.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Обнаружение объединенных ячеек в листе](/cells/ru/javascript-cpp/detect-merged-cells-in-a-worksheet/)
