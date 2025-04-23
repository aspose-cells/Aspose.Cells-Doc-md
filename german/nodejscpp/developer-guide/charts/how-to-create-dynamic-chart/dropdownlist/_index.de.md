---
title: Wie man mithilfe von Node.js über C++ ein dynamisches Diagramm mit Dropdown Liste erstellt
linktitle: Wie man ein dynamisches Diagramm mit Dropdown Liste erstellt
description: Erfahren Sie, wie Sie ein dynamisches Diagramm erstellen, das basierend auf einer Drop down Auswahl mit Aspose.Cells for Node.js via C++ aktualisiert wird. Unser Schritt für Schritt Leitfaden zeigt, wie Sie eine Dropdown Liste in Ihr Diagramm integrieren, um eine flexible Datenvisualisierung zu ermöglichen.
keywords: Aspose.Cells for Node.js via C++, Dynamisches Diagramm, Drop Down Liste, Datenvisualisierung, Integration, Flexible Visualisierung.
type: docs
weight: 76
url: /de/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Mögliche Verwendungsszenarien**
Ein dynamisches Diagramm mit Dropdown-Liste in Excel ist ein leistungsfähiges Werkzeug, das es Benutzern ermöglicht, interaktive Diagramme zu erstellen, die sich basierend auf den ausgewählten Daten dynamisch aktualisieren können. Diese Funktion ist besonders nützlich in Situationen, in denen mehrere Datensätze analysiert oder verschiedene Szenarien verglichen werden müssen.

Eine häufige Anwendung eines dynamischen Diagramms mit Dropdown-Liste liegt in der Finanzanalyse. Zum Beispiel kann ein Unternehmen mehrere Finanzdatensätze für verschiedene Jahre oder Abteilungen haben. Mithilfe einer Dropdown-Liste können Benutzer den spezifischen Datensatz auswählen, den sie analysieren möchten, und das Diagramm wird automatisch aktualisiert, um die entsprechenden Informationen anzuzeigen. Dies ermöglicht einen einfachen Vergleich und die Identifizierung von Trends oder Mustern.

Eine weitere Anwendung liegt im Verkauf und Marketing. Ein Unternehmen kann Verkaufsdaten für verschiedene Produkte oder Regionen haben. Mit einem dynamischen Diagramm mit Dropdown-Liste können Benutzer ein bestimmtes Produkt oder eine bestimmte Region aus der Dropdown-Liste auswählen, und das Diagramm wird sich dynamisch aktualisieren, um die Verkaufsleistung für die ausgewählte Option anzuzeigen. Dies hilft bei der Identifizierung der leistungsstärksten Bereiche oder Produkte und bei der datengesteuerten Entscheidungsfindung.

Zusammenfassend bietet ein dynamisches Diagramm mit Dropdown-Liste in Excel eine flexible und interaktive Möglichkeit, Daten zu visualisieren und zu analysieren. Es ist in Situationen wertvoll, in denen mehrere Datensätze verglichen oder verschiedene Szenarien untersucht werden müssen, wodurch es ein vielseitiges Werkzeug für Finanzanalyse, Verkauf und Marketing sowie viele andere Anwendungen ist.

## **Verwenden Sie Aspose Cells, um ein dynamisches Diagramm mit Dropdown-Liste zu erstellen**
Im folgenden Abschnitt zeigen wir Ihnen, wie Sie mit Aspose.Cells for Node.js via C++ ein dynamisches Diagramm mit Dropdown-Liste erstellen. Wir präsentieren den Code für das Beispiel sowie die Excel-Datei, die mit diesem Code erstellt wurde.

## **Beispielcode**
Der folgende Beispielcode wird die [Datei für das dynamische Diagramm mit Dropdown-Liste](DynamicChartWithDropdownlist.xlsx) generieren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **Anmerkungen**
In der generierten Datei zählt das Diagramm dynamisch die Daten für den ausgewählten Monat. Dies wird im Beispielcode mit der "OFFSET"-Formel durchgeführt:

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Sie können versuchen, den Wert der Dropdown-Liste in Zelle "Sheet1!$A$10" zu ändern, und Sie werden die dynamische Änderung des Diagramms sehen. Jetzt haben wir erfolgreich ein dynamisches Diagramm mit Dropdown-Liste unter Verwendung von Aspose.Cells erstellt.
