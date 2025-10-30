---
title: Benutzerdefinierte Musterformatierung für DBNum festlegen
linktitle: Benutzerdefinierte Musterformatierung für DBNum festlegen
description: Aspose.Cells ist eine JavaScript Bibliothek via C++, die das Formatieren von Daten und Zahlen mit benutzerdefinierten Formatmustern unterstützt. Dieser Artikel zeigt, wie das benutzerdefinierte Formatmuster dbnum für eine bessere Kontrolle der Zahlendarstellung festgelegt wird.
keywords: Aspose.Cells, JavaScript via C++, elektronische Tabellenkalkulation, benutzerdefiniertes Formatmuster, Formatierung, dbnum , Steuerung der Anzeige
type: docs
weight: 110
url: /de/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for JavaScript via C++ unterstützt das *DBNum*-benutzerdefinierte Musterformat. Zum Beispiel, wenn Ihr Zellwert 123 ist und Sie das benutzerdefinierte Format als [DBNum2][$-804]General angeben, wird es als 壹佰贰拾叁 angezeigt. Sie können das benutzerdefinierte Zellformat mit [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) Methode und [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) Methode festlegen.

## **Beispielcode**

Das folgende Beispiel zeigt, wie man die *DBNum*-benutzerdefinierte Musterformatierung festlegt. Bitte überprüfen Sie das [AusgabepDF](43352081.pdf) für weitere Unterstützung.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
