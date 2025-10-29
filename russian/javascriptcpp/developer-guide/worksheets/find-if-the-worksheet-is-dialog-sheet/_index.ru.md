---
title: Узнать, является ли лист диалоговым листом с помощью JavaScript через C++
linktitle: Проверить, является ли рабочий лист диалоговым листом
type: docs
weight: 90
url: /ru/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Эта статья содержит инструкции и пример кода для определения программно, является ли лист Excel диалоговым листом с помощью Aspose.Cells for JavaScript через C++.
keywords: нахождение типа диалогового листа Excel с помощью JavaScript через C++, диалоговый лист JavaScript через C++
---

## **Возможные сценарии использования**

Диалоговый лист — это устаревший формат листа, содержащий диалоговое окно. Такой лист может быть вставлен старой версией Microsoft Excel, например, 2003, как показано на скриншоте. Также его можно вставить с помощью VBA в более новых версиях, например, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Вы можете определить, является ли лист диалоговым или другого типа листа с помощью свойства [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--), предоставляемого Aspose.Cells for JavaScript через C++. Если оно возвращает значение перечисления [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), это означает, что вы работаете с диалоговым листом.

## **Определить, является ли рабочий лист диалоговым листом**

Следующий пример кода загружает [пример файла Excel](64716820.xlsx), содержащего диалоговый лист. Он проверяет свойство [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--), сравнивает его с [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype) и выводит сообщение. Для получения дополнительной информации посмотрите вывод в консоли приведенного ниже примера кода.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **Вывод в консоль**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
