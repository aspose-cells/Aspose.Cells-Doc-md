---
title: Skapar delsummer
type: docs
weight: 800
url: /sv/javascript-cpp/creating-subtotals/
description: Lär dig hur du skapar deltotaler för alla upprepade värden i ett kalkylblad med Aspose.Cells for JavaScript via C++ API.
keywords: Applicera delsummer, Ange delsummer, Lägg till delsummer, Skapa delsummer, Hur man lägger till delsummer till ett arbetsblad 
---

{{% alert color="primary" %}}

Du kan automatiskt skapa deltotaler för alla upprepade värden i ett kalkylblad. Aspose.Cells for JavaScript via C++ tillhandahåller API-funktioner som hjälper dig att lägga till deltotaler till kalkylblad programmässigt.

{{% /alert %}}

## **Använda Microsoft Excel**

För att lägga till delsummer i Microsoft Excel:

1. Skapa en enkel datalista i det första arbetsbladet i arbetsboken (som visas i figuren nedan) och spara filen som Book1.xls.
1. Välj valfri cell i listan.
1. Från **Data**-menyn väljer du **Delsummer**. Delsummerdialogrutan visas. Ange vilken funktion som ska användas och var delsummer ska placeras.

## **Med Aspose.Cells for JavaScript via C++ API**

Aspose.Cells for JavaScript via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) samling som möjliggör åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera kalkylblad och andra objekt. Varje kalkylblad består av en [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samling. För att lägga till deltotaler i ett kalkylblad, använd metod [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-klassen. Ange parametervärden för att specificera hur deltotalen ska beräknas och placeras.

I exemplen nedan har vi lagt till deltotaler i det första kalkylbladet i [mallfilen](book1.xlsx) med Aspose.Cells for JavaScript via C++ API. När koden körs skapas ett kalkylblad med deltotaler.

Kods som följer visar hur du lägger till deltotaler i ett kalkylblad med Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
