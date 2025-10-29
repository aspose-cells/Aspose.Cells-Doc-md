---
title: Автоматическое распространение формулы в таблице или списковом объекте при вводе данных в новые строки с помощью JavaScript через C++
linktitle: Устанавливает формулу таблицы
type: docs
weight: 260
url: /ru/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Узнайте, как автоматически распространять формулы в таблицах или списковых объектах при вводе данных в новые строки с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**
Иногда вам нужно, чтобы формула в вашей таблице или списковом объекте автоматически распространялась на новые строки при вводе новых данных. Это поведение по умолчанию в Microsoft Excel. Чтобы добиться такого же функционала с помощью Aspose.Cells for JavaScript через C++, используйте свойство [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--)

## **Автоматически распространяйте формулу в таблице или списковом объекте при вводе данных в новые строки**
Следующий пример кода создает таблицу или списковый объект таким образом, что формула в столбце B автоматически распространяется на новые строки при вводе новых данных. Проверьте [созданный экспортированный файл Excel](5115469.xlsx). Если вы введете любое число в ячейку A3, вы увидите, что формула в ячейке B2 автоматически распространяется на ячейку B3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cell A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
