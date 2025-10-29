---
title: Чтение и запись таблицы запросов на листе с помощью JavaScript через C++
linktitle: Чтение и запись запросов таблицы рабочего листа
type: docs
weight: 40
url: /ru/javascript-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет коллекцию Worksheet.QueryTables, которая возвращает объект типа QueryTable по индексу. У него есть два следующих свойства

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

Оба этих значения являются логическими. Вы можете просмотреть их в Microsoft Excel через Данные > Подключения > Свойства.

{{% /alert %}}

## Чтение и запись запросов таблицы рабочего листа

Следующий пример кода читает первую QueryTable первого листа и выводит оба свойства QueryTable. Затем он устанавливает свойство QueryTable.preserveFormatting в значение true.

Вы можете загрузить исходный файл Excel, используемый в этом коде, и выходной файл Excel, созданный кодом, по следующим ссылкам.

- [Исходный файл Excel](5115533.xlsx)
- [Выходной файл Excel](5115537.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells QueryTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
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
            document.getElementById('runExample').disabled = false;
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

            // Create workbook from source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first Query Table
            const qt = worksheet.queryTables.get(0);

            // Read Query Table Data (properties converted from getters)
            const adjustColumnWidth = qt.adjustColumnWidth;
            const preserveFormatting = qt.preserveFormatting;

            resultDiv.innerHTML = `<p>Adjust Column Width: ${adjustColumnWidth}</p><p>Preserve Formatting: ${preserveFormatting}</p>`;

            // Now set Preserve Formatting to true (setter converted to property assignment)
            qt.preserveFormatting = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">PreserveFormatting set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Вывод в консоли



{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Получение диапазона результатов запроса таблицы

Aspose.Cells предоставляет возможность чтения адреса, то есть диапазона результатов ячеек для таблицы запросов. Следующий код демонстрирует эту функцию, считывая адрес диапазона результатов для таблицы запросов. Образец файла можно скачать [здесь](72417290.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const queryTable = worksheet.queryTables.get(0);
            const resultRange = queryTable.resultRange;
            const address = resultRange.address;

            const addressText = (address && typeof address.toString === 'function') ? address.toString() : String(address);
            console.log(addressText);
            document.getElementById('result').innerHTML = `<p>Query table result range address: ${addressText}</p>`;
        });
    </script>
</html>
```
