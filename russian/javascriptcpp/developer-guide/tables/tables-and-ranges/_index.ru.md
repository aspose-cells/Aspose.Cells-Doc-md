---
title: Таблицы и диапазоны с помощью JavaScript через C++
linktitle: Таблицы и диапазоны
type: docs
weight: 50
url: /ru/javascript-cpp/tables-and-ranges/
---

## **Введение**  

Иногда вы создаете таблицу в Microsoft Excel и не хотите продолжать работу с функциональностью таблицы, которая в ней есть. Вместо этого вы хотите что-то, что похоже на таблицу. Чтобы сохранить данные в таблице без потери форматирования, преобразуйте таблицу в обычный диапазон данных.  
Aspose.Cells действительно поддерживает эту функцию Microsoft Excel для таблиц и объектов списка.  

## **Использование Microsoft Excel**  

Используйте функцию **Преобразовать в диапазон** , чтобы быстро преобразовать таблицу в диапазон без потери форматирования. В Microsoft Excel 2007/2010:  

1. Щелкните в любом месте таблицы, чтобы активная ячейка находилась в столбце таблицы.  
1. На вкладке **Разрботка** , в группе **Инструменты** , щелкните **Преобразовать в диапазон** .  

## **Использование Aspose.Cells**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Table to Range</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and convert the first table/list object to a normal range
            const worksheet = workbook.worksheets.get(0);
            const listObject = worksheet.listObjects.get(0);
            listObject.convertToRange();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

После преобразования таблицы в диапазон функции таблицы больше не доступны. Например, заголовки строк больше не включают стрелки сортировки и фильтра, и структурированные ссылки (ссылки, использующие имена таблиц) , используемые в формулах, превращаются в обычные ссылки на ячейки.  

{{% /alert %}}  

## **Преобразовать таблицу в диапазон с параметрами**  

Aspose.Cells предоставляет дополнительные опции при преобразовании таблицы в диапазон с помощью класса [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/).  Класс [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/) предоставляет свойство [**lastRow**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/#lastRow--), которое позволяет установить последний индекс строки таблицы. Форматирование таблицы будет сохранено до указанного индекса строки, а остальное форматирование будет удалено.  

Приведенный ниже примерный код демонстрирует использование класса [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Table to Range Example</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TableToRangeOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create TableToRangeOptions and set lastRow property
            const options = new TableToRangeOptions();
            options.lastRow = 5;

            // Convert the first table/list object (from the first worksheet) to normal range
            workbook.worksheets.get(0).listObjects.get(0).convertToRange(options);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
