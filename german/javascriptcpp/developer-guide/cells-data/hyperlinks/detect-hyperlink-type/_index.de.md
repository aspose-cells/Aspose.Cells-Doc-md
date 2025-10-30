---
title: Hyperlink Typ erkennen
type: docs
weight: 160
url: /de/javascript-cpp/detect-hyperlink-type/
description: Lernen Sie, wie man den Hyperlink Typ durch die Aspose.Cells for JavaScript via C++ API erkennt.
keywords: Hyperlink Typ erkennen JavaScript via C++, Erkennen des Hyperlink typs JavaScript via C++, Den Typ des Hyperlinks JavaScript via C++ ermitteln
---

## **Hyperlink-Typ erkennen**

Eine Excel-Datei kann verschiedene Arten von Hyperlinks haben, z.B. externe, Zellreferenz, Dateipfad usw. Aspose.Cells for JavaScript via C++ unterstützt die Funktion, den Hyperlink-Typ zu erkennen. Die Arten der Hyperlinks werden durch die [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) Enumeration dargestellt. Die [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) Enumeration enthält die folgenden Mitglieder.

- External: Externer Link
- FilePath: Lokale und vollständige Pfade zu Dateien/Ordnern.
- Email: E-Mail
- CellReference: Verweis auf Zelle oder benannten Bereich.

Um den Hyperlink-Typ zu überprüfen, stellt die Klasse [**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink) eine Eigenschaft [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) mit einem Rückgabetyp von [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) bereit. Der folgende Codeausschnitt zeigt die Verwendung der [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) Eigenschaft anhand dieser [Excel-Datei](94896195.xlsx).

### Quellcode

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
                const resultDiv = document.getElementById('result');

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


Das folgende ist die Ausgabe, die durch den obigen Codeausschnitt generiert wird.

### Konsolenausgabe
