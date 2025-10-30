---
title: Adresszelle, Zählung, Versatz, ganze Spalte und ganze Zeile des Bereichs mit JavaScript via C++ holen
linktitle: Adresse Zellenzahl Versatz Gesamte Spalte und Gesamte Zeile des Bereichs erhalten
type: docs
weight: 330
url: /de/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells for JavaScript via C++ stellt das Range-Objekt bereit, das verschiedene nützliche Methoden hat, die es dem Nutzer erleichtern, mit Excel-Bereichen zu arbeiten. Dieser Artikel zeigt die Verwendung der folgenden Methoden oder Eigenschaften des Range-Objekts.

- **Adresse**

Holt die Adresse des Bereichs ab.

- **Zellanzahl**

Holt alle Zellenanzahlen im Bereich ab.

- **Versatz**

Holt den Bereich durch Versatz ab.

- **Gesamte Spalte**

Ruft ein Range-Objekt ab, das die gesamte Spalte (oder Spalten) enthält, die den angegebenen Bereich enthält.

- **Gesamte Zeile**

Ruft ein Range-Objekt ab, das die gesamte Zeile (oder Zeilen) enthält, die den angegebenen Bereich enthält.

## **Holt Adresse, Zellanzahl, Versatz, gesamte Spalte und gesamte Zeile des Bereichs ab.**
Der folgende Beispielcode erklärt die Verwendung der oben diskutierten Methoden und Eigenschaften. Bitte beachten Sie die Konsolenausgabe des unten angegebenen Codes als Referenz.

## **Beispielcode**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **Konsolenausgabe**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
