---
title: Sammanfogning och ogemantfogar celler med JavaScript via C++
linktitle: Sammanfoga och dela upp celler
description: Aspose.Cells är ett JavaScript bibliotek för att arbeta med kalkylbladsfiler, vilket stödjer sammanslagning och olamslagning av celler. Den här artikeln introducerar hur man slår ihop och olamslagar celler med Aspose.Cells biblioteket, med alternativ för att anpassa den sammanslagna cellens stil.
keywords: Aspose.Cells, JavaScript bibliotek, kalkylblad, slå samman celler, olamslagning av celler, stilinställningar, anpassade stilar
type: docs
weight: 190
url: /sv/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder den här funktionen och kan också sammanslå celler i ett kalkylblad. Du kan också dela upp eller splittra de sammanslagna cellerna. En sammanslagen cells cellreferens är referensen för den översta vänstra cellen i det ursprungliga markerade området.

{{% /alert %}} 
## **Introduktion**
Du vill inte alltid ha samma antal celler i varje rad eller kolumn. Till exempel kan du vilja lägga en titel i en cell som spänner över flera kolumner. Eller om du skapar en faktura kan du vilja ha färre kolumner för den totala summan. För att göra en cell från två eller flera celler, sammanslag dem. Microsoft Excel låter användare välja filer och sammanfoga dem för att strukturera kalkylbladet på önskat sätt.

{{% alert color="primary" %}} 

 Observera att när celler sammanfogas behålls endast data i det övre vänstra cellen. Om det finns data i de andra cellerna i området tas denna data bort. Formatering baseras också på referenscellen så att när du sammanfogar celler tillämpas formateringsinställningarna för den övre vänstra cellen i området på den sammanslagna cellen. När cellen delas behåller de nya cellerna sina ursprungliga formateringsinställningar.

{{% /alert %}} 
## **Sammanslagning av celler i ett kalkylblad**
### **Sammanslagning av celler i Microsoft Excel**
Följande steg beskriver hur man sammanslår celler i kalkylbladet med hjälp av MS Excel.

1. Kopiera den data du vill ha till den övre vänstra cellen inom området.
1. Välj cellerna du vill sammanfoga.
1. För att sammanfoga celler i en rad eller kolumn och centrera cellinnehållet klickar du på ikonen **Sammanfoga och centrerat** på verktygsfältet **Formatering**.

### **Sammanslagning av celler med Aspose.Cells**
Aspose.Cells.Cells-klassen har några användbara metoder för uppgiften. Till exempel sammanfogar metoden `merge()` cellerna till en enda cell inom ett specificerat område.

Följande exempel visar hur man slår samman celler (C6:E7) i en arbetsbok.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Avfussning (delning) av sammanslagna celler**
### **Använda Microsoft Excel**
Följande steg beskriver hur man delar sammanslagna celler med hjälp av Microsoft Excel.

1. Välj den sammanslagna cellen.
   När cellerna har kombinerats väljs **Slå samman och centrera** på **Formateringsverktygsfältet**.
1. Klicka på **Slå samman och centrera** på **Formateringsverktygsfältet**.

### **Använda Aspose.Cells**
Aspose.Cells.Cells-klassen har en metod som heter `unmerge()` som delar upp cellerna till deras ursprungliga tillstånd. Metoden avfogar cellerna med hjälp av cellens referens i det sammanslagna cellområdet.

Följande exempel visar hur man delar de sammanslagna cellerna (C6). Exemplet använder filen som skapades i det föregående exemplet och delar de sammanslagna cellerna.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Identifiera sammanslagna celler i ett kalkylblad](/cells/sv/javascript-cpp/detect-merged-cells-in-a-worksheet/)
