---
title: Arbetsbladsvyer med JavaScript via C++
linktitle: Arbetsboks vy
type: docs
weight: 40
url: /sv/javascript-cpp/worksheet-views/
description: Denna artikel kommer att beskriva hur man använder JavaScript och JavaScript API för att interagera med sidbrytningsförhandsgranskningen av en Excel arbetsbok och arbetsblad. Arbeta med delade fönster, frysta fönster och zoomfaktor också.
---

## **Sidbrytning Förhandsgranskning**

Alla arbetsblad kan visas i två lägen:

- Normal vy.
- Sidbrytningsvy.

Normalt läge är ett arbetsbads standardvy. Sidbrytning förhandsgranskning är en redigeringsvy som visar ett arbetsblad som det kommer att skriva ut. Sidbrytning förhandsgranskning visar vilken data som kommer att gå på varje sida så att du kan justera utskriftsområdet och sidbrytningar. Med Aspose.Cells for JavaScript via C++ kan utvecklare aktivera normalt läge eller sidbrytningsförhandsgranskningslägen.

### **Styra vynlägen**

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att aktivera normal vy eller sidbrytningsvy används [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassens [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)-egenskap. [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) är en boolesk egenskap, vilket innebär att den bara kan lagra ett värde **true** eller **false**.

#### **Aktivera normal vy**

Ställ in ett arbetsblad till normal vy genom att ange [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassens [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)-egenskap till **false**.

#### **Aktivera sidbrytningsvy**

Ställ in valfritt arbetsblad till sidbrytningsvy genom att ange [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassens [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)-egenskap till **true**. Detta gör att arbetsbladet byts från normal vy till sidbrytningsvy.

Ett komplett exempel visas nedan som demonstrerar hur man använder [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)-egenskapen för att aktivera sidbrytningsvy för det första arbetsbladet i en Excel-fil.

Filen book1.xls öppnas genom att skapa en instans av klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). Vyn byts till sidbrytningsvy för det första arbetsbladet genom att ange att [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--)-egenskapen är **true**. Den modifierade filen sparas som output.xls.

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

## **Zoomfaktor**

### **Använda Microsoft Excel**

Microsoft Excel har en funktion som låter användare sätta en arbetsblads zoom- eller skalfaktor. Denna funktion hjälper användare att se arbetsbladsinnehållet i mindre eller större visningar. Användare kan sätta zoom-faktorn till vilket värde som helst.

### **Aspose.Cells och Zoom Faktor**

Aspose.Cells tillåter utvecklare att sätta arbetsblads zoom-faktor.
Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassen innehåller en [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att sätta en arbetsblads zoom-faktor använder man egenskapen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) i [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) klassen. Zoom-faktorn sätts genom att tilldela ett numeriskt (heltals) värde till egenskapen [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--).

Ett komplett exempel ges nedan som demonstrerar hur man använder egenskapen [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) för att ställa in zoomfaktorn för det första arksnittet i Excel-filen.

book1.xls-filen öppnas genom att skapa en instans av [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen. Zoom-faktorn på det första arbetsbladet sätts till 75 och den modifierade filen sparas som output.xls.

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

## **Frys Fönsterpaneler**

### **Använda Microsoft Excel**

Frysa rutor är en funktion som tillhandahålls av Microsoft Excel. Att frysa rutor gör att man kan välja data som ska förbli synlig när man rullar i ett arbetsblad.

### **Aspose.Cells och Frysa rutor**

Aspose.Cells tillåter utvecklare att applicera frysfönster på arbetsblad vid körning.

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassen innehåller en [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arksnitt representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) klassen. Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) erbjuder ett brett utbud av egenskaper och metoder för att hantera arksnitt. För att konfigurera frysta paneler, anropa Worksheet-klassens [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) metod. [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysen ska starta från.
- **Kolumn**, kolumnindexet för cellen som frysen ska starta från.
- **Frusna rader**, antalet synliga rader i toppfönstret.
- **Frysta kolumner**, antalet synliga kolumner i vänsterpanelen.

book1.xls-filen öppnas genom att man kallar på konstruktorn till [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen medan man instansierar den och några rader och kolumner frysas i det första arbetsbladet. Den modifierade filen sparas som output.xls.

Ett komplett exempel nedan visar hur man använder sig av [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) metoden för att frysa rader och kolumner (som börjar från C4, representerat av den fjärde raden och tredje kolumnen, där raderna och kolumnerna börjar från index 0) på det första arbetsbladet i Excel-filen.

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

## **Dela rutor**

Om du behöver dela skärmen för att få två olika vyer i samma arbetsblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som gör att du kan se mer än en kopia av ditt arbetsblad och för dig att kunna bläddra igenom varje ruta av ditt arbetsblad oberoende av varandra: dela rutor.

Fönstren fungerar samtidigt. Om du gör en förändring i ett, visas förändringen samtidigt i den andra. Aspose.Cells tillhandahåller split panes-funktionen för användarna.

### **Sätta på och Ta bort Delade paneler**

#### **Dela Fönster**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att implementera split vyer använder man sig av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) metoden. För att ta bort delade rutor, använder man sig av [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--) metoden.

I exemplet använder vi en enkel mallfil som laddas, sedan används inställningar för att dela rutor på en cell i det första arbetsbladet. Den uppdaterade filen sparas.

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

Efter att ovanstående kod har körts, kommer den genererade filen ha en delad vy.

#### **Ta bort rutor**

Ta bort delade rutor med metoden [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--).

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

## **Fortsatta ämnen**
- [Dölja visning av nollvärden i kalkylbladet](/cells/sv/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Ange färg på kalkylbladsflik](/cells/sv/javascript-cpp/set-worksheet-tab-color/)
- [Visa och dölj rutnät och radkolumnhuvuden](/cells/sv/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Visa och dölj rader kolumner och skrollbar](/cells/sv/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Visa och dölj arbetsblad och flikar](/cells/sv/javascript-cpp/show-and-hide-worksheets-and-tabs/)
- [Visa formler istället för värden i ett arbetsblad](/cells/sv/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Använd felkontrollalternativ](/cells/sv/javascript-cpp/use-error-checking-options/)
