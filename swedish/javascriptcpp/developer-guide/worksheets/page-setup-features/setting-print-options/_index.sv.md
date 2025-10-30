---
title: Ställ in utskriftsalternativ med JavaScript via C++
linktitle: Inställning av utskriftsalternativ
type: docs
weight: 40
url: /sv/javascript-cpp/setting-print-options/
description: Denna artikel visar hur man programmatiskt ställer in utskriftsalternativen för Excel arkets sidinställning med JavaScript API och C++ bibliotek. Du kan ställa in utskriftsområdet, utskriftstitlar och sidordning.
keywords: ställ in excel utskriftsområde JavaScript via C++, ställ in excel utskriftstitlar JavaScript via C++, ställ in excel sidordning JavaScript via C++
---

{{% alert color="primary" %}}

Microsoft Excels sidoinställningsinställningar ger flera utskriftsalternativ (även kallade kalkylblad) som låter användare styra hur kalkylbladssidor skrivs ut.

{{% /alert %}}

## **Ställa in utskriftsalternativ**

Dessa utskriftsalternativ låter användare:

- Välja ett specifikt utskriftsområde på en arbetsbok.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.

Aspose.Cells for JavaScript via C++ stöder alla utskriftsalternativ som erbjuds av Microsoft Excel och utvecklare kan enkelt konfigurera dessa alternativ för kalkylblad med hjälp av egenskaperna som erbjuds av [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)-klassen. Hur dessa egenskaper används diskuteras nedan i mer detalj.

### **Ange utskriftsområde**

Som standard omfattar utskriftsområdet alla områden på kalkylbladet som innehåller data. Utvecklare kan skapa ett specifikt utskriftsområde för kalkylbladet.

För att välja ett specifikt utskriftsområde, använd egenskapen [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) i klassen [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). Tilldela en cellintervall som definierar utskriftsområdet till denna egenskap.

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

### **Ställ in utskriftstitlar**

Aspose.Cells låter dig ange att rad- och kolumnrubriker ska upprepas på alla sidor av en utskriven arbetsbok. Gör så genom att använda egenskaperna [**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--) och [**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--) i klassen [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup).

Rader eller kolumner som kommer att upprepas definieras genom att ange deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

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

### **Ange andra utskriftsalternativ**

Klassen [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) tillhandahåller också flera andra egenskaper för att ange allmänna utskriftsalternativ enligt följande:

- [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--): en boolesk egenskap som definierar om rutnätslinjer ska skrivas ut eller inte.
- [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--): en boolesk egenskap som definierar om rad- och kolumnrubriker ska skrivas ut eller inte.
- [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--): en boolesk egenskap som definierar om bladet ska skrivas ut i svartvitt eller inte.
- [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--): anger vilken utskriftskommentarerna ska visas på kalkbladet eller i slutet av kalkbladet.
- [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--): en boolesk egenskap som anger om bladet ska skrivas ut utan grafik.
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--): definierar om cellfel ska skrivas ut som visas, tom, streck eller N/A.

 För att ställa in [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) och [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) egenskaper, tillhandahåller Aspose.Cells for JavaScript via C++ också två enumereringar, [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) och [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) som innehåller fördefinierade värden att tilldela egenskaperna [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) och [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--).

De fördefinierade värdena i uppräkningen [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) listas nedan med deras beskrivningar.

|**Kommentarstyper för utskrift**|**Beskrivning**|
| :- | :- |
|PrintInPlace|Specificerar att skriva ut kommentarer som visas på kalkylbladet.|
|PrintNoComments|Specificerar att inte skriva ut kommentarer.|
|PrintSheetEnd|Specificerar att skriva ut kommentarer i slutet av kalkylbladet.|

De fördefinierade värdena för uppräkningen [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) listas nedan med deras beskrivningar.

|**Feltyper för utskrift**|**Beskrivning**|
| :- | :- |
|PrintErrorsBlank|Anger inte att skriva ut felmeddelanden.|
|PrintErrorsDash|Anger att skriva ut fel som "--".|
|PrintErrorsDisplayed|Anger att skriva ut fel som visas.|
|PrintErrorsNA|Anger att skriva ut fel som "#N/A".|

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

### **Ange sidordning**

Klassen [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) tillhandahåller egenskapen [**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--) som används för att ordna flera sidor av ditt kalkblad som ska skrivas ut. Det finns två möjligheter att ordna sidorna på följande sätt.

-  skriver ut alla sidor nedan innan någon sida skrivs ut till höger.
-  skriver ut sidor från vänster till höger innan sidorna nedanför.

Aspose.Cells tillhandahåller en uppräkning, [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) som innehåller alla fördefinierade typer av ordningar.

De fördefinierade värdena för uppräkningen [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) listas nedan.

|**Utskriftsordningstyper**|**Beskrivning**|
| :- | :- |
|DownThenOver|Representerar utskriftsordning nedåt och sedan över.|
|OverThenDown|Representerar utskriftsordning över och sedan nedåt.|

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
