---
title: Verwendung der FormulaText Funktion in Aspose.Cells for JavaScript via C++
linktitle: Verwendung der FormulaText Funktion in Aspose.Cells
description: Dieser Artikel stellt die Verwendung der FormulaText Funktion in der Aspose.Cells Bibliothek vor, um Formeln in Microsoft Excel zu verarbeiten. Lernen Sie, den Formeltext von Zellen zu erhalten und zu setzen sowie geänderte Excel Dateien mit JavaScript via C++ zu speichern.
keywords: Aspose.Cells, Excel, FormulaText Funktionen JavaScript via C++
type: docs
weight: 60
url: /de/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText ist eine Funktion in Excel 2013 und späteren Versionen. Wird von früheren Versionen wie Excel 2010 oder 2007 nicht unterstützt. Wie der Name schon sagt, gibt sie den Text der Formel aus, die in einer Zelle vorhanden ist. Dieser Artikel zeigt, wie Sie diese Funktion mit Aspose.Cells for JavaScript via C++ verwenden können.

{{% /alert %}} 

Der folgende Beispielcode zeigt die Verwendung von FormulaText mit Aspose.Cells for JavaScript via C++. Der Code schreibt zunächst eine Formel in Zelle A1 und gibt anschließend den Formeltext in Zelle A2 mit FormulaText aus.

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
## **Konsolenausgabe**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
