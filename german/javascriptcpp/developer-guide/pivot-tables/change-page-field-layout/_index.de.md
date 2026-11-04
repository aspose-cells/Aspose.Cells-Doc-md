---
title: Layout des Seitenfeldbereichs in einer PivotTable ändern
linktitle: Layout des Seitenfeldbereichs in einer PivotTable ändern
description: Erfahren Sie, wie Sie mit Aspose.Cells for JavaScript via C++ das Layout des Seitenfeldbereichs in einer PivotTable steuern und die Anzeigereihenfolge, die Umbruchanzahl und die Reihenfolge der Seitenfelder oben in der PivotTable festlegen.
keywords: Aspose.Cells for JavaScript via C++, Tabellenkalkulation, PivotTable, Seitenfeld, Seitenfeldreihenfolge, Umbruchanzahl für Seitenfelder, Seitenfeld verschieben
type: docs
weight: 191
url: /de/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Dieser Artikel ist eine Fortsetzung des Themas **Seitenfeld in PivotTable hinzufügen**. Er veranschaulicht, wie Sie das Layout des Seitenfeldbereichs – der Leiste mit Filtersteuerelementen oben in einer PivotTable – steuern können. Dabei werden die Anzeigereihenfolge, die Umbruchanzahl und die Neuordnung der Felder behandelt.
{{% /alert %}}

## **Einführung**
Eine PivotTable in Microsoft Excel bietet einen eigenen **Seitenfeldbereich**, der oberhalb des Zeilen-, Spalten- und Datenbereichs der Tabelle angezeigt wird. Dieser Bereich wird als Leiste mit Dropdown-Filtersteuerelementen dargestellt (ein Steuerelement pro Seitenfeld). Endbenutzer klicken auf diese Filtersteuerelemente, um die PivotTable nach Kriterien wie Jahr oder Region zu filtern. Aspose.Cells bildet diesen Bereich über die Sammlung `pivotTable.pageFields` ab und stellt drei Eigenschaften bereit, die die visuelle Anordnung der Leiste steuern:
- `pivotTable.pageFieldOrder` (ein `Aspose.Cells.PrintOrderType`-Wert) bestimmt, ob zusätzliche Seitenfelder *neben* den vorhandenen Seitenfeldern oder *unterhalb von ihnen* angeordnet werden.
- `pivotTable.pageFieldWrapCount` legt fest, wie viele Seitenfelder pro Zeile oder Spalte angeordnet werden, bevor ein Umbruch erfolgt.
- `pivotTable.pageFields.move(currIndex, destIndex)` ordnet die Seitenfelder neu, ohne den Anordnungsmodus zu ändern.
Dieser Artikel zeigt in drei Codebeispielen, wie Sie diese Vorgänge mit einem gemeinsamen Datensatz ausführen und die resultierenden Layouts miteinander vergleichen können.

## **Quelldaten**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alle acht Zeilen werden in jedem Codebeispiel mit denselben Daten in derselben Reihenfolge befüllt. Die Quelldaten bleiben daher zwischen den Szenarien unverändert; lediglich die Eigenschaften des Seitenfeldlayouts unterscheiden sich.

