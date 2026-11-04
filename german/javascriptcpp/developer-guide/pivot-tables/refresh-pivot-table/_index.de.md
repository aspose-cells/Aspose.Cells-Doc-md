---
title: PivotTables und PivotCaches in Aspose.Cells for JavaScript via C++ aktualisieren
linktitle: PivotTables und PivotCaches
description: Erfahren Sie, wie Sie PivotTables in Aspose.Cells for JavaScript via C++ mithilfe der API zur Pivot-Aktualisierung ab Version v26.7 aktualisieren. Dieser Artikel behandelt workbook.refreshAll, worksheet.refreshPivotTables, pivotCache.refresh, pivotTable.calculateData und pivotCache.getPivotTables anhand praktischer Codebeispiele.
keywords: Aspose.Cells, JavaScript via C++, PivotTable, aktualisieren, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /de/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet eine mehrstufige Aktualisierungs-API, mit der Sie Pivot-Daten in vier verschiedenen Umfängen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen PivotTable. Mit **Aspose.Cells for JavaScript via C++ v26.7** ist die frühere Methode `pivotTable.refreshData()` als veraltet markiert und sollte durch die effizienteren APIs ersetzt werden, die den PivotCache berücksichtigen und in diesem Artikel beschrieben werden.
{{% /alert %}}

## Einführung
Das Aktualisieren einer PivotTable ist selten ein einzelner Vorgang. Hinter den Kulissen verwaltet Aspose.Cells eine mehrstufige Datenkette, die die ursprünglichen Quelldaten mit den im Arbeitsblatt angezeigten Werten verbindet. Das Verständnis dieser Kette ist entscheidend, um in jeder Situation die richtige Aktualisierungs-API auszuwählen.
Die vierstufige Datenkette umfasst:
1. **Datenquelle** – die ursprünglichen Arbeitsblattbereiche, die Datenbankabfrage oder den Konsolidierungsbereich, in denen die Rohwerte vorliegen.
2. **PivotCache** – die im Arbeitsspeicher gehaltene Momentaufnahme der Quelldaten. Jede PivotTable basiert auf einem `PivotCache`; in diesem werden alle Daten gesammelt und aggregiert.
3. **PivotTable** – das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *ausschließlich* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** – die Arbeitsblattzellen, die von `getCells()` zurückgegeben werden und in denen die berechneten Werte und Formatierungen der PivotTable dargestellt werden.

{{% alert color="primary" %}}
`pivotCache.getSourceType()` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `pivotCache.refresh()` nur die Quellentypen **`SHEET`** und **`CONSOLIDATION`** – also Daten, die in Arbeitsblattbereichen gespeichert sind. Externe Quellen wie Datenbanken oder externe Verbindungen können noch nicht über die Cache-API aktualisiert werden.
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`pivotTable.calculateData()`** – berechnet die Darstellung einer einzelnen `PivotTable` anhand der bereits zwischengespeicherten Daten neu, ohne Daten aus der Datenquelle erneut abzurufen.
Alle Szenarien in diesem Artikel verwenden Quellendaten aus Arbeitsblattzellen. Der Quellentyp ist daher `SHEET`, und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
{{% /alert %}}

## Schnellstart
Wenn Sie nur den kürzestmöglichen Code benötigen, der alle PivotTables in der Arbeitsmappe aktualisiert, genügt ein einziger Aufruf:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

Alles Weitere in diesem Artikel erläutert, wann Sie stattdessen eine gezieltere API auswählen sollten.

## Erforderliche Importe
Alle JavaScript-Beispiele in diesem Artikel beginnen mit dem folgenden Modulimport, da die Pivot-Typen über den namespace `Aspose.Cells.Pivot` bereitgestellt werden:
- `const Aspose = require('aspose.cells');`

