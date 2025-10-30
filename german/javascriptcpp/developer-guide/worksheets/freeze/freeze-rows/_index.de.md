---
title: Obere Zeile(n) der Excel Arbeitsmappe mit JavaScript via C++ einfrieren
linktitle: Zeilen einfrieren
type: docs
weight: 190
url: /de/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie Sie die oberen Zeilen von Excel Arbeitsblättern programmatisch mit der JavaScript Bibliothek und C++ API einfrieren.
keywords: Obere Zeilen einfrieren, obere Zeile mit JavaScript via C++.
---

## **Einführung**

In diesem Artikel lernen wir, wie man die obere Zeile(n) einfrieren kann. Wenn Sie eine große Datenmenge unter einer gemeinsamen Überschrift haben, können Sie die Überschrift beim Herunterscrollen nicht mehr sehen. Sie können die obere Zeile(n) einfrieren, sodass Sie diesen eingefrorenen Bereich auch beim Scrollen des restlichen Inhalts sehen können. Header in den oberen Zeilen sind leicht sichtbar.

## **Zeilen in Excel einfrieren**

**![Oberste Zeile(n) in Excel einfrieren](Freeze-Rows.png)**

1. Wenn Sie die oberen Zeile(n) einfrieren möchten, wählen Sie zuerst die Zeile unter der zu frierenden Zeile aus.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Wählen Sie im Dropdown-Menü "Oberste Zeile einfrieren" aus.
4. Wenn Sie nach unten scrollen, befindet sich die erste Zeile immer im oberen Sichtbereich.

**![Gefrorene Zeile](Frozen-Row.png)**

Wie Sie sehen können, ist die erste Zeile eingefroren; die erste Zeile bleibt beim Herunterscrollen immer oben im Blickfeld.

Das Einfrieren von Zeilen ermöglicht es Ihnen, große Datenmengen zu sehen, ohne die Zeilenbeschriftung im Blick behalten zu müssen.

## **Zeilen mit Aspose.Cells for JavaScript via C++ einfrieren**
Das Einfrieren von Zeilen mit Aspose.Cells for JavaScript via C++ ist einfach. 
Verwenden Sie die [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) Methode, um die Zeile(n) an der ausgewählten Zeile einzufrieren.
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Frieren Sie die erste Zeile mit der Worksheet.freezePanes() Methode ein.
3. Die Datei speichern.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Angehängte [Beispielquelle für Excel-Datei](../Freeze.xlsx).
