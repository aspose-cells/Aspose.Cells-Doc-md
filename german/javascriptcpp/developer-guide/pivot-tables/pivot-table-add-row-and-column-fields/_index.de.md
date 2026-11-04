---
title: Hinzufügen von Zeilen- und Spaltenfeldern zu einer PivotTable in Aspose.Cells for JavaScript via C++
linktitle: Hinzufügen von Zeilen- und Spaltenfeldern zu einer PivotTable
description: Erfahren Sie, wie Sie Zeilen- und Spaltenfelder zu einer PivotTable hinzufügen und Zwischensummen von PivotTable-Feldern mithilfe von PivotField.SetSubtotals und PivotFieldSubtotalType in Aspose.Cells for JavaScript via C++ steuern.
keywords: Aspose.Cells, JavaScript via C++, PivotTable, Zeilenfeld, Spaltenfeld, PivotField, setSubtotals, PivotFieldSubtotalType, Zwischensummen, JavaScript, Excel-PivotTable
type: docs
weight: 220
url: /de/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**
Die Methode `pivotTable.addFieldToArea(fieldType, fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier PivotTable-Bereiche. Das Argument `fieldType` akzeptiert einen der folgenden `PivotFieldType`-Werte.
- `Row` — vertikal links angeordnete Felder
- `Column` — horizontal oben angeordnete Felder
- `Data` — Felder, deren Werte aggregiert werden
- `Page` — Felder, die als Berichtsfilter verwendet werden
Die Reihenfolge der Feldverschachtelung ist wichtig. Wenn Sie zunächst `Category` und anschließend `Item` zum Zeilenbereich hinzufügen, entsteht eine PivotTable, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Eine umgekehrte Reihenfolge kehrt die Hierarchie um.

## **Zwischensummen für PivotTable-Felder**
Die Methode `pivotField.setSubtotals(subtotalType, shown)` steuert, welche Zwischensummenzeilen für ein PivotTable-Feld angezeigt werden. Jeder Aufruf aktiviert oder deaktiviert unabhängig genau einen Zwischensummentyp. Bei `shown = true` wird die Zwischensumme angezeigt, bei `shown = false` wird sie ausgeblendet. Da jeder Aufruf nur einen Typ beeinflusst, können durch mehrfache Aufrufe der Methode mit unterschiedlichen `subtotalType`-Werten eine benutzerdefinierte Teilmenge von Zwischensummen erstellt werden.
Die Aufzählung `PivotFieldSubtotalType` definiert die verfügbaren Arten von Zwischensummen.
- `Automatic` — Aspose.Cells wählt die Standardauswahl aus (in der Regel `Sum` für numerische Felder)
- `None` — unterdrückt alle Zwischensummenzeilen
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Zwischensummen werden nur dargestellt, wenn der Zeilenbereich (oder der Spaltenbereich) zwei oder mehr PivotTable-Felder enthält. Bei einem einzigen Feld gibt es keine Gruppen, zwischen denen eine Zwischensumme sinnvoll berechnet werden könnte. Daher haben `setSubtotals`-Aufrufe in diesem Fall keine sichtbare Wirkung. Dieser Artikel verwendet deshalb in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Grenze zwischen den `Category`-Gruppen anhand der Zwischensummen sichtbar wird.
{{% /alert %}}

## **Szenario 1 — Automatische Zwischensummen (Standard)**
Wenn Sie `setSubtotals` nicht aufrufen, wendet Aspose.Cells die Auswahl `Automatic` auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten ausdrücklich, indem es `setSubtotals(PivotFieldSubtotalType.Automatic, true)` für das äußere Zeilenfeld `Category` aufruft.

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
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Szenario 2 — Unterdrücken aller Zwischensummen (None)**
Der Aufruf von `setSubtotals(PivotFieldSubtotalType.None, true)` entfernt alle Zwischensummenzeilen aus der PivotTable und lässt nur die Feldzeilen und das Gesamtergebnis am unteren Rand stehen. Dies ist nützlich, wenn Sie die gruppierten Rohdaten ohne jegliche Zusammenfassungszeilen anzeigen möchten.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Szenario 3 — Benutzerdefinierte Teilmenge von Zwischensummen (Sum + Average)**
Sie sind nicht auf einen einzigen Zwischensummentyp beschränkt. Jeder `setSubtotals`-Aufruf wirkt unabhängig auf genau einen Typ, sodass zwei Aufrufe – einmal mit `Sum` und einmal mit `Average` – eine benutzerdefinierte Teilmenge aus zwei Zwischensummenzeilen für jede `Category`-Gruppe erzeugen.

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const pivotTable = pivotTables.add("=A1:D9", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Zusammenfassung**
Die drei Szenarien unterscheiden sich nur durch die `setSubtotals`-Aufrufe. Alles andere – der Datensatz, die Felder und die Bereiche, denen sie zugewiesen sind – ist identisch, sodass die Layouts direkt vergleichbar sind.
- **Felder zuordnen.** `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` verschiebt eine Quellspalte in einen Bereich. Innerhalb eines Bereichs entspricht die Reihenfolge der Aufrufe der Anzeigereihenfolge, sodass der erste Aufruf die äußerste Gruppe bildet. Zwischensummen erfordern zwei oder mehr Felder im selben Bereich: Bei einem einzigen Feld gibt es keine Gruppen, zwischen denen eine Zwischensumme berechnet werden könnte.
- **Szenario 1 — automatische Zwischensummen.** Bleibt `setSubtotals` una aufgerufen, wird die Auswahl Excel überlassen. Excel wendet für numerische Felder eine eigene Standard-Zwischensumme an. Ein Aufruf von `setSubtotals` mit `PivotFieldSubtotalType.Automatic` legt diese Auswahl ausdrücklich fest, anstatt sie implizit zu belassen.
- **Szenario 2 — keine Zwischensummen.** `setSubtotals` mit `PivotFieldSubtotalType.None` deaktiviert die Standard-Zwischensumme, sodass die PivotTable die Feldzeilen und das Gesamtergebnis beibehält, die Zwischensummenzeilen jedoch weglässt, die Excel andernfalls dazwischen einfügen würde.
- **Szenario 3 — eine ausgewählte Teilmenge.** Jeder Aufruf schaltet genau einen Zwischensummentyp um, und aufeinanderfolgende Aufrufe wirken sich kumulativ aus, statt einander zurückzusetzen. Ein Aufruf mit `PivotFieldSubtotalType.Sum` und ein weiterer mit `PivotFieldSubtotalType.Average` lassen daher beide Typen aktiviert, sodass die PivotTable eine `Sum`-Zwischensumme, eine `Average`-Zwischensumme und ein Gesamtergebnis darstellt.

{{% alert color="primary" %}}
Zwischensummen sind nicht auf den Zeilenbereich beschränkt. Dieselben `setSubtotals`-Aufrufe für ein Feld aus `pivotTable.getColumnFields()` erzeugen dieselben drei Layouts auf der Spaltenachse, da die Einstellung zum PivotTable-Feld und nicht zu der Achse gehört, auf der es liegt.
{{% /alert %}}

## **Verwandte Artikel**
- [Seitenfelder in PivotTables](/cells/de/javascript-cpp/add-page-field-in-pivot-table/)
- [PivotTables in Aspose.Cells for JavaScript via C++ aktualisieren](/cells/de/javascript-cpp/refresh-pivot-table/)
- [Stile auf PivotTables anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}