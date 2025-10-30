---
title: Wie man Drucktitel mit JavaScript via C++ einstellt
linktitle: Wie man Drucktitel festlegt
type: docs
weight: 200
url: /de/javascript-cpp/how-to-set-print-titles/
description: Dieser Artikel zeigt, wie man Drucktitel mit der Aspose.Cells Bibliothek für JavaScript via C++ einstellt.
keywords: Zeilen und Spalten wiederholt drucken, JavaScript Wie man Drucktitel einstellt, Drucktitel mit JavaScript setzen und löschen, Drucktitel in JavaScript löschen, Drucktitel mit JavaScript hinzufügen, Drucktitel mit JavaScript entfernen, Drucktitel in Excel festlegen, Drucktitel in Excel löschen.  
---

## **Mögliche Verwendungsszenarien**  

Das Festlegen von Drucktiteln in Excel stellt sicher, dass bestimmte Zeilen oder Spalten auf jeder gedruckten Seite wiederholt werden, was besonders bei großen Tabellen, die sich über mehrere Seiten erstrecken, nützlich ist. Hier sind einige Gründe, warum Sie Drucktitel festlegen könnten:  

1. Verbesserte Lesbarkeit: Drucktitel helfen den Lesern, die Daten zu verstehen, indem sie Kopfzeilen auf allen Seiten sichtbar halten, was die Interpretation der Informationen auf jeder Seite erleichtert, ohne auf die erste Seite zurückgreifen zu müssen.  

1. Professionelles Erscheinungsbild: Das konsequente Anzeigen von Kopfzeilen oder Label auf jeder Seite schafft ein professionelleres und gepflegteres Druckdokument.  

1. Verbesserte Navigation: Bei umfangreichen Daten ermöglicht das Wiederholen der Kopfzeilen auf jeder Seite eine schnellere Navigation und Referenzierung, wodurch das Hin- und Herblättern zwischen den Seiten reduziert wird.  

1. Weniger Fehler: Wenn Kopfzeilen auf jeder Seite vorhanden sind, minimieren Sie die Chancen für Missinterpretationen oder Eingabefehler, da Benutzer den Datenzusammenhang leicht erkennen können.  

1. Konsistenz: Die Sicherstellung, dass wichtige Informationen wie Spaltenüberschriften oder Zeilenbeschriftungen immer sichtbar sind, gewährleistet Konsistenz und Klarheit im gesamten Dokument.  

## **So legen Sie Drucktitel in Excel fest**  

Um Drucktitel in Excel festzulegen, folgen Sie diesen Schritten:  

1. Öffnen Sie die Registerkarte Seitenlayout: Klicken Sie auf die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.  
1. Zugriff auf Drucktitel: Klicken Sie im "Seiteneinrichtung"-Bereich auf "Drucktitel".  
1. Zeilen zum Wiederholen festlegen: Im Dialogfeld "Seite einrichten" gehen Sie auf die Registerkarte "Blatt". Im Abschnitt "Drucktitel" geben Sie die Zeilen an, die oben wiederholt werden sollen, indem Sie das Kästchen neben "Zeilen, die oben wiederholt werden" aktivieren und die Zeile(n) auswählen, die wiederholt werden sollen.  
1. Spalten zum Wiederholen festlegen (falls erforderlich): Ebenso können Sie die Spalten angeben, die links wiederholt werden sollen, indem Sie das Kästchen neben "Spalten, die links wiederholt werden" aktivieren und die Spalte(n) auswählen, die wiederholt werden sollen.  
<br>  
<img src="3.png" width=60% />  

1. Bestätigen und Drucken: Klicken Sie auf "OK", um die Einstellungen anzuwenden. Beim Drucken des Arbeitsblatts erscheinen die angegebenen Zeilen oder Spalten auf jeder gedruckten Seite.  

## **So entfernen Sie Drucktitel in Excel**  

Um Drucktitel in Excel zu entfernen, müssen Sie die Zeilen oder Spalten löschen, die so eingestellt sind, dass sie auf jeder Seite wiederholt werden. So geht's:  

1. Öffnen Sie die Registerkarte Seitenlayout: Klicken Sie auf die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.  
1. Zugriff auf Drucktitel: Klicken Sie im "Seiteneinrichtung"-Bereich auf "Drucktitel".  
1. Drucktitel entfernen: Im Dialogfeld "Seiteneinrichtung" wechseln Sie zum Reiter "Blatt". Löschen Sie den Text in den Feldern für "Zeilen, die oben wiederholt werden" und "Spalten, die links wiederholt werden", indem Sie den Inhalt löschen.  
<br>  
<img src="4.png" width=60% />  

1. Bestätigen und schließen: Klicken Sie auf "OK", um die Änderungen zu übernehmen.  

## **Wie man Drucktitel mit Aspose.Cells for JavaScript via C++ einstellt**  

Um Drucktitel in einem bestimmten Arbeitsblatt festzulegen: Laden Sie zuerst die [Beispieldatei](input.xlsx) und ändern Sie dann die Eigenschaften [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) und [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) des Objekts [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) für das gewünschte Arbeitsblatt. Das Festlegen dieser Eigenschaften auf einen Range-String setzt die Drucktitel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Titles</title>
    </head>
    <body>
        <h1>Set Print Titles Example</h1>
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

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set rows to repeat at the top (e.g., rows 1 and 2)
            worksheet.pageSetup.printTitleRows = "$1:$2";

            // Set columns to repeat at the left (e.g., columns A and B)
            worksheet.pageSetup.printTitleColumns = "$A:$B";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Das Ausgabenergebnis:  
<br>  
<img src="1.png" width=60% />  

## **So löschen Sie Drucktitel mit Aspose.Cells for JavaScript über C++**  

Um Drucktitel in einem bestimmten Arbeitsblatt zu entfernen: Laden Sie zuerst die [Beispieldatei](input.xlsx) und ändern Sie dann die Eigenschaften [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) und [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) des Objekts [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) für das gewünschte Arbeitsblatt. Das Festlegen dieser Eigenschaften auf einen leeren String löscht die Drucktitel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Clear Print Titles Example</title>
    </head>
    <body>
        <h1>Clear Print Titles Example</h1>
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

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the rows and columns set to repeat
            worksheet.pageSetup.printTitleRows = "";
            worksheet.pageSetup.printTitleColumns = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Das Ausgabenergebnis:  
<br>  
<img src="2.png" width=60% />
