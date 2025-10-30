---
title: Erstspalte(n) einer Excel Arbeitsmappe mit JavaScript via C++ einfrieren
linktitle: Spalten fixieren
type: docs
weight: 190
url: /de/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: Erfahren Sie, wie Sie die linken Spalten von Excel Arbeitsblättern programmatisch mit Aspose.Cells for JavaScript via C++ einfrieren.
keywords: Linke Spalten einfrieren, Erste Spalten einfrieren, Spalte(n) sperren
---

## **Einführung**  

In diesem Artikel lernen wir, wie man linke Spalte(n) einfriert. Wenn Sie eine große Datenmenge in einer Zeile haben, können Sie die linken Spalten beim horizontalen Scrollen durch das Arbeitsblatt nicht sehen. Sie können die erste(n) Spalte(n) einfrieren und sperren, sodass Sie diesen eingefrorenen Bereich auch beim Scrollen des restlichen Inhalts sehen können. Header in den linken Spalten sind leicht sichtbar.  

## **Spalten in Excel einfrieren**  

**![Linke Spalte(n) in Excel einfrieren](freeze-columns.png)**  

1. Wenn du die linke(n) Spalte(n) einfrieren möchtest, wähle zuerst die Spalte unter der Spalte, die eingefroren werden soll.
2. Klicken Sie auf Ansicht > Fenster einfrieren.
3. Klicken Sie im Dropdown-Menü auf Spalte fixieren.
4. Wenn du nach unten scrollst, ist die erste Spalte immer im linken Ansichtsbereich.

**![Gefrorene Spalte](frozen-columns.png)**  

Wie Sie sehen können, ist die erste Spalte eingefroren, und die erste Spalte bleibt beim horizontalen Scrollen immer oben im Blickfeld fixiert.

Das Einfrieren von Spalten ermöglicht es Ihnen, große Datenmengen ohne Schwierigkeiten im Blick zu behalten.

## **Spalten mit Aspose.Cells for JavaScript via C++ einfrieren**  
Das Einfrieren der ersten Spalte(n) mit Aspose.Cells for JavaScript via C++ ist einfach.  
Bitte verwenden Sie die Methode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-), um die Spalte(n) an der ausgewählten Spalte einzufrieren.  
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.
2. Frieren Sie die erste Spalte mit der Worksheet.freezePanes() Methode ein.
3. Die Datei speichern.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
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

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).
