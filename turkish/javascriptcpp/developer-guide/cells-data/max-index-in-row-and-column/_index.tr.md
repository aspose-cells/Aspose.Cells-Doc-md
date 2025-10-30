---
title: Satırda Maksimum Sütun Endeksini ve Sütunda Maksimum Satır Endeksini Al
type: docs
weight: 600
url: /tr/javascript-cpp/get-max-index-in-row-and-column/
description: Aspose.Cells for JavaScript ile C++ API üzerinden Satırdaki En Yüksek Sütun ve Sütundaki En Yüksek Satır Indeksini Nasıl Alırım öğrenin.
keywords: Satırda En Yüksek Sütun İndeksi, C++ kullanılarak JavaScript te alınabilir. Sütunda En Yüksek Satır İndeksi ve Satırda En Yüksek Veri Sütunu İndeksi, JavaScript ile C++, Satırda En Yüksek Veri Satırı İndeksi ve Sütunda En Yüksek Veri Sütunu İndeksi nasıl alınır.
---

## **Olası Kullanım Senaryoları**
Sadece satır veya sütun verileriyle ilgileniyorsanız, satır ve sütunların veri aralığını bilmeniz gerekir. Aspose.Cells for JavaScript aracıyla C++ bu özelliği sunar. Bir satırda en yüksek sütun indeksini almak için [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--) ve [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--) metodlarını kullanabilir, ardından en yüksek sütun indeksini ve maksimum veri sütun indeksini almak için [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) metodunu kullanabilirsiniz. Ancak, bir sütunda en yüksek satır indeksini ve en yüksek satır veri indeksini almak için, sütunda bir aralık oluşturmanız, aralığı dolaşmanız ve son hücreyi bulmanız ve sonunda [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) metodunu bu hücre üzerinde çağırmanız gerekir.

Aspose.Cells for JavaScript, C++ üzerinden aşağıdaki özellikleri ve metodları sunar ki bu da hedeflerinize ulaşmanıza yardımcı olur.
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **Satırda Maksimum Sütun İndeksi ve Sütunda Maksimum Satır İndeksi Alın**
Bu örnek aşağıdakileri göstermektedir:

1. [Örnek dosyayı](örnek.xlsx) yükleyin.
1. Maksimum sütun dizinini ve maksimum veri sütun dizinini elde etmek için satırı alın.
1. Hücrede [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) metodunu çağırın.
1. Sütuna dayalı bir aralık oluşturun.
1. İteratörü alın ve aralığı gezin.
1. Hücrede [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) metodunu çağırın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result pre { background: #f4f4f4; padding: 10px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
        </style>
    </head>
    <body>
        <h1>Get Max Row/Column Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Accessing cells collection
            const cells = sheet.cells;

            // Check row at index 1
            const row = cells.checkRow(1);
            const outputLines = [];

            if (row != null) {
                // get Maximum column index of Row which contains data or style.
                outputLines.push("Max column index in row: " + row.lastCell.column);

                // get Maximum column index of Row which contains data.
                outputLines.push("Max data column index in row: " + row.lastDataCell.column);
            } else {
                outputLines.push("Row 1 is empty (checkRow returned null).");
            }

            // create the range of column B (index 1)
            const columnRange = cells.createRange(1, 1, true);

            var max_row_index  = cells.maxRow + 1;
            var maxRow = 0;
            var maxDataRow = 0;

            for (let row_index = 0; row_index < max_row_index; row_index++) {
                var curr_cell = cells.get(row_index, 1);

                if (curr_cell) {
                    if (curr_cell.stringValue) {
                        maxDataRow = curr_cell.row;
                    }

                    if (curr_cell.stringValue || curr_cell.hasCustomStyle) {
                        maxRow = curr_cell.row;
                    }
                }
            }

            // Maximum row index of Column which contains data or style.
            outputLines.push("Max row index in Column: " + maxRow);

            // Maximum row index of Column which contains data.
            outputLines.push("Max data row index in Column: " + maxDataRow);

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```
