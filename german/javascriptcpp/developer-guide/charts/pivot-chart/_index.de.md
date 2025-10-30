---
title: Wie man mit Aspose.Cells for JavaScript über C++ ein PivotDiagramm hinzufügt
linktitle: Pivot Diagramm
type: docs
weight: 100
url: /de/javascript-cpp/how-to-add-pivot-chart/
description: Wie man mit Aspose.Cells for JavaScript über C++ ein PivotDiagramm hinzufügt.
keywords: PivotDiagramm JavaScript über C++
---
## Was ist ein PivotChart

Ein Pivot-Chart ist eine visuelle Darstellung der Daten in einer Pivot-Tabelle. Pivot-Charts bieten eine Möglichkeit, Zusammenfassungen zu erstellen, zu analysieren, zu erkunden und präsentabel zu machen. Hier sind einige wichtige Funktionen und Aspekte von Pivot-Charts:

1. Dynamische Datenrepräsentation: Pivot-Charts aktualisieren sich automatisch, um Änderungen an der Pivot-Tabelle widerzuspiegeln. Wenn Felder in der Pivot-Tabelle hinzugefügt oder entfernt werden, wird das Pivot-Chart entsprechend aktualisiert.

1. Interaktiv: Pivot-Charts sind interaktiv, ermöglichen es Benutzern, Daten zu filtern, zu sortieren und zu vertiefen. Dadurch ist es einfach, verschiedene Aspekte des Datensatzes zu erkunden.

1. Flexibles Layout: Benutzer können das Layout des Pivot-Diagrams durch Ziehen und Ablegen von Feldern ändern, was Flexibilität bei der Visualisierung von Daten bietet.

1. Verschiedene Diagrammtypen: Pivot-Diagramme können mit verschiedenen Diagrammtypen wie Säulendiagrammen, Liniendiagrammen, Kreisdiagrammen und mehr erstellt werden, je nach Art der Daten und den gewünschten Erkenntnissen.

1. Zusammenfassung: Pivot-Diagramme fassen große Datenmengen zusammen und können Summen, Durchschnitte, Zählen oder andere Zusammenfassungsstatistiken anzeigen.

1. Filtern: Sie bieten Filterfunktionen, mit denen nur Daten angezeigt werden, die bestimmte Kriterien erfüllen.

<br>
Pivot-Diagramme werden häufig in Business Intelligence und Datenanalyse verwendet, um eine klare und prägnante visuelle Zusammenfassung komplexer Datensätze zu bieten. Sie sind ein mächtiges Werkzeug, um datengetriebene Entscheidungen zu treffen.

## Wie man mit Aspose.Cells for JavaScript über C++ ein PivotDiagramm hinzufügt

### **Hinzufügen einer Pivot-Tabelle**

Erstellen einer Pivot-Tabelle mit Aspose.Cells for JavaScript über C++:

1. Fügen Sie Daten in ein Arbeitsblatt ein, indem Sie die `putValue`-Methode eines Zellobjekts verwenden. Sie können auch eine bereits mit Daten gefüllte Vorlage verwenden. Die Daten werden als Datenquelle für die Pivot-Tabelle verwendet.
1. Fügen Sie eine Pivot-Tabelle zum Arbeitsblatt hinzu, indem Sie die `add`-Methode der `PivotTables`-Sammlung aufrufen.
1. Greifen Sie auf das neue PivotTable-Objekt aus der `PivotTables`-Sammlung zu, indem Sie seinen Index übergeben. Verwenden Sie eines der PivotTable-Objekte innerhalb des PivotTable-Objekts, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Populate Worksheet and Download</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Name the sheet
            sheet.name = "Data";
            const cells = sheet.cells;

            // Setting the header values to the cells
            cells.get("A1").value = "Employee";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Product";
            cells.get("D1").value = "Continent";
            cells.get("E1").value = "Country";
            cells.get("F1").value = "Sale";

            const namesAndValues = [
                ["David", 1, "Maxilaku", "Asia", "China", 2000],
                ["David", 2, "Maxilaku", "Asia", "India", 500],
                ["David", 3, "Chai", "Asia", "Korea", 1200],
                ["David", 4, "Maxilaku", "Asia", "India", 1500],
                ["James", 1, "Chang", "Europe", "France", 500],
                ["James", 2, "Chang", "Europe", "France", 1500],
                ["James", 3, "Chang", "Europe", "Germany", 800],
                ["James", 4, "Chang", "Europe", "Italy", 900],
                ["James", 4, "Chang", "Europe", "France", 500],
                ["Miya", 1, "Geitost", "America", "U.S.", 1600],
                ["Miya", 2, "Chai", "America", "U.S.", 600],
                ["Miya", 3, "Geitost", "America", "Brazil", 2000],
                ["Miya", 2, "Geitost", "America", "U.S.", 500],
                ["Miya", 3, "Maxilaku", "America", "Canada", 900],
                ["Miya", 4, "Geitost", "America", "U.S.", 700],
                ["Miya", 5, "Geitost", "America", "U.S.", 1400],
                ["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
                ["Miya", 7, "Ikuru", "Europe", "France", 300],
                ["Miya", 8, "Ikuru", "Europe", "Italy", 500],
                ["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
                ["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
                ["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
                ["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
                ["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
                ["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
                ["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
                ["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
            ];

            namesAndValues.forEach((item, index) => {
                const rowIndex = index + 2;
                cells.get(`A${rowIndex}`).value = item[0];
                cells.get(`B${rowIndex}`).value = item[1];
                cells.get(`C${rowIndex}`).value = item[2];
                cells.get(`D${rowIndex}`).value = item[3];
                cells.get(`E${rowIndex}`).value = item[4];
                cells.get(`F${rowIndex}`).value = item[5];
            });

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet populated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hinzufügen eines Pivot-Diagramms**

Erstellen eines PivotDiagramms mit Aspose.Cells for JavaScript über C++:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie die `PivotSource` des Diagramms so, dass sie sich auf eine vorhandene Pivot-Tabelle im Spreadsheet bezieht.
1. Setzen Sie andere Attribute.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Pivot Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new sheet of Chart type
            const sheetIndex = workbook.worksheets.add(AsposeCells.SheetType.Chart);
            const sheet3 = workbook.worksheets.get(sheetIndex);
            sheet3.name = "PivotChart";

            // Adding a column chart
            const index = sheet3.charts.add(AsposeCells.ChartType.Column, 0, 5, 28, 16);

            // Setting the pivot chart data source and hiding pivot field buttons
            const chart = sheet3.charts.get(index);
            chart.pivotSource = "PivotTable!PivotTable1";
            chart.hidePivotFieldButtons = false;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'pivotChart_test_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
