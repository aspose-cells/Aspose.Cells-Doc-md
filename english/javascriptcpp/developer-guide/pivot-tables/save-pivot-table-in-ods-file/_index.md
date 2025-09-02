---
title: Save Pivot Table in ODS file
type: docs
weight: 150
url: /javascript-cpp/save-pivot-table-in-ods-file/
---

Aspose.Cells for JavaScript via C++ provides the ability to save pivot table in ODS files. For this, you just convert a workbook with existing pivot table or create a new pivot table and save the file in the ODS format. Be sure to call [**PivotTable.calculateData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#calculatedata--) before saving to ensure that the pivot table is rendered in the output ODS file. The following code snippet demonstrates saving pivot table in ODS file.

## Sample Code

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable ODS Example</title>
    </head>
    <body>
        <h1>PivotTable Save In ODS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, Utils } = AsposeCells;
        
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

            // Create a new workbook or load from selected file
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;

            let cell = cells.get("A1");
            cell.value = "Sport";
            cell = cells.get("B1");
            cell.value = "Quarter";
            cell = cells.get("C1");
            cell.value = "Sales";
            cell = cells.get("A2");
            cell.value = "Golf";
            cell = cells.get("A3");
            cell.value = "Golf";
            cell = cells.get("A4");
            cell.value = "Tennis";
            cell = cells.get("A5");
            cell.value = "Tennis";
            cell = cells.get("A6");
            cell.value = "Tennis";
            cell = cells.get("A7");
            cell.value = "Tennis";
            cell = cells.get("A8");
            cell.value = "Golf";
            cell = cells.get("B2");
            cell.value = "Qtr3";
            cell = cells.get("B3");
            cell.value = "Qtr4";
            cell = cells.get("B4");
            cell.value = "Qtr3";
            cell = cells.get("B5");
            cell.value = "Qtr4";
            cell = cells.get("B6");
            cell.value = "Qtr3";
            cell = cells.get("B7");
            cell.value = "Qtr4";
            cell = cells.get("B8");
            cell.value = "Qtr3";
            cell = cells.get("C2");
            cell.value = 1500;
            cell = cells.get("C3");
            cell.value = 2000;
            cell = cells.get("C4");
            cell.value = 600;
            cell = cells.get("C5");
            cell.value = 1500;
            cell = cells.get("C6");
            cell.value = 4070;
            cell = cells.get("C7");
            cell.value = 5000;
            cell = cells.get("C8");
            cell.value = 6430;

            const pivotTables = sheet.pivotTables;
            const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");
            const pivotTable = pivotTables.get(index);
            pivotTable.rowGrand = false;
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(PivotFieldType.Column, 1);
            pivotTable.addFieldToArea(PivotFieldType.Data, 2);
            pivotTable.calculateData();

            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PivotTableSaveInODS_out.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created and file ready. Click the download link to get the ODS file.</p>';
        });
    </script>
</html>
```

The output file generated the above code is attached for your reference.

[Output ODS File](PivotTableSaveInODS_out.ods)