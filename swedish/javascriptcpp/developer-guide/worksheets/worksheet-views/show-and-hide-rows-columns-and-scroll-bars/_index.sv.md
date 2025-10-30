---
title: Visa och Dölj Rader, Kolumner och Skrollfält med JavaScript via C++
linktitle: Visa och Dölja rader, Kolumner och Rullningslistor
type: docs
weight: 20
url: /sv/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/
description: Denna artikel visar hur man programmässigt visar och döljer rader och kolumner i ett Excel ark med JavaScript via C++. Kontrollera synligheten för skrollfält och dölja flera rader och kolumner effektivt.
---

{{% alert color="primary" %}}  
Aspose.Cells tillhandahåller sätt att kontrollera synligheten av rader, kolumner och rullningslistor på ett kalkylblad.  
{{% /alert %}}  

## **Visa och göm rader och kolumner**  

Aspose.Cells for JavaScript via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) samling som ger utvecklare möjlighet att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) ger en [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) samling som representerar alla celler i arbetsbladet. Samlingen [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) tillhandahåller flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan.  

### **Visa Rader och Kolumner**  

Utvecklare kan visa vilken dold rad eller kolumn som helst genom att anropa metoderna [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) och [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) av [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen respektive. Båda metoder tar två parametrar:  

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.  
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unhide Row and Column Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.unhideRow(2, 13.5);
            worksheet.cells.unhideColumn(1, 8.5);

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

{{% alert color="primary" %}}  
När du gör en dold kolumn synlig, om du behöver återställa den till den tidigare tilldelade eller ursprungliga bredden, vänligen gör kolumnen ovisbar med negativ bredd. Till exempel: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Dölj Rader och Kolumner**  

Utvecklare kan dölja en rad eller kolumn genom att anropa metoderna [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) och [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) av [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen respektive. Båda metoder tar rad- och kolumnindex som parameter för att dölja den specifika raden eller kolumnen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Hide Row/Column Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Hide the 3rd row (index 2) and 2nd column (index 1)
            worksheet.cells.hideRow(2);
            worksheet.cells.hideColumn(1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row and column hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.  
{{% /alert %}}  

### **Dölj Flera Rader och Kolumner**  

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa metoderna [**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-) och [**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-) av [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen respektive. Båda metoder tar startrad- eller startkolumnindex och antalet rader eller kolumner som ska döljas som parametrar.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Rows and Columns</title>
    </head>
    <body>
        <h1>Hide Rows and Columns Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4 and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

            // Saving the modified Excel file
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

## **Visa och dölj bildrullningsfält**  

Rullningslistor används för att navigera bland innehållet i en fil. Vanligtvis finns det två typer av rullningslistor:  

- Vertikala bildrullningsfält  
- Horisontella bildrullningsfält  

Microsoft Excel tillhandahåller också horisontella och vertikala bildrullningsfält så att användare kan bläddra genom arbetsbladets innehåll. Med Aspose.Cells kan utvecklare kontrollera synligheten av båda typer av bildrullningsfält i Excelfiler.  

### **Kontrollera Synligheten för Rullningslistor**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för rullningsfält, använd egenskaperna [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) och [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) och [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) är booleska egenskaper, vilket betyder att dessa egenskaper endast kan lagra **true** eller **false** värden.  

#### **Gör bildrullningsfält synliga**  

Gör rullningsfält synliga genom att ställa in [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) -klassens egenskaper [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) eller [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) till **true**.  

#### **Dölja bildrullningsfält**  

Dölj rullningsfält genom att ställa in egenskaperna [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) -klassens [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) eller [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) till **false**.  

**Exempelkod**  

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, gömmer båda rullningsfälten och sparar sedan den modifierade filen som output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Hide Scrollbars Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the vertical scroll bar of the Excel file
            workbook.settings.isVScrollBarVisible = false;

            // Hiding the horizontal scroll bar of the Excel file
            workbook.settings.isHScrollBarVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scrollbars hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
