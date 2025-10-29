---
title: Анализ кэшированных записей сводной таблицы при загрузке файла Excel
type: docs
weight: 70
url: /ru/javascript-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Возможные сценарии использования**

При создании сводной таблицы Microsoft Excel делает копию исходных данных и хранит их в кэше сводной таблицы. Кэш сводной таблицы хранится в памяти Microsoft Excel. Вы его не видите, но это данные, на которые ссылается сводная таблица при построении или изменении выбора среза или перемещении строк/столбцов. Это позволяет Microsoft Excel очень быстро реагировать на изменения сводной таблицы, но также может удвоить размер вашего файла. В конце концов, кэш сводной таблицы просто дублирует ваши исходные данные, поэтому логично, что размер вашего файла может увеличиться вдвое.

При загрузке вашего файла Excel внутри объекта Workbook вы можете решить, загружать ли также записи кэша сводной таблицы, используя свойство [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-). Значение по умолчанию этого свойства — **false**. Если кэш сводной таблицы достаточно большой, это может повысить производительность. Но если вы также хотите загрузить записи кэша, установите это свойство в **true**.

## **Анализ кэшированных записей сводной таблицы при загрузке файла Excel**

Следующий пример объясняет использование свойства [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-). Он загружает [пример файла Excel](61767773.xlsx), одновременно парся записи кэша сводной таблицы. Затем он обновляет сводную таблицу и сохраняет ее как [выходной файл Excel](61767774.xlsx).

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Parsing Pivot Cached Records While Loading Example</title>
    </head>
    <body>
        <h1>Parsing Pivot Cached Records While Loading Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options
            const options = new LoadOptions();
            // Set ParsingPivotCachedRecords true, default value is false
            options.parsingPivotCachedRecords = true;

            // Load the Excel file with load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first pivot table
            const pt = ws.pivotTables.get(0);

            // Set refresh data flag true
            pt.refreshDataFlag = true;

            // Refresh and calculate pivot table
            pt.refreshData();
            pt.calculateData();

            // Set refresh data flag false
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
