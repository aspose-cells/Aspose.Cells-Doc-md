---
title: Hantera data i Excel filer
linktitle: Cellers data
type: docs
weight: 110
url: /sv/javascript-cpp/view-and-edit-excel-data/
description: Den här artikeln beskriver hur man kan visa och redigera data i Excel filer med Aspose.Cells biblioteket för JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, Hantera data i Excel fil, lägg till data till Excel fil, hämta data från Excel fil, Hur man förbättrar effektiviteten vid tillägg av data, hantera cellers data, uppdatera cellers data, hämta cellers data, infoga cells data
---

{{% alert color="primary" %}}

I [Åtkomst till celler i ett arbetsblad](/cells/sv/javascript-cpp/accessing-cells-of-a-worksheet/) diskuterades grundläggande metoder för att komma åt celler i ett arbetsblad. Denna artikel använder en av dessa metoder för att lägga till olika typer av data till celler.

{{% /alert %}}

## **Hur man lägger till data i celler**

Aspose.Cells for JavaScript via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells tillåter utvecklare att lägga till data till cellerna i kalkylbladen genom att anropa [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassens [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-metod. Aspose.Cells erbjuder överlagrade versioner av [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-metoden som låter utvecklare lägga till olika typer av data i celler. Med dessa överlagrade versioner av [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-metoden kan man lägga till ett Boolean-värde, sträng, double, heltal eller datum/tid m.m. i en cell.

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
            const fileInput = document.getElementById('fileInput');
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **Hur man förbättrar effektiviteten**

Om du använder [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)-metoden för att lägga mycket data i en arbetsblad, bör du lägga till värden till cellerna först radvis och sedan kolumnvis. Detta förbättrar kraftigt effektiviteten i dina applikationer.

## **Hur man hämtar data från celler**

Aspose.Cells for JavaScript via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) samling som möjliggör åtkomst till arbetsblad i filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen ger en [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen.

Klassen [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) tillhandahåller flera egenskaper som gör att utvecklare kan hämta värden från celler baserat på deras datatyp. Dessa egenskaper inkluderar:

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): returnerar cellens värde som sträng.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): returnerar cellens dubbla värde.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): returnerar cellens booleanvärde.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): returnerar cellens datum/tid-värde.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): returnerar cellens flyttal värde.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): returnerar cellens heltalsvärde.

När ett fält inte är ifyllt, kastar celler med [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) eller [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) ett undantag.

Typen av data som finns i en cell kan också kontrolleras med [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassens [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--)-metod. Faktum är att [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassens [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--)-metod är baserad på [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype)-uppräkningen vars fördefinierade värden listas nedan:

|**Cellvärdestyper**|**Beskrivning**|
| :- | :- |
|IsBool| Specificerar att cellvärdet är Booleskt.
|IsDateTime| Specificerar att cellvärdet är datum/tid.
|IsNull| Representerar en tom cell.
|IsNumeric| Specificerar att cellvärdet är numeriskt.
|IsString| Specificerar att cellvärdet är en sträng.
|IsUnknown| Specificerar att cellvärdet är okänt.

Du kan även använda ovan nämnda fördefinierade cellvärdestyper för att jämföra med datatypen som finns i varje cell.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

När man arbetar med kalkylblad kan användare lägga till olika typer av data i cellerna. Dessa datatyper kan inkludera Boolean, heltal, flyttal, text eller datum/tid. Med Aspose.Cells kan du få rätt värden från cellerna enligt deras datatyper.

{{% /alert %}}

## **Fortsatta ämnen**
- [Tillgång till celler i ett arbetsblad](/cells/sv/javascript-cpp/accessing-cells-of-a-worksheet/)
- [Konvertera text numerisk data till nummer](/cells/sv/javascript-cpp/convert-text-numeric-data-to-number/)
- [Skapa delsummering](/cells/sv/javascript-cpp/creating-subtotals/)
- [Datafiltrering](/cells/sv/javascript-cpp/data-filtering/)
- [Data sortering](/cells/sv/javascript-cpp/sort-data-of-excel/)
- [Data validering](/cells/sv/javascript-cpp/data-validation/)
- [Hitta eller Sök Data](/cells/sv/javascript-cpp/find-or-search-data/)
- [Få cellsträngvärde med och utan formatering](/cells/sv/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [Lägg till HTML Rich Text i cellen](/cells/sv/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [Infoga hyperlänkar i Excel eller OpenOffice](/cells/sv/javascript-cpp/insert-hyperlinks-to-excel/)
- [Hur och var man använder uppräknare](/cells/sv/javascript-cpp/how-and-where-to-use-enumerators/)
- [Mät bredden och höjden på cellvärdet i enheten pixlar](/cells/sv/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Läsa cellvärden i flera trådar samtidigt](/cells/sv/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Konvertering mellan cellnamn och rad/kolumnindex](/cells/sv/javascript-cpp/names-and-indices/)
- [Fylla data först per rad och sedan per kolumn](/cells/sv/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [Bevara enskild citattecken prefiks av cellvärde eller område](/cells/sv/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Åtkomst och uppdatering av delar av riktad text från cellen](/cells/sv/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
