---
title: Wie man ein Dynamisches Diagramm mit Dropdown Liste mit JavaScript via C++ erstellt
linktitle: Wie man ein dynamisches Diagramm mit Dropdown Liste erstellt
description: Lernen Sie, wie man ein dynamisches Diagramm erstellt, das auf einer Dropdown Auswahl basiert, mit Aspose.Cells for JavaScript via C++. Unser Schritt für Schritt Leitfaden zeigt, wie man eine Dropdown Liste in Ihr Diagramm integriert für eine flexible Datenvisualisierung.
keywords: Aspose.Cells for JavaScript via C++, Dynamisches Diagramm, Dropdown Liste, Datenvisualisierung, Integration, Flexible Visualisierung.
type: docs
weight: 76
url: /de/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Mögliche Verwendungsszenarien**
Ein dynamisches Diagramm mit Dropdown-Liste in Excel ist ein leistungsfähiges Werkzeug, das es Benutzern ermöglicht, interaktive Diagramme zu erstellen, die sich basierend auf den ausgewählten Daten dynamisch aktualisieren können. Diese Funktion ist besonders nützlich in Situationen, in denen mehrere Datensätze analysiert oder verschiedene Szenarien verglichen werden müssen.

Eine häufige Anwendung eines dynamischen Diagramms mit Dropdown-Liste liegt in der Finanzanalyse. Zum Beispiel kann ein Unternehmen mehrere Finanzdatensätze für verschiedene Jahre oder Abteilungen haben. Mithilfe einer Dropdown-Liste können Benutzer den spezifischen Datensatz auswählen, den sie analysieren möchten, und das Diagramm wird automatisch aktualisiert, um die entsprechenden Informationen anzuzeigen. Dies ermöglicht einen einfachen Vergleich und die Identifizierung von Trends oder Mustern.

Eine weitere Anwendung liegt im Verkauf und Marketing. Ein Unternehmen kann Verkaufsdaten für verschiedene Produkte oder Regionen haben. Mit einem dynamischen Diagramm mit Dropdown-Liste können Benutzer ein bestimmtes Produkt oder eine bestimmte Region aus der Dropdown-Liste auswählen, und das Diagramm wird sich dynamisch aktualisieren, um die Verkaufsleistung für die ausgewählte Option anzuzeigen. Dies hilft bei der Identifizierung der leistungsstärksten Bereiche oder Produkte und bei der datengesteuerten Entscheidungsfindung.

Zusammenfassend bietet ein dynamisches Diagramm mit Dropdown-Liste in Excel eine flexible und interaktive Möglichkeit, Daten zu visualisieren und zu analysieren. Es ist in Situationen wertvoll, in denen mehrere Datensätze verglichen oder verschiedene Szenarien untersucht werden müssen, wodurch es ein vielseitiges Werkzeug für Finanzanalyse, Verkauf und Marketing sowie viele andere Anwendungen ist.

## **Verwenden Sie Aspose Cells, um ein dynamisches Diagramm mit Dropdown-Liste zu erstellen**
Im nächsten Absatz zeigen wir, wie man mit Aspose.Cells for JavaScript via C++ ein dynamisches Diagramm mit Dropdown-Liste erstellt. Wir präsentieren den Code für das Beispiel sowie die Excel-Datei, die mit diesem Code erstellt wurde.

## **Beispielcode**
Der folgende Beispielcode wird die [Datei für das dynamische Diagramm mit Dropdown-Liste](DynamicChartWithDropdownlist.xlsx) generieren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Chart with Dropdown List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, BackgroundType, Color, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A3").putValue("Tea");
            sheet.cells.get("A4").putValue("Coffee");
            sheet.cells.get("A5").putValue("Sugar");

            // In this example, we will add 12 months of data
            sheet.cells.get("B2").putValue("Jan");
            sheet.cells.get("C2").putValue("Feb");
            sheet.cells.get("D2").putValue("Mar");
            sheet.cells.get("E2").putValue("Apr");
            sheet.cells.get("F2").putValue("May");
            sheet.cells.get("G2").putValue("Jun");
            sheet.cells.get("H2").putValue("Jul");
            sheet.cells.get("I2").putValue("Aug");
            sheet.cells.get("J2").putValue("Sep");
            sheet.cells.get("K2").putValue("Oct");
            sheet.cells.get("L2").putValue("Nov");
            sheet.cells.get("M2").putValue("Dec");
            const allMonths = 12;
            const iCount = 3;
            for (let i = 0; i < iCount; i++) {
                for (let j = 0; j < allMonths; j++) {
                    const _row = i + 2;
                    const _column = j + 1; 
                    sheet.cells.get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
                }
            }

            // This is the Dropdownlist for Dynamic Data
            const ca = CellArea.createCellArea(9, 0, 9, 0);
            const _index = sheet.validations.add(ca);
            const _va = sheet.validations.get(_index);
            _va.type = ValidationType.List;
            _va.inCellDropDown = true;
            _va.formula1 = "=$B$2:$M$2";
            sheet.cells.get("A9").putValue("Current Month");
            sheet.cells.get("A10").putValue("Jan");
            const _style = sheet.cells.get("A10").style;
            _style.font.isBold = true;
            _style.pattern = BackgroundType.Solid;
            _style.foregroundColor = Color.Yellow;
            sheet.cells.get("A10").style = _style;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtMonthData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtXLabels");
            sheets.names.get(index).refersTo = "=Sheet1!$A$3:$A$5";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Column, 8, 2, 20, 8);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("month", true);
            chart.nSeries.get(0).name = "=Sheet1!$A$10";
            chart.nSeries.get(0).values = "Sheet1!ChtMonthData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtXLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicChartWithDropdownlist.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **Anmerkungen**
In der generierten Datei zählt das Diagramm dynamisch die Daten für den ausgewählten Monat. Dies wird im Beispielcode mit der "OFFSET"-Formel durchgeführt:
