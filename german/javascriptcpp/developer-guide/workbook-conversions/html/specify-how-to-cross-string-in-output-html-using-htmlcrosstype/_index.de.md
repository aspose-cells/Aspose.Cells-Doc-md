---
title: Geben Sie an, wie Sie in der Ausgabe HTML die Zeichenfolge mit HtmlCrossType unter Verwendung von JavaScript über C++ kreuzen
linktitle: Geben Sie an, wie Zeichenkette in der Ausgabe HTML mit HtmlCrossType geschnitten werden soll
type: docs
weight: 140
url: /de/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Erfahren Sie, wie Sie die Textüberlaufsteuerung in HTML durch Angabe von HtmlCrossType in Aspose.Cells for JavaScript über C++ vornehmen.
---

## **Mögliche Verwendungsszenarien**

Wenn eine Zelle Text oder eine Zeichenkette enthält, die größer ist als die Breite der Zelle, läuft die Zeichenkette über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie diesen Überlauf steuern, indem Sie den Kreuztyp mit der [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)-Aufzählung angeben. Es hat folgende Werte:

- **HtmlCrossType.Default**: Anzeige wie MS Excel; hängt von der nächsten Zelle ab. Wenn die nächste Zelle null ist, läuft die Zeichenkette über oder wird abgeschnitten.

- **HtmlCrossType.MSExport**: Zeigen Sie den String wie MS Excel, der HTML exportiert.

- **HtmlCrossType.Cross**: HTML-Kreuzzeichen anzeigen; die Leistung beim Erstellen großer HTML-Dateien ist mehr als zehnmal schneller als das Einstellen auf Default oder FitToCell.

- **HtmlCrossType.FitToCell**: Nur innerhalb der Breite der Zelle anzeigen.

## **Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740732.xlsx) und speichert sie im HTML-Format, indem verschiedene [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) angegeben werden. Bitte laden Sie die [Ausgabedateien HTML](51740734.zip) herunter, die mit diesem Code generiert wurden. Die Beispiel-Excel-Datei enthält das Bild mit rotem Rahmen, wie in diesem Screenshot gezeigt, der die Wirkung der [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)-Werte auf das Ausgabe-HTML zeigt.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
