---
title: Указание значимых цифр для хранения в Excel файле с помощью JavaScript через C++
linktitle: Указание значащих разрядов для хранения в файле Excel
type: docs
weight: 30
url: /ru/javascript-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Научитесь указывать значимые цифры для хранения в Excel файле с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

По умолчанию Aspose.Cells for JavaScript через C++ хранит 17 значимых цифр значения типа double внутри Excel-файла, в отличие от MS-Excel, которая хранит только 15 значимых цифр. Вы можете изменить поведение Aspose.Cells с 17 значимых цифр на 15, используя свойство [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--).  

## **Указание значащих разрядов для хранения в файле Excel**  

Следующий пример кода принуждает Aspose.Cells использовать 15 значимых цифр при сохранении double значений внутри файла Excel. Проверьте [выходной файл Excel](22774105.xlsx). Переименуйте расширение в .zip, распакуйте и увидите, что внутри файла сохраняется только 15 значимых цифр. Следующий скриншот демонстрирует эффект свойства [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--) на итоговый файл Excel.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Significant Digits</title>
    </head>
    <body>
        <h1>Significant Digits Example</h1>
        <p>This example sets CellsHelper.significantDigits to 15 and writes a double to cell A1.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // By default, Aspose.Cells stores 17 significant digits unlike MS-Excel which stores only 15 significant digits
            CellsHelper.significantDigits = 15;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const c = worksheet.cells.get("A1");

            // Put double value, only 15 significant digits as specified by CellsHelper.significantDigits above will be stored
            c.value = 1234567890.123451711;

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_SignificantDigits.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
