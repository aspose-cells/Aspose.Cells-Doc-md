---
title: Infoga pivot tabell
linktitle: Pivot tabeller
type: docs
weight: 160
url: /sv/javascript-cpp/create-pivot-table/
description: Skapa och formatera pivottabeller i Excel kalkylbladsfiler.
---

## **Skapa Pivottabell**

Det är möjligt att använda Aspose.Cells for JavaScript via C++ för att programmässigt lägga till pivottabeller i kalkylblad.

### **Pivot-tabell objektmodell**

Aspose.Cells for JavaScript via C++ tillhandahåller en speciell uppsättning klasser som används för att skapa och styra pivottabeller. Dessa klasser används för att skapa och ställa in [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) objekt, byggstenarna för en pivottabell. Objekten är:

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) representerar en fält i en [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection) representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) objekt i [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) representerar en PivotTable på ett kalkylblad.
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) representerar en samling av alla [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) objekt på ett kalkylblad.

### **Skapa en enkel pivot-tabell med hjälp av Aspose.Cells**

1. Lägg till data på ett kalkylblad genom att använda [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) objektets [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) metod.
   Denna data kommer att användas som pivot-tabellens datakälla.
1. Lägg till en pivot-tabell i kalkylbladet genom att anropa [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) samlingen [**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-) metod, som är innesluten i Worksheet-objektet.
1. Kom åt det nya [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)-objektet från [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection)-samlingen genom att passera PivotTable-indexet.
1. Använd något av [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)-objekten (förklaras ovan) för att hantera pivot-tabellen.

Efter att ha kört exempelkoden läggs en pivot-tabell till kalkylbladet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pivot Table Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Instantiate a new Workbook object
                const workbook = new Workbook();

                // Obtaining the reference of the newly added worksheet
                const sheetIndex = workbook.worksheets.add();
                const sheet = workbook.worksheets.get(sheetIndex);
                const cells = sheet.cells;

                // Setting the value to the cells
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

                // Adding a PivotTable to the worksheet
                const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

                // Accessing the instance of the newly added PivotTable
                const pivotTable = pivotTables.get(index);

                // Unshowing grand totals for rows.
                pivotTable.rowGrand = false;

                // Dragging the first field to the row area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

                // Dragging the second field to the column area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 1);

                // Dragging the third field to the data area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);

                // Saving the Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'CreatePivotTable_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
            });
        });
    </script>
</html>
```

{{% alert color="primary" %}}

När du tilldelar ett cellområde som datakälla måste området gå från övre vänstra till nedre högra. Till exempel är "A1:C3" giltigt men "C3:A1" är inte det.

{{% /alert %}}
