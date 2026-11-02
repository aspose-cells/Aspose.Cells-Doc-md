---
title: Excel-Kamera in Aspose.Cells for JavaScript via C++
linktitle: Excel-Kamera
description: Erfahren Sie, wie Sie mit der Excel-Kamera in Aspose.Cells for JavaScript via C++ ein dynamisches Bild erstellen, das mit einem Zellbereich verknüpft ist, sich bei Änderungen der Quelldaten automatisch aktualisiert und die gesamte Formatierung des Quellbereichs beibehält.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Excel-Kamera, dynamisches Bild, verknüpftes Bild, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /de/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Die Excel-Kamera ist ein Arbeitsblattobjekt, das ein dynamisches Bild eines Zellbereichs rendert und auf der Zeichnungsebene wie ein gewöhnliches Bild schwebt. Aspose.Cells unterstützt zwei Erstellungsmodi: ein dynamisches Bild, das sich automatisch aktualisiert, sobald sich die Quelldaten ändern, sowie ein statisches Bild, das eine einmalige Momentaufnahme eines Bereichs erfasst. Dieser Artikel beschreibt beide Ansätze, damit Sie den passenden Ansatz für Ihr Layout auswählen können.

## Was ist die Excel-Kamera?
Die Excel-Kamera ist im Wesentlichen ein Bildobjekt, das auf der Zeichnungsebene des Arbeitsblatts an einer bestimmten Zeile und Spalte verankert ist. Anders als ein gewöhnliches eingefügtes Bild ist die Kamera über eine A1-artige Formel wie `"A1:F10"` mit einem Quellbereich verknüpft. Sobald sich eine beliebige Zelle in diesem Bereich ändert, wird das Kamerabild automatisch aktualisiert und gibt den neuen Inhalt wieder. Die Kamera bewahrt die vollständige Formatierung des Quellbereichs – Rahmen, Hintergrundfarben, Schriftarten und Zahlenformate –, sodass alles, was in den Zellen sichtbar ist, ebenfalls im Kamerabild erscheint. Dadurch ist die Kamera besonders für Dashboards, Zusammenfassungen, Seitenleisten und Berichtslayouts nützlich, in denen Sie eine sichtbare Vorschau auf einen an anderer Stelle im Arbeitsblatt liegenden Bereich anzeigen möchten, ohne zu scrollen oder Daten zu wiederholen. Es gelten jedoch zwei Einschränkungen: Sie müssen `updateSelectedValue()` vor dem Speichern der Arbeitsmappe aufrufen und die Datei in HTML oder PDF exportieren, da diese Formate auf den eingebetteten Bilddaten und nicht auf einer Neuberechnung in Echtzeit beruhen.

