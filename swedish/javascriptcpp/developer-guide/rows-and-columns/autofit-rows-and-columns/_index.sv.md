---
title: Automatisk anpassning av rader och kolumner med JavaScript via C++
linktitle: Automatisk anpassning av rader och kolumner
type: docs
weight: 20
url: /sv/javascript-cpp/autofit-rows-and-columns/
description: Denna artikel visar hur man automatisk anpassar rader, kolumner, rader av sammanslagna celler och rader i ett cellområde med hjälp av Aspose.Cells for JavaScript via C++.
keywords: Autofit rader JavaScript via C++, autofit kolumner JavaScript via C++, autofit rad i ett cellområde JavaScript via C++, autofit rader av sammanslagna celler JavaScript via C++
---

{{% alert color="primary" %}}  
Microsoft Excel tillåter användare att automatiskt anpassa bredd och höjd på celler enligt deras innehåll. Den här funktionen är också tillgänglig via Aspose.Cells for JavaScript via C++, så utvecklare kan automatiskt anpassa dimensionerna på en cell vid körning.  
{{% /alert %}}  

## **Autostorlek**  

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som ger åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. Denna artikel tittar på hur man använder [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen för att autofit-rader eller kolumner.  

### **AutoFit Row - Enkelt**  

Det enklaste sättet att auto-anpassa bredd och höjd på en rad är att anropa [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassens [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-)-metod. [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-)-metoden tar ett radindex (på raden som ska ändras storlek på) som parameter.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>AutoFit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1 is the 2nd row; original code used 1)
            worksheet.autoFitRow(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Hur man Autofitrad i ett område av celler**  

En rad består av många kolumner. Aspose.Cells tillåter utvecklare att autofit-a en rad baserat på innehållet i ett cellområde inom raden genom att anropa en överlagrad version av [**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-)-metoden. Den tar följande parametrar:  

- **Radindex**, index för raden som ska autofit.  
- **Första kolumnindex**, index för radens första kolumn.  
- **Sista kolumnindex**, index för radens sista kolumn.  

[**autoFitRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRow-number-number-number-)-metoden kontrollerar innehållet i alla kolumner i raden och autofitar sedan raden.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoFit Row</title>
    </head>
    <body>
        <h1>Auto-Fit Row Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the 3rd row of the worksheet (row index 1, startColumn 0, endColumn 5)
            worksheet.autoFitRow(1, 0, 5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Hur man Autofittar kolumn i ett område av celler**  

En kolumn består av många rader. Det är möjligt att auto-anpassa en kolumn baserat på innehållet i ett cellområde i kolumnen genom att anropa en överlagrad version av [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-)-metoden som tar följande parametrar:  

- **Kolumnindex**, index för kolumnen som ska autofit.  
- **Första radindex**, index för kolumnens första rad.  
- **Sista radindex**, index för kolumnens sista rad.  

[**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-)-metoden kontrollerar innehållet i alla rader i kolumnen och autofitar sedan kolumnen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells AutoFit Column Example</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Auto-fitting the Column of the worksheet (column index 4)
            worksheet.autoFitColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column auto-fitted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Hur man Autofittar rader för sammanfogade celler**  

Med Aspose.Cells är det möjligt att autofit-a rader även för celler som har sammanslagits med hjälp av [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions)-API:et. [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions)-klassen tillhandahåller en [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--)-egenskap som kan användas för att autofit-a rader för sammanslagna celler. [**AutoFitterOptions.autoFitMergedCellsType()**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#autoFitMergedCellsType--) accepterar [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/javascript-cpp/autofitmergedcellstype)-enumeration som har följande medlemmar.  

- Ingen: Ignorera sammanslagna celler.  
- FörstaLinjen: Utökar endast höjden på den första raden.  
- SistaLinjen: Utökar endast höjden på den sista raden.  
- VarjeRad: Utökar endast höjden på varje rad.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows for Merged Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoFitterOptions, AutoFitMergedCellsType } = AsposeCells;

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

            // Create or load workbook
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Get the first (default) worksheet
            const worksheet = wb.worksheets.get(0);

            // Create a range A1:B1
            const range = worksheet.cells.createRange(0, 0, 1, 2);

            // Merge the cells
            range.merge();

            // Insert value to the merged cell A1
            const cell = worksheet.cells.get(0, 0);
            cell.value = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end";

            // Create a style object
            const style = cell.style;

            // Set wrapping text on
            style.isTextWrapped = true;

            // Apply the style to the cell
            cell.style = style;

            // Create an object for AutoFitterOptions
            const options = new AutoFitterOptions();

            // Set auto-fit for merged cells
            options.autoFitMergedCellsType = AutoFitMergedCellsType.EachLine;

            // Autofit rows in the sheet (including the merged cells)
            worksheet.autoFitRows(options);

            // Save the Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AutofitRowsforMergedCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Du kan också försöka använda de överlagrade versionerna av [**autoFitRows**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) & [**autoFitColumns**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-)-metoderna som accepterar ett rad- eller kolumnområde och en instans av [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) för att autofit-a de valda raderna/kolumnerna med önskad [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions).  

Signaturerna för dessa metoder är som följer:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Viktigt att veta**  

{{% alert color="primary" %}}  
Om en cell är sammanslagen kommer inte autoFit-metoderna att tillämpas, vilket är samma beteende som i Microsoft Excel. Du kan kringgå detta genom att använda autofilter-API:et. Dessutom, om texten i en cell är omsluten, kommer inte heller [**autoFitColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#autoFitColumn-number-)-metoden att tillämpas. En annan sak du bör veta är att *autoFit*-metoderna är tidskrävande. Så du bör använda dessa metoder så sällan som möjligt för att säkerställa att din applikation är effektiv.  
{{% /alert %}}  

## **Fortsatta ämnen**  
- [Automatisk justering av rader för sammanfogade celler](/cells/sv/javascript-cpp/autofit-rows-for-merged-cells/)
