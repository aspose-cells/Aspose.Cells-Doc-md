---
title: Infoga och ta bort rader och kolumner i Excelfil
linktitle: Infoga och ta bort rader och kolumner
type: docs
weight: 70
url: /sv/javascript-cpp/inserting-and-deleting-rows-and-columns/
description: Den här artikeln visar hur man infogar och tar bort rader och kolumner med Aspose.Cells for JavaScript via C++ API.
keywords: Aspose.Cells JavaScript via C++ hanterar rader och kolumner, infogar rader och kolumner, tar bort rader och kolumner
---

## **Introduktion**

Oavsett om du skapar en ny arbetsbok från grunden eller arbetar med en befintlig arbetsbok kan vi behöva lägga till extra rader eller kolumner för att rymma mer data. Å andra sidan kan det också hända att vi behöver ta bort rader eller kolumner från angivna positioner i arbetsboken. 
För att uppfylla dessa krav tillhandahåller Aspose.Cells for JavaScript via C++ en mycket enkel uppsättning av klasser och metoder, diskuterade nedan.

### **Hantera rader och kolumner**

Aspose.Cells for JavaScript via C++ tillhandahåller en klass [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) samling som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) samling som representerar alla celler i kalkylbladet.

Samlingen [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) ger flera metoder för att hantera rader och kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}}

När rader eller kolumner läggs till skiftas innehållet i arbetsbladet nedåt eller åt höger, och om rader eller kolumner tas bort skiftas innehållet uppåt eller åt vänster.

{{% /alert %}}


## **Infoga rader och kolumner**

### **Hur man infogar en rad**

Infoga en rad i kalkylbladet på valfri plats genom att anropa [**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-)-metoden i [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen. Metoden [**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) tar indexet för raden där den nya raden ska infogas.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert Row Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting a row into the worksheet at 3rd position (index 2)
            worksheet.cells.insertRow(2);

            // Saving the modified Excel file as Excel97To2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hur man infogar flera rader**

För att infoga flera rader i ett kalkylblad, anropa [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-)-metoden i [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen. Metoden [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, det totala antalet rader som ska infogas.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Rows Example</title>
    </head>
    <body>
        <h1>Insert Rows Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting 10 rows into the worksheet starting at index 2
            worksheet.cells.insertRows(2, 10);

            // Saving the modified Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hur man infogar en rad med formatering**

För att infoga en rad med formateringsalternativ, använd överbelastningen [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) som tar [**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions) som parameter. Sätt egenskapen [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) för [**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions)-klassen med [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/)-enum. [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) enum har tre medlemmar listade nedan.

- SameAsAbove: Formaterar raden samma som ovanstående rad.
- SameAsBelow: Formaterar raden liknande raden nedanför.
- Rensa: Rensar formateringen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Inserting a Row With Formatting Example</title>
    </head>
    <body>
        <h1>Inserting a Row With Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, InsertOptions, CopyFormatType, Utils } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting Formatting options
            const insertOptions = new InsertOptions();
            insertOptions.copyFormatType = CopyFormatType.SameAsAbove;

            // Inserting a row into the worksheet at 3rd position
            worksheet.cells.insertRows(2, 1, insertOptions);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertingARowWithFormatting.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hur man infogar en kolumn**

Utvecklare kan också infoga en kolumn i kalkylbladet på valfri plats genom att anropa [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertColumn-number-boolean-)-metoden i [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen. Metoden [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertColumn-number-boolean-) tar indexet för kolumnen där den nya kolumnen ska infogas.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Insert Column Example</title>
    </head>
    <body>
        <h1>Insert Column Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting a column into the worksheet at 2nd position
            worksheet.cells.insertColumn(1);

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ta bort rader och kolumner**

### **Hur man tar bort flera rader**

För att ta bort flera rader från ett kalkylblad, anropa [**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-)-metoden i [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen. Metoden [**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, det totala antalet rader som ska tas bort.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Delete Rows Example</title>
    </head>
    <body>
        <h1>Delete Rows Example</h1>
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

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Deleting 10 rows from the worksheet starting from 3rd row (index 2)
            worksheet.cells.deleteRows(2, 10);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Hur man tar bort en kolumn**

För att ta bort en kolumn från kalkylbladet på valfri plats, anropa [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteColumn-number-boolean-)-metoden i [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen. Metoden [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteColumn-number-boolean-) tar indexet för kolumnen som ska tas bort.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Column Example</title>
    </head>
    <body>
        <h1>Delete Column Example</h1>
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

            // Deleting a column from the worksheet at 5th position (zero-based index 4)
            worksheet.cells.deleteColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
