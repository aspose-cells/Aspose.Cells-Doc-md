---
title: Skapa och kopiera namngivna områden med JavaScript via C++
linktitle: Skapa åtkomst och kopiera namngivna intervall
type: docs
weight: 200
url: /sv/javascript-cpp/create-access-and-copy-named-ranges/
description: Lär dig hur du skapar, får åtkomst till och kopierar namngivna områden i Excel med Aspose.Cells for JavaScript via C++.
---

## **Introduktion**  

Vanligtvis används kolumn- och radetiketter för att referera till enskilda celler. Det är möjligt att skapa beskrivande namn för att representera celler, områden av celler, formler eller konstanter. Ordet **namn** kan referera till en sträng av tecken som representerar en cell, ett område av celler, en formel eller ett konstant värde. Att tilldela ett namn till ett område betyder att detta område kan refereras till med dess namn. Använd lättförståeliga namn, som Produkter, för att referera till svårförståeliga områden, som Försäljning!C20:C30. Etiketterna kan användas i formler som hänvisar till data på samma kalkylblad; vill du representera ett område på ett annat kalkylblad kan du använda ett namn. *Namngivna områden är en av de mäktigaste funktionerna i Microsoft Excel, särskilt när de används som datakälla för listkontroller, pivottabeller, diagram och liknande.*  

## **Arbeta med namngivet intervall med Microsoft Excel**  

### **Skapa namngivna intervall**  

Följande steg beskriver hur du namnger en cell eller ett cellområde med **MS Excel**. Denna metod gäller för **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** och **2002**.  

1. Välj den cell eller det cellområde som du vill namnge.  
2. Klicka på **Namnrutan** till vänster om formelfältet.  
3. Skriv in namnet för cellerna.  
4. Tryck på ENTER.  

{{% alert color="primary" %}}  
Du kan inte namnge en cell medan du ändrar innehållet i cellen.  
{{% /alert %}}  

## **Arbeta med namngivna områden med hjälp av Aspose.Cells**  

Här använder vi Aspose.Cells API för att utföra uppgiften.  
Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samling.  

### **Skapa namngivet område**  

Det är möjligt att skapa ett namngivet område genom att anropa den överlagrade metoden [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) i samlingen [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). En vanlig version av [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-)-metoden tar följande parametrar:  

- Namn på övre vänstra cell, namnet på den översta vänstra cellen i området.  
- Namnet på den nedre högra cellen, namnet på den längst ner till höger i området.  

När metoden [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) kallas returneras det nysskapade området som en instans av klassen [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). Använd detta [**Range**](https://reference.aspose.com/cells/javascript-cpp/range)-objekt för att konfigurera det namngivna området. Till exempel, ställ in namnet på området med hjälp av egenskapen [**name**](https://reference.aspose.com/cells/javascript-cpp/range/#name--). Följande exempel visar hur man skapar ett namngivet område av celler som sträcker sig över B4:G14.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating a named range
            const range = worksheet.cells.createRange("B4", "G14");

            // Setting the name of the named range
            range.name = "TestRange";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Ange data i cellerna i det namngivna området**  

Du kan sätta in data i de individuella cellerna i ett område enligt mönstret  

- **JavaScript**: Range[row,column]  

Säg att du har ett namngivet område av celler som sträcker sig över A1:C4. Matrisen skapar 4 * 3 = 12 celler. De individuella områdets celler är arrangerade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Använd följande egenskaper för att identifiera cellerna i området:  

- firstRow returnerar indexen för den första raden i det namngivna området.  
- firstColumn returnerar indexen för den första kolumnen i det namngivna området.  
- rowCount returnerar det totala antalet rader i det namngivna området.  
- columnCount returnerar det totala antalet kolumner i det namngivna området.  

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = workbook.worksheets.get(0);

            // Create a range of cells based on H1:J4.
            const range = worksheet1.cells.createRange("H1", "J4");

            // Name the range.
            range.name = "MyRange";

            // Input some data into cells in the range.
            range.get(0, 0).value = "USA";
            range.get(0, 1).value = "SA";
            range.get(0, 2).value = "Israel";
            range.get(1, 0).value = "UK";
            range.get(1, 1).value = "AUS";
            range.get(1, 2).value = "Canada";
            range.get(2, 0).value = "France";
            range.get(2, 1).value = "India";
            range.get(2, 2).value = "Egypt";
            range.get(3, 0).value = "China";
            range.get(3, 1).value = "Philipine";
            range.get(3, 2).value = "Brazil";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rangecells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range populated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **Identifiera celler i det namngivna området**  

Du kan sätta in data i de individuella cellerna i ett område enligt mönstret:  

- **JavaScript**: Range[row,column]  

Om du har ett namngivet område som sträcker sig över A1:C4. Matrisen skapar 4 * 3 = 12 celler. De individuella områdets celler är arrangerade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Använd följande egenskaper för att identifiera cellerna i området:  

- firstRow returnerar indexen för den första raden i det namngivna området.  
- firstColumn returnerar indexen för den första kolumnen i det namngivna området.  
- rowCount returnerar det totala antalet rader i det namngivna området.  
- columnCount returnerar det totala antalet kolumner i det namngivna området.  

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Named Range</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const range = workbook.worksheets.rangeByName("TestRange");

            if (!range) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
                return;
            }

            // Identify range cells and display properties
            const firstRow = range.firstRow;
            const firstColumn = range.firstColumn;
            const rowCount = range.rowCount;
            const columnCount = range.columnCount;

            const html = [
                `<p>First Row : ${firstRow}</p>`,
                `<p>First Column : ${firstColumn}</p>`,
                `<p>Row Count : ${rowCount}</p>`,
                `<p>Column Count : ${columnCount}</p>`
            ].join('');

            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

