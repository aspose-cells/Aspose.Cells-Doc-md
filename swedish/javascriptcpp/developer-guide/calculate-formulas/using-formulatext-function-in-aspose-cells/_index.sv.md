---
title: Använder FormulaText funktionen i Aspose.Cells for JavaScript via C++
linktitle: Använda FormulaText funktion i Aspose.Cells
description: Denna artikel presenterar hur man använder FormulaText funktionen i Aspose.Cells biblioteket för att bearbeta formler i Microsoft Excel. Lär dig att få och ställa in formeltext för celler och spara ändrade Excel filer med JavaScript via C++.
keywords: Aspose.Cells, Excel, Funktioner för FormelText JavaScript via C++
type: docs
weight: 60
url: /sv/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText är en funktion för Excel 2013 och senare. Den stöds inte av tidigare versioner som Excel 2010 eller 2007 osv. Som namnet antyder, skriver den ut formelns text som finns i en given cell. Denna artikel visar hur du använder denna funktion med Aspose.Cells for JavaScript via C++.

{{% /alert %}} 

Följande exempel visar användningen av FormulaText med Aspose.Cells for JavaScript via C++. Koden skriver först en formel i cell A1 och skriver sedan ut formelns text med FormulaText i cell A2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2, It will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```
## **Konsoloutput**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
