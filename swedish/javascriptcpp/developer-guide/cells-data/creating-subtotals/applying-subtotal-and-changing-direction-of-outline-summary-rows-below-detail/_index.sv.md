---
title: Tillämpa delsumma och ändra riktning på sammanfattning av sammanfattningsrader nedanför detaljer
type: docs
weight: 100
url: /sv/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Lär dig hur du använder subtotal och ändrar riktning på outline sammanfattande rader nedanför detalj med hjälp av Aspose.Cells for JavaScript via C++ API.
keywords: Tillämpa delsumma, Lägg till delsumma, ändra riktning på summering underdetalj rader, ändra riktning på summering av summeringar underdetalj kolumner till höger om detalj, skapa delsumma och ändra riktning på summering underdetalj rader
---

{{% alert color="primary" %}}

Denna artikel förklarar hur du tillämpar delsumma på data och ändrar riktningen på sammanfattningsrader under detaljerna.

Du kan tillämpa delsumma på data med hjälp av [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-) metoden. Den tar följande parametrar.

- **CellArea** - Intervallet att tillämpa delsumma på
- **GroupBy** - Fältet som ska grupperas efter, som en nollbaserad heltalsförskjutning
- **Function** - Delsummeringsfunktionen.
- **TotalList** - En matris med nollbaserade fältförskjutningar som indikerar fälten som delsummorna läggs till.
- **Replace** - Indikerar om de nuvarande delsummorna ska ersättas
- **Sidbrytningar** - Indikerar om man ska lägga till sidbrytning mellan grupper
- **SummaryBelowData** - Indikerar om en sammanfattning ska läggas till under datan.

Du kan också styra riktningen för översiktsrader under detaljer som visas i följande skärmbild med hjälp av Worksheet.Outline.SummaryRowBelow-egenskapen. Du kan öppna denna inställning i Microsoft Excel med **Data > Översikt > Inställningar**

![todo:image_alt_text](1.png)

{{% /alert %}}

## Bilder av käll- och utdatafiler

Följande skärmbild visar den ursprungliga Excel-filen som används i den kodexempel nedan som innehåller några data i kolumnerna A och B.

![todo:image_alt_text](2.png)

Följande skärmbild visar den genererade Excel-filen som skapats av provkoden. Som du kan se har subtotalen tillämpats på intervall A2:B11 och riktningen på översikten är sammanfattningar av rader under detaljer.

![todo:image_alt_text](3.png)

## JavaScript för att tillämpa subtotal och ändra riktningen på outline sammanfattande rader



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
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
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
