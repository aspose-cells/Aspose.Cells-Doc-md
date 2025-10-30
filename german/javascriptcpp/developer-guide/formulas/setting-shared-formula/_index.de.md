---
title: Gemeinsame Formel mit JavaScript via C++ festlegen
linktitle: Einstellung gemeinsamer Formel
type: docs
weight: 10
url: /de/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Wenn Sie eine Funktion in einem Arbeitsblatt hinzufügen möchten, die Berechnungen durchführt, erklärt dieser Artikel, wie Sie diese Aufgabe mit Aspose.Cells for JavaScript via C++ realisieren.

{{% /alert %}}

## Gemeinsame Formel mit Aspose.Cells for JavaScript via C++ festlegen

Angenommen, Sie haben ein Arbeitsblatt mit Daten im Format, das wie das folgende Beispieldatenblatt aussieht.

|**Eingabedatei mit einer Spalte Daten**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Sie möchten eine Funktion in B2 hinzufügen, die die Umsatzsteuer für die erste Datensatzreihe berechnet. Die Steuer beträgt **9%**. Die Formel zur Berechnung der Umsatzsteuer lautet: **"=A2*0,09"**. In diesem Artikel wird erläutert, wie diese Formel mit Aspose.Cells angewendet wird.

Mit Aspose.Cells können Sie eine Formel mit der Eigenschaft [**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) angeben. Es gibt zwei Optionen, um Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte hinzuzufügen.

Entweder tun Sie das, was Sie für die erste Zelle gemacht haben, indem Sie die Formel effektiv für jede Zelle festlegen und die Zellreferenz entsprechend aktualisieren (A3*0.09, A4*0.09, A5*0.09 und so weiter). Dies erfordert, dass die Zellreferenzen für jede Zeile aktualisiert werden. Es erfordert auch, dass Aspose.Cells jede Formel einzeln parst, was bei großen Tabellen und komplexen Formeln zeitaufwendig sein kann. Es fügt auch zusätzliche Zeilen Code hinzu, obwohl Schleifen sie etwas reduzieren können.

Ein anderer Ansatz ist die Verwendung einer **gemeinsamen Formel**. Mit einer gemeinsamen Formel werden die Formeln automatisch für die Zellbezüge in jeder Zeile aktualisiert, sodass die Steuer ordnungsgemäß berechnet wird. Die Methode [**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) ist effizienter als die erste Methode.

Das folgende Beispiel zeigt, wie es verwendet wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
