---
title: Obtener el valor de cadena de la celda con o sin formato
type: docs
weight: 240
url: /es/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: Aprenda cómo obtener el valor de cadena de la celda con y sin formato a través del API de Aspose.Cells for JavaScript via C++.
keywords: Obtener Valor de Cadena de la Celda con y sin Formato en JavaScript a través de C++, Recuperar Valor de Cadena de la Celda con y sin Formato en JavaScript a través de C++, Obtener Valor de Cadena de la Celda con y sin Formato en JavaScript a través de C++
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una propiedad [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) que se puede usar para obtener el valor de cadena de la celda con o sin formato. Suponga que tiene una celda con valor 0.012345 y la ha formateado para mostrar solo dos decimales. Entonces se mostrará como 0.01 en Excel. Puede recuperar valores de cadena tanto como 0.01 como 0.012345 usando la propiedad [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--). Toma [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) como parámetro de enumeración con los siguientes valores

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

El siguiente código de ejemplo explica el uso de la propiedad [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--).

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
