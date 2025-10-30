---
title: Render Gradientfüllung für WordArt beim Konvertieren von Tabellen in HTML mit JavaScript über C++
linktitle: Verlaufsfüllung für den WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern
type: docs
weight: 90
url: /de/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Erfahren Sie, wie Sie eine Gradientfüllung für WordArt beim Konvertieren von Tabellen in HTML mit Aspose.Cells for JavaScript über C++ rendern.
---

## **Mögliche Verwendungsszenarien**  
Vor Aspose.Cells 17.1 rendert Aspose.Cells die Gradientfüllung von WordArt beim Konvertieren der Excel-Datei in HTML nicht. Seit der Version Aspose.Cells 17.1 wird die WordArt-Gradientfüllung unterstützt. Das folgende Screenshot vergleicht den Effekt der Gradientfüllung bei Umwandlung der Excel-Datei mit Aspose.Cells 17.1 und der älteren Version.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Verlaufsfüllung für den WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern**  
Der folgende Beispielcode konvertiert die [Quell-Excel](22774111.xlsx) in [Ausgabe-HTML](22774109.zip). Die Quelldatei enthält ein WordArt-Objekt mit Gradientfüllung, wie im oben stehenden Screenshot.  

## **Beispielcode**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
