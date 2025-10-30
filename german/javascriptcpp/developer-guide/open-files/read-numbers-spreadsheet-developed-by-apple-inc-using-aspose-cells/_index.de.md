---
title: Apple Inc. entwickelte Zahlen Tabellen mit Aspose.Cells for JavaScript über C++ lesen
linktitle: Zahlen Tabelle entwickelt von Apple Inc. unter Verwendung von Aspose.Cells
type: docs
weight: 140
url: /de/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Lernen Sie, wie Sie Zahlen Tabellen von Apple Inc. mit Aspose.Cells for JavaScript über C++ lesen. 
---

## **Mögliche Verwendungsszenarien**

Numbers ist eine Tabellenkalkulationsanwendung, entwickelt von Apple Inc. Aspose.Cells kann Numbers-Tabellen lesen, aber das Schreiben in sie wird nicht unterstützt. Es kann Daten, Formatierungen und Formeln aus Numbers-Tabellen lesen.

## ** Zahlen-Tabellen von Apple Inc. mit Aspose.Cells for JavaScript über C++ lesen**

Der folgende Beispielcode lädt die [Beispiel Numbers Tabelle](sampleNumbersByAppleInc.numbers) und konvertiert sie in [Ausgabe PDF-Format](outputNumbersByAppleInc.pdf). Sie müssen die [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions)-Klasse verwenden und [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) als Parameter im Konstruktor angeben, um sie erfolgreich zu laden. Laden Sie beide von den angegebenen Links herunter. Sie können den Code mit jeder Numbers-Tabelle ausprobieren. Bitte lesen Sie auch die Kommentare im Code für weitere Hilfe.

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
