---
title: Fenster in Excel Arbeitsblatt mit JavaScript über C++ einfrieren
linktitle: Fenster einfrieren
type: docs
weight: 190
url: /de/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie man Fenster in Excel Arbeitsblättern programmatisch mit Aspose.Cells for JavaScript über C++ einfriert.
keywords: Fenster einfrieren, Fenster fixieren.
---

## **Einführung**  

In diesem Artikel lernen Sie, wie man Fenster einfriert. Wenn Sie große Datenmengen unter einer gemeinsamen Überschrift haben, können Sie die Überschrift beim Herunterscrollen im Arbeitsblatt nicht mehr sehen. Jedes Datensatz enthält viele Daten. Sie können Fenster einfrieren, sodass Sie den eingefrorenen Bereich auch beim Scrollen des restlichen Daten sehen können. Sie können Kopfzeilen in den oberen Zeilen oder den ersten Spalten leicht erkennen. Das Einfrieren und Aufheben des Einfrierens ändert nur die Ansicht der Daten, ohne die Daten selbst zu verändern.  

## **In Excel**  

**![Fenster einfrieren in Excel](Freeze-panes.png)**  

1. Wenn Sie Fenster einfrieren möchten, Zeilen und Spalten einfrieren, wählen Sie zuerst eine Zelle (wie B2).  
2. Klicken Sie auf Ansicht > Fenster einfrieren.  
3. Im Dropdown-Menü klicken Sie auf Fenster einfrieren.  
4. Wenn Sie nach unten oder nach rechts scrollen, sind die erste Zeile und die erste Spalte eingefroren.  

**![Eingefrorene Fenster](Frozen-Panes.png)**  

Wie Sie sehen können, sind die Zeile 1 und die Spalte A eingefroren, die zweite Zeile ist 32 und die zweite sichtbare Spalte ist D.  

Das Einfrieren von Fenstern ermöglicht es Ihnen, Ihre großen Daten zu betrachten, ohne Zeilen- oder Spaltenbeschriftungen im Blick zu behalten.  

## **Fenster mit Aspose.Cells for JavaScript über C++ einfrieren**  
Das Einfrieren von Fenstern mit Aspose.Cells for JavaScript über C++ ist einfach. Bitte verwenden Sie die [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)-Methode, um die Fenster an der ausgewählten Zelle zu fixieren.  
1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen oder eine leere Datei zu erstellen.  
Zeige Pane mit der Methode Worksheet.freezePanes() an.  
3. Die Datei speichern.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

Anbei [Beispielquelle Excel-Datei](Freeze.xlsx).
