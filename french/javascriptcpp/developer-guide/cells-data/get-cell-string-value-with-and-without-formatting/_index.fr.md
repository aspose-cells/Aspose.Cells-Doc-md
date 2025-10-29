---
title: Obtenir la valeur de la chaîne de la cellule avec et sans mise en forme
type: docs
weight: 240
url: /fr/javascript-cpp/get-cell-string-value-with-and-without-formatting/
description: Apprenez à obtenir la valeur de chaîne de la cellule avec ou sans mise en forme via l API Script Aspose.Cells for Java via C++.
keywords: Obtenez la valeur de chaîne de la cellule avec ou sans mise en forme JavaScript via C++, Récupérez la valeur de chaîne de la cellule avec ou sans mise en forme JavaScript via C++, Obtenez la valeur de chaîne de la cellule avec ou sans mise en forme JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells fournit une propriété [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--) qui peut être utilisée pour obtenir la valeur de chaîne de la cellule avec ou sans mise en forme. Supposons que vous avez une cellule avec une valeur 0.012345 et que vous l'avez formatée pour afficher uniquement deux décimales. Elle s'affichera alors comme 0,01 dans Excel. Vous pouvez récupérer les valeurs de chaîne tant comme 0,01 que comme 0,012345 en utilisant la propriété [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--). Elle prend comme paramètre l'énumération [**CellValueFormatStrategy**](https://reference.aspose.com/cells/javascript-cpp/cellvalueformatstrategy/) qui a les valeurs suivantes

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la propriété [**Cell.stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--).

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
