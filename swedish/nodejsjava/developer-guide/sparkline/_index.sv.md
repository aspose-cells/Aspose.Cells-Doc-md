---
title: Sparklines i Aspose.Cells for Node.js via Java
linktitle: Sparklines i Aspose.Cells for Node.js via Java
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
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Steg 3: Bygg en CellArea som pekar på målcellen F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // kolumn F (0-indexerad)
dest.setEndColumn(5);
dest.setStartRow(0);      // rad 1 (0-indexerad)
dest.setEndRow(0);
// Steg 4: Lägg till en linje-sparkline från A1:E1 i F1
// SparklineGroups.Add returnerar index för den nyligen tillagda gruppen
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjens färg
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Steg 6: Aktivera markörer för hög- och lågpunkt
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Steg 7: Spara arbetsboken
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
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Steg 2: Skriv exempelvärden till A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Steg 3: Skapa ett CellArea som pekar mot F1 (kolumnindex 5, radindex 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Steg 4: Lägg till en kolumnsparkline i målcellen
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Steg 5: Bekräfta sparklinjetypen genom att läsa group.Type
console.log("Sparkline Type added: " + group.getType());
// Steg 6: Spara arbetsboken
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
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Steg 2: Fylla i exempeldata i rad 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Steg 3: Bygg en CellArea som pekar mot F1 (kolumn 5, rad 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // rad 1
dest.setEndRow(0);
// Steg 4: Lägg till en Vinst/Förlust-sparkline (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Steg 5: Anpassa sparkline-gruppen
// Aktivera markörer för hög- och lågpunkt
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Ställ in färgen för högpunkten till grön
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Ställ in färgen för lågpunkten till röd
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Ställ in färgen för negativa punkter till orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Ställ in standardfärg för serien (används för positiva staplar)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Steg 6: Spara arbetsboken
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinera alla tre sparkline-typer**
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar samtidigt.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Steg 3: Lägg till en linje-sparklinegrupp vid F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Anpassa linje-sparklinefärgen via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Steg 4: Lägg till en kolumn-sparklinegrupp vid F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Anpassa kolumn-sparkline-seriefärgen
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Steg 5: Lägg till en vinst/förlust (staplad) sparklinegrupp vid F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Anpassa vinst/förlust-sparkline-seriefärgen
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Steg 6: Spara arbetsboken
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

{{< app/cells/assistant language="javascript" >}}