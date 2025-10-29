---
title: Указание предупреждения сортировки при сортировке данных
type: docs
weight: 140
url: /ru/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: Узнайте, как указывать предупреждение при сортировке данных с помощью скрипта Aspose.Cells for Java и API C++.
keywords: Добавить предупреждение о сортировке при сортировке данных, установить предупреждение о сортировке при сортировке данных, выбрать предупреждение о сортировке при сортировке данных.
---

## **Возможные сценарии использования**

Рассмотрите эти текстовые данные, т.е. {11, 111, 22}. Они отсортированы как текст, потому что 111 идет перед 22. Но если вы хотите сортировать эти данные как числа, то они будут {11, 22, 111}, так как числовое значение 111 следует за 22. Скрипт Aspose.Cells for Java через C++ предоставляет свойство {0} для решения этой задачи. Установите это свойство в **true**, и ваш текст будет отсортирован как числовые данные. Следующий скриншот показывает предупреждение о сортировке, которое отображает Microsoft Excel, когда сортируются текстовые данные, похожие на числовые.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Образец кода**

В следующем образце кода показано использование свойства [**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-), как объяснено ранее. Пожалуйста, проверьте его [образцовый файл Excel](43352075.xlsx) и [выходной файл Excel](43352076.xlsx) для получения дополнительной помощи.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
