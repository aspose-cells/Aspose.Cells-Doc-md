---
title: Используйте свойство Sheet.SheetId OpenXml с помощью Aspose.Cells for JavaScript через C++
linktitle: Использование свойства Sheet.SheetId из OpenXml с помощью Aspose.Cells
type: docs
weight: 200
url: /ru/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Эта статья демонстрирует, как использовать свойство Sheet.SheetId OpenXml с помощью Excel манипуляций через Aspose.Cells for JavaScript с помощью программирования на C++.
keywords: свойство id листа OpenXml JavaScript через C++, лист id в Excel листе JavaScript через C++
---

## **Возможные сценарии использования**

*Sheet.SheetId* доступен внутри модуля *DocumentFormat.OpenXml.Spreadsheet* и является частью OpenXml. Вы можете увидеть это свойство и его значение внутри *workbook.xml*, как показано на следующем скриншоте. Aspose.Cells предоставляет аналогичное свойство как [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Используйте свойство Sheet.SheetId OpenXml с помощью Aspose.Cells for JavaScript в C++**

В следующем образце кода загружается [образцовый Excel-файл](51740716.xlsx), читается его идентификатор листа или вкладки, затем назначается новый идентификатор вкладки и сохраняется как [выходной файл Excel](51740717.xlsx). Также обратитесь к выводу консоли приведенного ниже кода для справки.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **Вывод в консоль**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
