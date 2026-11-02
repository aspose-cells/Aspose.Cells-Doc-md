---
title: Filterfelder zu einer PivotTable in Aspose.Cells for JavaScript via C++ hinzufügen
linktitle: Filterfelder zu einer PivotTable
description: Erfahren Sie, wie Sie mit Aspose.Cells for JavaScript via C++ Filterfelder zu PivotTables hinzufügen und konfigurieren, einschließlich des Hinzufügens von Filterfeldern sowie der Einzelauswahl- und Mehrfachauswahlfilterung.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, PivotTable, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in PivotTables. Sie können ein Filterfeld entweder über eine komfortable High-Level-API oder über die Sammlung `getPageFields()` auf niedrigerer Ebene hinzufügen. Außerdem können Sie den Filter im Einzelauswahlmodus konfigurieren, ihn so zurücksetzen, dass alle Filterelemente angezeigt werden, oder das Feld auf Mehrfachauswahl umstellen, sodass Benutzer über die Kontrollkästchen-Oberfläche in Excel mehrere Filterelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**
Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten im PivotTable-Inhalt angezeigt wird. Endbenutzer sehen es in Excel als Dropdown-Liste am oberen Rand einer dargestellten PivotTable. Wenn sie eines der verfügbaren Filterelemente auswählen, wird der PivotTable-Inhalt neu aufgebaut, sodass nur die zu diesem Filterelement gehörenden Datensätze zusammengefasst werden. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.Page` statt `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data` registriert wird.

## **Hinzufügen eines Filterfelds**

### Hinzufügen eines Filterfelds mit `addFieldToArea`
Das folgende Beispiel erstellt einen kleinen Datensatz mit den Spalten `Fruit`, `Year` und `Amount`, platziert eine PivotTable in Zelle E3, ordnet `Fruit` dem Zeilenbereich, `Amount` dem Datenbereich und `Year` dem Filterbereich zu, aktualisiert die PivotTable und speichert die Arbeitsmappe.

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
            // Neue Arbeitsmappe erstellen
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            // Kopfzeile einrichten
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 Zeilen mit Beispieldaten befüllen: Fruit, Year, Amount
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // Fügen Sie eine Pivot-Tabelle hinzu, die an Zelle E3 verankert ist
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Fügen Sie Felder ihren Bereichen hinzu: Fruit als Zeile, Amount als Daten, Year als Seitenfeld
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // Aktualisieren und berechnen Sie die Pivot-Tabellendaten
            pivotTable.calculateData();
            // Arbeitsmappe speichern
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### Hinzufügen eines Filterfelds mit `getPageFields().add`
Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `pivotTable.getPageFields().add(pivotField)` übergeben. Die PivotTable und das Filterfeld werden genau wie im vorherigen Szenario erstellt; lediglich die abschließende Registrierung im Filterbereich wird durch den Aufruf einer API auf niedrigerer Ebene ersetzt.

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
            // — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
            //   Szenario 1a erstellt (Fruit/Year/Amount-Daten, Pivot bei E3, Fruit→Zeile,
            //   Amount→Daten). Unten holen wir das Year-PivotField aus der
            //   BaseFields-Auflistung und übergeben es an PageFields.Add —
            //   die Low-Level-Alternative zu AddFieldToArea. Das Ergebnis ist
            //   funktional identisch mit Szenario 1a.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Kopfzeilen
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // Beispieldaten (9 Zeilen)
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // Pivot-Tabelle bei E3 hinzufügen, die A1:C10 abdeckt
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Fruit -> Zeile, Amount -> Daten (Year wird unten zur Seite hinzugefügt)
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Low-Level-Ansatz: Das vorhandene Year-PivotField aus BaseFields abrufen
            // und über PageFields.Add(PivotField) im Seitenbereich registrieren.
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe berücksichtigt wird
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Einzelauswahlfilterung (Anzeige eines Filterelements)**
Im Standardverhalten der Einzelauswahl wird das Filterfeld als einzelne Dropdown-Liste dargestellt. Der ganzzahlige Wert `pivotField.currentPageItem` bestimmt, welches Filterelement den PivotTable-Inhalt steuert. Die Zuweisung eines bestimmten Index wählt genau dieses eine Element aus; die Zuweisung des besonderen Sentinel-Werts `0x7FFD` (dezimal 32765) hebt den Filter auf, sodass alle Filterelemente gleichzeitig zusammengefasst werden. Die Einzelauswahl ist der Standard und muss nicht ausdrücklich aktiviert werden.

### Alle Elemente anzeigen
Das Setzen von `currentPageItem` auf den Sentinel-Wert `0x7FFD` entspricht dem Aufheben des Filters: Der PivotTable-Inhalt fasst jedes Filterelement so zusammen, als ob kein Filter angewendet würde.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Eine neue Arbeitsmappe erstellen
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Daten für Obst/Jahr/Menge ausfüllen
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // Pivottabelle bei E3 erstellen
            const pivotTables = sheet.pivotTables;
            const pivotTableIndex = pivotTables.add("=A1:C7", "E3", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Pivotfelder konfigurieren: Fruit→Zeile, Amount→Daten, Year→Seite
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // Seitenfilter zurücksetzen, sodass jedes Element im Seitenfeld sichtbar ist.
            // 0x7FFD (dezimal 32765) ist der spezielle Sentinel-Wert, der „alle Elemente“ bedeutet —
            // entspricht der Auswahl „(Alle)“ im Dropdown-Feld für Seitenfelder in Excel.
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

### Ein bestimmtes Element anzeigen
Das Setzen von `currentPageItem` auf einen konkreten Index wählt genau dieses eine Filterelement aus. Der Index entspricht der Position des Elements in der sortierten Liste der Elemente des Filterfelds. Beispielsweise wählt `1` nach der Sortierung das zweite Element aus.

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
            const { Workbook, SaveFormat } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // Arbeitsmappe erstellen
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Beispieldaten hinzufügen (Frucht/Jahr/Menge)
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // Pivottabelle bei E3 hinzufügen
                const pivotTables = sheet.pivotTables;
                const pivotTableIndex = pivotTables.add("=A1:C5", "E3", "PivotTable1");
                const pivotTable = pivotTables.get(pivotTableIndex);
                // Felder hinzufügen: Frucht→Zeile, Menge→Daten, Jahr→Seite
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // Seitenfeldspezifische Operationen
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = zweiter Eintrag in sortierter Reihenfolge (z. B. "2021")
                // Pivottabelle aktualisieren und berechnen
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Mehrfachauswahlfilterung**
Die Mehrfachauswahlfilterung wandelt die Dropdown-Liste des Filters in eine Liste mit Kontrollkästchen um und ermöglicht es Endbenutzern, mehrere Filterelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `pivotField.isMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Oberfläche für die Mehrfachauswahl überhaupt wirksam wird. Nach der Aktivierung steuert `pivotItem.isHidden`, welche Elemente in der Liste mit Kontrollkästchen erscheinen. So können Sie entweder alle Elemente anzeigen oder nur bestimmte Elemente über eine Positivliste zur Auswahl zulassen.

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
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
                //   Szenario 1a erstellt (Fruit/Year/Amount-Daten, Pivot bei E3, Fruit→Zeile,
                //   Amount→Daten, Year→Seite über AddFieldToArea).
                //   Im Folgenden wenden wir eine Mehrfachauswahl-Filterung auf das Seitenfeld an.
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Beispieldaten: Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTableIndex = pivots.add("=A1:C10", "E3", "PivotTable1");
                const pivotTable = pivots.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — Mehrfachauswahl für das Seitenfeld aktivieren
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // Teil A — ALLE Elemente auswählen (jedes Element sichtbar machen)
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // Teil B — Nur bestimmte Elemente nach Quellwert auswählen
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **Hinweis:** Bei Verwendung der Mehrfachauswahlfilterung über `pivotItem.isHidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`isHidden === false`). Wenn alle Elemente ausgeblendet sind, stürzt Excel entweder beim Öffnen der Datei ab oder zeigt eine leere PivotTable an. Stellen Sie sicher, dass Ihre Positivliste für die Mehrfachauswahl mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welchen Modus sollte ich verwenden?**
Die folgende Tabelle fasst zusammen, wann welche API und welcher Modus verwendet werden sollten, damit Sie die passende Kombination auswählen können, ohne jedes Szenario im Detail lesen zu müssen.
| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Ein Filterfeld anhand des Namens der Quellspalte hinzufügen (häufigster Anwendungsfall) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | entfällt | High-Level-API, einzeilig. Verwenden Sie diese Option, sofern Sie keine `PivotField`-Referenz benötigen. |
| Ein Filterfeld hinzufügen, wenn Sie bereits über ein `PivotField`-Objekt verfügen | `pivotTable.getPageFields().add(pivotField)` | entfällt | Verwenden Sie diese Option, wenn das Feldobjekt an anderer Stelle abgerufen wurde oder wiederverwendet werden soll. |
| Auf ein einzelnes Filterelement filtern (Standardmodus) | `pivotField.currentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste an. |
| Alle Elemente anzeigen / Filter aufheben | `pivotField.currentPageItem` | auf `0x7FFD` setzen | Der Sonderwert `0x7FFD` (dezimal 32765) ist der Sentinel-Wert für „alle Elemente“. |
| Oberfläche für die Mehrfachauswahl in Excel aktivieren | `pivotField.isMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor Zuweisungen von `isHidden` wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste ausblenden bzw. anzeigen | `pivotItem.isHidden` | je Element festlegen | Mindestens ein Element muss sichtbar bleiben (`isHidden === false`). |

{{% alert color="primary" %}}
Beachten Sie bei der Konfiguration der Mehrfachauswahlfilterung stets die Sichtbarkeitsanforderung. Wenn jedes `PivotItem` in einem Filterfeld mit Mehrfachauswahl ausgeblendet ist, stürzt Excel beim Öffnen ab oder zeigt eine leere PivotTable an. Erstellen Sie Ihre Positivliste anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt. So können Ihre gespeicherten Arbeitsmappen auf jedem Computer zuverlässig geöffnet werden.
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}