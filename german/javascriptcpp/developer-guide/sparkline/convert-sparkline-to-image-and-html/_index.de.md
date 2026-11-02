---
title: Sparkline mit Aspose.Cells for JavaScript via C++ in ein Bild und HTML konvertieren
linktitle: Sparkline mit Aspose.Cells for JavaScript via C++ in ein Bild und HTML konvertieren
description: Erfahren Sie, wie Sie mit Aspose.Cells Sparklines als eigenständige Bilder zum Einbetten in Zellen rendern und Arbeitsblätter mit Sparklines mithilfe von HtmlSaveOptions in HTML exportieren.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Sparkline, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, Sparkline rendern, Sparkline in ein Bild konvertieren, Sparkline in HTML exportieren
type: docs
weight: 120
url: /de/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines sind Miniaturdiagramme, die in Zellen eines Arbeitsblatts platziert werden. Mit Aspose.Cells können Sie jede Sparkline als eigenständiges Bild extrahieren (zum Einbetten in eine andere Zelle oder einen externen Bericht) und außerdem das gesamte Arbeitsblatt mit Sparklines für die browserbasierte Verteilung in HTML exportieren. Die in diesem Artikel verwendete Eigenschaft `cell.embeddedImage` ist in **Aspose.Cells 26.5 und später** verfügbar.
{{% /alert %}}

## **Einleitung**
Sparklines bieten eine kompakte Möglichkeit, Trends direkt in einem Arbeitsblatt zu visualisieren. Excel-Benutzer sehen sie normalerweise direkt an Ort und Stelle, doch in vielen realen Szenarien muss eine Sparkline aus der Zelle herausgelöst werden – beispielsweise, um als statisches Bild in eine andere Zelle eingebettet, einer automatisierten E-Mail beigefügt oder als Teil eines im Web veröffentlichten HTML-Berichts gerendert zu werden.
Aspose.Cells unterstützt beide Vorgänge. Die Methode `sparkline.toImage` rendert eine einzelne Sparkline als `Buffer`, und die resultierenden Bytes können `cell.embeddedImage` zugewiesen werden, sodass das Bild in einer einzelnen Zelle der Arbeitsmappe gespeichert ist. Mit `HtmlSaveOptions` können Sie separat die gesamte Arbeitsmappe – einschließlich aller Sparklines – in eine eigenständige HTML-Datei konvertieren. Dieser Artikel beschreibt beide Arbeitsabläufe umfassend.

## **Arbeitsablauf 1 – Sparklines als Bilder rendern und in Zellen einbetten**
In diesem Arbeitsablauf erstellen Sie ein Arbeitsblatt mit einem kleinen Bereich von Quellwerten, ordnen diesem Bereich drei verschiedene Sparkline-Gruppen (Line, Column und Stacked (Gewinn/Verlust)) zu, rendern jede Gruppe als PNG und schreiben die PNG-Bytes in benachbarte Zellen als eingebettete Bilder. Das Endergebnis ist eine einzelne `.xlsx`-Datei, die sowohl die nativen Sparklines als auch ihre entsprechenden PNG-Darstellungen enthält.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie ein neues `Workbook` und rufen Sie eine Referenz auf das erste `Worksheet` ab.
2. Füllen Sie die Zellen `A1` bis `E1` mit fünf numerischen Beispielwerten (z. B. täglichen Verkaufszahlen oder Temperaturmessungen).
3. Fügen Sie dem Arbeitsblatt drei `SparklineGroup`-Objekte hinzu, indem Sie `worksheet.getSparklineGroups().add(...)` aufrufen:
   - Eine `SparklineType.Line`-Gruppe, die in `F1` verankert ist, mit dem Datenbereich `A1:E1`.
   - Eine `SparklineType.Column`-Gruppe, die in `G1` verankert ist, mit dem Datenbereich `A1:E1`.
   - Eine `SparklineType.Stacked`-Gruppe (Gewinn/Verlust), die in `H1` verankert ist, mit dem Datenbereich `A1:E1`.
4. Erstellen Sie eine Instanz von `ImageOrPrintOptions` und legen Sie die Eigenschaft `imageType` auf `ImageType.Png` fest, damit jede Sparkline als PNG-Bild gerendert wird.
5. Speichern Sie die Arbeitsmappe als `output_with_sparklines.xlsx`.

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
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Eine neue Arbeitsmappe erstellen und auf das erste Arbeitsblatt zugreifen
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Beispieldaten in den Zellen A1:E1 einfüllen
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // Eine Sparkline-Gruppe vom Typ Linie hinzufügen, die in F1 verankert ist (Spalte 5, Zeile 0)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // Eine Sparkline-Gruppe vom Typ Säule hinzufügen, die in G1 verankert ist (Spalte 6, Zeile 0)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // Eine Gewinn/Verlust-Sparkline-Gruppe (gestapelt) hinzufügen, die in H1 verankert ist (Spalte 7, Zeile 0)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // Bildoptionen für die PNG-Ausgabe konfigurieren
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Die Liniendiagramm-Sparkline in ein Bild umwandeln und in Zelle F2 einbetten
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Die Säulendiagramm-Sparkline in ein Bild umwandeln und in Zelle G2 einbetten
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Die Gewinn/Verlust-Sparkline in ein Bild umwandeln und in Zelle H2 einbetten
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Arbeitsmappe auf der Festplatte speichern
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Der obige Code erzeugt eine Arbeitsmappe, in der jede visuelle Darstellung einer Sparkline in zwei Formen vorliegt: als native Sparkline, die in Zeile 1 verankert ist, und als statisches PNG-Bild, das direkt in eine benachbarte Zelle in Zeile 2 eingebettet ist. Da die Bilder in der Datei selbst gespeichert sind, bleibt die Arbeitsmappe ein einzelnes, eigenständiges Artefakt, das per E-Mail versendet oder archiviert werden kann, ohne dass die Verweise auf eingebettete Bilder verloren gehen.

