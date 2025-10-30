---
title: So skalieren Sie ein Arbeitsblatt mit JavaScript über C++
linktitle: So skalieren Sie ein Arbeitsblatt
type: docs
weight: 130
url: /de/javascript-cpp/how-to-scale-a-worksheet/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man ein Arbeitsblatt mithilfe von Aspose.Cells for JavaScript über C++ skaliert.
keywords: JavaScript skaliert ein Arbeitsblatt, Wie man ein Arbeitsblatt mit JavaScript über C++ skaliert, Ein Arbeitsblatt in JavaScript über C++ skalieren.
---

## **Mögliche Verwendungsszenarien**
Das Skalieren eines Arbeitsblatts kann aus verschiedenen Gründen nützlich sein, abhängig vom Kontext, in dem Sie arbeiten. Hier sind einige häufige Gründe für das Skalieren eines Arbeitsblatts:
1. An Seite anpassen: Damit alle Inhalte auf eine einzelne Seite oder eine bestimmte Anzahl von Seiten passen, beim Drucken, um das Lesen und die Verwaltung zu erleichtern, ohne durch mehrere Seiten blättern zu müssen.

1. Präsentation: Damit das Arbeitsblatt ordentlicher und professioneller aussieht, insbesondere bei der Weitergabe in Meetings oder Berichten.

1. Lesbarkeit: Um die Textgröße und andere Elemente für eine bessere Lesbarkeit anzupassen, insbesondere für Personen, die Schwierigkeiten haben, kleinere Schriftarten zu lesen.

1. Raumausnutzung: Um die Nutzung des Raums auf einem Arbeitsblatt zu optimieren, damit kein unnötiger Leerraum entsteht und alle wichtigen Informationen sichtbar sind, ohne übermäßig zu scrollen.

1. Datenvisualisierung: Bei Diagrammen und Grafiken kann das Skalieren helfen, sie verständlicher zu machen, indem die Größe an den verfügbaren Platz angepasst wird.

1. Konsistenz: Um ein konsistentes Aussehen und Gefühl über mehrere Arbeitsblätter oder Dokumente hinweg zu bewahren, was in professionellen und Bildungskontexten besonders wichtig ist.

## **Wie man ein Arbeitsblatt in Excel skaliert**
Das Skalieren eines Arbeitsblatts in Excel kann dabei helfen, den Inhalt auf eine einzelne Seite oder eine bestimmte Anzahl von Seiten beim Drucken anzupassen. Hier sind die Schritte, um ein Arbeitsblatt zu skalieren:

1. Das Arbeitsblatt öffnen: Öffnen Sie das Excel-Arbeitsblatt, das Sie skalieren möchten.

1. Zum Reiter Seitenlayout gehen: Klicken Sie auf den Reiter Seitenlayout im Menüband.

1. Gruppierung zum Anpassen anpassen: Im Reiter Seitenlayout finden Sie die Gruppe Seitenanpassung. Hier können Sie die Skalierung einstellen. Breite: Hier legen Sie fest, wie viele Seiten breit das gedruckte Arbeitsblatt sein sollen. Höhe: Hier legen Sie fest, wie viele Seiten hoch das gedruckte Arbeitsblatt sein sollen. Skalierung: Hier können Sie auch einen benutzerdefinierten Prozentsatz einstellen.
<br>
<img src="1.png" width=60% />

1. Breite und Höhe anpassen: Stellen Sie Breite und Höhe auf die gewünschte Anzahl an Seiten ein. Beispiel: Beide auf 1 Seite setzen, wenn das Arbeitsblatt auf eine Seite passen soll.

1. Skalierungsprozentsatz anpassen (falls erforderlich): Wenn Sie eine bestimmte Skalierung in Prozent einstellen möchten, passen Sie das Scale-Feld an. Beispiel: 50 % macht alles halb so groß.


## **So skalieren Sie ein Arbeitsblatt mit JavaScript über C++**
Aspose.Cells for JavaScript über C++ ist eine leistungsstarke Bibliothek für die programmatische Arbeit mit Excel-Dateien. Um ein Arbeitsblatt mit Aspose.Cells zu skalieren, folgen Sie diesen Schritten: Laden Sie [Beispieldatei](sample.xlsx) und passen Sie die Druckeinstellungen an, sodass der Inhalt auf die gewünschte Anzahl von Seiten oder einen bestimmten Prozentsatz der Originalgröße passt.

### **Beispiel: Auf Seite anpassen**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Fit To Page Example</title>
    </head>
    <body>
        <h1>Fit Worksheet to One Page</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the worksheet to fit to 1 page wide and 1 page tall
            pageSetup.fitToPagesWide = 1;
            pageSetup.fitToPagesTall = 1;

            // Saving the modified workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_fit_to_page.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet fitted to one page. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="3.png" width=60% />

### **Beispiel: Skalierung in Prozent**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Scale Worksheet</title>
    </head>
    <body>
        <h1>Scale Worksheet Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access the PageSetup object
            const pageSetup = sheet.pageSetup;

            // Set the scaling to a specific percentage (e.g., 75%)
            pageSetup.zoom = 75;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_scaled_percentage.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Scaled Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
<br>
<img src="2.png" width=60% />
