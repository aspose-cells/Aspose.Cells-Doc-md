---
title: Zellenzeichenfolgenwert mit und ohne Formatierung abrufen
type: docs
weight: 240
url: /de/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: Erfahren Sie, wie Sie den Zellen String Wert mit und ohne Formatierung über die Aspose.Cells for JavaScript via C++ API abrufen.
keywords: Zellen String Wert mit und ohne Formatierung in JavaScript via C++ abrufen, Zellen String Wert mit und ohne Formatierung in JavaScript via C++ wiederherstellen, Zellen String Wert mit und ohne Formatierung in JavaScript via C++ erhalten
---

{{% alert color="primary" %}}

Aspose.Cells bietet eine Eigenschaft [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--), mit der der String-Wert der Zelle mit oder ohne Formatierung abgerufen werden kann. Angenommen, Sie haben eine Zelle mit dem Wert 0,012345 und formatiert, nur zwei Dezimalstellen anzuzeigen. In Excel wird sie dann als 0,01 angezeigt. Sie können String-Werte sowohl als 0,01 als auch als 0,012345 mit der Eigenschaft [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) abrufen. Es nimmt [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) Enum als Parameter, der folgende Werte hat

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Der folgende Beispielcode erklärt die Verwendung der Eigenschaft [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--).

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
