---
title: Wie man Druckbereich mit JavaScript via C++ einstellt
linktitle: So legen Sie den Druckbereich fest
type: docs
weight: 200
url: /de/javascript-cpp/how-to-set-print-area/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man den Druckbereich mit der Aspose.Cells Bibliothek für JavaScript via C++ festlegt.
keywords: Druckbereich begrenzen, Druckbereich setzen, Druckbereich löschen, Druckbereich mit JavaScript via C++ setzen und löschen, Wie man Druckbereich mit JavaScript via C++ festlegt, Druckbereich mit JavaScript via C++ setzen und löschen, Druckbereich in JavaScript via C++ löschen, Druckbereich mit JavaScript via C++ hinzufügen, Druckbereich mit JavaScript via C++ entfernen, Druckbereich in Excel festlegen, Druckbereich in Excel löschen
---

## **Mögliche Verwendungsszenarien**

Das Festlegen eines Druckbereichs in einem Dokument, wie z.B. einer Excel-Tabelle, hilft dabei, zu steuern, welche Inhalte beim Drucken enthalten sind. Hier sind einige Gründe, einen Druckbereich festzulegen:

1. Fokus auf bestimmte Daten: Sie können nur die relevantesten Abschnitte drucken und unnötigen Inhalt vermeiden.
1. Verbesserte Gestaltung: Es hilft, den Inhalt ordentlich auf den gedruckten Seiten anzuordnen und anzupassen, um Brüche oder unerwünschte Seitenumbrüche zu vermeiden.
1. Ressourcen sparen: Durch Begrenzung des Druckbereichs können Sie Papier- und Tintenverbrauch reduzieren.
1. Professionelle Darstellung: Es stellt sicher, dass nur die fertig ausgearbeitete Version der Daten gedruckt wird, was besonders bei Berichten oder Präsentationen wichtig ist.
1. Konsistenz: Beim mehrfachen Drucken desselben Dokuments sorgt ein festgelegter Druckbereich für einheitliches Ergebnis.

<br>
Das Festlegen eines Druckbereichs ist besonders in größeren Dokumenten nützlich, bei denen nur ein Teil in gedruckter Form geteilt oder überprüft werden soll.

## **So legen Sie den Druckbereich in Excel fest**

Um einen Druckbereich in Excel festzulegen, befolgen Sie diese Schritte:

1. Zellen auswählen: Klicken und ziehen Sie, um den Zellbereich auszuwählen, den Sie als Druckbereich festlegen möchten.
1. Gehen Sie auf die Registerkarte Seitenlayout: Wechseln Sie in die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.
1. Druckbereich festlegen: Klicken Sie im Bereich "Seite einrichten" auf "Druckbereich". Wählen Sie aus dem Dropdown-Menü "Druckbereich festlegen".
<br>
<img src="3.png" width=60% />

1. Zum Druckbereich hinzufügen: Wenn Sie zusätzliche Zellen zum bestehenden Druckbereich hinzufügen möchten, wählen Sie die zusätzlichen Zellen aus, gehen Sie im Menü "Seitenlayout" auf "Druckbereich" und wählen Sie "Druckbereich hinzufügen".

<br>
Diese Aktion legt die ausgewählten Zellen als Druckbereich fest. Wenn Sie das Arbeitsblatt drucken, wird nur dieser definierte Bereich gedruckt.

## **So entfernen Sie den Druckbereich in Excel**

Um den Druckbereich in Excel zu entfernen, folgen Sie diesen Schritten:

1. Öffnen Sie die Registerkarte Seitenlayout: Klicken Sie auf die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.
1. Druckbereich entfernen: Klicken Sie im Gruppenfeld "Seite einrichten" auf "Druckbereich". Wählen Sie im Dropdown-Menü "Druckbereich löschen".
<br>
<img src="4.png" width=60% />

<br>
Diese Aktion entfernt jeden zuvor festgelegten Druckbereich, sodass das gesamte Arbeitsblatt gedruckt werden kann.

## **Was passiert nach dem Entfernen des Druckbereichs**

Das Entfernen des Druckbereichs in einer Tabellenkalkulationsanwendung wie Excel mit Aspose.Cells führt dazu, dass beim Drucken das gesamte Arbeitsblatt eingeschlossen wird. Wenn ein Druckbereich festgelegt ist, wird nur der angegebene Zellbereich gedruckt. Durch das Entfernen des Druckbereichs wird sichergestellt, dass kein spezifischer Bereich mehr definiert ist und das Standarddruckverhalten, das das gesamte Blatt umfasst, wirksam wird.

1. Standard-Druckverhalten: Das gesamte Arbeitsblatt wird für den Druck berücksichtigt. Das bedeutet, alle Zellen mit Daten oder Formatierungen werden gedruckt.
1. Keine Druckbereichsbegrenzung: Vorher festgelegte Druckbereichsgrenzen werden entfernt. Wenn bestimmte Zeilen und Spalten für den Druck festgelegt waren, gelten diese Begrenzungen nicht mehr.
1. Vollständiger Inhalt: Alle Inhalte, einschließlich Kopf- und Fußzeilen sowie anderer Daten im Arbeitsblatt, werden im Druckauftrag eingeschlossen.

## **Wie man Druckbereich mit Aspose.Cells for JavaScript via C++ festlegt**

Um den Druckbereich in einem bestimmten Arbeitsblatt festzulegen: Laden Sie zunächst die [Beispieldatei](input.xlsx), und dann müssen Sie die [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--)-Eigenschaft des [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)-Objekts für das gewünschte Arbeitsblatt modifizieren. Das Festlegen dieser Eigenschaft auf eine Bereichszeichenfolge setzt den Druckbereich.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Area</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet (first worksheet)
            const worksheet = workbook.worksheets.get(0);

            // Set the print area - specify the range you want to print
            worksheet.pageSetup.printArea = "A1:D10";

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Das Ausgabenergebnis:
<br>
<img src="1.png" width=60% />

## **Wie man Druckbereich mit Aspose.Cells for JavaScript via C++ löscht**

Um den Druckbereich in einem bestimmten Arbeitsblatt zu löschen: Laden Sie zuerst die [Beispieldatei](input.xlsx), und ändern Sie dann die Eigenschaft [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) des Objekts [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) für das gewünschte Arbeitsblatt. Das Setzen dieser Eigenschaft auf einen leeren String löscht den Druckbereich.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Clear Print Area</title>
    </head>
    <body>
        <h1>Clear Print Area Example</h1>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the print area
            worksheet.pageSetup.printArea = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultEl.innerHTML = '<p style="color: green;">Print area cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Das Ausgabenergebnis:
<br>
<img src="2.png" width=60% />
