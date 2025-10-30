---
title: Untersummen erstellen
type: docs
weight: 800
url: /de/javascript-cpp/creating-subtotals/
description: Erfahren Sie, wie Sie Zwischensummen für wiederkehrende Werte in einem Tabellenblatt mit der Aspose.Cells for JavaScript via C++ API erstellen.
keywords: Untertotale anwenden, Untertotale festlegen, Untertotale hinzufügen, Untertotale erstellen, Wie Sie Untertotale zu einem Arbeitsblatt hinzufügen 
---

{{% alert color="primary" %}}

Sie können automatisch Zwischensummen für wiederkehrende Werte in einem Tabellenblatt erstellen. Aspose.Cells for JavaScript via C++ bietet API-Funktionen, mit denen Sie Zwischensummen programmatisch hinzufügen können.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um Teilsummen in Microsoft Excel hinzuzufügen:

1. Erstellen Sie eine einfache Datenliste im ersten Arbeitsblatt der Arbeitsmappe (wie unten gezeigt) und speichern Sie die Datei als Book1.xls.
1. Wählen Sie eine beliebige Zelle innerhalb Ihrer Liste aus.
1. Wählen Sie im **Daten**-Menü **Teilsummen** aus. Der Dialog für Teilsummen wird angezeigt. Definieren Sie, welche Funktion verwendet werden soll und wo die Teilsummen platziert werden sollen.

## **Verwendung der Aspose.Cells for JavaScript via C++ API**

Aspose.Cells for JavaScript via C++ bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) dargestellt. Die Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern und anderen Objekten. Jedes Arbeitsblatt besteht aus einer [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung. Um Zwischensummen zu einem Arbeitsblatt hinzuzufügen, verwenden Sie die Methode [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Klasse. Geben Sie Parameterwerte an, um zu bestimmen, wie die Zwischensumme berechnet und platziert werden soll.

In den untenstehenden Beispielen haben wir Zwischensummen im ersten Arbeitsblatt der [Vorlagendatei](book1.xlsx) mit der Aspose.Cells for JavaScript via C++ API hinzugefügt. Bei Ausführung des Codes wird ein Arbeitsblatt mit Zwischensummen erstellt.

Die folgenden Codeausschnitte zeigen, wie Sie Zwischensummen mit Aspose.Cells for JavaScript via C++ zu einem Arbeitsblatt hinzufügen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
