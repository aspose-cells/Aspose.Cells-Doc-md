---
title: Formatteil einer PivotTable
linktitle: Formatteil einer PivotTable
description: Formatiere einen Teil einer PivotTable in Aspose.Cells for JavaScript via C++ indem Styles auf semantische PivotArea‑Bereiche oder CellArea‑Rechtecke über PivotTable.Format angewendet werden, wobei Formate in PivotTable.PivotFormats gespeichert werden und beim Aktualisieren der PivotTable erhalten bleiben.
keywords: Aspose.Cells for JavaScript via C++, PivotTable, Format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /de/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
`PivotTable.FormatAll` wendet einen einzigen Stil auf die gesamte PivotTable an und wird auf der übergeordneten Seite behandelt. Es unterscheidet nicht zwischen Beschriftungen, Werten, Summen oder bestimmten Bereichen des Berichts.  
In der Praxis muss in der Regel nur ein Teil einer PivotTable hervorgehoben werden. Häufige Ziele sind die Beschriftungen, die zu einem Zeilenfeld gehören, die Wertzellen, die von einem Feld erzeugt werden, die Gesamtsummenzeile oder ein beliebiges Rechteck wie die ersten beiden Elementzeilen.  
Das direkte Anwenden eines Stils auf die Arbeitsblattzellen einer PivotTable ist nicht gleichwertig. Excel speichert die Formatierung von PivotTables als semantische `PivotArea`‑Bereiche statt als gewöhnliche Zellformat‑Einträge. Ein `PivotArea`‑Format bleibt an einem Bereich wie den Beschriftungen eines Feldes oder Datenwerten befestigt und wird neu aufgelöst, wenn die PivotTable neu berechnet, aktualisiert oder erweitert wird. Ein direkt in eine Zelle geschriebener Stil hingegen gehört zu dieser Zellenposition und wird vom Pivot‑Modell nicht verfolgt.  
Aspose.Cells stellt die vollständige Überladungsfamilie von `PivotTable.Format` zur Verfügung, sodass beide Arten der Formatierung verfügbar sind:
- `Format(PivotArea, Style)` verankert einen Stil an einem semantischen Bereich, der mit `PivotArea.Select` oder `PivotArea.SelectField` erstellt wird.
- `Format(CellArea, Style)` verankert einen Stil an einem Arbeitsblatt‑Rechteck innerhalb der PivotTable.
- `Format(int row, int column, Style)` richtet sich an eine einzelne Zelle.
- `FormatAll(Style)` formatiert die gesamte PivotTable.

## **PivotArea formatieren**
Der semantische‑Bereich‑Workflow ist der empfohlene Ansatz, wenn eine Hervorhebung einem Feld oder einem Bereich des Berichts folgen muss.
1. Erstelle ein `PivotArea` mit `new PivotArea(pivotTable)`. Das Objekt beschreibt einen semantischen Bereich, der zu dieser spezifischen PivotTable gehört.
2. Wähle ein Feld anhand seiner nullbasierten Position auf einer angegebenen Achse mit `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` aus.
   - `PivotTableSelectionType.DataAndLabel` wählt sowohl die Beschriftungen als auch die Daten des Feldes aus.
   - `PivotTableSelectionType.LabelOnly` wählt nur die Beschriftungen des Feldes aus.
   - `PivotTableSelectionType.DataOnly` wählt nur die Datenzellen des Feldes aus.
