---
title: Formatcode der Werte der Diagrammserie mit JavaScript über C++ festlegen
description: Lernen Sie, wie Sie den Werte Formatcode der Diagrammserie in Aspose.Cells for JavaScript via C++ einstellen. Dieser Leitfaden hilft Ihnen, Ihre Diagrammdaten mit dem entsprechenden Formatcode zu formatieren, um Ihre Daten genau und professionell darzustellen.
keywords: Aspose.Cells for JavaScript via C++, Diagrammserie, Werte Formatcode, Formatierung, Datenpräsentation, Genauigkeit, Professionalität.
linktitle: Zahlenformat
type: docs
weight: 100
url: /de/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **Mögliche Verwendungsszenarien**
 Sie können den Werte-Formatcode der Diagrammserie mit der [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) Eigenschaft festlegen. Diese Eigenschaft ist nicht nur nützlich für Serien, die auf dem Bereich innerhalb des Arbeitsblatts basieren, sondern funktioniert auch gut für Serien, die mit einem Werte-Array erstellt wurden.

## **Setzen des Werteformatcodes der Diagrammserie**
Der folgende Beispielcode fügt einer leeren Diagrammserie, die vorher keine Serie hatte, eine Serie hinzu. Dabei wird die Serie mit einem Werte-Array hinzugefügt. Nach dem Hinzufügen wird sie mit dem Code $#,##0 formatiert, indem die Eigenschaft [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) verwendet wird, und die Zahl 10000 wird in $10.000 umgewandelt. Der Screenshot zeigt die Wirkung des Codes auf die [Beispiel-Excel-Datei](51740712.xlsx) und die [Ausgabedatei](51740713.xlsx) nach der Ausführung.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Beispielcode**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
