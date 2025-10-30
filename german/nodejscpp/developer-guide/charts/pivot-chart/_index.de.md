---
title: So fügen Sie ein PivotChart mit Aspose.Cells for Node.js via C++ hinzu
linktitle: Pivot Diagramm
type: docs
weight: 100
url: /de/nodejs-cpp/how-to-add-pivot-chart/
description: So fügen Sie ein PivotChart mit Aspose.Cells for Node.js via C++ hinzu.
keywords: PivotChart Node.js über C++
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

## So fügen Sie ein PivotChart mit Aspose.Cells for Node.js via C++ hinzu

### **Hinzufügen einer Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells for Node.js via C++ zu erstellen:

1. Fügen Sie Daten in ein Arbeitsblatt ein, indem Sie die `putValue`-Methode eines Zellobjekts verwenden. Sie können auch eine bereits mit Daten gefüllte Vorlage verwenden. Die Daten werden als Datenquelle für die Pivot-Tabelle verwendet.
1. Fügen Sie eine Pivot-Tabelle zum Arbeitsblatt hinzu, indem Sie die `add`-Methode der `PivotTables`-Sammlung aufrufen.
1. Greifen Sie auf das neue PivotTable-Objekt aus der `PivotTables`-Sammlung zu, indem Sie seinen Index übergeben. Verwenden Sie eines der PivotTable-Objekte innerhalb des PivotTable-Objekts, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

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
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **Hinzufügen eines Pivot-Diagramms**

Um ein PivotChart mit Aspose.Cells for Node.js via C++ zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie die `PivotSource` des Diagramms so, dass sie sich auf eine vorhandene Pivot-Tabelle im Spreadsheet bezieht.
1. Setzen Sie andere Attribute.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