### **Åtkomst till namngivna områden**  

#### **Åtkomst till ett specifikt namngivet område**  

Anropa [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)-kollektionens [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-)-metod för att få ett område med det angivna namnet. En typisk [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-)-metod tar namnet på det namngivna området och returnerar det angivna namngivna området som en instans av klassen [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). Följande exempel visar hur man åtkommer ett angivet område med dess namn.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const worksheets = workbook.worksheets;
            const range = worksheets.rangeByName("TestRange");

            if (range !== null) {
                document.getElementById('result').innerHTML = `<p>Named Range : ${range.refersTo}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
            }
        });
    </script>
</html>
```  

#### **Åtkomst till alla namngivna områden i ett kalkylblad**  

Anropa [**worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) samlingens [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) metod för att få alla namngivna områden i ett kalkylblad. [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) metoden returnerar en array av alla namngivna områden i [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) samlingen.  

Följande exempel visar hur man åtkommer alla namngivna områden i en arbetsbok.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Named Ranges</title>
    </head>
    <body>
        <h1>Get Named Ranges Example</h1>
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

            // Getting all named ranges
            const ranges = workbook.worksheets.namedRanges;

            if (ranges) {
                // Some collections expose 'count', others may expose 'length'
                const total = (typeof ranges.count !== 'undefined') ? ranges.count : ranges.length;
                document.getElementById('result').innerHTML = `<p style="color: green;">Total Number of Named Ranges: ${total}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No named ranges found.</p>';
            }
        });
    </script>
</html>
```  

### **Kopiera namngivna områden**  

Aspose.Cells tillhandahåller [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-pasteoptions-)-metoden för att kopiera ett cellområde med formatering till ett annat område.  

Följande exempel visar hur man kopierar en källräcka med celler till ett annat namngivet område.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Ranges</title>
    </head>
    <body>
        <h1>Copy Ranges Example</h1>
        <p>Select an Excel file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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

            // Instantiate a new Workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = workbook.worksheets.get(0);

            // Create a range of cells.
            const range1 = worksheet.cells.createRange("E12", "I12");

            // Name the range.
            range1.name = "MyRange";

            // Set the outline border to the range.
            range1.outlineBorder = { borderType: BorderType.TopBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.BottomBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.LeftBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.RightBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };

            // Input some data with some formattings into a few cells in the range.
            range1.get(0, 0).putValue("Test");
            range1.get(0, 4).putValue("123");

            // Create another range of cells.
            const range2 = worksheet.cells.createRange("B3", "F3");

            // Name the range.
            range2.name = "testrange";

            // Copy the first range into second range.
            range2.copy(range1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyranges.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