## Alle PivotTables in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder PivotCache und jede PivotTable in der Arbeitsmappe die aktuellen Quelldaten widerspiegelt, ist `workbook.refreshAll()` die einfachste und umfassendste API. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe – er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet anschließend jede abhängige `PivotTable` neu. Dies ist die empfohlene Vorgehensweise für allgemeine Aktualisierungen des gesamten Dokuments, wenn die Leistung nicht entscheidend ist.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Quellbereich für die Spalten `Fruit`, `Year` und `Amount`, erstellt eine PivotTable, ändert einige Quellwerte und verwendet anschließend `refreshAll()`, um alles mit einem einzigen Aufruf auf den neuesten Stand zu bringen.

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
            const cells = worksheet.cells;
            // Kopfzeile in die Zellen A1:C1 schreiben
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Datenzeilen in die Zellen A2:C9 schreiben (8 Zeilen mit Fruchtdaten für 2020 und 2021)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // Pivot-Tabelle hinzufügen: Quellbereich "A1:C9", ZieldZelle "E3"
            const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
            // Pivot-Felder zuweisen: Fruit zu Zeilen, Year zu Spalten, Amount zu Daten
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Mehrere Amount-Werte in den Quelldaten ändern, um Änderungen zu simulieren
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // Alle Pivot-Tabellen/Pivot-Caches in der Arbeitsmappe aktualisieren
            workbook.refreshAll();
            // Arbeitsmappe speichern
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Alle PivotTables in einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die PivotTables eines bestimmten Arbeitsblatts aktualisieren – beispielsweise, wenn die PivotTables in anderen Arbeitsblättern bekanntermaßen nicht damit zusammenhängen und nicht verändert werden sollen. Für diesen Fall stellt Aspose.Cells die Methode `worksheet.refreshPivotTables()` bereit, deren Aktualisierungsbereich auf eine einzelne `Worksheet`-Instanz beschränkt ist.

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
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
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

## Eine einzelne PivotTable aktualisieren
Wenn Sie eine einzelne PivotTable detailliert steuern möchten, bietet die cachebasierte API zwei Optionen. Die Wahl hängt davon ab, was sich tatsächlich geändert hat: die zugrunde liegenden Quelldaten oder lediglich die Ansichts- und Layouteinstellungen der PivotTable selbst.

### Quelldaten geändert — `pivotCache.refresh()` verwenden
Wenn sich die zugrunde liegenden Quelldaten geändert haben, ist `pivotTable.getPivotCache().refresh()` der richtige Einstiegspunkt. Dieser Aufruf liest die Quelldaten erneut in den PivotCache ein und berechnet anschließend jede `PivotTable` neu, die von diesem PivotCache abhängt.

