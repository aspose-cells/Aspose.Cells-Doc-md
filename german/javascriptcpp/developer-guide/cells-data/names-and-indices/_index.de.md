---
title: Umwandlung zwischen Zellnamen und Zeile/Spaltenindex
linktitle: Zellname und Indexumwandlung
type: docs
weight: 10
url: /de/javascript-cpp/names-and-indices/
description: Lernen Sie, wie man die Umwandlung zwischen Zellname und Zeilen /Spaltenindex mithilfe des Aspose.Cells for JavaScript via C++ API durchführt.
keywords: JavaScript via C++ Erhalten des Zellnamens aus Zeilen und Spaltenindizes, Erhalten der Zeilen und Spaltenindizes aus Zellname, Erstellen sicherer Arbeitsblattnamen, Hinzufügen sicherer Arbeitsblattnamen
---

## **Zellnamen aus Zeilen- und Spaltenindizes erhalten**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells for JavaScript via C++ bietet die Methode CellsHelper.cellIndexToName, die Entwicklern ermöglicht, den Namen einer Zelle zu erhalten, wenn sie die Zeilen- und Spaltenindex angeben.

{{% alert color="primary" %}} 

Microsoft Excel zählt Zeilen- und Spaltenindizes ab 1. Im Gegensatz dazu beginnt Aspose.Cells for JavaScript via C++ ab 0.

{{% /alert %}} 

 Der folgende Beispielcode zeigt, wie man CellsHelper.cellIndexToName verwendet, um den Namen der Zelle anhand eines bekannten Zeilen- und Spaltenindex zu erhalten. Der Code erzeugt die folgende Ausgabe.



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
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **Zeilen- und Spaltenindizes aus Zellnamen erhalten**
Es ist möglich, den Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells for JavaScript via C++ bietet die Methode CellsHelper.cellNameToIndex, die Entwicklern ermöglicht, einen Zeilen- und Spaltenindex anhand des Zellnamens zu erhalten.

{{% alert color="primary" %}} 

Microsoft Excel zählt Zeilen- und Spaltenindizes ab 1. Im Gegensatz dazu beginnt Aspose.Cells for JavaScript via C++ ab 0.

{{% /alert %}} 

 Der folgende Beispielcode zeigt, wie man CellsHelper.cellNameToIndex verwendet, um den Zeilen- und Spaltenindex anhand des Zellnamens zu erhalten. Der Code erzeugt die folgende Ausgabe.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **Sichere Blattnamen erstellen**
Manchmal besteht die Notwendigkeit, den Blattnamen zur Laufzeit festzulegen. Dabei können Blattnamen zusätzliche Zeichen wie <>+(?” enthalten. Es ist erforderlich, solche unerlaubten Zeichen durch vom Benutzer vorgegebene Ersatzzeichen zu ersetzen. Ebenso kann die Länge 31 Zeichen überschreiten und muss gekürzt werden. Apache POI bietet Funktionen zur Erstellung sicherer Namen, eine vergleichbare Funktion bietet Aspose.Cells for JavaScript via C++ zur Lösung dieser Probleme. Das folgende Beispiel zeigt diese Funktionalität:



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

Ergebnis:

das ist der erste Name, der erstellt wurde

` `<> + (Adj. Privat _ "Privat"
