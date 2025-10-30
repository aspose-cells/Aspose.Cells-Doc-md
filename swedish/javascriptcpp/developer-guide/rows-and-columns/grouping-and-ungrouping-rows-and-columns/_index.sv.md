---
title: Grupp och Omgående av rader och kolumner med JavaScript via C++
linktitle: Gruppering och avgruppering av rader och kolumner
type: docs
weight: 50
url: /sv/javascript-cpp/grouping-and-ungrouping-rows-and-columns/
description: Upptäck hur du grupperar och avgrupperar rader och kolumner i Excel med Aspose.Cells for JavaScript via C++.
---

## **Introduktion**

I en Microsoft Excel-fil kan du skapa en översikt över data för att kunna visa och dölja detaljnivåer med en enda musklick.

Klicka på **Översiktssymbolerna**, 1,2,3, + och - för att snabbt visa endast de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en individuell sammanfattning eller rubrik som visas nedan i figuren:

|**Gruppering av rader och kolumner.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Grupperingshantering av rader och kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samling som representerar alla celler i kalkylbladet.

[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen ger flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras nedan i mer detalj.

### **Gruppering av rader och kolumner**

Det är möjligt att gruppera rader eller kolumner genom att anropa [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#groupRows-number-number-boolean-) och [**groupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#groupColumns-number-number-)-metoderna i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen. Båda metoderna tar följande parametrar:

- Första radens/kolumnens index, den första raden eller kolumnen i gruppen.
- Sista radens/kolumnens index, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Rows and Columns Example</title>
    </head>
    <body>
        <h1>Group Rows and Columns Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows and columns grouped successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **Gruppinställningar**

Microsoft Excel tillåter att du konfigurerar gruppinställningar för att visa:

- Sammanfattande rader under detaljer.
- Sammanfattande kolumner till höger om detaljer.

Utvecklare kan konfigurera dessa gruppinställningar med [**outline**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#outline--)-egenskapen i [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen.

### **Sammanfattande rader nedanför detalj**

Det är möjligt att kontrollera om sammanfattningsrader visas under detaljer genom att sätta [**Outline**](https://reference.aspose.com/cells/javascript-cpp/outline)-klassens [**summaryRowBelow**](https://reference.aspose.com/cells/javascript-cpp/outline/#summaryRowBelow--)-egenskap till **true** eller **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Group Rows/Columns and Set Outline</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Grouping first six rows and first three columns
            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            // Setting SummaryRowBelow property to false
            worksheet.outline.summaryRowBelow = false;

            // Saving the modified Excel file (Excel97To2003 -> .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Sammanfattande kolumner till höger om detalj**

Utvecklare kan också kontrollera visningen av sammanfattningskolumner till höger om detaljer genom att sätta [**summaryColumnRight**](https://reference.aspose.com/cells/javascript-cpp/outline/#summaryColumnRight--)-egenskapen i [**Outline**](https://reference.aspose.com/cells/javascript-cpp/outline)-klassen till **true** eller **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Group Rows and Columns Example</h1>
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

            // Grouping first six rows and first three columns
            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            // Set summary column to right
            worksheet.outline.summaryColumnRight = true;

            // Saving the modified Excel file (Excel 97-2003 format)
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

## **Avgruppering av rader och kolumner**

För att ogruppera några grupperade rader eller kolumner, ring [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingens [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupRows-number-number-boolean-)- och [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupColumns-number-number-)-metoder. Båda metoderna tar två parametrar:

- Första radens/kolumnens index, den första raden/kolumnen att avgrupperas.
- Sista radens/kolumnens index, den sista raden/kolumnen att avgrupperas.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupRows-number-number-boolean-) har en överbelastning som tar en tredje Boolean-parameter. Att ställa in den till **true** tar bort all gruppinformation. Annars tas bara den yttre gruppinformationen bort.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Ungroup Rows and Columns Example</h1>
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

            // Instantiating a Workbook object with file content
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Ungrouping first six rows (from 0 to 5)
            worksheet.cells.ungroupRows(0, 5);

            // Ungrouping first three columns (from 0 to 2)
            worksheet.cells.ungroupColumns(0, 2);

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
