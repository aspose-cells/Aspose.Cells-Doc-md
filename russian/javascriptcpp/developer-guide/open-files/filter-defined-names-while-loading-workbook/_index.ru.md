---
title: Фильтрация определённых имен при загрузке рабочей книги с помощью JavaScript через C++
linktitle: Фильтрация заданных имен при загрузке рабочей книги
type: docs
weight: 50
url: /ru/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет фильтровать или удалять определенные имена внутри рабочей книги. Пожалуйста, используйте [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) для загрузки определенных имен и [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) для их удаления при загрузке книги. Обратите внимание, что при удалении определенных имен формулы внутри книги могут перестать работать.

## **Фильтрация заданных имен при загрузке рабочей книги**

Следующий пример кода загружает [пример файла Excel](61767860.xlsx), в ячейке **C1** содержится формула с определенными именами, т.е. *=SUM(MyName1, MyName2)*. Поскольку мы используем [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) для удаления определенных имен при загрузке, формула в ячейке C1 в [выходной Excel-файл](61767861.xlsx) ломается, и вместо этого отображается *#NAME?*. Посмотрите следующий скриншот, который демонстрирует эффект кода на пример файла Excel.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
