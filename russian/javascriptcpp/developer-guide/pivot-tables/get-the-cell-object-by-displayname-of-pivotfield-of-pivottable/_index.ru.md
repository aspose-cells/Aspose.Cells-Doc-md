---
title: Получение объекта ячейки по отображаемому имени поля сводной таблицы
type: docs
weight: 70
url: /ru/javascript-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Как получить объект ячейки по DisplayName поля сводной таблицы с помощью Aspose.Cells for JavaScript для C++.
keywords: Aspose.Cells for JavaScript для C++ Excel, библиотека Excel JavaScript, Получить объект ячейки по DisplayName поля сводной таблицы с помощью Aspose.Cells for JavaScript для C++.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript для C++ предоставляет метод [**PivotTable.cellByDisplayName(string)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#cellByDisplayName-string-), который можно использовать для доступа к объекту ячейки по отображаемому имени поля сводной таблицы. Этот метод полезен, когда нужно выделить или отформатировать заголовок поля сводной таблицы. В этой статье объясняется, как получить объект ячейки по отображаемому имени поля данных и применить к нему форматирование.

{{% /alert %}}

## **Как получить объект ячейки по отображаемому имени поля сводной таблицы**

Приведенный ниже код получает доступ к первой сводной таблице на листе, а затем получает ячейку по отображаемому имени второго поля данных сводной таблицы. Затем он меняет цвет заливки и цвет шрифта ячейки на голубой и черный соответственно. Ниже приведены скриншоты, показывающие, как выглядит сводная таблица до и после выполнения кода.

|**СводнаяТаблица - До**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pivot Table Cell Styling Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table inside the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Access cell by display name of 2nd data field of the pivot table
            const dataFieldDisplayName = pivotTable.dataFields.get(1).displayName;
            const cell = pivotTable.cellByDisplayName(dataFieldDisplayName);

            // Access cell style and set its fill color and font color
            const style = cell.style;
            style.foregroundColor = AsposeCells.Color.LightBlue;
            style.font.color = AsposeCells.Color.Black;

            // Set the style of the cell
            pivotTable.format(cell.row, cell.column, style);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

|**СводнаяТаблица - После**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
