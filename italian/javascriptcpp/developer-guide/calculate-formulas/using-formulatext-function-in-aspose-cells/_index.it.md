---
title: Utilizzando la funzione FormulaText in Aspose.Cells for JavaScript tramite C++
linktitle: Utilizzo della funzione FormulaText in Aspose.Cells
description: Questo articolo introduce come utilizzare la funzione FormulaText nella libreria Aspose.Cells per elaborare le formule in Microsoft Excel. Impara come ottenere e impostare il testo della formula delle celle e salvare i file Excel modificati usando JavaScript tramite C++.
keywords: Aspose.Cells, Excel, funzioni FormulaText JavaScript tramite C++
type: docs
weight: 60
url: /it/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText è una funzione di Excel 2013 e versioni successive. Non è supportata da versioni precedenti come Excel 2010 o 2007, ecc. Come suggerisce il nome, stampa il testo della formula presente in una data cella. Questo articolo ti mostrerà come utilizzare questa funzione con Aspose.Cells for JavaScript tramite C++.

{{% /alert %}} 

 Il seguente esempio di codice mostra l'uso di FormulaText con Aspose.Cells for JavaScript tramite C++. Il codice prima scrive una formula nella cella A1 e poi stampa il testo della formula usando FormulaText nella cella A2.

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
## **Output della console**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
