---
title: Anwendung von Zwischensumme und Änderung der Richtung der Zusammenfassungszeilen unterhalb der Details
type: docs
weight: 100
url: /de/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Lernen Sie, wie Sie Zwischensummen anwenden und die Richtung der Outline Zusammenfassungszeilen unterhalb der Detailzeilen mit dem Aspose.Cells for JavaScript via C++ API ändern.
keywords: Zwischensumme anwenden, Zwischensumme hinzufügen, Richtung der Zusammenfassungszeilen unterhalb des Details ändern, Richtung der Zusammenfassungszeilen rechts neben dem Detail ändern, Zwischensumme erstellen und Richtung der Zusammenfassungszeilen unterhalb des Details ändern
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie eine Zwischensumme auf Daten anwenden und die Richtung der Zusammenfassungszeilen unterhalb des Details ändern können.

Sie können eine Zwischensumme für Daten mithilfe der [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-) Methode anwenden. Es nimmt die folgenden Parameter an.

- **CellArea** - Der Bereich, auf den die Zwischensumme angewendet werden soll
- **GroupBy** - Das Feld, nach dem gruppiert werden soll, als nullbasierter Ganzzahlenoffset
- **Funktion** - Die Zwischensummenfunktion
- **TotalList** - Ein Array von nullbasierten Feldoffsets, die die Felder angeben, zu denen die Zwischensummen hinzugefügt werden
- **Ersetzen** - Gibt an, ob die aktuellen Zwischensummen ersetzt werden sollen
- **Seitenumbrüche** - Gibt an, ob zwischen den Gruppen ein Seitenumbruch hinzugefügt werden soll
- **Zusammenfassung unterhalb der Daten** - Gibt an, ob eine Zusammenfassung unterhalb der Daten hinzugefügt werden soll

Außerdem können Sie die Richtung der Zusammenfassungszeilen unterhalb des Details wie im folgenden Screenshot gezeigt steuern, indem Sie die Worksheet.Outline.SummaryRowBelow-Eigenschaft verwenden. Sie können diese Einstellung in Microsoft Excel unter **Daten > Gliederung > Einstellungen** öffnen

![todo:image_alt_text](1.png)

{{% /alert %}}

## Bilder von Quell- und Ausgabedateien

Der folgende Screenshot zeigt die verwendete Excel-Quelldatei im untenstehenden Beispielcode, die einige Daten in den Spalten A und B enthält.

![todo:image_alt_text](2.png)

Der folgende Screenshot zeigt die von dem Beispielcode generierte Ausgabedatei in Excel. Wie Sie sehen können, wurde eine Zwischensumme für den Bereich A2:B11 angewendet und die Richtung der Zusammenfassung ist unterhalb der Detailinformationen.

![todo:image_alt_text](3.png)

## JavaScript zur Anwendung von Zwischensummen und Änderung der Richtung der Outline-Zusammenfassungszeilen



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
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
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
