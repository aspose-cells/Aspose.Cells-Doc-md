---
title: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 290
url: /ru/javascript-cpp/sort-data-in-column-with-custom-sort-list/
description: Узнайте, как сортировать данные в столбце с помощью пользовательского списка с помощью скрипта Aspose.Cells for Java и API C++.
keywords: Сортировка данных в столбце с помощью пользовательского списка, Сортировка данных по пользовательскому списку.
---

## **Возможные сценарии использования**

Вы можете отсортировать данные в столбце, используя пользовательский список. Это можно сделать с помощью метода [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-string-). Однако этот метод работает только в случае, если элементы в пользовательском списке не содержат запятых. Если там есть запятые, как в "USA,US", "China,CN" и т.д., тогда необходимо использовать метод [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-). Здесь последний параметр — не строка, а массив строк.

## **Сортировка данных в столбце с пользовательским списком**

Следующий пример кода показывает, как использовать метод [**DataSorter.addKey(number, SortOrder, string[])**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addKey-number-sortorder-stringarray-) для сортировки данных с помощью пользовательского списка сортировки. Пожалуйста, посмотрите на [пример файла Excel](50528327.xlsx), используемый в этом коде, и [сгенерированный выходной файл Excel](50528328.xlsx). Следующий скриншот показывает эффект работы кода на примере файла Excel при выполнении.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort List</title>
    </head>
    <body>
        <h1>Custom Sort List Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Specify cell area - sort from A1 to A40
            const ca = AsposeCells.CellArea.createCellArea("A1", "A40");

            // Create Custom Sort list
            const customSortList = ["USA,US", "Brazil,BR", "China,CN", "Russia,RU", "Canada,CA"];

            // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
            wb.dataSorter.addKey(0, AsposeCells.SortOrder.Ascending, customSortList);

            wb.dataSorter.sort(ws.cells, ca);

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
