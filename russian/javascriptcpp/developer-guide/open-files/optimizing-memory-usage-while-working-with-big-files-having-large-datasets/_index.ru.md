---
title: Оптимизация использования памяти при работе с большими файлами с большими наборами данных с помощью JavaScript через C++
linktitle: Оптимизация использования памяти при работе с большими файлами с большими наборами данных
type: docs
weight: 180
url: /ru/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

При создании рабочей книги с большими наборами данных или при чтении большого файла Microsoft Excel всегда актуальна проблема использования RAM. Существуют меры, которые могут быть адаптированы для решения этой задачи. Aspose.Cells for JavaScript через C++ предоставляет некоторые важные параметры и вызовы API для снижения, уменьшения и оптимизации использования памяти. Также, он помогает процессу работать более эффективно и быстрее.

Используйте опцию [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) для оптимизации использования памяти для данных ячеек и уменьшения общей затраты памяти. При создании большого набора данных для ячеек можно сохранить определенное количество памяти по сравнению с использованием настройки по умолчанию ([**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)).

{{% /alert %}}

## **Оптимизация памяти**

### **Чтение больших файлов Excel**

Следующий пример показывает, как считать большой файл Microsoft Excel в оптимизированном режиме.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - LoadOptions MemorySetting</title>
    </head>
    <body>
        <h1>LoadOptions MemorySetting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, MemorySetting, SaveFormat, Utils } = AsposeCells;

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

            // Specify the LoadOptions
            const opt = new LoadOptions();
            // Set the memory preferences (converted from setMemorySetting)
            opt.memorySetting = MemorySetting.MemoryPreference;

            // Instantiate the Workbook - load the big Excel file with options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opt);

            // Save the workbook to XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook loaded with MemoryPreference. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Запись больших файлов Excel**

Следующий пример показывает, как записать большой набор данных на листе в оптимизированном режиме.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Memory Setting Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Memory Setting Example</h1>
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
                // If no file is selected, create a new workbook (similar to new AsposeCells.Workbook() in Node)
                // and proceed to set memory settings and populate sheets.
            }

            // Load workbook from file if provided, otherwise create empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Set the memory preferences on the workbook settings
            workbook.settings.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook
            // To change the memory setting of existing sheets, change memory setting for them manually:
            let cells = workbook.worksheets.get(0).cells;
            cells.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells to demonstrate
            const firstCell = cells.get(0, 0);
            firstCell.value = "Sample Data 1";
            cells.get(1, 0).value = "Sample Data 2";

            // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
            const sheet2 = workbook.worksheets.add("Sheet2");
            const cells2 = sheet2.cells;
            // .........
            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells in Sheet2
            cells2.get(0, 0).value = "Sheet2 Data 1";
            cells2.get(1, 0).value = "Sheet2 Data 2";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Предостережение**

Стандартная настройка, [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/), применяется ко всем версиям. В некоторых случаях при создании рабочей книги с большим набором данных для ячеек опция [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) может оптимизировать использование памяти и снизить расходы на память. Однако в некоторых случаях это может снизить производительность, например, как описано ниже.

1. **Доступ к ячейкам случайным образом и повторно**: наиболее эффективная последовательность доступа к коллекции ячеек — ячейка за ячейкой по строке, затем строка за строкой. Особенно, если вы получаете доступ к строкам/ячейкам через перечислитель, полученный из [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) и [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), производительность будет максимально возможной с [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
2. **Вставка и удаление ячеек и строк**: обратите внимание, что при большом количестве операций вставки/удаления для ячеек/строк производительность заметно ухудшается в режиме *MemoryPreference* по сравнению с режимом *Normal*.
3. **Работа с разными типами ячеек**: если большинство ячеек содержат строковые значения или формулы, затраты памяти будут примерно такими же, как в режиме *Normal*, но если много пустых ячеек или значения ячеек — числовые, логические и т.п., то опция [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) обеспечит лучшую производительность.
