---
title: Hämta Pivot Table uppdateringsdatum och information om vem som uppdaterade
type: docs
weight: 100
url: /sv/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Hur man får pivotdiagrammets uppdateringsdatum och information om vem som uppdaterade med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript Excel, Excel JavaScript bibliotek, få pivotdiagrammets uppdateringsdatum och information om vem som uppdaterade med Aspose.Cells for JavaScript Excel bibliotek.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ stöder nu hämtning av uppdateringsdatum och information om vem som har uppdaterat från en arbetsbok.

{{% /alert %}}

## **Hur man får pivot-tabellens uppdateringsdatum och information om vem som uppdaterade**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--) returnerar datumet då PivotTable-rapporten senast uppdaterades. På liknande sätt returnerar [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--)-egenskapen namnet på användaren som senast uppdaterade rapporten. Följande exempel demonstrerar denna funktion och provfilen kan laddas ner från följande länk.

[SourcePivotTable.xlsx](77496335.xlsx)

**Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refresh by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refresh by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```
