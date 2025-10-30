---
title: Zusammenführen und Aufheben der Zusammenführung von Zellen mit JavaScript über C++
linktitle: Zusammenführen und Aufteilen von Zellen
description: Aspose.Cells ist eine JavaScript Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die das Zusammenführen und Trennen von Zellen unterstützt. Dieser Artikel stellt vor, wie man Zellen mit der Aspose.Cells Bibliothek zusammenführt und trennt, mit Optionen zur Anpassung des Stils der zusammengeführten Zellen.
keywords: Aspose.Cells, JavaScript Bibliothek, Tabellenkalkulation, Zellen zusammenführen, Zellen trennen, Stil Einstellungen, benutzerdefinierte Stile
type: docs
weight: 190
url: /de/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können auch Zellen trennen oder aufteilen. Der Zellenbezug einer zusammengeführten Zelle ist der Bezug der links oben Zelle im ursprünglich ausgewählten Bereich.

{{% /alert %}} 
## **Einführung**
Nicht immer benötigen Sie dieselbe Anzahl von Zellen in jeder Zeile oder Spalte. Zum Beispiel möchten Sie möglicherweise einen Titel in einer Zelle haben, die mehrere Spalten umspannt. Oder wenn Sie eine Rechnung erstellen, möchten Sie weniger Spalten für die Gesamtsumme haben. Um eine Zelle aus zwei oder mehr Zellen zu machen, führen Sie sie zusammen. Microsoft Excel ermöglicht es Benutzern, Zellen auszuwählen und zu verschmelzen, um die Tabelle nach ihren Wünschen zu strukturieren.

{{% alert color="primary" %}} 

Beachten Sie, dass beim Zusammenführen von Zellen nur die Daten in der oberen linken Zelle beibehalten werden. Wenn in den anderen Zellen im Bereich Daten vorhanden sind, werden diese gelöscht. Formatierung basiert ebenfalls auf der Referenzzelle, sodass beim Zusammenführen von Zellen die Formatierungseinstellungen der oberen linken Zelle im Bereich auf die zusammengeführte Zelle angewendet werden. Beim Aufteilen der Zelle behalten die neuen Zellen ihre ursprünglichen Formatierungseinstellungen.

{{% /alert %}} 
## **Zellen in einem Arbeitsblatt zusammenführen**
### **Zusammenführen von Zellen in Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie Zellen im Arbeitsblatt mit MS Excel zusammenführen können.

1. Kopieren Sie die Daten, die Sie in die oberste linke Zelle innerhalb des Bereichs einfügen möchten.
1. Wählen Sie die Zellen aus, die Sie zusammenführen möchten.
1. Um Zellen in einer Zeile oder Spalte zusammenzuführen und den Zellinhalt zu zentrieren, klicken Sie auf das Icon **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

### **Zellen zusammenführen mit Aspose.Cells**
Die Aspose.Cells.Cells-Klasse verfügt über nützliche Methoden für diese Aufgabe. Zum Beispiel verbindet die Methode `merge()` die Zellen in einem bestimmten Bereich zu einer einzigen Zelle.

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Aufsplitten (Teilen) von zusammengeführten Zellen**
### **Verwendung von Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie zusammengeführte Zellen mit Microsoft Excel aufspalten können.

1. Wählen Sie die zusammengeführte Zelle aus.
   Wenn Zellen kombiniert wurden, ist **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste ausgewählt.
1. Klicken Sie auf **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

### **Verwendung von Aspose.Cells**
Die Klasse Aspose.Cells.Cells hat eine Methode namens `unmerge()`, die die Zellen in ihren ursprünglichen Zustand zurücksetzt. Die Methode entmerge die Zellen anhand der Referenz der Zelle im zusammengeführten Zellenbereich.

Das folgende Beispiel zeigt, wie die zusammengeführten Zellen (C6) aufgeteilt werden. Das Beispiel verwendet die Datei, die im vorherigen Beispiel erstellt wurde, und teilt die zusammengeführten Zellen auf.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Erkennen von zusammengeführten Zellen in einem Arbeitsblatt](/cells/de/javascript-cpp/detect-merged-cells-in-a-worksheet/)
