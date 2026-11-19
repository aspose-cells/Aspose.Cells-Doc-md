---
title: Sparklines i Aspose.Cells for Node.js via Java
linktitle: Sparklines
description: Aspose.Cells är ett Node.js via Java-bibliotek för att arbeta med kalkylbladsfiler som stöder skapande av sparklines — miniatyrdiagram placerade inuti kalkylbladsceller. Den här artikeln förklarar hur du lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylblad, sparklines, linjesparkline, kolumnsparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder skapande av sparklines inuti kalkylbladsceller. Sparklines är miniatyrdiagram som passar inom en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stödjer linje-, kolumn- och vinst/förlust-sparklines, och varje typ kan anpassas med avseende på färg, linjetjocklek, högsta/lägsta punkter samt markörer.
{{% /alert %}}

## **Introduktion**
Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend bredvid en rad eller kolumn med data utan att ta upp utrymmet för ett fullstort diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet genom API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `com.aspose.cells.Charts`.
I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.SparklineGroups.add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ställa in sparkline-typen, dataområdet, destinationscellen samt visuella egenskaper som linjefärg, linjetjocklek, markörer och indikatorer för högsta/lägsta punkt.
Den här artikeln går igenom alla tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur du lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linjesparklines**
En linjesparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linjesparkline genom att skicka `SparklineType.Line` till metoden `SparklineGroups.add`.
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumn A till E) med de värden du vill visualisera.
3. Skapa en `CellArea` som beskriver destinationscellen där sparklinen ska ritas.
4. Anropa `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Det tredje argumentet — `false` — anger att dataområdet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Valfritt: anpassa den returnerade `SparklineGroup`. För en linjesparkline kan du ställa in linjefärgen med `group.Line.Color` (som förväntar sig en `CellsColor` från `com.aspose.cells.Drawing`), justera linjetjockleken samt aktivera markörer för högsta/lägsta punkt.
6. Spara arbetsboken.
Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till E1 och lägger till en linjesparkline i cell F1 som följer dessa värden. Det anpassar också linjefärgen till röd och aktiverar markörer för högsta och lägsta punkt.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;   // column F (0-indexed)
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1 (0-indexed)
dest.EndRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Kolumnsparklines**
En kolumnsparkline återger varje datapunkt som ett vertikalt stapeldiagram. Detta gör den väl lämpad för data där storleken är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumnsparkline genom att skicka `SparklineType.Column` till metoden `SparklineGroups.add`.
Proceduren speglar exemplet med linjesparkline:
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumn A till E) med de värden du vill visualisera.
3. Skapa en `CellArea` som beskriver destinationscellen.
4. Anropa `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Valfritt: anpassa den resulterande `SparklineGroup` — till exempel genom att ställa in `group.Type` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken i en separat utdatafil så att den inte skriver över exemplet med linjesparkline.
Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumnsparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att se positiva och negativa bidrag med en blick.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.COLUMN, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Vinst/Förlust-sparklines**
En vinst/förlust-sparkline är en speciell variant av kolumnsparkline som är utformad för att endast visa två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat eller andra binära utfall över tid.
I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.Stacked` till metoden `SparklineGroups.add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-renderingen.)
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets storlek ingen roll — endast dess tecken gör det. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Skapa en `CellArea` som beskriver destinationscellen.
4. Anropa `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Valfritt: anpassa den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett unikt filnamn så att alla tre exemplen kan samexistera på disk.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Build a CellArea pointing to F1 (column 5, row 0)
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;   // F
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1
dest.EndRow = 0;
// Step 4: Add a Win/Loss sparkline (SparklineType.STACKED)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.STACKED,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinera alla tre sparkline-typer**
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar samtidigt.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.COLUMN, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.STACKED, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Anpassa sparkline-utseendet**
När en `SparklineGroup` har skapats och lagts till i `worksheet.SparklineGroups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De vanligaste egenskaperna att anpassa är:
- **`group.Type`** — `SparklineType` (Linje, Kolumn eller Stacked). Den ställs in när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.Line.Color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.createCellsColor()`. Detta är egenskapen som ska användas för streckfärgen hos en linjesparkline.
- **`group.Line.Weight`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Högsta/Lägsta punktmarkörer** — flaggor som aktiverar små markörer på de högsta och lägsta datapunkterna, användbart för att betona extremvärden.
- **Första/Sista/Negativa punktmarkörer** — flaggor som växlar markörer på den första, sista och negativa datapunkten.
För att ändra en färg ska du alltid skapa en `CellsColor`-instans och tilldela den till relevant egenskap. Tilldela inte en `java.awt.Color` direkt till sparkline-färgegenskaper — de förväntar sig typen `CellsColor` från `com.aspose.cells.Drawing`. Metoden `SparklineGroups.add` returnerar i sig ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.

{{< app/cells/assistant language="nodejs-java" >}}