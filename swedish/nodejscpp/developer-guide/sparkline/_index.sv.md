---
title: Sparklinjer i Aspose.Cells for Node.js via C++
linktitle: Sparklinjer i Aspose.Cells for Node.js via C++
description: Aspose.Cells är ett Node.js-bibliotek för att arbeta med kalkylbladsfiler som stöder skapande av sparklinjer — miniatyrdiagram placerade inuti kalkylbladsceller. Denna artikel förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklinjer med Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Node.js-bibliotek, kalkylblad, sparklinjer, linje-sparklinje, kolumn-sparklinje, vinst/förlust-sparklinje, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder skapande av sparklinjer inuti kalkylbladsceller. Sparklinjer är miniatyrdiagram som passar inom en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklinjer, och var och en kan anpassas med avseende på färg, linjetjocklek, hög/låg-punkter och markeringar.

## **Introduktion**
Sparklinjer är små diagram i celler som är användbara när du vill visa en snabb trend bredvid en rad eller kolumn med data utan att ta upp utrymmet för ett helt diagram. Excel stöder tre typer av sparklinjer: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet genom API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `Aspose.Cells.Charts`.
I Aspose.Cells skapas varje sparklinje du lägger till via `worksheet.sparklineGroups.add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ställa in sparklinjetyp, dataområde, målcell och visuella egenskaper som linjefärg, linjetjocklek, markeringar och indikatorer för hög/låg-punkter.
Denna artikel går igenom var och en av de tre sparklinjetyper som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklinjer**
En linje-sparklinje ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör det till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparklinje genom att skicka `SparklineType.Line` till metoden `sparklineGroups.add`.
1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumn A till E) med de värden du vill visualisera.
3. Skapa en `CellArea` som beskriver målcellen där sparklinjen ska ritas.
4. Anropa `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Det tredje argumentet — `false` — talar om för Aspose.Cells att dataområdet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparklinje kan du ställa in linjefärgen med `group.line.color` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken och växla markeringar för hög/låg-punkter.
6. Spara arbetsboken.
Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till E1, och lägger till en linje-sparklinje i cell F1 som spårar dessa värden. Det anpassar också linjefärgen till röd och aktiverar markeringar för hög- och låg-punkterna.

```javascript
const AsposeCells = require("aspose.cells");
// Steg 1: Skapa en arbetsbok och hämta det första kalkylbladet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Steg 3: Bygg ett CellArea som pekar på destinationscell F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // kolumn F (0-indexerad)
dest.setEndColumn(5);
dest.setStartRow(0);      // rad 1 (0-indexerad)
dest.setEndRow(0);
// Steg 4: Lägg till en linje-sparkline från A1:E1 i F1
// SparklineGroups.Add returnerar index för den nyligen tillagda gruppen
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjens färg
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Steg 6: Aktivera markörer för högsta och lägsta punkt
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Steg 7: Spara arbetsboken
workbook.save("output_line.xlsx");
```

## **Kolumn-sparklinjer**
En kolumn-sparklinje renderar varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparklinje genom att skicka `SparklineType.Column` till metoden `sparklineGroups.add`.
Proceduren speglar exemplet med linje-sparklinje:
1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
2. Bygg en `CellArea` som beskriver målcellen.
3. Anropa `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
4. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att ställa in `group.type` för att bekräfta typen, eller genom att justera stapelfärgen.
5. Spara arbetsboken till en separat utdatafil så att den inte skriver över exemplet med linje-sparklinje.
Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumn-sparklinje i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör positiva och negativa bidrag lätta att se direkt.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Steg 2: Skriv exempelvärden till A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Steg 3: Bygg en CellArea som pekar mot F1 (kolumnindex 5, radindex 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Steg 4: Lägg till en kolumnsparkline i målcellen
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Steg 5: Bekräfta sparkline-typen genom att läsa group.Type
console.log("Sparkline Type added: " + group.getType());
// Steg 6: Spara arbetsboken
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Vinst/Förlust-sparklinjer**
En vinst/förlust-sparklinje är en speciell variant av kolumn-sparklinjen som är utformad för att visa endast två utfall: ett positivt värde ritas som en "upp"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "ned"-stapel (en förlust). Vinst/förlust-sparklinjer används vanligtvis för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat, eller andra binära utfall över tid.
I Aspose.Cells skapas en vinst/förlust-sparklinje genom att skicka `SparklineType.Stacked` till metoden `sparklineGroups.add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-rendering.)
1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
2. Fyll källområdet. Eftersom vinst/förlust-sparklinjer behandlar varje värde som antingen en vinst eller en förlust spelar storleken på värdet ingen roll — bara dess tecken. Positiva värden blir upp-staplar och icke-positiva värden blir ned-staplar.
3. Skapa en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förlust-staplarna.
6. Spara arbetsboken under ett distinkt filnamn så att alla tre exemplen kan samexistera på disk.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Steg 2: Fyll i exempeldata i rad 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Steg 3: Bygg ett CellArea som pekar mot F1 (kolumn 5, rad 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // rad 1
dest.setEndRow(0);
// Steg 4: Lägg till en Win/Loss-sparkline (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Steg 5: Anpassa sparkline-gruppen
// Aktivera markeringar för hög- och lågpunkter
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Ställ in högpunktens färg till grön
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// Ställ in lågpunktens färg till röd
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// Ställ in negativa punkters färg till orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// Ställ in standardfärg för serien (används för positiva staplar)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// Steg 6: Spara arbetsboken
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinera alla tre sparklinjetyper**
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6, och lägger sedan till tre sparklinjegrupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparklinjestilar samtidigt.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Steg 3: Lägg till en linjesparklinegrupp i F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Anpassa linjesparklinefärgen via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// Steg 4: Lägg till en kolumn-sparklinegrupp i F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Anpassa seriefärgen för kolumn-sparkline
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// Steg 5: Lägg till en vinst/förlust-sparklinegrupp (staplad) i F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Anpassa seriefärgen för vinst/förlust-sparkline
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// Steg 6: Spara arbetsboken
workbook.save("output_all.xlsx");
```

## **Anpassa sparklinjers utseende**
När en `SparklineGroup` har skapats och lagts till i `worksheet.sparklineGroups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De vanligaste anpassade egenskaperna är:
- **`group.type`** — `SparklineType` (Linje, Kolumn eller Stacked). Den ställs in när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.line.color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.createCellsColor()`. Detta är egenskapen som ska användas för linje-sparklinjens streckfärg.
- **`group.line.weight`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Hög/Låg-punktmarkeringar** — flaggor som aktiverar små markeringar på de högsta och lägsta datapunkterna, användbara för att betona extremvärden.
- **Första/Sista/Negativa punktmarkeringar** — flaggor som växlar markeringar på den första, sista och negativa datapunkterna.
För att ändra en färg, skapa alltid en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte en `System.Drawing.Color` direkt till sparklinjers färgegenskaper — de förväntar sig `CellsColor`-typen från `Aspose.Cells.Drawing`. Själva metoden `sparklineGroups.add` returnerar ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}