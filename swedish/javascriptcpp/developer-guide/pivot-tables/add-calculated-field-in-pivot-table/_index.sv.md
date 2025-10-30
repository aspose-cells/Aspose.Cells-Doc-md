---
title: Lägg till beräknat fält i pivottabell
type: docs
weight: 130
url: /sv/javascript-cpp/add-calculated-field-in-pivot-table/
description: Hur man lägger till ett kalkylerat fält i pivottabell med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript bibliotek, Lägga till ett kalkylerat fält i pivottabell med JavaScript Excel bibliotek.
---

## **Möjliga användningsscenario**
När du skapar en pivottabell baserad på kända data finner du att datan i den inte är det du vill ha. Den data du vill ha är kombinationen av denna ursprungliga data. Till exempel behöver du lägga till, subtrahera, multiplicera och dividera den ursprungliga datan innan du vill ha datan. Vid den här tiden behöver du bygga ett beräknat fält och ställa in motsvarande formel för beräkning. Utför sedan vissa statistik och andra operationer på det beräknade fältet. 

## **Hur man lägger till beräknat fält i pivot-tabell i Excel**
Så här lägger du till ett beräknat fält i en pivot-tabell i Excel, följ dessa steg:

1. Välj pivottabellen som du vill lägga till ett beräknat fält i. 
2. Gå till fliken Pivottabell analysera på menyfliken.
3. Klicka på "Fält, artiklar och uppsättningar" och välj sedan "Beräknat fält" i rullgardinsmenyn.
4. I fältet "Namn" anger du ett namn för det beräknade fältet.
5. I fältet "Formel" anger du formeln för beräkningen du vill utföra med hjälp av lämpliga PivotTable-fältnamn och matematiska operatorer. 
<br>
<img src="1.png" width=80% />
6. Klicka på "ok" för att skapa det beräknade fältet.
7. Det nya beräknade fältet kommer att visas i PivotTable Field List under avsnittet Värden.
8. Dra det beräknade fältet till värdesektionen i PivotTable för att visa de beräknade värdena.
<br>
<img src="2.png" width=80% />

## ** Hur man lägger till kalkylerat fält i Pivottabell med Aspose.Cells for JavaScript via C++-bibliotek**
Lägg till beräknat fält till Excel-fil med Aspose.Cells for JavaScript via C++. Se följande exempel. Efter att ha kört exempel-koden läggs en pivottabell med beräknat fält till arbetsbladet.
1. Ange originaldata och skapa en pivot-tabell. 
2. Skapa det beräknade fältet enligt det befintliga PivotField i pivot-tabellen.
3. Lägg till det beräknade fältet i dataområdet. 
4. Slutligen sparas arbetsboken i [utdata XLSX](ut.xlsx)-format. 

## **Exempelkod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";
            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";
            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;
            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Adding a PivotTable to the worksheet (converted getPivotTables -> pivotTables)
            const i = ws.pivotTables.add("=A1:C5", "D10", "PivotTable1");
            // Accessing the instance of the newly added PivotTable
            const pivotTable = ws.pivotTables.get(i);
            pivotTable.addFieldToArea(PivotFieldType.Row, 0);
            // Adding a calculated field to PivotTable and drag it to data area.
            pivotTable.addCalculatedField("total", "=Count*Price", true);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
