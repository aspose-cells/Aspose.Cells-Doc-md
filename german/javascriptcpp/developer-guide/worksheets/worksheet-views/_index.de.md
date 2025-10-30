---
title: Arbeitsblatt Ansichten mit JavaScript via C++
linktitle: Arbeitsblattansichten
type: docs
weight: 40
url: /de/javascript-cpp/worksheet-views/
description: Dieser Artikel beschreibt, wie man mit JavaScript und der JavaScript API die Seitenumbruchvorschau eines Excel Arbeitsbuchs und der Arbeitsblätter nutzt. Arbeiten Sie mit geteilten Fenstern, eingefrorenen Fenstern und Zoomfaktor.
---

## **Seitenwechselvorschau**

Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenwechselvorschau.

Normalansicht ist die Standardansicht eines Arbeitsblatts. Seitenumbruch-Vorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenumbruch-Vorschau zeigt, welche Daten auf jede Seite kommen, damit Sie Druckbereich und Seitenumbrüche anpassen können. Mit Aspose.Cells for JavaScript via C++ können Entwickler den Normalansicht- oder Seitenumbruch-Vorschau-Modus aktivieren.

### **Steuerung der Ansichtsmodi**

Aspose.Cells bietet eine [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse, die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Normal- oder Seitenumbruchvorschau zu aktivieren, verwenden Sie die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) und die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--). [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) ist eine boolesche Eigenschaft, die nur einen Wert von **true** oder **false** speichern kann.

#### **Normale Ansicht aktivieren**

Legen Sie ein Arbeitsblatt auf Normalansicht, indem Sie die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) der Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) auf **false** setzen.

#### **Aktivieren der Seitenwechselvorschau**

Legen Sie ein Arbeitsblatt auf die Seitenumbruchvorschau, indem Sie die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) der Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) auf **true** setzen. Dadurch wird das Arbeitsblatt von der Normalansicht zur Seitenumbruchvorschau gewechselt.

Im Folgenden finden Sie ein vollständiges Beispiel, das zeigt, wie die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) verwendet wird, um den Seitenumbruchvorschau-Modus für das erste Arbeitsblatt einer Excel-Datei zu aktivieren.

Die Datei book1.xls wird durch Erstellen einer Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) geöffnet. Die Ansicht wird für das erste Arbeitsblatt auf die Seitenumbruchvorschau umgeschaltet, indem die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) auf **true** gesetzt wird. Die geänderte Datei wird als output.xls gespeichert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Break Preview</title>
    </head>
    <body>
        <h1>Page Break Preview Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Displaying the worksheet in page break preview
            worksheet.isPageBreakPreview = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Zoom-Faktor**

### **Verwendung von Microsoft Excel**

Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, die Arbeitsblattinhalte in kleineren oder größeren Ansichten zu sehen. Benutzer können den Zoom-Faktor auf beliebige Werte setzen.

### **Aspose.Cells & Zoomfaktor**

Aspose.Cells ermöglicht Entwicklern, den Zoomfaktor des Arbeitsblatts festzulegen.
Aspose.Cells bietet eine [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse, die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die Eigenschaft [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) der Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Der Zoomfaktor wird durch Zuweisen eines numerischen (ganzzahligen) Werts zur Eigenschaft [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) festgelegt.

Ein vollständiges Beispiel wird unten gezeigt, das demonstriert, wie die [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--)-Eigenschaft verwendet wird, um den Zoomfaktor des ersten Arbeitsblatts in der Excel-Datei einzustellen.

Die Datei book1.xls wird durch Erstellen einer Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) geöffnet. Der Zoomfaktor für das erste Arbeitsblatt wird auf 75 eingestellt und die geänderte Datei wird als output.xls gespeichert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Worksheet Zoom Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the zoom factor of the worksheet to 75
            worksheet.zoom = 75;

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Zoom set to 75 successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fenster fixieren**

### **Verwendung von Microsoft Excel**

Freeze panes ist eine Funktion von Microsoft Excel. Durch das Einfrieren von Fenstern können Sie auswählen, dass Daten beim Scrollen in einem Arbeitsblatt sichtbar bleiben.