## Methode 1 – Dynamisches Kamerabild hinzufügen
Die dynamische Kamera ist der häufigste Ansatz und entspricht am ehesten dem integrierten Kamerawerkzeug von Excel. Sie funktioniert, indem zunächst ein leeres Bild hinzugefügt und diesem anschließend eine `formula` zugewiesen wird, die auf den Quellbereich verweist. Nach der Zuweisung der Formel aktualisiert der Aufruf von `updateSelectedValue()` die eingebetteten Bilddaten, sodass sie mit den Zellen des Quellbereichs übereinstimmen. Die Kamera wird nicht durch eine dedizierte Klasse implementiert, sondern vollständig auf Basis des standardmäßigen `Picture`-Typs umgesetzt.
Die wichtigsten APIs sind:
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` – fügt ein Bild hinzu, das an der angegebenen Zeile und Spalte verankert ist. Die Übergabe von `null` als Bildparameter erzeugt ein leeres Bild, das als Platzhalter für eine dynamische Kamera dient. Die Methode gibt den Index des neuen Bildes zurück.
- `worksheet.getPictures().get(index)` – ruft ein bestimmtes `Picture` aus der Sammlung ab.
- `picture.formula` – eine Zeichenfolgeeigenschaft, die den A1-artigen Verweis auf den Quellbereich enthält, den die Kamera abbildet, beispielsweise `"A1:F10"`.
- `picture.updateSelectedValue()` – eine Methode ohne Rückgabewert, die die eingebetteten Bilddaten aus den durch `formula` referenzierten Zellen aktualisiert.

{{% alert color="primary" %}}
`updateSelectedValue()` MUSS vor dem Speichern aufgerufen werden, wenn die Ausgabe HTML oder PDF ist; andernfalls enthält die exportierte Datei keine Bilddaten, und die Kamera erscheint in der gerenderten Ausgabe als leeres Bild.
Der folgende Code erstellt eine Arbeitsmappe, fügt ein leeres Bild ein, das in Zeile 10 und Spalte 6 verankert ist, verknüpft es über die Eigenschaft `formula` mit dem Quellbereich `A1:F10`, aktualisiert die eingebetteten Bilddaten und speichert die Arbeitsmappe.
{{% /alert %}}

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
            worksheet.name = "CameraDemo";
            // Dynamische Kamera: Ein leeres Bild hinzufügen, über Formula mit A1:F10 verknüpfen und anschließend aktualisieren
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Methode 2 – Statisches Kamerabild hinzufügen
Die statische Kamera ist im Wesentlichen eine einmalig gerenderte Vorschau eines Zellbereichs. Statt eine Live-Verknüpfung beizubehalten, rendern Sie den Bereich einmal in Bildbytes, fassen Sie diese Bytes in einem `Buffer` zusammen und fügen Sie sie als gewöhnliches Bild hinzu. Der Bildinhalt bleibt ab dem Erstellungszeitpunkt unverändert und wird nicht automatisch aktualisiert, wenn sich die Quellzellen ändern.
Die wichtigsten APIs sind:
- `cells.createRange(address)` – erstellt ein `Range`-Objekt aus einer A1-artigen Adresse wie `"A1:F10"`.
- `range.toImage(options)` – rendert den Bereich in Bildbytes. Wenn `null` übergeben wird, werden die Standardoptionen für die Darstellung verwendet; Überladungen ermöglichen eine genauere Steuerung der Ausgabe.
- `Buffer.from(imageBytes)` – fasst die gerenderten Bildbytes in einem `Buffer` zusammen, der an `worksheet.getPictures().add` übergeben werden kann.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` – fügt das an der angegebenen Zeile und Spalte verankerte Bild hinzu; diesmal wird der durch die Darstellung erzeugte `Buffer` übergeben.
Der folgende Code erstellt eine Arbeitsmappe, erzeugt einen `Range` für `A1:F10`, rendert ihn mit `range.toImage(null)` in Bildbytes, fasst die Bytes in einem `Buffer` zusammen, fügt das in Zeile 10 und Spalte 6 verankerte Bild hinzu und speichert die Arbeitsmappe.

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
            worksheet.name = "CameraDemo";
            // Statische Kamera: Bereich erstellen, in Bytes rendern, in einen MemoryStream einschließen und als Bild hinzufügen
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Auswahl zwischen dynamischer und statischer Kamera
- **Dynamische Kamera:** wird bei jeder Neuberechnung aktualisiert, unterstützt nach einem Aufruf von `updateSelectedValue()` den Export als HTML und PDF und bewahrt die dynamische Verknüpfung während der gesamten Lebensdauer der Datei.
- **Statische Kamera:** eine einmalige Darstellung, die nie aktualisiert wird und nützlich ist, wenn Sie zum Erstellungszeitpunkt einen festen visuellen Schnappschuss einbetten möchten, anstatt einer dynamischen Spiegelung der Daten.
Aspose.Cells unterstützt sowohl eine dynamische, automatisch aktualisierende Kamera auf Basis von `picture.formula` und `updateSelectedValue()` als auch eine statische Kamera für eine einmalige Darstellung auf Basis von `range.toImage` und `Buffer`. Wählen Sie den dynamischen Ansatz, wenn die Ausgabe mit den Quellzellen synchron bleiben muss, und den statischen Ansatz, wenn Sie lediglich zum Erstellungszeitpunkt einen festen visuellen Schnappschuss benötigen.

## Verwandte Artikel
- [Sparkline in Aspose.Cells for JavaScript via C++ in ein Bild und HTML konvertieren](/cells/de/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Filterfelder zu einer PivotTable in Aspose.Cells for JavaScript via C++ hinzufügen](/cells/de/javascript-cpp/add-page-field-in-pivot-table/)
- [Stile auf PivotTables in Aspose.Cells for JavaScript via C++ anwenden](/cells/de/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}