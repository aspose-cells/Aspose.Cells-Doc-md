---
title: Specificera den absoluta positionen för pivotposten
type: docs
weight: 50
url: /sv/javascript-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Ibland behöver användaren ange den absoluta positionen för pivottabelelementen, Aspose.Cells for JavaScript via C++ API har exponerat några nya egenskaper och en metod för att uppnå användarens krav.

- Lagt till egenskapen [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-) som kan användas för att ange positionens index för alla PivotItems oavsett föräldernod. Lagt till egenskapen [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) som kan användas för att ange positionens index för PivotItems under samma föräldernod.
- Lagt till metoden [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) för att flytta posten upp eller ner baserat på räkningsvärdet, där räkningsvärdet är antalet positioner att flytta PivotItem upp eller ner. Om räkningsvärdet är mindre än noll kommer posten att flyttas upp, medan om räkningsvärdet är större än noll kommer PivotItem att flyttas ner, Boolean typen isSameParent-parameter specificerar om flytoperationen måste utföras i samma föräldernod eller inte.
- Obsoletade metoden [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) *PivotItem.move(int count)* därför rekommenderas det att använda den nyare tillagda metoden [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) istället.

{{% /alert %}}

Följande provkod skapar en pivottabell och sedan specificerar den pivotpostens positioner i samma föräldernod. Du kan ladda ner [käll-Excel](5112632.xlsx)- och [utdata-Excel](5112619.xlsx)-filer för din referens. Om du öppnar utdata-Excel-filen kommer du att se att pivotposten "4H12" är på 0: e position i förälder "K11" och "DIF400" är på 3: e position. På samma sätt är CA32 på position 1 och AAA3 är på position 2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, PivotFieldSubtotalType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Add pivot worksheet and get data worksheet
            const wsPivot = workbook.worksheets.add("pvtNew Hardware");
            const wsData = workbook.worksheets.get("New Hardware - Yearly");

            // Get the pivottables collection for the pivot sheet
            const pivotTables = wsPivot.pivotTables;

            // Add PivotTable to the worksheet
            const index = pivotTables.add("='New Hardware - Yearly'!A1:D621", "A3", "HWCounts_PivotTable");

            // Get the PivotTable object
            const pvtTable = pivotTables.get(index);

            // Add vendor row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Vendor");

            // Add item row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Item");

            // Add data field
            pvtTable.addFieldToArea(PivotFieldType.Data, "2014");

            // Turn off the subtotals for the vendor row field
            const pivotField = pvtTable.rowFields.get("Vendor");
            pivotField.subtotals = PivotFieldSubtotalType.None;

            // Turn off grand total
            pvtTable.columnGrand = false;

            /*
             * Please call the PivotTable.refreshData() and PivotTable.calculateData()
             * before using PivotItem.setPosition,
             * PivotItem.setPositionInSameParentNode and PivotItem.move methods.
            */
            pvtTable.refreshData();
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("4H12").positionInSameParentNode = 0;
            pvtTable.rowFields.get("Item").pivotItems.get("DIF400").positionInSameParentNode = 3;

            /* 
             * As a result of using PivotItem.setPositionInSameParentNode,
             * it will change the original sort sequence.
             * So when you use PivotItem.setPositionInSameParentNode in another parent node.
             * You need call the method named "calculateData" again. 
            */
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("CA32").positionInSameParentNode = 1;
            pvtTable.rowFields.get("Item").pivotItems.get("AAA3").positionInSameParentNode = 2;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Observera att det är nödvändigt att använda metoderna [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-) och [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) i början av applikationen, det vill säga; innan du kallar några andra objekt i Aspose.Cells API.

{{% /alert %}}
