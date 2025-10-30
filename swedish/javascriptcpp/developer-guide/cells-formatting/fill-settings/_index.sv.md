---
title: Fyllningsinställningar
linktitle: Fyllningsinställningar
description: Lär dig hur du anpassar fyllningsinställningarna, bakgrunden och stilen för celler med Aspose.Cells biblioteket för JavaScript via C++.
keywords: Aspose.Cells, Celler, Fyllningsinställningar, Bakgrund, Stil, JavaScript via C++
type: docs
weight: 50
url: /sv/javascript-cpp/cells-fill-settings/
---

## **Färger och bakgrundsmönster**

Microsoft Excel kan ställa in förgrund (omridning) och bakgrundsfärger (fyllning) för celler och bakgrundsmönster.

Aspose.Cells stöder även dessa funktioner på ett flexibelt sätt. I det här avsnittet lär vi oss att använda dessa funktioner med hjälp av Aspose.Cells.

### **Inställning av färger och bakgrundsmönster**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som ger åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen ger en [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen.

 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) har egenskapen [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) som används för att få och ställa in en cells formatering. Klassen [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) tillhandahåller egenskaper för att ställa in cellens förgrunds- och bakgrundsfärger. Aspose.Cells tillhandahåller en [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) uppräkning som innehåller en uppsättning fördefinierade bakgrundsmönster som anges nedan.

|**Bakgrundsmönster**|**Beskrivning**|
| :- | :- |
|DiagonalCrosshatch|Representerar diagonalt kryssmönster|
|DiagonalStripe|Representerar diagonalt rutmönster|
|Gray6|Representerar 6,25% grått mönster|
|Gray12|Representerar 12,5% grått mönster|
|Gray25|Representerar 25% grått mönster|
|Gray50|Representerar 50% grått mönster|
|Gray75|Representerar 75% grått mönster|
|HorizontalStripe|Representerar horisontellt rutmönster|
|None|Representerar ingen bakgrund|
|ReverseDiagonalStripe|Representerar omvänd diagonalt rutmönster|
|Solid|Representerar enfärgat mönster|
|ThickDiagonalCrosshatch|Representerar tjockt diagonalt kryssmönster|
|ThinDiagonalCrosshatch|Representerar tunt diagonalt kryssmönster|
|ThinDiagonalStripe|Representerar tunt diagonalt rutmönster|
|ThinHorizontalCrosshatch|Representerar tunt horisontellt kryssmönster|
|ThinHorizontalStripe|Representerar tunt horisontellt rutmönster|
|ThinReverseDiagonalStripe|Representerar tunt omvänt diagonalt rutmönster|
|ThinVerticalStripe|Representerar tunt vertikalt rutmönster|
|VerticalStripe|Representerar vertikalt rutmönster|

I exemplet nedan är förgrundsfärgen för cellen A1 inställd men A2 är konfigurerad för att ha både förgrund och bakgrundsfärger med ett bakgrundsmönster med vertikal rand.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **Viktigt att veta**

{{% alert color="primary" %}}

- För att ställa in en cell's förgrunds- eller bakgrundsfärg, använd [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) objektets [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) eller [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) egenskaper. Båda träder i kraft endast om [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) objektets [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) egenskap är konfigurerad.
- [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) egenskapen sätter cellens nyansfärg. [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) egenskapen specificerar typen av bakgrundsmönster som används för förgrunds- eller bakgrundsfärgen. Aspose.Cells erbjuder en uppräkning, [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype), som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.
- Om du väljer *BackgroundType.None* värde från [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) uppräkningen, tillämpas inte förgrundsfärgen. Likaså tillämpas inte bakgrundsfärgen om du väljer värdena *BackgroundType.None* eller *BackgroundType.Solid*.
- Vid hämtning av cellens skugg-/fyllfärg, om [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) är *BackgroundType.None*, kommer [**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) att returnera *Color.Empty*.

{{% /alert %}}

### **Tillämpning av gradientfylleffekter**

För att tillämpa ditt önskade gradientfyllningseffekter på cellen, använd [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) objektets [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) egenskap därefter.

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Färger och Palett**

En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.

Med Aspose.Cells är det möjligt att inte bara använda palettens befintliga färger utan också anpassade färger. Innan du använder en anpassad färg, lägg till den först i paletten.

Detta ämne diskuterar hur man lägger till anpassade färger i paletten.

### **Lägga till Anpassade Färger i Paletten**

Aspose.Cells stöder Microsoft Excels 56-färgspalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen i paletten.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-)-metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:

- Anpassad färg, den anpassade färgen som ska läggas till.
- Index, index för färgen i paletten som den anpassade färgen kommer att ersätta. Ska vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg (Orchid) i paletten innan den tillämpas på en font.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och alla element i filen formaterade med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast då det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.

{{% /alert %}}