## **Beispiel 1: Over Then Down**
Im ersten Szenario konfigurieren Sie die beiden Seitenfelder (`Year`, `Region`) so, dass sie **nebeneinander in einer einzigen Zeile** oben in der PivotTable angezeigt werden. Sie weisen `Fruit` der Zeilenachse zu, platzieren `Year` an erster und `Region` an zweiter Stelle des Seitenfeldbereichs (die Reihenfolge der `addFieldToArea`-Aufrufe bestimmt den Ausgangsindex), fügen `Amount` (Sum) als Datenfeld hinzu und setzen anschließend `pivotTable.pageFieldOrder` auf `PrintOrderType.OverThenDown` sowie `pivotTable.pageFieldWrapCount = 2`. Bei `OverThenDown` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder horizontal nebeneinander in einer einzigen Zeile oben in der PivotTable angeordnet. Die Leiste belegt somit eine Zeile und ist zwei Felder breit.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // Kopfzeilen (Zeile 0)
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // Zeile 1: Apple, 2022, North, 150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // Zeile 2: Apple, 2023, North, 180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // Zeile 3: Banana, 2022, South, 120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // Zeile 4: Banana, 2023, South, 140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // Zeile 5: Cherry, 2022, East, 200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // Zeile 6: Cherry, 2023, East, 220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // Zeile 7: Grape, 2022, West, 90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // Zeile 8: Grape, 2023, West, 110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // Arbeitsblatt PivotTableReport hinzufügen
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // Pivottabelle aus PivotData!A1:D9 erstellen und auf PivotTableReport an Position A1 platzieren
            const pivotTable = pivotTables.add("PivotData!A1:D9", 0, 0);
            // Felder hinzufügen
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Obst
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Jahr
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Betrag
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // Layout des Seitenfeldbereichs konfigurieren: Seitenfelder zuerst horizontal anordnen, nach jeweils 2 Feldern umbrechen
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // Aktualisieren und berechnen
            pivotTable.calculateData();
            // Speichern
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Beispiel 2: Down Then Over**
Ordnen Sie in diesem Beispiel `Fruit` der Zeilenachse, `Year` und `Region` dem Seitenfeldbereich (`Year` zuerst) sowie `Amount` (Sum) dem Datenfeld zu – genau wie in Beispiel 1. Anschließend setzen Sie `pivotTable.pageFieldOrder` auf `PrintOrderType.DownThenOver` und `pivotTable.pageFieldWrapCount` auf `2`. Bei `DownThenOver` und einer Umbruchanzahl von 2 werden die beiden Seitenfelder vertikal gestapelt: `Year` oben und `Region` direkt darunter. Zusammen bilden sie eine einzige Spalte oben in der PivotTable. Die Leiste belegt daher zwei Zeilen und ist ein Feld breit.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTable = pivotReport.pivotTables.add("=PivotData!A1:D9", 0, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Beispiel 3: Ein Seitenfeld verschieben**
Im dritten Szenario behalten Sie diesen Datensatz und diese Feldzuordnung bei, legen ein neutrales Layout fest (`OverThenDown` mit der Umbruchanzahl `2`) und veranschaulichen anschließend den Vorgang `pivotTable.pageFields.move`. Der Aufruf `move(0, 1)` verschiebt das Seitenfeld an Index 0 (`Year`) auf Position 1, während das zuvor an Position 1 befindliche Seitenfeld (`Region`) auf Position 0 rückt. Nach diesem Aufruf ist `Region` das erste und `Year` das zweite Seitenfeld. Die Umbrucheinstellung und der Anordnungsmodus bleiben unverändert. Die Leiste wird daher weiterhin horizontal nebeneinander dargestellt; lediglich die Reihenfolge der beiden Dropdown-Steuerelemente wurde vertauscht.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTable = pivotSheet.pivotTables.add("=PivotData!A1:D9", 2, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Verwandte Artikel**
- [Seitenfeld in PivotTable hinzufügen](/cells/de/javascript-cpp/add-page-field-in-pivot-table/) – die übergeordnete Seite, auf der erläutert wird, wie Seitenfelder zu einer PivotTable hinzugefügt werden.
- [Wertfelder in PivotTable verwalten](/cells/de/javascript-cpp/manage-value-fields/) – beschreibt, wie der Datenbereich (Wertbereich) konfiguriert wird, einschließlich der in diesem Artikel verwendeten `Sum`-Aggregation.
- [Formatierung auf PivotTable anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/) – zeigt, wie Sie die dargestellte PivotTable formatieren, nachdem die Leiste mit Seitenfeldern angeordnet wurde.

{{< app/cells/assistant language="javascript-cpp" >}}