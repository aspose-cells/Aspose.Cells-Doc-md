---
title: Kantinställningar
linktitle: Kantinställningar
description: Hur man använder Aspose.Cells biblioteket i JavaScript via C++ för att ställa in kantlinjestil och färg på celler. Genom att justera bredd, stil och färg på kanten får du större kontroll över hur cellerna ser ut och visas.
keywords: Aspose.Cells, Cellgränseinställningar, JavaScript via C++, Gränsebreddsbredd, Gränsstil, Gränsfärg
type: docs
weight: 40
url: /sv/javascript-cpp/cells-border-settings/
---

## **Lägga till ramar till celler**

Microsoft Excel låter användare formatera celler genom att lägga till kanter. Typen av kant beror på var den läggs till. Till exempel är en övre kant en som läggs till i cellens övre position. Användare kan också ändra linjestilen och färgen på kanterna.

Med Aspose.Cells for JavaScript via C++, kan utvecklare lägga till ramar och anpassa deras utseende på samma flexibla sätt som i Microsoft Excel.

### **Lägga till ramar till celler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen.

Aspose.Cells tillhandahåller egenskapen [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) i klassen [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) används för att ställa in cellens formateringsstil. Klassen [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) tillhandahåller egenskaper för att lägga till ramar till celler.

#### **Lägga till ramar till en cell**

Utvecklare kan lägga till kanter till en cell genom att använda [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektets [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)-samling. Kantens typ anges som ett index i [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)-samlingen. Alla kanttyper är fördefinierade i [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype)-enumerationen.

**Kantuppräkning**

|**Ramtyper**|**Beskrivning**|
| :- | :- |
|BottomBorder|En nederkantslinje|
|DiagonalDown|En diagonal linje från övre vänster till höger nedan|
|DiagonalUp|En diagonal linje från nedre vänster till höger upp|
|LeftBorder|En vänsterkantlinje|
|RightBorder|En högerkantlinje|
|TopBorder|En övre kantlinje|

Kollektionssamlingen [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) innehåller alla kanter. Varje kant i [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--)-kollektionen representeras av ett [**Border**](https://reference.aspose.com/cells/javascript-cpp/border)-objekt som tillhandahåller två egenskaper, [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) och [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-), för att ställa in kantlinjens färg och stil respektive.

För att ställa in en gräns linfärg, välj en färg med hjälp av färguppräkningen (del av JavaScript) och tilldela den till Border-objektets färg-egenskap.

Kantlinjens stil anges genom att välja en linje från [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype)-enumerationen.

**CellBorderType-enumen**

|**Linjestilar**|**Beskrivning**|
| :- | :- |
|DashDot|Tunn streckpunktad linje|
|DashDotDot|Tunn streck-punktpunktad linje|
|Dashed|Streckad linje|
|Dotted|Punkterad linje|
|Double|Dubbel linje|
|Hair|Hårlinje|
|MediumDashDot|Medium streckpunktad linje|
|MediumDashDotDot|Medium streck-punktpunktad linje|
|MediumDashed|Medium streckad linje|
|None|Ingen linje|
|Medium|Medium linje|
|SlantedDashDot|Snedstreckad mediumstreckpunktad linje|
|Thick|Tjock linje|
|Thin|Tunn linje|
Välj en av linjestilarna och tilldela den till [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) objektets [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) egenskap.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
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

{{% alert color="primary" %}}
Du bör ställa in både linjestil och färg samtidigt. De två diagonala kantlinjerna ska ha samma linjestil och färg.
{{% /alert %}}

#### **Lägga till Gränser till en Rad av Celler**

Det är också möjligt att lägga till ramar till ett cellområde snarare än en enskild cell. För att göra det, först skapa ett cellområde genom att anropa [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingens [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-)-metod. Den tar följande parametrar:

- Första rad, den första raden av området.
- Första kolumn, representerar den första kolumnen av området.
- Antal rader, antalet rader i området.
- Antal kolumner, antalet kolumner i området.

Metoden [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) returnerar ett [**Range**](https://reference.aspose.com/cells/javascript-cpp/range)-objekt, som innehåller det angivna cellområdet. [**Range**](https://reference.aspose.com/cells/javascript-cpp/range)-objektet ger en [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-)-metod som tar följande parametrar för att lägga till en ram till cellområdet:

- **Ramtipo**, ramens typ, vald från [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype) enumarationen.
- **Linjestil**, ramens linjestil, vald från [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype) enumarationen.
- **Färg**, linjens färg, vald från Färg uppräkningen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
