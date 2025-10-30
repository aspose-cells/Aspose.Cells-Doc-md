---
title: Uppdatera och beräkna pivottabell med beräknade poster
type: docs
weight: 40
url: /sv/javascript-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ stöder nu att uppdatera och beräkna pivottabeller med beräknade objekt. Använd [**PivotTable.refreshData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshdata--) och [**PivotTable.calculateData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#calculatedata--) som vanligt för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabell med beräknade poster**

Följande exempel laddar [källexcelfil](5115238.xlsx) som innehåller en pivottabell med tre beräknade objekt såsom "add", "div", "div2". Vi ändrar först värdet i cell D2 till 20 och uppdaterar och beräknar sedan pivottabellen med Aspose.Cells for JavaScript via C++ API:erna och sparar arbetsboken i PDF-format. Resultatet i [utdata PDF](5115229.pdf) visar att Aspose.Cells for JavaScript via C++ framgångsrikt uppdaterade och beräknade pivottabellen med beräknade objekt. Du kan verifiera detta genom att manuellt skriva in värdet 20 i cell D2 och sedan uppdatera pivottabellen med genvägen Alt+F5 eller genom att klicka på pivottabellens Uppdatera-knapp.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh and Calculate Pivot Table Items</title>
    </head>
    <body>
        <h1>Refresh and Calculate Pivot Table Items</h1>
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Change the value of cell D2
            const cell = sheet.cells.get("D2");
            cell.value = 20;

            // Refresh and calculate all the pivot tables inside this sheet
            sheet.refreshPivotTables();

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshAndCalculateItems_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            result.innerHTML = '<p style="color: green;">Pivot tables refreshed and calculated. Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