3. Wähle ein Feld anhand des Namens mit `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` aus. Wird ein Zeilenfeld nach Name ausgewählt, löst sich der Bereich zu den von den Elementen dieses Feldes erzeugten Wertzellen auf.
4. Erstelle einen `Style` mit `Workbook.CreateStyle()`, konfiguriere seine Schriftart, Vordergrundfarbe und ein einheitliches Hintergrundmuster und übergebe den Stil an `PivotTable.Format(area, style)`.
5. Jeder Aufruf der `PivotArea`‑Überladung fügt einen `PivotTableFormat`‑Eintrag zu `PivotTable.PivotFormats` hinzu.
6. Feldverankerte Formate werden gezeichnet, wenn die PivotTable‑Daten berechnet werden. Daher rufe `PivotTable.CalculateData()` nach dem Anwenden der Formate auf, damit die Stile sichtbar werden.  
Das folgende Beispiel erstellt eine kleine PivotTable für Obstverkäufe, formatiert die Zeilenbeschriftungen `Fruit` mit `PivotArea.Select` und `PivotTableSelectionType.LabelOnly`, formatiert die von demselben Zeilenfeld erzeugten Wertzellen mit `PivotArea.SelectField` und berechnet anschließend die PivotTable neu, sodass beide Stile angewendet werden.

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
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **CellArea der PivotTable formatieren**
Verwende `PivotTable.Format(CellArea, Style)`, wenn der interessierende Bereich ein einfaches Arbeitsblatt‑Rechteck und kein semantischer Pivot‑Bereich ist.  
`CellArea` wird durch die Felder `startRow`, `startColumn`, `endRow` und `endColumn` beschrieben. Die Werte sind nullbasierte Arbeitsblattkoordinaten, und die Endkoordinaten geben die letzte Zeile und Spalte an, die im Rechteck enthalten sind, sodass der Bereich die Zellen von der Start‑ bis zur Endposition (inklusive) umfasst.  
Im Gegensatz zu einem feldverankerten Format wird ein `CellArea`‑Format sofort auf die Zellen angewendet. Ein weiterer Aufruf von `CalculateData()` ist nicht erforderlich, damit der Stil erscheint.  
Ein `CellArea`‑Rechteck kann sowohl Beschriftungszellen als auch Wertzellen enthalten. Der nächste Abschnitt beschreibt, wie Aspose.Cells und Excel dieses Rechteck intern darstellen.  
Das folgende Beispiel formatiert das Rechteck `E4:F5` der PivotTable mit einem kursiven, hellblauen Stil und speichert die Arbeitsmappe ohne weitere Neuberechnung.

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
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Wie PivotArea und CellArea abgebildet werden**
Excel speichert die Formatierung von PivotTables als `pivotArea`‑Einträge statt als gewöhnliche Arbeitsblatt‑Zellstil‑Einträge. Dasselbe Modell wird von Aspose.Cells verwendet, sodass eine Formatierungsanforderung beim Aufzeichnen in PivotArea‑Bereiche übersetzt wird.  
Die Beziehung zwischen dem vom Benutzer bereitgestellten `CellArea` und den intern gespeicherten PivotArea‑Einträgen ist in beide Richtungen viele‑zu‑viele.
- Ein `CellArea` kann mehrere PivotArea erzeugen. Wenn das Rechteck sowohl Beschriftungs‑ als auch Wertzellen umfasst, wird es in separate Beschriftungs‑ und Datenregeln aufgeteilt, da das Pivot‑Modell Beschriftungs‑ und Datenformatierung unabhängig behandelt.
- Eine PivotArea kann sich in mehrere disjunkte `CellArea`‑Instanzen auflösen. Ein semantischer Bereich wie eine Gesamtsummenzeile oder ein Feld, dessen Elemente nicht zusammenhängend sind, kann mehrere Rechtecke abdecken. Deshalb gibt `PivotArea.GetCellAreas()` eine Sammlung zurück statt eines einzelnen Rechtecks.
Jeder über `PivotTable.Format` ausgeführte Formatierungsvorgang wird in `PivotTable.PivotFormats` aufgezeichnet. Jeder `PivotTableFormat`‑Eintrag stellt das zugehörige `PivotArea` und den darauf angewendeten `Style` bereit. Die `PivotArea`‑Überladung fügt genau einen Eintrag pro Aufruf hinzu, während ein `CellArea`, das verschiedene semantische Regionen enthält, mehrere Einträge hinzufügen kann.  
Um die gespeicherten Regionen zu unterscheiden, stellt jedes `PivotArea` die Flags `OnlyLabel` und `OnlyData` bereit. Das untenstehende Beispiel formatiert ein einzelnes Rechteck, das sowohl Beschriftungen als auch Werte abdeckt, untersucht `PivotTable.PivotFormats` und gibt die `CellArea`‑Koordinaten aus, zu denen jede gespeicherte PivotArea aufgelöst wird.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
Da die Formate als PivotAreas und nicht als gewöhnliche Zellstile gespeichert werden, überleben sie Neu‑Berechnungen und Aktualisierungen. Wenn die PivotTable mit `PivotTable.RefreshData` aktualisiert, mit `CalculateData` neu berechnet oder gespeichert und erneut geladen wird, löst sich jede gespeicherte PivotArea erneut an die aktuelle Position ihres Bereichs auf und ihr Stil wird wieder angewendet.
{{% /alert %}}

Verwende ein `PivotArea`, das mit `Select` oder `SelectField` erstellt wurde, wenn eine Hervorhebung über Aktualisierungen hinweg an einem Feld oder einem semantischen Bereich befestigt bleiben muss, und verwende ein `CellArea`, wenn das Formatieren eines festen Rechtecks im aktuellen Pivot‑Tabellen‑Layout ausreicht. Die Einzelzellen‑Überladung `Format(int row, int column, Style)` richtet sich an eine einzelne Zelle. Verwende `FormatAll`, das auf der übergeordneten Seite behandelt wird, wenn die gesamte PivotTable auf einmal neu gestaltet werden soll.

## **Verwandte Artikel**
- [Stil auf PivotTable anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)
- [PivotTable‑Zeilen‑ und Spaltenfelder hinzufügen](/cells/de/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Wertfelder in PivotTable verwalten](/cells/de/javascript-cpp/manage-value-fields/)
- [PivotTable aktualisieren](/cells/de/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}