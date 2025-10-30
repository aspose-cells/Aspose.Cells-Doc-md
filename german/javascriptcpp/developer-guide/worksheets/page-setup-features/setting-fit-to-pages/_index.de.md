---
title: Wie man Excel mit JavaScript über C++ als Anpassungseinstellung druckt
linktitle: Wie drucke ich Excel auf zugeschnittenen Seiten breit und hoch
type: docs
weight: 200
url: /de/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man FitToPagesWide und FitToPagesTall mit Aspose.Cells for JavaScript über C++ einstellt.
keywords: JavaScript via C++ Wie man FitToPagesWide und FitToPagesTall einstellt, Wie man FitToPagesWide und FitToPagesTall in JavaScript hinzufügt, Wie man FitToPagesWide und FitToPagesTall in Excel setzt, Wie man FitToPagesWide und FitToPagesTall in Excel löscht, Wie man Excel als Anpassungseinstellung druckt, Wie man Arbeitsblatt auf einer Seite druckt, Wie man alle Spalten des Arbeitsblatts auf einer Seite druckt.
---

## **Einführung**

Die Einstellungen FitToPagesWide und FitToPagesTall werden in Tabellenkalkulationsanwendungen (wie Microsoft Excel) verwendet, um die Skalierung eines Tabellenblatts beim Drucken zu steuern. Diese Einstellungen helfen sicherzustellen, dass Ihre gedruckte Ausgabe innerhalb einer festgelegten Anzahl von Seiten passt, sowohl horizontal als auch vertikal. Hier eine Aufschlüsselung: 

1. FitToPagesWide: Diese Einstellung gibt die Anzahl der Seiten an, in die die gedruckte Ausgabe horizontal passt. Zum Beispiel bedeutet das Setzen von FitToPagesWide auf 1, dass der Inhalt auf die Breite einer Seite skaliert wird, egal wie breit das Tabellenblatt ist.
2. FitToPagesTall: Diese Einstellung gibt die Anzahl der Seiten an, die die gedruckte Ausgabe in der Höhe einpassen soll. Zum Beispiel bedeutet das Festlegen von FitToPagesTall auf 1, dass der Inhalt so skaliert wird, dass er in einer einzigen Seitengröße passt, unabhängig von der Anzahl der Zeilen.

## **Warum FitToPagesWide und FitToPagesTall verwenden**
Hier sind einige Gründe, warum Sie FitToPagesWide und FitToPagesTall einstellen sollten:
1. Kontrolle über das gedruckte Layout: Durch die Angabe der Anzahl der Seiten in der Breite und Höhe können Sie sicherstellen, dass Ihr gedrucktes Dokument leicht lesbar und gut organisiert ist, ohne dass Spalten oder Zeilen ungünstig auf mehrere Seiten aufgeteilt werden.
2. Konsistenz: Wenn Sie mehrere Blätter oder Berichte drucken, helfen diese Einstellungen, ein einheitliches Format beizubehalten, wodurch der Vergleich und die Analyse gedruckter Dokumente erleichtert werden.
3. Professionelle Präsentation: Das richtige Skalieren und Anpassen des Inhalts auf eine bestimmte Seitenzahl kann zu einer professionelleren und polierten Präsentation Ihrer Daten führen.

## **So drucken Sie eine Datei als angepasste Seiten breit und hoch in Excel**

Um die Einstellungen FitToPagesWide und FitToPagesTall in Microsoft Excel festzulegen, befolgen Sie diese Schritte:

1. Öffnen Sie Ihre Excel-Arbeitsmappe und wechseln Sie auf das Blatt, das Sie drucken möchten.
2. Gehen Sie auf die Registerkarte Seitenlayout im Ribbon.
3. Klicken Sie in der Gruppe Seitenlayout auf den kleinen Pfeil in der unteren rechten Ecke, um das Dialogfeld Seite einrichten zu öffnen.
4. Gehen Sie im Dialogfeld Seite einrichten zur Registerkarte Seite.
5. Unter Skalierung wählen Sie die Option "Anpassen an" und geben dann die Anzahl der Seiten in der Breite und Höhe an, die Sie möchten: Geben Sie die gewünschte Anzahl der Seiten in der ersten Box ein (Anpassen an x Seiten breit). Geben Sie die gewünschte Anzahl der Seiten in der zweiten Box ein (Anpassen an y Seiten hoch).
<br>
<img src="2.png" width=60% />

6. Klicken Sie auf OK, um die Einstellungen anzuwenden.

## **Wie man Excel als angepasste Seiten Breite und Höhe mit Aspose.Cells for JavaScript über C++ druckt**

Um FitToPagesWide und FitToPagesTall in einem bestimmten Arbeitsblatt einzustellen: Zuerst laden Sie die [Beispieldatei](input.xlsx), dann müssen Sie die Eigenschaften [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) und [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) des [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) Objekts für das gewünschte Arbeitsblatt anpassen. Hier ist ein Beispiel in JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Das Ausgabenergebnis:
<br>
<img src="1.png" width=60% />

## **Wie man Arbeitsblatt als eine Seite mit Aspose.Cells for JavaScript über C++ druckt**

Um Arbeitsblatt als eine Seite zu drucken: Zuerst laden Sie die [Beispieldatei](sample.xlsx), dann müssen Sie die Eigenschaft [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) des [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/) Objekts einstellen. Hier ist ein Beispiel in JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Das Ausgabenergebnis:
<br>
<img src="3.png" width=60% />

## **Wie man alle Spalten eines Arbeitsblatts auf einer Seite mit Aspose.Cells for JavaScript über C++ druckt**

Um alle Spalten eines Arbeitsblatts auf einer Seite zu drucken: Zuerst laden Sie die [Beispieldatei](sample.xlsx), dann müssen Sie die Eigenschaft [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) des [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/) Objekts einstellen. Hier ist ein Beispiel in JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Das Ausgabenergebnis:
<br>
<img src="4.png" width=60% />
