---
title: Hitta maximala rader och kolumner som stöds av XLS och XLSX format med JavaScript via C++
linktitle: Hitta maxrader och maxkolumner som stöds av XLS och XLSX format
type: docs
weight: 20
url: /sv/javascript-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Möjliga användningsscenario**  

Det finns olika antal rader och kolumner som stöds av Excel-format. Till exempel stöder XLS 65536 rader och 256 kolumner, medan XLSX stöder 1048576 rader och 16384 kolumner. Om du vill veta hur många rader och kolumner som stöds av ett givet format kan du använda [**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--) och [**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--) egenskaper.  

## **Hitta maxrader och maxkolumner som stöds av XLS och XLSX-format**  

Följande exempel skapar först en arbetsbok i XLS-format och sedan i XLSX-format. Efter skapandet skriver den ut värdena för [**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--) och [**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--) egenskaperna. Vänligen se konsolutmatningen av koden nedan för referens.  

## **Exempelkod**  

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

## **Konsoloutput**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}
