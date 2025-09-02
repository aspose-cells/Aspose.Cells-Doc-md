---
title: Create Pivot Tables and Pivot Charts
type: docs
weight: 20
url: /javascript-cpp/create-pivot-tables-and-pivot-charts/
description: How to add Pivot Tables and Pivot Charts with Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript library, Add Pivot Tables and Pivot Charts Using Aspose.Cells for JavaScript via C++ Excel Library.
---

{{% alert color="primary" %}}

A pivot table is an interactive summary of records. For example, you may have hundreds of invoice entries in a list in a worksheet. A pivot table can total the invoices by customer, product or date. With Microsoft Excel it is possible to quickly re-arrange the information in the pivot table by dragging buttons to a new position.

A pivot chart is an interactive graphical representation of the data in a pivot table. Pivot charts were introduced in Excel 2000. Using a pivot chart makes it even easier to understand the data since the pivot table creates subtotals and totals automatically.

Aspose.Cells for JavaScript via C++ supports [pivot tables](/cells/javascript-cpp/create-pivot-tables-and-pivot-charts/) and [pivot charts](/cells/javascript-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Add Pivot Tables and Charts Using Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ provides a special set of classes used to create pivot tables. These classes are used to create and set PivotTable objects, which act as a PivotTable object's basic building blocks:

- PivotField, a field in a pivot table report.
- PivotFields, a collection of all the PivotField objects in a pivot table.
- PivotTable, a PivotTable report on a worksheet.
- PivotTables, a collection of all the PivotTable objects on the worksheet.

### **Prepare to use Aspose.Cells for JavaScript via C++**
1. Install Aspose.Cells for JavaScript via C++ from NPM, use command as:  $ npm install aspose.cells.node.
1. You can also follow the step-by-step instructions on how to install “Aspose.Cells for JavaScript via C++” to your developer environment.


### **How to Add a Pivot Table Using Aspose.Cells for JavaScript via C++**

To create a pivot table using Aspose.Cells for JavaScript via C++:

1. Add some data to a worksheet cells using a Cell object's put_value method. You also use a template file already filled with data. The data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the PivotTables collection's add method (encapsulated in the Worksheet object).
1. Access the new PivotTable object from the PivotTables collection by passing its index. # Use any of the pivot table objects encapsulated in the PivotTable object to manage the table.

Code examples are given below.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Pivot Table Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Name the sheet
            sheet.name = "Data";

            const cells = sheet.cells;

            let cell = cells.get("A1");
            cell.value = "Employee";
            cell = cells.get("B1");
            cell.value = "Quarter";
            cell = cells.get("C1");
            cell.value = "Product";
            cell = cells.get("D1");
            cell.value = "Continent";
            cell = cells.get("E1");
            cell.value = "Country";
            cell = cells.get("F1");
            cell.value = "Sale";
            cell = cells.get("A2");
            cell.value = "David";
            cell = cells.get("A3");
            cell.value = "David";
            cell = cells.get("A4");
            cell.value = "David";
            cell = cells.get("A5");
            cell.value = "David";
            cell = cells.get("A6");
            cell.value = "James";
            cell = cells.get("A7");
            cell.value = "James";
            cell = cells.get("A8");
            cell.value = "James";
            cell = cells.get("A9");
            cell.value = "James";
            cell = cells.get("A10");
            cell.value = "James";
            cell = cells.get("A11");
            cell.value = "Miya";
            cell = cells.get("A12");
            cell.value = "Miya";
            cell = cells.get("A13");
            cell.value = "Miya";
            cell = cells.get("A14");
            cell.value = "Miya";
            cell = cells.get("A15");
            cell.value = "Miya";
            cell = cells.get("A16");
            cell.value = "Miya";
            cell = cells.get("A17");
            cell.value = "Miya";
            cell = cells.get("A18");
            cell.value = "Elvis";
            cell = cells.get("A19");
            cell.value = "Elvis";
            cell = cells.get("A20");
            cell.value = "Elvis";
            cell = cells.get("A21");
            cell.value = "Elvis";
            cell = cells.get("A22");
            cell.value = "Elvis";
            cell = cells.get("A23");
            cell.value = "Elvis";
            cell = cells.get("A24");
            cell.value = "Elvis";
            cell = cells.get("A25");
            cell.value = "Jean";
            cell = cells.get("A26");
            cell.value = "Jean";
            cell = cells.get("A27");
            cell.value = "Jean";
            cell = cells.get("A28");
            cell.value = "Ada";
            cell = cells.get("A29");
            cell.value = "Ada";
            cell = cells.get("A30");
            cell.value = "Ada";
            cell = cells.get("B2");
            cell.value = "1";
            cell = cells.get("B3");
            cell.value = "2";
            cell = cells.get("B4");
            cell.value = "3";
            cell = cells.get("B5");
            cell.value = "4";
            cell = cells.get("B6");
            cell.value = "1";
            cell = cells.get("B7");
            cell.value = "2";
            cell = cells.get("B8");
            cell.value = "3";
            cell = cells.get("B9");
            cell.value = "4";
            cell = cells.get("B10");
            cell.value = "4";
            cell = cells.get("B11");
            cell.value = "1";
            cell = cells.get("B12");
            cell.value = "1";
            cell = cells.get("B13");
            cell.value = "2";
            cell = cells.get("B14");
            cell.value = "2";
            cell = cells.get("B15");
            cell.value = "3";
            cell = cells.get("B16");
            cell.value = "4";
            cell = cells.get("B17");
            cell.value = "4";
            cell = cells.get("B18");
            cell.value = "1";
            cell = cells.get("B19");
            cell.value = "1";
            cell = cells.get("B20");
            cell.value = "2";
            cell = cells.get("B21");
            cell.value = "3";
            cell = cells.get("B22");
            cell.value = "3";
            cell = cells.get("B23");
            cell.value = "4";
            cell = cells.get("B24");
            cell.value = "4";
            cell = cells.get("B25");
            cell.value = "1";
            cell = cells.get("B26");
            cell.value = "2";
            cell = cells.get("B27");
            cell.value = "3";
            cell = cells.get("B28");
            cell.value = "1";
            cell = cells.get("B29");
            cell.value = "2";
            cell = cells.get("B30");
            cell.value = "3";
            cell = cells.get("C2");
            cell.value = "Maxilaku";
            cell = cells.get("C3");
            cell.value = "Maxilaku";
            cell = cells.get("C4");
            cell.value = "Chai";
            cell = cells.get("C5");
            cell.value = "Maxilaku";
            cell = cells.get("C6");
            cell.value = "Chang";
            cell = cells.get("C7");
            cell.value = "Chang";
            cell = cells.get("C8");
            cell.value = "Chang";
            cell = cells.get("C9");
            cell.value = "Chang";
            cell = cells.get("C10");
            cell.value = "Chang";
            cell = cells.get("C11");
            cell.value = "Geitost";
            cell = cells.get("C12");
            cell.value = "Chai";
            cell = cells.get("C13");
            cell.value = "Geitost";
            cell = cells.get("C14");
            cell.value = "Geitost";
            cell = cells.get("C15");
            cell.value = "Maxilaku";
            cell = cells.get("C16");
            cell.value = "Geitost";
            cell = cells.get("C17");
            cell.value = "Geitost";
            cell = cells.get("C18");
            cell.value = "Ikuru";
            cell = cells.get("C19");
            cell.value = "Ikuru";
            cell = cells.get("C20");
            cell.value = "Ikuru";
            cell = cells.get("C21");
            cell.value = "Ikuru";
            cell = cells.get("C22");
            cell.value = "Ipoh Coffee";
            cell = cells.get("C23");
            cell.value = "Ipoh Coffee";
            cell = cells.get("C24");
            cell.value = "Ipoh Coffee";
            cell = cells.get("C25");
            cell.value = "Chocolade";
            cell = cells.get("C26");
            cell.value = "Chocolade";
            cell = cells.get("C27");
            cell.value = "Chocolade";
            cell = cells.get("C28");
            cell.value = "Chocolade";
            cell = cells.get("C29");
            cell.value = "Chocolade";
            cell = cells.get("C30");
            cell.value = "Chocolade";
            cell = cells.get("D2");
            cell.value = "Asia";
            cell = cells.get("D3");
            cell.value = "Asia";
            cell = cells.get("D4");
            cell.value = "Asia";
            cell = cells.get("D5");
            cell.value = "Asia";
            cell = cells.get("D6");
            cell.value = "Europe";
            cell = cells.get("D7");
            cell.value = "Europe";
            cell = cells.get("D8");
            cell.value = "Europe";
            cell = cells.get("D9");
            cell.value = "Europe";
            cell = cells.get("D10");
            cell.value = "Europe";
            cell = cells.get("D11");
            cell.value = "America";
            cell = cells.get("D12");
            cell.value = "America";
            cell = cells.get("D13");
            cell.value = "America";
            cell = cells.get("D14");
            cell.value = "America";
            cell = cells.get("D15");
            cell.value = "America";
            cell = cells.get("D16");
            cell.value = "America";
            cell = cells.get("D17");
            cell.value = "America";
            cell = cells.get("D18");
            cell.value = "Europe";
            cell = cells.get("D19");
            cell.value = "Europe";
            cell = cells.get("D20");
            cell.value = "Europe";
            cell = cells.get("D21");
            cell.value = "Oceania";
            cell = cells.get("D22");
            cell.value = "Oceania";
            cell = cells.get("D23");
            cell.value = "Oceania";
            cell = cells.get("D24");
            cell.value = "Oceania";
            cell = cells.get("D25");
            cell.value = "Africa";
            cell = cells.get("D26");
            cell.value = "Africa";
            cell = cells.get("D27");
            cell.value = "Africa";
            cell = cells.get("D28");
            cell.value = "Africa";
            cell = cells.get("D29");
            cell.value = "Africa";
            cell = cells.get("D30");
            cell.value = "Africa";
            cell = cells.get("E2");
            cell.value = "China";
            cell = cells.get("E3");
            cell.value = "India";
            cell = cells.get("E4");
            cell.value = "Korea";
            cell = cells.get("E5");
            cell.value = "India";
            cell = cells.get("E6");
            cell.value = "France";
            cell = cells.get("E7");
            cell.value = "France";
            cell = cells.get("E8");
            cell.value = "Germany";
            cell = cells.get("E9");
            cell.value = "Italy";
            cell = cells.get("E10");
            cell.value = "France";
            cell = cells.get("E11");
            cell.value = "U.S.";
            cell = cells.get("E12");
            cell.value = "U.S.";
            cell = cells.get("E13");
            cell.value = "Brazil";
            cell = cells.get("E14");
            cell.value = "U.S.";
            cell = cells.get("E15");
            cell.value = "U.S.";
            cell = cells.get("E16");
            cell.value = "Canada";
            cell = cells.get("E17");
            cell.value = "U.S.";
            cell = cells.get("E18");
            cell.value = "Italy";
            cell = cells.get("E19");
            cell.value = "France";
            cell = cells.get("E20");
            cell.value = "Italy";
            cell = cells.get("E21");
            cell.value = "New Zealand";
            cell = cells.get("E22");
            cell.value = "Australia";
            cell = cells.get("E23");
            cell.value = "Australia";
            cell = cells.get("E24");
            cell.value = "New Zealand";
            cell = cells.get("E25");
            cell.value = "S.Africa";
            cell = cells.get("E26");
            cell.value = "S.Africa";
            cell = cells.get("E27");
            cell.value = "S.Africa";
            cell = cells.get("E28");
            cell.value = "Egypt";
            cell = cells.get("E29");
            cell.value = "Egypt";
            cell = cells.get("E30");
            cell.value = "Egypt";
            cell = cells.get("F2");
            cell.value = 2000;
            cell = cells.get("F3");
            cell.value = 500;
            cell = cells.get("F4");
            cell.value = 1200;
            cell = cells.get("F5");
            cell.value = 1500;
            cell = cells.get("F6");
            cell.value = 500;
            cell = cells.get("F7");
            cell.value = 1500;
            cell = cells.get("F8");
            cell.value = 800;
            cell = cells.get("F9");
            cell.value = 900;
            cell = cells.get("F10");
            cell.value = 500;
            cell = cells.get("F11");
            cell.value = 1600;
            cell = cells.get("F12");
            cell.value = 600;
            cell = cells.get("F13");
            cell.value = 2000;
            cell = cells.get("F14");
            cell.value = 500;
            cell = cells.get("F15");
            cell.value = 900;
            cell = cells.get("F16");
            cell.value = 700;
            cell = cells.get("F17");
            cell.value = 1400;
            cell = cells.get("F18");
            cell.value = 1350;
            cell = cells.get("F19");
            cell.value = 300;
            cell = cells.get("F20");
            cell.value = 500;
            cell = cells.get("F21");
            cell.value = 1000;
            cell = cells.get("F22");
            cell.value = 1500;
            cell = cells.get("F23");
            cell.value = 1500;
            cell = cells.get("F24");
            cell.value = 1600;
            cell = cells.get("F25");
            cell.value = 1000;
            cell = cells.get("F26");
            cell.value = 1200;
            cell = cells.get("F27");
            cell.value = 1300;
            cell = cells.get("F28");
            cell.value = 1500;
            cell = cells.get("F29");
            cell.value = 1400;
            cell = cells.get("F30");
            cell.value = 1000;

            // Adding a new sheet
            const sheet2 = workbook.worksheets.get(workbook.worksheets.add());

            // Naming the sheet
            sheet2.name = "PivotTable";

            // Getting the pivottables collection in the sheet
            const pivotTables = sheet2.pivotTables;

            // Adding a PivotTable to the worksheet
            const index = pivotTables.add("=Data!A1:F30", "B3", "PivotTable1");

            // Accessing the instance of the newly added PivotTable
            const pivotTable = pivotTables.get(index);

            // Showing the grand totals
            pivotTable.rowGrand = true;
            pivotTable.columnGrand = true;

            // Setting the PivotTable report is automatically formatted
            pivotTable.isAutoFormat = true;

            // Setting the PivotTable autoformat type.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report6;

            // Dragging the first field to the row area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

            // Dragging the third field to the row area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 2);

            // Dragging the second field to the row area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 1);

            // Dragging the fourth field to the column area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 3);

            // Dragging the fifth field to the data area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 5);

            // Setting the number format of the first data field
            pivotTable.dataFields.get(0).numberFormat = "$#,##0.00";

            // Saving the Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'pivotTable_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **How to Add a Pivot Chart Using Aspose.Cells for JavaScript via C++ Library**

To create a PivotChart using Aspose.Cells for JavaScript via C++:

1. Add a chart.
1. Set the PivotSource of the chart to refer to an existing pivot table in the spreadsheet.
1. Set other attributes.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Pivot Chart</title>
    </head>
    <body>
        <h1>Create Pivot Chart Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new sheet of Chart type and retrieving it
            const worksheets = workbook.worksheets;
            const addedSheetIndex = worksheets.add(AsposeCells.SheetType.Chart);
            const sheet3 = worksheets.get(addedSheetIndex);

            // Naming the sheet
            sheet3.name = "PivotChart";

            // Adding a column chart
            const chartIndex = sheet3.charts.add(AsposeCells.ChartType.Column, 0, 5, 28, 16);

            // Setting the pivot chart data source and hiding pivot field buttons
            const chart = sheet3.charts.get(chartIndex);
            chart.pivotSource = "PivotTable!PivotTable1";
            chart.hidePivotFieldButtons = false;

            // Saving the modified Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'pivotChart_test_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```