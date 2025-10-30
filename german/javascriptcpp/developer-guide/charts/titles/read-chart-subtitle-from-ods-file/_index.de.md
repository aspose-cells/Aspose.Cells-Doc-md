---
title: Diagrammtitel aus ODS Datei mit JavaScript via C++ lesen
linktitle: Lese Diagramm Untertitel aus ODS Datei
description: Lernen Sie, wie Sie mit Aspose.Cells for JavaScript via C++ den Diagrammtitel aus einer OpenDocument Spreadsheet (ODS) Datei lesen. Unser Leitfaden zeigt, wie man den Titel eines Diagramms extrahiert und darauf zugreift für weitere Analysen oder Anzeige.
keywords: Aspose.Cells for JavaScript via C++, Diagrammtitel lesen, OpenDocument Spreadsheet, ODS Datei, Diagrammauszug, Datenanalyse.
type: docs
weight: 160
url: /de/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **Diagramm-Untertitel aus ODS-Datei lesen**

Aspose.Cells ermöglicht es Ihnen, Diagrammtitel in ODS-Dateien mit der Eigenschaft [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) zu lesen. Der folgende Beispielcode lädt die [Beispiel-ODS-Datei](89620481.ods) und liest den Diagrammtitel mit der Eigenschaft [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) und gibt ihn im Konsolenfenster aus. Bitte beachten Sie die Konsolenausgabe des unten angegebenen Codes zur Referenz.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
