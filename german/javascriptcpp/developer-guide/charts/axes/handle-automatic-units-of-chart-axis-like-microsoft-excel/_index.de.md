---
title: Automatische Einheiten der Diagrammarchse wie Microsoft Excel mit JavaScript via C++ verwalten
linktitle: Behandeln von automatischen Einheiten der Diagrammachse wie Microsoft Excel
description: Lernen Sie, wie man automatische Einheiten auf Diagrammarchsen in Aspose.Cells for JavaScript mit C++ verwaltet. Unser Leitfaden zeigt, wie Sie automatische Einheiten auf einer Diagrammarchse konfigurieren und anpassen, einschließlich der Anzeige im wissenschaftlichen Format und der Skalierung.
keywords: Aspose.Cells for JavaScript mit C++, Diagrammarchsen, automatische Einheiten, Microsoft Excel, Konfiguration, Anpassung, wissenschaftliche Notation, Skalierung.
type: docs
weight: 120
url: /de/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Mögliche Verwendungsszenarien**  
Frühere Versionen von Aspose.Cells for JavaScript mit C++ konnten die automatischen Einheiten der Diagrammarchse beim Rendern in Bild oder PDF nicht richtig verarbeiten. Jetzt unterstützt Aspose.Cells for JavaScript mit C++ die Handhabung der automatischen Einheiten der Diagrammarchse. Es gibt keine Code-Änderungen. Konvertieren Sie einfach Ihr Diagramm in ein Bild oder PDF, und die Achse wird genau wie bei Microsoft Excel gerendert.  

## **Behandeln Sie automatische Einheiten der Diagrammachse wie Microsoft Excel**  
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767755.xlsx) und erstellt das [Ausgabepdf-Diagramm](61767752.pdf). Der Screenshot zeigt die automatischen Einheiten der Diagrammarchse in roten Rechtecken und vergleicht die Beispiel-Excel-Datei mit dem output PDF-Diagramm. Beide sind exakt gleich.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Beispielcode**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
