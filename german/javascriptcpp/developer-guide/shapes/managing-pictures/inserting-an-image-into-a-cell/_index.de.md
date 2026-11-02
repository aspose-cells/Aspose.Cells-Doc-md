---
title: Einfügen eines Bildes in eine Zelle
linktitle: Einfügen eines Bildes in eine Zelle
description: Aspose.Cells for JavaScript via C++ ist eine Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Dieser Artikel erläutert, wie ein Bild genau an eine einzelne Zelle angepasst werden kann, indem entweder ein schwebendes Bild über der Zelle platziert oder das Bild direkt in die Zelle eingebettet wird.
keywords: Aspose.Cells, JavaScript-via-C++-Bibliothek, Tabellenkalkulation, Bild einfügen, Bild einbetten, Bild in einer Zelle, Bild an eine Zelle anpassen, Pictures, EmbeddedImage
type: docs
weight: 80
url: /de/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet zwei unterschiedliche Möglichkeiten, ein Bild einer einzelnen Zelle zuzuordnen. Ein schwebendes Bild ist eine Form auf der Zeichnungsebene des Arbeitsblatts, die einen Zellbereich visuell überlagert. Ein eingebettetes Bild wird hingegen in der Zelle selbst gespeichert und automatisch auf deren Anzeigebereich skaliert. Wählen Sie den Ansatz, der Ihren Layoutanforderungen am besten entspricht.
{{% /alert %}}

## **Einführung**
Das genaue Anpassen eines Bildes an eine einzelne Zelle ist eine häufige Anforderung beim Erstellen von Tabellenkalkulationen, die als visuelle Berichte, Produktkataloge, Mitarbeiterverzeichnisse, Dashboards oder Bestandslisten dienen. Anstatt ein Bild über mehrere Zellen zu strecken oder es auf einem Arbeitsblatt frei zu platzieren, benötigen Sie möglicherweise ein sauberes, an eine Zelle gebundenes Bild, das an der besitzenden Zelle ausgerichtet bleibt.
Aspose.Cells unterstützt dieses Szenario auf zwei sich ergänzende Arten:
- **Ansatz 1 — Ein schwebendes Bild über einer Zelle platzieren.** Fügen Sie dem Arbeitsblatt ein `Picture` hinzu, legen Sie seine Platzierung mit `picture.setPlacement(PlacementType.MoveAndSize)` fest und passen Sie die Ankerzellen über `picture.setUpperLeftRow()`, `picture.setUpperLeftColumn()`, `picture.setLowerRightRow()` und `picture.setLowerRightColumn()` so an, dass das Bild genau eine Zelle abdeckt.
- **Ansatz 2 — Ein Bild direkt in eine Zelle einbetten.** Weisen Sie der Zelle einen `Buffer` mit den Bilddaten über `cell.setEmbeddedImage(imageBuffer)` zu. Das Bild wird automatisch so skaliert, dass es in den Anzeigebereich der Zelle passt, und bleibt an die Zelle gebunden.
Im Folgenden werden beide Ansätze erläutert, die relevanten APIs erklärt und ihre Verwendung im Code gezeigt.

## **Ansatz 1: Ein Bild über einer Zelle platzieren**
Ein schwebendes Bild ist ein `Picture`-Objekt, das auf der Zeichnungsebene des Arbeitsblatts angezeigt wird. Obwohl es keiner einzelnen Zelle zugeordnet ist, ist es an einen Zellbereich verankert. Die Ankerzellen des Bildes — seine obere linke und untere rechte Ecke — bestimmen seine sichtbare Ausdehnung auf dem Arbeitsblatt. Standardmäßig erstreckt sich ein frisch hinzugefügtes Bild über mehrere Zellen.
Damit ein schwebendes Bild **genau eine Zelle** abdeckt, müssen Sie Folgendes tun:
1. Fügen Sie das Bild mit `worksheet.getPictures().add(row, column, imageBuffer)` hinzu, wobei `imageBuffer` ein `Buffer` mit den Bilddaten ist. Dadurch wird das neue Bild an der angegebenen Zelle verankert.
2. Legen Sie die vier Ankerwerte so fest, dass das Begrenzungsrechteck des Bildes mit der Zielzelle übereinstimmt.
3. Rufen Sie `picture.setPlacement(PlacementType.MoveAndSize)` auf, damit sich das Bild zusammen mit der zugrunde liegenden Zelle bewegt und seine Größe ändert, wenn der Benutzer die Spaltenbreite oder Zeilenhöhe ändert.