### **Aspose.Cells & Einfrieren von Fenstern**

Aspose.Cells ermöglicht Entwicklern, das Einfrieren von Zeilen und Spalten in Arbeitsblättern zur Laufzeit anzuwenden.

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um Freeze-Panes zu konfigurieren, rufen Sie die Methode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) der Worksheet-Klasse auf. Die [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-)-Methode nimmt die folgenden Parameter entgegen:

- **Zeile**, der Zeilenindex der Zelle, von der das Einfrieren startet.
- **Spalte**, der Spaltenindex der Zelle, von der das Einfrieren startet.
- **Eingefrorene Zeilen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Gefrorene Spalten**, die Anzahl der sichtbaren Spalten im linken Bereich.

Die Datei book1.xls wird geöffnet, indem der Konstruktor der Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) aufgerufen wird, während sie instanziiert wird, und einige Zeilen und Spalten werden im ersten Arbeitsblatt eingefroren. Die modifizierte Datei wird als output.xls gespeichert.

Im folgenden wird ein vollständiges Beispiel gezeigt, das zeigt, wie die Methode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) zum Einfrieren von Zeilen und Spalten (beginnend ab C4, dargestellt durch die 4. Zeile und 3. Spalte, wobei Zeilen und Spalten ab dem Index 0 beginnen) des ersten Arbeitsblatts der Excel-Datei verwendet wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Applying freeze panes settings: topRows = 3, leftColumns = 2, top = 3, left = 2
            worksheet.freezePanes(3, 2, 3, 2);

            // Saving the modified Excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Geteilte Fenster**

Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten im selben Arbeitsblatt zu erhalten, verwenden Sie geteilte Fenster. Microsoft Excel bietet eine sehr praktische Funktion, die es Ihnen ermöglicht, mehr als eine Kopie Ihres Arbeitsblatts anzuzeigen und durch jede Ansicht Ihres Arbeitsblatts unabhängig zu scrollen: geteilte Fenster.

Die Panes arbeiten gleichzeitig. Wenn Sie eine Änderung in einer vornehmen, erscheint die Änderung gleichzeitig in der anderen. Aspose.Cells bietet die Funktion für geteilte Fenster für die Benutzer.

### **Anwenden und Entfernen von geteilten Fenstern**

#### **Teilen von Fenstern**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um Split-Ansichten zu implementieren, verwenden Sie die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Methode der Klasse. Verwenden Sie zum Entfernen der Split-Panes die [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--)-Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, und dann wird das Feature der aufgeteilten Bereiche auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Window Example</title>
    </head>
    <body>
        <h1>Split Worksheet Window Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new workbook and open the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Set the active cell (converted from setActiveCell -> activeCell)
            sheet.activeCell = "A20";

            // Split the worksheet window
            sheet.split();

            // Save the excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet window split and active cell set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Nach Ausführung des obigen Codes hat die generierte Datei eine Split-Ansicht.

#### **Panes entfernen**

Entfernen Sie geteilte Fenster mit der Methode [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Remove Split Example</h1>
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

            // Instantiate a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Set the active cell
            worksheet.activeCell = "A20";

            // Split the worksheet window - remove any existing split
            worksheet.removeSplit();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Ausblenden der Anzeige von Nullwerten im Arbeitsblatt](/cells/de/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Arbeitsblattregisterfarbe festlegen](/cells/de/javascript-cpp/set-worksheet-tab-color/)
- [Gitternetzlinien und Zeilen- und Spaltenüberschriften anzeigen oder ausblenden](/cells/de/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Zeilen, Spalten und Bildlaufleisten anzeigen oder ausblenden](/cells/de/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Arbeitsblätter und Registerkarten anzeigen oder ausblenden](/cells/de/javascript-cpp/show-and-hide-worksheets-and-tabs/)
- [Formeln anstelle von Werten im Arbeitsblatt anzeigen](/cells/de/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Fehlerüberprüfungsoptionen verwenden](/cells/de/javascript-cpp/use-error-checking-options/)
