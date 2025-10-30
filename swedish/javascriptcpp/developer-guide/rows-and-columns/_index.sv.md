---
title: Formatera rader och kolumner med JavaScript via C++
linktitle: Rader och kolumner
type: docs
weight: 100
url: /sv/javascript-cpp/adjusting-row-height-and-column-width/
description: Aspose.Cells for JavaScript via C++ kan stödja ändring av radhöjd eller kolumnbredd, samt tillämpa formatering på rader eller kolumner.
keywords: Ange radhöjd och kolumnbredd, Justera radhöjd och kolumnbredd, ändra radhöjd eller kolumnbredd, formatera rader och kolumner, hur man anger radhöjd och kolumnbredd.
---

{{% alert color="primary" %}}
 När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra radens höjd eller kolumnens bredd. Ibland innebär tillämpning av formatering på rader eller kolumner att den aktuella höjden eller bredden måste ändras för att visa datan. Normalt justerar användare radhöjd och kolumnbredd i en WYSIWYG-miljö med Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer i realtid.
{{% /alert %}}

## **Arbeta med rader**

### **Hur man justerar radhöjden**

Aspose.Cells for JavaScript via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) som ger åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samling som representerar alla celler i arbetsbladet.

 Samlingen [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) erbjuder flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan i mer detalj.

### **Hur man ställer in höjden på en rad**

 Det är möjligt att ange höjden för en enskild rad genom att anropa {}-samlingens {}-metod. {}-metoden tar följande parametrar:

- **Radindex**, index för den rad vars höjd du ändrar.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Row Height Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.rows.get(1).height = 13;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hur man ställer in höjden på alla rader i ett kalkylblad**

 Om utvecklare behöver sätta samma radhöjd för alla rader i arbetsbladet kan de göra det genom att använda [**standardHeight()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardHeight--)-egenskapen hos [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Standard Row Height</title>
    </head>
    <body>
        <h1>Set Standard Row Height Example</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the height of all rows in the worksheet to 15
            worksheet.cells.standardHeight = 15;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Standard row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Arbeta med kolumner**

### **Hur man ställer in bredden på en kolumn**

 Sätt kolumnbredden genom att anropa [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingens [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-)-metod. [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-)-metoden tar följande parametrar:

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Column Width Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Set Column Width</button>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of the second column to 17.5
            worksheet.cells.columns.get(1).width = 17.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hur man ställer in kolumnbredd i pixlar**

 Sätt kolumnbredden genom att anropa [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingens [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-)-metod. [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-)-metoden tar följande parametrar:

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd i pixlar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Column Width In Pixels</title>
    </head>
    <body>
        <h1>Set Column Width In Pixels</h1>
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

            // Set the width of the column in pixels
            // Converted from: worksheet.getCells().setColumnWidthPixel(7, 200);
            // UNIVERSAL GETTER/SETTER CONVERSION applied:
            worksheet.cells.columnWidthPixel = [7, 200];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetColumnWidthInPixels_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hur man ställer in bredden på alla kolumner i en arbetsbok**

 För att sätta samma kolumnbredd för alla kolumner i arbetsbladet använd [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingens [**standardWidth()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardWidth--)-egenskap.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Standard Width Example</title>
    </head>
    <body>
        <h1>Set Standard Width Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of all columns in the worksheet to 20.5
            worksheet.cells.standardWidth = 20.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Standard width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [AutoAnpassa rader och kolumner](/cells/sv/javascript-cpp/autofit-rows-and-columns/)
- [Konvertera Text till Kolumner med Aspose.Cells](/cells/sv/javascript-cpp/convert-text-to-columns-using-aspose-cells/)
- [Kopiera rader och kolumner](/cells/sv/javascript-cpp/copying-rows-and-columns/)
- [Ta bort tomma rader och kolumner i en arbetsbok](/cells/sv/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/)
- [Gruppering och avgruppering av rader och kolumner](/cells/sv/javascript-cpp/grouping-and-ungrouping-rows-and-columns/)
- [Dölja och visa rader och kolumner](/cells/sv/javascript-cpp/hiding-and-showing-rows-and-columns/)
- [Infoga eller ta bort rader i en Excel-arbetsbok](/cells/sv/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/)
- [Infoga och ta bort rader och kolumner i Excel-fil](/cells/sv/javascript-cpp/inserting-and-deleting-rows-and-columns/)
- [Ta bort dubblettrader i ett kalkylblad](/cells/sv/javascript-cpp/remove-duplicate-rows-in-a-worksheet/)
- [Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad](/cells/sv/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
