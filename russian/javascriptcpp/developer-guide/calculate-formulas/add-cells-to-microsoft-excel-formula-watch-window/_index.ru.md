---
title: Добавление ячеек в окно наблюдения формул Microsoft Excel с помощью JavaScript через C++
linktitle: Добавление ячеек в окно наблюдения формул Microsoft Excel
description: Как использовать библиотеку Aspose.Cells для добавления ячеек в окно наблюдения формул в Excel с помощью JavaScript через C++. Загружая существующий файл Excel или создавая новый, мы можем манипулировать ячейками и задавать формулы. В конце мы сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, окно наблюдения формул, ячейки, добавление, JavaScript через C++
type: docs
weight: 60
url: /ru/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Возможные сценарии использования**

Окно наблюдения Microsoft Excel — полезный инструмент для удобного отслеживания значений ячеек и их формул. Вы можете открыть *Окно наблюдения* в Microsoft Excel, щёлкнув по *Формулы > Окно наблюдения*. В нём есть кнопка *Добавить наблюдение*, которую можно использовать для добавления ячеек для проверки. Аналогично, вы можете использовать метод [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-), чтобы добавлять ячейки в *Окно наблюдения* через API Aspose.Cells.

## **Добавление ячеек в окно наблюдения формул Microsoft Excel**

Следующий пример кода задаёт формулу ячеек C1 и E1 и добавляет их в Окно наблюдения. Затем он сохраняет рабочую книгу как [выходной файл Excel](67338481.xlsx). Если открыть выходной файл Excel и просмотреть *Окно наблюдения*, вы увидите обе ячейки, как показано на скриншоте.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
