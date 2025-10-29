---
title: Получить диапазон ячеек
type: docs
weight: 600
url: /ru/javascript-cpp/get-cells-range/
description: Узнайте, как получить диапазон ячеек через API Aspose.Cells for JavaScript через C++.
keywords: Получите максимальный диапазон отображения ячеек, получите максимальный ряд ячеек, получите максимальную строку данных ячеек, получите максимальный столбец ячеек, получите максимальный столбец данных ячеек. 
---

## **Возможные сценарии использования**
Когда вам нужно только манипулировать некоторыми данными на листе, необходимо знать диапазон данных всего листа. Aspose.Cells for JavaScript через C++ предлагает эту функцию. Aspose.Cells for JavaScript через C++ предоставляет следующие свойства и методы для достижения ваших целей.
- [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--)
- [**Cells.maxRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxRow--)
- [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--)
- [**Cells.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxColumn--)
- [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--)

## **Получить диапазон ячеек с помощью Aspose.Cells for JavaScript через C++**
Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Получить ячейки [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Inspect Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatType, Color } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new workbook with XLSX format
            const workbook = new Workbook(FileFormatType.Xlsx);
            const cells = workbook.worksheets.get(0).cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            cell = cells.get("E10");
            var temp = workbook.createStyle();
            temp.font.color = new Color(255, 0, 0);
            cell.style = temp;

            // Get max display range of worksheet
            var range = cells.maxDisplayRange;

            //get maximum row index of cell which contains data or style.
            var maxRow = cells.maxRow;

            //get maximum row index of cell which contains data.
            var maxDataRow = cells.maxDataRow;

            //get maximum column index of cell which contains data or style.
            var maxColumn = cells.maxColumn;

            //get maximum column index of cell which contains data.
            var maxDataColumn = cells.maxDataColumn;

            // Prepare result display
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Workbook created and populated.</p>' +
                `<p>Max Display Range: ${range ? range.address : 'N/A'}</p>` +
                `<p>Max Row (data or style): ${maxRow}</p>` +
                `<p>Max Data Row: ${maxDataRow}</p>` +
                `<p>Max Column (data or style): ${maxColumn}</p>` +
                `<p>Max Data Column: ${maxDataColumn}</p>`;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
