---
title: Druckoptionen mit JavaScript via C++ einstellen
linktitle: Druckoptionen festlegen
type: docs
weight: 40
url: /de/javascript-cpp/setting-print-options/
description: Dieser Artikel demonstriert, wie man die Druckoptionen der Excel Tabellenblattseite Programmgesteuert mit der JavaScript API und C++ Bibliothek festlegt. Sie können den Druckbereich, Drucktitel und Seitenreihenfolge einstellen.
keywords: Excel Druckbereich mit JavaScript via C++ einstellen, Excel Drucktitel mit JavaScript via C++ einstellen, Seitenreihenfolge mit JavaScript via C++ einstellen
---

{{% alert color="primary" %}}

Die Seiteneinrichtungseinstellungen von Microsoft Excel bieten mehrere Druckoptionen (auch als Bogenoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden.

{{% /alert %}}

## **Druckoptionen einstellen**

Diese Druckoptionen ermöglichen es Benutzern:

- Einen bestimmten Druckbereich auf einem Arbeitsblatt auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Aspose.Cells for JavaScript via C++ unterstützt alle Druckoptionen, die von Microsoft Excel angeboten werden, und Entwickler können diese Optionen für Arbeitsblätter einfach mit den Eigenschaften der [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) Klasse konfigurieren. Wie diese Eigenschaften genutzt werden, wird unten im Detail besprochen.

### **Druckbereich festlegen**

Standardmäßig umfasst der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

Um einen spezifischen Druckbereich auszuwählen, verwenden Sie die Eigenschaft [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). Weisen Sie dieser Eigenschaft einen Zellenbereich zu, der den Druckbereich definiert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Area Example</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Specifying the cells range (from A1 cell to T35 cell) of the print area
            pageSetup.printArea = "A1:T35";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintArea_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Drucktitel festlegen**

Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften auf allen Seiten eines gedruckten Arbeitsblatts zu wiederholen. Verwenden Sie dazu die Eigenschaften [**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--) und [**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup).

Die zu wiederholenden Zeilen oder Spalten werden durch Übergabe ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Title</title>
    </head>
    <body>
        <h1>Set Print Title Columns and Rows Example</h1>
        <p>You may optionally select an existing Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Defining column numbers A & B as title columns
            pageSetup.printTitleColumns = "$A:$B";

            // Defining row numbers 1 & 2 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintTitle_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print title columns and rows set successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **Andere Druckoptionen festlegen**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) bietet auch mehrere andere Eigenschaften zur Festlegung allgemeiner Druckoptionen wie folgt:

- [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--): eine boolesche Eigenschaft, die festlegt, ob Gitterlinien gedruckt werden sollen oder nicht.
- [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--): eine boolesche Eigenschaft, die festlegt, ob Zeilen- und Spaltenüberschriften gedruckt werden sollen oder nicht.
- [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--): eine boolesche Eigenschaft, die festlegt, ob das Arbeitsblatt in Schwarz-Weiß-Modus gedruckt wird oder nicht.
- [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--): legt fest, ob die Druckkommentare im Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden sollen.
- [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--): eine boolesche Eigenschaft, die festlegt, ob das Blatt ohne Grafiken gedruckt wird.
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--): definiert, ob Zellfehler wie angezeigt, leer, Strich oder N/V gedruckt werden sollen.

Um die Eigenschaften [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) und [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) festzulegen, bietet Aspose.Cells for JavaScript via C++ auch zwei Aufzählungen, [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) und [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype), die vordefinierte Werte enthalten, die den Eigenschaften [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) und [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) zugewiesen werden können.

Die vordefinierten Werte der [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)-Aufzählung sind nachfolgend mit ihren Beschreibungen aufgelistet.

|**Druckkommentartypen**|**Beschreibung**|
| :- | :- |
|PrintInPlace| Gibt an, Kommentare so zu drucken, wie sie auf dem Arbeitsblatt angezeigt werden.|
|PrintNoComments| Gibt an, Kommentare nicht zu drucken.|
|PrintSheetEnd| Gibt an, Kommentare am Ende des Arbeitsblatts zu drucken.|

Die vordefinierten Werte der [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype)-Aufzählung sind nachfolgend mit ihren Beschreibungen aufgelistet.

|**Druckfehlertypen**|**Beschreibung**|
| :- | :- |
|PrintErrorsBlank| Gibt an, Fehler nicht zu drucken.|
|PrintErrorsDash| Gibt an, Fehler als "--" zu drucken.|
|PrintErrorsDisplayed| Gibt an, Fehler wie angezeigt zu drucken.|
|PrintErrorsNA| Gibt an, Fehler als "#N/A" zu drucken.|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Other Print Options</title>
    </head>
    <body>
        <h1>Other Print Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintCommentsType, PrintErrorsType } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = PrintErrorsType.PrintErrorsNA;

            // Saving the modified workbook to Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OtherPrintOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Seitenreihenfolge festlegen**

Die [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)-Klasse stellt die [**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--)-Eigenschaft bereit, mit der mehrere Seiten Ihres Arbeitsblatts zum Drucken geordnet werden können. Es gibt zwei Möglichkeiten, die Seiten zu ordnen, wie folgt.

-  druckt alle Seiten nach unten, bevor irgendwelche Seiten nach rechts gedruckt werden.
-  druckt Seiten links nach rechts, bevor die Seiten unten gedruckt werden.

Aspose.Cells stellt eine Aufzählung [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) bereit, die alle vordefinierten Ordnungstypen enthält.

Die vordefinierten Werte der [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype)-Aufzählung sind nachfolgend aufgelistet.

|**Druckreihenfolgetypen**|**Beschreibung**|
| :- | :- |
|DownThenOver|Stellt die Druckreihenfolge als zuerst nach unten und dann nach rechts dar.
|OverThenDown|Stellt die Druckreihenfolge als über dann nach unten dar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Set Page Order Example</title>
    </head>
    <body>
        <h1>Set Page Order Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintOrderType } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;
            pageSetup.order = PrintOrderType.OverThenDown;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPageOrder_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page order set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