{{% alert color="primary" %}}
Da jede Sparkline-Gruppe in einer einzelnen Zelle verankert ist, können Sie sie über den Indexer `group.getSparklines()[0]` adressieren, statt die Auflistung zu durchlaufen. So bleibt der Rendering-Code kurz und folgt dem typischen Muster „eine Sparkline pro Ankerzelle“. Das Speichern der Bild-Bytes über `cell.embeddedImage` erfordert Aspose.Cells 26.5 oder höher.
{{% /alert %}}

## **Arbeitsablauf 2 – Das Arbeitsblatt mit Sparklines in HTML exportieren**
Sobald die Arbeitsmappe native Sparklines (und optional eingebettete PNG-Darstellungen) enthält, kann das gesamte Arbeitsblatt durch Speichern als HTML im Web veröffentlicht werden. Mit der Klasse `HtmlSaveOptions` können Sie diesen Export steuern. In diesem Arbeitsablauf wird die in Arbeitsablauf 1 erzeugte Datei `output_with_sparklines.xlsx` erneut verwendet und in ein übersichtliches, einseitiges HTML-Dokument konvertiert.

### **Schritt-für-Schritt-Anleitung**
1. Stellen Sie sicher, dass die in Arbeitsablauf 1 erzeugte Datei `output_with_sparklines.xlsx` im Arbeitsverzeichnis auf dem Datenträger vorhanden ist.
2. Laden Sie diese Datei in eine neue `Workbook`-Instanz.
3. Instanziieren Sie `HtmlSaveOptions` und legen Sie die Eigenschaft `exportActiveWorksheetOnly` auf `true` fest, damit die resultierende HTML-Datei nur das aktive Arbeitsblatt und nicht die gesamte Arbeitsmappe enthält.
4. Rufen Sie `workbook.save("sparklines.html", htmlOptions)` auf, um die HTML-Ausgabe auf den Datenträger zu schreiben.

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
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

Der obige Code übernimmt die Arbeitsmappe mit Sparklines aus Arbeitsablauf 1 und wandelt sie in eine portable HTML-Datei um. Die Sparkline-Gruppen werden als Inline-Bilder in der erzeugten HTML-Tabelle gerendert, sodass Endbenutzer die Trends in jedem modernen Browser ansehen können, ohne Excel installieren zu müssen. Wenn Sie `exportActiveWorksheetOnly` auf `true` festlegen, verhindern Sie, dass versehentlich ausgeblendete Blätter oder Hilfsdaten veröffentlicht werden; exportiert wird nur das aktuell für den Benutzer sichtbare Arbeitsblatt.

{{% alert color="primary" %}}
Die Klasse `HtmlSaveOptions` bietet zusätzliche Eigenschaften zur Feinabstimmung der Ausgabe, etwa `exportHiddenWorksheet`, `exportImagesAsBase64` und `encoding`. Passen Sie diese Eigenschaften nach Bedarf an die Zielumgebung an.
{{% /alert %}}

## **API-Zusammenfassung**
Die obigen Arbeitsabläufe verwenden eine kleine Anzahl von Aspose.Cells-APIs, die gemeinsam eingesetzt werden.
- `SparklineGroup` und die Zugriffsfunktion für die Sammlung `worksheet.getSparklineGroups()` werden verwendet, um den Typ (Line, Column, Stacked), den Datenbereich und die Ankerzelle für jede Sparkline-Gruppe festzulegen. In diesem Artikel ist jede Gruppe in einer einzelnen Zelle verankert, sodass sie über `worksheet.getSparklineGroups()[i]` abgerufen wird.
- `Sparkline` und der Indexer `group.getSparklines()[0]` geben die einzelne Sparkline innerhalb einer Gruppe zurück. Da jede Gruppe im Beispiel genau eine Sparkline enthält, ist keine Iterationsschleife erforderlich.
- `sparkline.toImage(imageOrPrintOptions)` ist die Rendering-Methode, die ein Bild der Sparkline als `Buffer` zurückgibt. Die zurückgegebenen Bytes können direkt `cell.embeddedImage` zugewiesen werden.
- `HtmlSaveOptions.exportActiveWorksheetOnly` (ein boolescher Wert) beschränkt den HTML-Export auf das aktive Arbeitsblatt. Dabei handelt es sich um eine der am häufigsten verwendeten Eigenschaften von `HtmlSaveOptions` bei der Erstellung einseitiger Berichte.
- `ImageOrPrintOptions.imageType` wählt das Bildformat (z. B. `ImageType.Png`), das beim Rendern mit `toImage` und beim Drucken von Arbeitsblättern in Bildern verwendet wird.

{{< app/cells/assistant language="javascript-cpp" >}}