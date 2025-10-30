---
title: Ottieni il valore di una stringa della cella con o senza formattazione
type: docs
weight: 240
url: /it/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: Impara come ottenere il valore stringa della cella con e senza formattazione tramite l API Aspose.Cells for JavaScript tramite C++.
keywords: Ottieni il Valore Stringa della Cella con e senza Formattazione JavaScript tramite C++, Recupera il Valore Stringa della Cella con e senza Formattazione JavaScript tramite C++, Ottieni il Valore Stringa della Cella con e senza Formattazione JavaScript tramite C++
---

{{% alert color="primary" %}}

Aspose.Cells fornisce una proprietà [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) che può essere usata per ottenere il valore stringa della cella con o senza qualsiasi formattazione. Supponi, hai una cella con valore 0.012345 e l'hai formattata per mostrare solo due decimali. Verrà visualizzata come 0.01 in Excel. Puoi recuperare valori stringa sia come 0.01 che come 0.012345 usando la proprietà [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--). Essa accetta un enum [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) che ha i seguenti valori

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Il seguente esempio di codice illustra l'uso della proprietà [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--).

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
