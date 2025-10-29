---
title: Вырезать и вставить диапазон с помощью JavaScript через C++
linktitle: Вырезать и вставить диапазон
type: docs
weight: 130
url: /ru/javascript-cpp/cut-and-paste-cells/
description: Узнайте, как вырезать и вставить ячейки внутри листа с помощью Aspose.Cells for JavaScript через C++.
---

## **Вырезать и вставить ячейки**

Aspose.Cells for JavaScript через C++ позволяет вырезать и вставлять ячейки внутри листа, используя метод [**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/). [**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) принимает следующие параметры.  

- [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/): Диапазон ячеек для вырезания.  
- Индекс строки: Индекс строки для вставки ячеек.  
- Индекс столбца: Индекс столбца для вставки ячеек.  
- [**ShiftType**](https://reference.aspose.com/cells/javascript-cpp/shifttype/): Направление сдвига столбцов.  

В следующем примере показано, как вырезать и вставить ячейки в пределах рабочего листа.  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Cut and Paste Cells Example</title>
    </head>
    <body>
        <h1>Cut and Paste Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ShiftType } = AsposeCells;

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

            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);

            // Set cell values (columns are zero-based; C is column 2)
            worksheet.cells.get(0, 2).value = 1;
            worksheet.cells.get(1, 2).value = 2;
            worksheet.cells.get(2, 2).value = 3;
            worksheet.cells.get(2, 3).value = 4;

            // Create a named range for the block starting at row 0, column 2, 3 rows, 1 column
            worksheet.cells.createRange(0, 2, 3, 1).name = "NamedRange";

            // Create a range for entire column C and cut/paste it
            const cut = worksheet.cells.createRange("C:C");
            worksheet.cells.insertCutCells(cut, 0, 1, ShiftType.Right);

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CutAndPasteCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
