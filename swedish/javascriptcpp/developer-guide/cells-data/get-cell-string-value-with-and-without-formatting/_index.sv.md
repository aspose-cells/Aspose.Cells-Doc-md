---
title: Hämta cellsträngvärde med och utan formatering
type: docs
weight: 240
url: /sv/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: Lär dig hur du hämtar cellens strängvärde med och utan formatering genom Aspose.Cells for JavaScript via C++ API.
keywords: Hämta cellens strängvärde med och utan formatering Javascript via C++, hämta cellens strengvärde med och utan formatering Javascript via C++, få cellens strängvärde med och utan formatering Javascript via C++
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en egenskap [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) som kan användas för att hämta cellens strängvärde med eller utan någon formatering. Anta att du har en cell med värdet 0.012345 och du har formaterat den för att visa endast två decimaler. Den kommer då att visas som 0,01 i Excel. Du kan hämta strängvärden både som 0,01 och som 0,012345 med egenskapen [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--). Den tar [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) enum som parameter med följande värden

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Följande exempel kod förklarar användningen av egenskapen [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Cell } = AsposeCells;

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
            // Creating a new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Put value inside the cell
            cell.putValue(0.012345);

            // Format the cell that it should display 0.01 instead of 0.012345
            const style = cell.style;
            style.number = 2;
            cell.style = style;

            // Get string value as Cell Style
            let value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML = `<p>Formatted string value: ${value}</p>`;

            // Get string value without any formatting
            value = cell.stringValue;
            console.log(value);
            document.getElementById('result').innerHTML += `<p>Unformatted string value: ${value}</p>`;

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```
