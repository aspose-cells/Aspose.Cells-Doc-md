---
title: Fügen Sie Zellen in das Microsoft Excel Formelüberwachungsfenster mit JavaScript via C++ hinzu
linktitle: Zellen zur Microsoft Excel Formelüberwachung hinzufügen
description: Wie man die Aspose.Cells Bibliothek verwendet, um Zellen in das Formelüberwachungsfenster in Excel mit JavaScript via C++ hinzuzufügen. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen können wir die Zellen manipulieren und Formeln setzen. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Formelüberwachungsfenster, Zellen, Hinzufügen, JavaScript via C++
type: docs
weight: 60
url: /de/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Mögliche Verwendungsszenarien**

Das Microsoft Excel Überwachungsfenster ist ein nützliches Tool, um Zellwerte und -formeln bequem in einem Fenster zu beobachten. Sie können das *Watch Window* in Microsoft Excel öffnen, indem Sie auf *Formeln > Überwachung > Überwachungsfenster* klicken. Es gibt einen *Überwachung hinzufügen*-Button, um Zellen zur Inspektion hinzuzufügen. Ebenso können Sie die Methode [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-) verwenden, um Zellen mithilfe der Aspose.Cells API in das *Watch Window* hinzuzufügen.

## **Zellen zur Microsoft Excel-Formelüberwachung hinzufügen**

Das folgende Beispiel setzt die Formel der Zellen C1 und E1 und fügt beide im Überwachungsfenster hinzu. Anschließend wird die Arbeitsmappe als [Ausgabedatei für Excel](67338481.xlsx) gespeichert. Wenn Sie die Ausgabedatei öffnen und das *Watch Window* anzeigen, sehen Sie beide Zellen, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
