---
title: Изменение выравнивания ячеек и сохранение существующего форматирования
linktitle: Изменение выравнивания ячеек и сохранение существующего форматирования
description: Используйте библиотеку Aspose.Cells для изменения выравнивания ячейки и сохранения существующего форматирования в JavaScript через C++
keywords: Aspose.Cells, JavaScript через C++, выравнивание ячейки, сохранение существующего форматирования
type: docs
weight: 340
url: /ru/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Возможные сценарии использования**

Иногда нужно изменить выравнивание нескольких ячеек и при этом сохранить существующее форматирование. Скрипт Aspose.Cells for JavaScript через C++ позволяет это сделать с помощью метода [**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-). Если установить его в значение **true**, произойдут изменения выравнивания, иначе — нет. Обратите внимание, объект [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) передается как параметр методу [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-), который фактически применяет форматирование к диапазону ячеек.

## **Изменение выравнивания ячеек и сохранение существующего форматирования**

Приведенный ниже образец кода загружает [образец файла Excel](67338585.xlsx), создает диапазон и центрирует его по горизонтали и вертикали, сохраняя все существующее форматирование нетронутым. Ниже приведено сравнение образца файла Excel и [выходного файла Excel](67338586.xlsx) и показано, что все существующее форматирование ячеек такое же, за исключением того, что ячейки теперь центрированы по горизонтали и вертикали.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");

            // Create style object
            const style = workbook.createStyle();

            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments true

            // Apply style to range of cells
            range.applyStyle(style, flag);

            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
