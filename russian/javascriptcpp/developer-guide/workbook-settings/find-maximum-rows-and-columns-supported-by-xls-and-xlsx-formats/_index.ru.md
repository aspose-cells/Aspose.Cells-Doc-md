---
title: Найти максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX, с помощью JavaScript через C++
linktitle: Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX
type: docs
weight: 20
url: /ru/javascript-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Возможные сценарии использования**  

Различные форматы Excel поддерживают разное количество строк и столбцов. Например, XLS поддерживает 65536 строк и 256 столбцов, а XLSX — 1048576 строк и 16384 столбца. Если хотите узнать, сколько строк и столбцов поддерживает конкретный формат, используйте свойства [**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--) и [**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--).  

## **Найдите максимальное количество строк и столбцов, поддерживаемых форматами XLS и XLSX**  

Следующий пример создает рабочую книгу сначала в формате XLS, затем в XLSX. После создания он выводит значения свойств [**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--) и [**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--). Пожалуйста, ознакомьтесь с выводом в консоли приведенного ниже кода для справки.  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Maximum Rows and Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, Utils } = AsposeCells;

        const runBtn = document.getElementById('runExample');
        const resultDiv = document.getElementById('result');

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            runBtn.disabled = false;
        });

        runBtn.addEventListener('click', async () => {
            // Print message about XLS format.
            resultDiv.innerHTML = '<p>Maximum Rows and Columns supported by XLS format.</p>';

            // Create workbook in XLS format.
            let wb = new Workbook(AsposeCells.FileFormatType.Excel97To2003);

            // Print the maximum rows and columns supported by XLS format.
            let maxRows = wb.settings.maxRow + 1;
            let maxCols = wb.settings.maxColumn + 1;
            resultDiv.innerHTML += `<p>Maximum Rows: ${maxRows}</p>`;
            resultDiv.innerHTML += `<p>Maximum Columns: ${maxCols}</p>`;
            resultDiv.innerHTML += '<hr/>';

            // Print message about XLSX format.
            resultDiv.innerHTML += '<p>Maximum Rows and Columns supported by XLSX format.</p>';

            // Create workbook in XLSX format.
            wb = new Workbook(AsposeCells.FileFormatType.Xlsx);

            // Print the maximum rows and columns supported by XLSX format.
            maxRows = wb.settings.maxRow + 1;
            maxCols = wb.settings.maxColumn + 1;
            resultDiv.innerHTML += `<p>Maximum Rows: ${maxRows}</p>`;
            resultDiv.innerHTML += `<p>Maximum Columns: ${maxCols}</p>`;
        });
    </script>
</html>
```  

## **Вывод в консоль**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}
