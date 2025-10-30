---
title: Format celler med JavaScript via C++
description: Lär dig hur man formaterar och stiliserar celler i Aspose.Cells for JavaScript via C++, inklusive nummerformatering, datumenformatering, typsnittstyper och andra cellstilstilval. Vår guide hjälper dig att skapa attraktiva och professionella kalkylblad.
keywords: Aspose.Cells for JavaScript via C++, cellformatering, styling, nummerformat, datumenformatering, typsnittsstil, cellstiltillval, kalkylblad, skapa, professionellt utseende, formatera rader och kolumner.
linktitle: Formatera celler
type: docs
weight: 120
url: /sv/javascript-cpp/cells-formatting/
---

## **Introduktion**

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) och [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) metoder för [Cell](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen, som används för att få/sett formateringsstil för en cell. Aspose.Cells erbjuder också en [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) klass.

{{% /alert %}}

## **Hur man formaterar celler med stilmetoder**

Tillämpa olika typer av formateringsstilar på celler för att ställa in bakgrund eller förgrundsfärger, ramar, typsnitt, horisontell och vertikal justering, indenteringsnivå, textriktning, rotationsvinkel och mycket mer.

### **Hur man använder stilmetoderna**

Om utvecklare behöver tillämpa olika formateringsstilar på olika celler är det bättre att få [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) av cellen med hjälp av [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)-metoden, specificera stilde attributes och sedan tillämpa formateringen med [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)-metoden. Ett exempel ges nedan för att demonstrera detta tillvägagångssätt för att tillämpa olika formatering på en cell.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hur man använder Style-objektet för att formatera olika celler**

Om utvecklare behöver tillämpa samma formateringsstil på olika celler kan de använda [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet. Följ stegen nedan för att använda [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet:

1. Lägg till ett [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objekt genom att anropa [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--)-metoden av [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen
2. Åtkomst till det nyss tillagda [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet
3. Sätt de önskade egenskaperna/attributen för [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet för att tillämpa önskad formateringsinställning
4. Tilldela det konfigurerade [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet till dina önskade celler

Denna metod kan avsevärt förbättra effektiviteten i dina applikationer och spara minne också.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Hur man använder Microsoft Excel 2007 Fördefinierade Stilar**

Om du behöver tillämpa olika formateringsstilar för Microsoft Excel 2007, tillämpa stilar med hjälp av Aspose.Cells API. Ett exempel ges nedan för att visa denna metod att tillämpa en fördefinierad stil på en cell.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **Hur man formaterar valda tecken i en cell**

Hantera typsnittsinställningar förklarar hur man formaterar text i celler, men det förklarar bara hur man formaterar allt cellinnehåll. Vad händer om du vill formatera endast utvalda tecken?

Aspose.Cells stöder också denna funktion. Denna guide förklarar hur man använder denna funktion effektivt.

### **Hur man formaterar valda tecken**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som tillåter åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen.

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen tillhandahåller [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-)-metoden som tar följande parametrar för att välja ett teckenintervall inom en cell:

- **Startindex**, index för tecknet som urvalet börjar från.
- **Antal tecken**, antalet tecken att välja.

'[**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-)'-metoden returnerar en instans av [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)-klassen som tillåter utvecklare att formatere tecknen på samma sätt som de skulle formatera en cell, som visas nedan i kodexemplet. I utdatafilen kommer ordet 'Visit' i cell A1 att formateras med standardteckensnitt men 'Aspose!' är fetstilt och blå.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Om du är intresserad av att formatera en del av Rich Text i en cell, överväg att använda [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) & [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)-metoderna. [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--)-metoden används för att komma åt textdelarna och sedan kan ändringar göras med [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)-metoden medan 'Get'-metoden returnerar en array av [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)-objekt som kan manipuleras för att ställa in olika egenskaper såsom teckensnittnamn, teckenfärg, fetstil m.m. och 'Set'-metoden kan användas för att tillämpa ändringarna.

{{% /alert %}}

## **Hur man formaterar rader och kolumner**

Ibland behöver utvecklare tillämpa samma formatering på rader eller kolumner. Att tillämpa formatering på celler en i taget tar ofta längre tid och är inte en bra lösning.
För att lösa detta problem tillhandahåller Aspose.Cells ett enkelt, snabbt sätt som diskuteras utförligt i den här artikeln.

### **Formatering av rader & kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen ger en [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samling. [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen ger en [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--)-samling.

### **Hur man formaterar en rad**

Varje objekt i [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--)-samlingen representerar ett [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)-objekt. [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)-objektet erbjuder [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)-metoden som används för att ställa in radens formatering. För att tillämpa samma formatering på en rad, använd [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet. Stegen nedan visar hur man använder det.

1. Lägg till ett [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objekt till [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen genom att anropa dess [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--)-metod.
2. Sätt egenskaperna för [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet för att tillämpa formateringsinställningarna.
3. Gör de relevanta attributen ON för [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)-objektet.
4. Tilldela det konfigurerade [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet till [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)-objektet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Hur man formaterar en kolumn**

[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen ger också en [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--)-samling. Varje objekt i [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--)-samlingen representerar ett [**Column**](https://reference.aspose.com/cells/javascript-cpp/column)-objekt. Liknande ett [**Row**](https://reference.aspose.com/cells/javascript-cpp/row)-objekt, erbjuder [**Column**](https://reference.aspose.com/cells/javascript-cpp/column)-objektet också [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)-metoden för att formatera en kolumn.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Justering inställningar](/cells/sv/javascript-cpp/cells-alignment-settings/)
- [Kantinställningar](/cells/sv/javascript-cpp/cells-border-settings/)
- [Ställa in villkorlig formatering av Excel och ODS-filer.](/cells/sv/javascript-cpp/conditional-formatting/)
- [Excel-teman och färger](/cells/sv/javascript-cpp/excel-themes-and-colors/)
- [Fyllinställningar](/cells/sv/javascript-cpp/cells-fill-settings/)
- [Typsnittinställningar](/cells/sv/javascript-cpp/cells-font-settings/)
- [Formatera kalkylbladsceller i en arbetsbok](/cells/sv/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [Implementera 1904 Datasystem](/cells/sv/javascript-cpp/implement-1904-date-system/)
- [Sammanfoga och dela upp celler](/cells/sv/javascript-cpp/merging-and-unmerging-cells/)
- [Antalseinställningar](/cells/sv/javascript-cpp/cells-number-settings/)
- [Hämta och ange stil för celler](/cells/sv/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
