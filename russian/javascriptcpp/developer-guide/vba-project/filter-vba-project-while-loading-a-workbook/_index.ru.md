---
title: Фильтрация проекта VBA при загрузке рабочей книги с помощью JavaScript через C++
linktitle: Фильтрация проекта VBA при загрузке книги
type: docs
weight: 140
url: /ru/javascript-cpp/filter-vba-project-while-loading-a-workbook/
description: Узнайте, как фильтровать VBA проекты при загрузке книг Excel с помощью Aspose.Cells for JavaScript через C++.
---

## **Фильтрация VBA-проекта при загрузке книги Excel в JavaScript через C++**

Некоторые файлы .xlsm/.xslb содержат чрезвычайно большое количество макросов (или очень длинных макросов). Aspose.Cells for JavaScript через C++ будет безусловно загружать эти (мета) данные при открытии таких книг. Возможно, потребуется контролировать это через [**LoadDataFilterOptions**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions), если вам действительно нужно только извлечь имена листов для большого количества книг, пропуская ненужный контент. Этот фильтр реализуется путём добавления новой опции, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions).

## **Образец кода**

Приведенный ниже образец кода загружает книгу так, чтобы было выполнено только фильтрование VBA. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sample Macro-Enabled Workbook to XLSM</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Set the load options, we do not want to load VBA
            const loadOptions = new LoadOptions(LoadFormat.Auto);
            const loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.VBA);
            loadOptions.loadFilter = loadFilter;

            // Create workbook object from uploaded file using load options
            const book = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in xlsm format
            const outputData = book.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputSampleMacroEnabledWorkbook.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download OutputSampleMacroEnabledWorkbook.xlsm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Processing completed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
