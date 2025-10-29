---
title: Как проверить состояние фиксации без Excel, используя JavaScript через C++
linktitle: Замороженное состояние
type: docs
weight: 190
url: /ru/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: В этой статье вы узнаете, как программно проверить состояние фиксации листа Excel, используя JavaScript с библиотекой C++.
---

## **Введение**

В этой статье мы узнаем, как программно проверить состояние фиксации листа Excel. Мы можем легко определить, зафиксирован ли лист или разделён в MS Excel. Но есть ли способ определить это через JavaScript? Мы можем выполнить это с помощью Aspose.Cells for JavaScript через C++.

## **Заморожены ли оконные рамы**
С помощью Aspose.Cells for JavaScript через C++ мы можем проверить, закреплено ли окно, и сколько строк и столбцов заблокировано.

Пожалуйста, используйте свойство [**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--) для проверки состояния оконных панелей и получения заблокированных строк и столбцов с помощью свойства [**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--).
1. Создайте рабочую книгу для открытия файла.
2. Проверьте, заморожен ли лист.
3. Получить заблокированные строки и столбцы.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