### Nur Ansicht/Layout geändert — `pivotTable.calculateData()` verwenden
Wenn sich die Quelldaten *nicht* geändert haben, sondern lediglich die Ansicht oder die Layouteinstellungen der PivotTable geändert wurden – beispielsweise ein Feld in einen anderen Bereich verschoben oder eine Einstellung zum Aktualisieren beim Öffnen umgeschaltet wurde –, ist es nicht erforderlich, erneut auf die Datenquelle zuzugreifen. Der PivotCache enthält bereits die richtigen Daten; nur die dargestellte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.calculateData()` die richtige Wahl.
Das folgende Beispiel ändert eine Eigenschaft, die nicht die Datenquelle betrifft, und ruft anschließend `calculateData()` auf, um die PivotTable aus dem vorhandenen PivotCache neu darzustellen.

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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Kopfzeile für Obst / Jahr / Menge schreiben
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // 8 Datenzeilen schreiben (Zeilen 2–9, passend zum Quellbereich A1:C9)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // Eine Pivot-Tabelle hinzufügen, die in der Zielzelle E3 platziert wird und ihre Daten aus A1:C9 bezieht
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                // Felder zuweisen: Fruit der Zeile, Year der Spalte, Amount den Daten
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // Eine Ansichts-/Layouteigenschaft ändern – dies ist eine reine Darstellungsänderung,
                // daher müssen die Quelldaten nicht über PivotCache.Refresh() erneut gelesen werden.
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Formatierung) aus den
                // bereits im PivotCache gespeicherten Daten neu. Da sich die Quelldaten nicht geändert haben,
                // wird kein Rückgriff auf die Quelle durchgeführt – nur die zwischengespeicherten Werte werden
                // in die Zellen des Arbeitsblatts neu berechnet.
                pivotTable.calculateData();
                // Arbeitsmappe auf der Festplatte speichern
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Eine Arbeitsmappe enthält häufig viele PivotTables, die alle auf einem gemeinsamen PivotCache basieren. Um sie aufzulisten – etwa vor einer Stapelaktualisierung oder zur Diagnose der Auswirkungen eines gemeinsamen PivotCache –, verwenden Sie `pivotCache.getPivotTables()`. Diese Methode gibt die Auflistung aller PivotTables zurück, die vom angegebenen PivotCache abhängen.

## Migration von der veralteten `pivotTable.refreshData()`
Vor Aspose.Cells for JavaScript via C++ v26.7 war die Standardmethode zum Aktualisieren einer PivotTable der Aufruf von `pivotTable.refreshData()` für jede PivotTable einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen APIs ersetzt werden, die den PivotCache berücksichtigen.
Es gibt zwei Gründe, weshalb sich der tabellenweise Einsatz von `refreshData()` in Arbeitsmappen der Praxis als problematisch erweist:
- Bei jedem Aufruf werden die Daten erneut aus der Quelle abgerufen, selbst wenn sich die Quelle nicht geändert hat.
Die empfohlenen Ersetzungen sind die oben beschriebenen cachebasierten APIs.
Das folgende Beispiel veranschaulicht das neue effiziente Muster für Arbeitsmappen mit mehreren PivotTables, die einen gemeinsamen PivotCache teilen.

## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und erläutert, wann Sie die jeweilige API auswählen sollten.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `workbook.refreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur PivotTables in einem einzelnen Arbeitsblatt aktualisieren | `worksheet.refreshPivotTables()` | Auf ein einzelnes Arbeitsblatt begrenzt. |
| Quelldaten für einen Cache geändert | `pivotTable.getPivotCache().refresh()` | Aktualisiert ALLE PivotTables, die diesen gemeinsamen PivotCache verwenden. |
| Nur Ansicht-/Layouteinstellungen geändert | `pivotTable.calculateData()` | Vermeidet den unnötigen Rückgriff auf die Quelle. |
| Alle PivotTables für einen gemeinsamen PivotCache auflisten | `pivotCache.getPivotTables()` | Dient zum Auflisten vor einer Massenaktualisierung. |
In der Praxis sollten Sie cachebasierte APIs der veralteten tabellenweisen `refreshData()`-Methode vorziehen. Sie berücksichtigen gemeinsame PivotCaches, vermeiden redundante Datenabrufe aus der Quelle und ermöglichen es Ihnen, den kleinsten Umfang auszuwählen, der Ihren Anforderungen an die Aktualisierung genügt.

## Häufige Fehler
- **Vergessen, vor dem Speichern zu aktualisieren.** Eine PivotTable schreibt ihre dargestellten Werte erst dann in das Arbeitsblatt, wenn ihre Datenkette aktualisiert wurde. Wenn Sie Quellzellen ändern, rufen Sie `pivotCache.refresh()` (oder `workbook.refreshAll()`) vor `workbook.save()` auf. Andernfalls enthält die gespeicherte Datei weiterhin die alten aggregierten Werte.
- **Aufruf der veralteten `refreshData()` pro Tabelle.** In v26.7 ist `pivotTable.refreshData()` als veraltet markiert und ruft die Quelle bei jedem Aufruf erneut ab. Bei mehreren PivotTables mit gemeinsamem PivotCache bedeutet dies N redundante Datenabrufe aus der Quelle. Ersetzen Sie dies durch einen einzigen Aufruf von `pivotCache.refresh()`, gefolgt von `pivotTable.calculateData()` pro Tabelle.
- **Aktualisierung, obwohl sich nur das Layout geändert hat.** Wenn Sie lediglich die Ansicht einer PivotTable geändert haben (Spaltenreihenfolge, `getConsolidationFunction()` usw.), ohne die Quelldaten zu ändern, ist `pivotCache.refresh()` unnötig und langsam. Rufen Sie `pivotTable.calculateData()` auf, um die PivotTable aus dem vorhandenen PivotCache neu darzustellen.
- **Externe Quelle wird von `pivotCache.refresh()` nicht unterstützt.** Wenn die Quelle der PivotTable aus einer externen Verbindung stammt (Datenbank, OLAP-Cube usw.), kann `pivotCache.refresh()` sie in v26.7 nicht aktualisieren – derzeit werden nur die Quellentypen `SHEET` und `CONSOLIDATION` unterstützt. Für externe Quellen öffnen Sie die Arbeitsmappe erneut oder erstellen Sie den PivotCache aus der Quelle neu.

{{< app/cells/assistant language="javascript-cpp" >}}