### **Das Bild an eine einzelne Zelle verankern**
Der Anker des Bildes wird durch vier nullbasierte Indexwerte definiert:
- `picture.getUpperLeftRow()` und `picture.setUpperLeftRow(value)` — der Zeilenindex der Oberkante des Bildes.
- `picture.getUpperLeftColumn()` und `picture.setUpperLeftColumn(value)` — der Spaltenindex der linken Kante des Bildes.
- `picture.getLowerRightRow()` und `picture.setLowerRightRow(value)` — der Zeilenindex der Unterkante des Bildes. Um die Unterkante des Bildes am unteren Rand der Zeile `r` auszurichten, setzen Sie diesen Wert auf `r + 1`.
- `picture.getLowerRightColumn()` und `picture.setLowerRightColumn(value)` — der Spaltenindex der rechten Kante des Bildes. Um die rechte Kante des Bildes am rechten Rand der Spalte `c` auszurichten, setzen Sie diesen Wert auf `c + 1`.

{{% alert color="primary" %}}
Zeilen- und Spaltenindizes in Aspose.Cells sind **nullbasiert**. Die Zelle C6 hat den Zeilenindex 5 und den Spaltenindex 2. Off-by-one-Fehler bei den Ankern für die untere rechte Ecke sind die häufigste Ursache dafür, dass Bilder scheinbar in eine benachbarte Zelle hineinreichen.
{{% /alert %}}

