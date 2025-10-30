---
title: Tillgång till tabell från cell och lägga till värden inuti den med hjälp av rad och kolumnförskjutningar med JavaScript via C++
linktitle: Få åtkomst till tabell från cell och lägg till värden inuti den med hjälp av rad och kolumnförflyttningar
type: docs
weight: 230
url: /sv/javascript-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}  

Normalt sett lägger du till värden inuti tabellen eller listobjektet med hjälp av [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-metoden. Men ibland kan du behöva lägga till värden inuti tabellen eller listobjektet med rad- och kolumnförflyttningar.  

För att komma åt tabell eller listaobjekt från en cell, använd [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--)-egenskapen. För att lägga till värden med hjälp av rad- och kolumnförskjutningar, använd [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-)-metoden.  

{{% /alert %}}  

Följande skärmbild visar källfilen Excel som används i koden. Den innehåller den tomma tabellen och markerar cell D5 som ligger innanför tabellen. Vi kommer att komma åt denna tabell från cell D5 med [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--)-egenskapen och sedan lägga till värden i den med både [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) och [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-) metoder.  

## Exempel  

### Skärmbilder som jämför käll- och utdatafiler  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Följande skärmbild visar den genererade utdata-Excel-filen av koden. Som du kan se har cellen D5 ett värde och cellen F6, som ligger vid förflyttning 2,2 inuti tabellen, har ett värde.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### JavaScript-kod för att komma åt tabell från cell och för att lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar  

Följande provkod laddar den angivna källan Excel-filen som visas i skärmdumpen ovan och lägger till värden inne i tabellen och genererar den resulterande Excel-filen som visas ovan.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Accessing Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell D5 which lies inside the table
            const cell = worksheet.cells.get("D5");

            // Put value inside the cell D5
            cell.value = "D5 Data";

            // Access the Table from this cell
            const table = cell.table;

            // Add some value using Row and Column Offset
            table.putCellValue(2, 2, "Offset [2,2]");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