### **Platzierungsverhalten steuern**
`picture.getPlacement()` und `picture.setPlacement(value)` verwenden den Aufzählungstyp `PlacementType`, um zu steuern, wie sich das Bild verhält, wenn der Benutzer die Größe der darunterliegenden Zeile oder Spalte ändert. Der empfohlene Wert für ein Bild in einer einzelnen Zelle ist `PlacementType.MoveAndSize`. Dadurch werden Position und Größe des Bildes gemeinsam mit der zugrunde liegenden Zelle angepasst, sodass die exakte Anpassung erhalten bleibt.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` oder öffnen Sie eine vorhandene.
2. Greifen Sie über `workbook.getWorksheets().getAt(0)` auf das Ziel-Arbeitsblatt `Worksheet` zu.
3. Lesen Sie die Bilddatei mithilfe der Node.js-Funktion `fs.readFileSync` von der Festplatte in einen `Buffer` ein.
4. Rufen Sie `worksheet.getPictures().add(5, 2, imageBuffer)` auf, um ein an die Zelle C6 verankertes Bild hinzuzufügen. Die Methode gibt den Index des neuen Bildes in der `Pictures`-Sammlung zurück; verwenden Sie diesen Index, um das entsprechende `Picture` abzurufen.
5. Legen Sie die vier Ankerkoordinaten so fest, dass das Bild nur die Zelle C6 abdeckt: `picture.setUpperLeftRow(5)`, `picture.setUpperLeftColumn(2)`, `picture.setLowerRightRow(6)` und `picture.setLowerRightColumn(3)`.
6. Rufen Sie `picture.setPlacement(PlacementType.MoveAndSize)` auf, damit das Bild an C6 ausgerichtet bleibt, wenn die Größe der Spalte oder Zeile geändert wird.
7. Fügen Sie optional Beispieltext in umgebende Zellen ein, um zu veranschaulichen, dass nur die Zelle C6 das Bild enthält.
8. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code veranschaulicht den vollständigen Ansatz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
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
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
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

## **Ansatz 2: Ein Bild direkt in eine Zelle einbetten**
Aspose.Cells stellt außerdem einen einfacheren Mechanismus für zellengebundene Bilder bereit: die Methode `cell.setEmbeddedImage(imageBuffer)`. Mit dieser Methode werden Bilddaten direkt der Zelle zugeordnet, als wäre das Bild Inline-Inhalt.

### **Funktionsweise eingebetteter Bilder**
- Das Bild wird als Teil des Zelleninhalts und nicht als Form auf der Zeichnungsebene gespeichert.
- Das Bild wird automatisch so skaliert, dass es in den sichtbaren Bereich der Zelle passt. Ankerkoordinaten oder Platzierungseinstellungen sind nicht erforderlich.
- Die Zelle bleibt eine reguläre Zelle mit einer konkreten Adresse, die in Formeln referenziert, als Teil einer Zeile sortiert oder für andere Operationen auf Zellebene verwendet werden kann.
Damit ist `cell.setEmbeddedImage(imageBuffer)` die kürzeste Variante, wenn Sie lediglich ein Bild in dieser Zelle einfügen möchten.

### **Schritt-für-Schritt-Anleitung**
1. Erstellen Sie eine neue `Workbook` oder öffnen Sie eine vorhandene.
2. Greifen Sie über `workbook.getWorksheets().getAt(0)` auf das Ziel-Arbeitsblatt `Worksheet` zu.
3. Lesen Sie die Bilddatei mithilfe der Node.js-Funktion `fs.readFileSync` von der Festplatte in einen `Buffer` ein.
4. Rufen Sie eine Referenz auf die Zielzelle ab — entweder über `worksheet.getCells().get("C6")` oder `worksheet.getCells().get(5, 2)`.
5. Übergeben Sie den `Buffer` mithilfe von `cell.setEmbeddedImage(imageBuffer)` an die Zelle.
6. Passen Sie optional die Zeilenhöhe und Spaltenbreite der Zielzeile und Zielspalte an, um das eingebettete Bild deutlicher hervorzuheben.
7. Speichern Sie die Arbeitsmappe als `.xlsx`-Datei auf der Festplatte.
Der folgende Code veranschaulicht den vollständigen Ansatz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
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
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Zelle C6 abrufen
            const cell = worksheet.cells.get("C6");
            // Bilddatei in ein Byte-Array einlesen
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // Bild direkt in die Zelle einbetten
            cell.embeddedImage = imageData;
            // Optional die Zeilenhöhe und Spaltenbreite anpassen, damit das eingebettete Bild besser sichtbar ist
            worksheet.cells.setColumnWidth(2, 30); // Spalte C (Index 2)
            worksheet.cells.setRowHeight(5, 100); // Zeile 6 (Index 5)
            // Resultierende Arbeitsmappe als .xlsx-Datei speichern
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Auswahl des geeigneten Ansatzes**
Beide Ansätze führen zu einem Bild, das in eine einzelne Zelle passt, unterscheiden sich jedoch hinsichtlich der Speicherung und des Verhaltens des Bildes:
- **Verwenden Sie ein schwebendes Bild (Ansatz 1), wenn:**
  - Sie eine feinere Kontrolle über die Platzierung, die Ebenenreihenfolge oder die Ausrichtung relativ zu anderen Zeichnungsobjekten benötigen.
  - Sie möchten, dass sich das Bild wie eine Form verhält, die ausgewählt, neu angeordnet oder mit anderen Formen gruppiert werden kann.
  - Sie die Abwärtskompatibilität mit vorhandenem Code sicherstellen müssen, der bereits mit der über `worksheet.getPictures()` abgerufenen `Pictures`-Sammlung arbeitet.
  - Sie Ankerkoordinaten dynamisch basierend auf dem Layout des Arbeitsblatts berechnen müssen.
- **Verwenden Sie ein eingebettetes Bild (Ansatz 2), wenn:**
  - Sie ein Bild so einfach wie möglich in eine Zelle einfügen möchten.
  - Das Bild sich wie jeder andere Zelleninhalt mit der Zelle bewegen soll.

## Verwandte Artikel
- [Excel-Kamera in Aspose.Cells for JavaScript via C++](/cells/de/javascript-cpp/excel-camera/)
- [Filterfelder zu einer PivotTable in Aspose.Cells for JavaScript via C++ hinzufügen](/cells/de/javascript-cpp/add-page-field-in-pivot-table/)
- [Stile auf PivotTables in Aspose.Cells for JavaScript via C++ anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)
- [Sparkline in ein Bild und HTML in Aspose.Cells for JavaScript via C++ konvertieren](/cells/de/javascript-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript-cpp" >}}