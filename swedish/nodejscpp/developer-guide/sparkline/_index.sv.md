---
title: Sparklines i Aspose.Cells for Node.js via C++
linktitle: Sparklines
description: Aspose.Cells är ett Node.js-bibliotek för att arbeta med kalkylarksfiler som stöder skapande av sparklines — miniatyrdiagram placerade inuti kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Node.js-bibliotek, kalkylark, sparklines, linje-sparkline, kolumn-sparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder skapande av sparklines inuti kalkylbladsceller. Sparklines är miniatyrdiagram som får plats inom en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och varje typ kan anpassas med avseende på färg, linjetjocklek, hög-/låg-punkter samt markörer.

{{% /alert %}}

## **Introduktion**

Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymmet för ett helt diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet genom API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `Aspose.Cells.Charts`.

I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.sparklineGroups.add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ange sparkline-typ, dataintervall, målcell och visuella egenskaper som linjefärg, linjetjocklek, markörer samt indikatorer för högsta/lägsta punkt.

{{% alert color="primary" %}}

En enskild `SparklineGroup` kan innehålla en eller flera sparklines som delar samma stil. När du anropar `add` och skickar en rad med data plus en enda målcell får du en sparkline i den cellen. Om ditt målintervall är bredare än en cell ritas en separat sparkline i varje målcell, alla med samma stil och dataintervall.

{{% /alert %}}

Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinster/Förluster** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**

En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.Line` till metoden `sparklineGroups.add`.

Arbetsflödet är detsamma som för alla andra sparkline-typer:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll i en rad med källdata (till exempel rad 1, kolumnerna A till och med E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen där sparkline ska ritas.
4. Anropa `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Det tredje argumentet — `false` — anger att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Valfritt: anpassa den returnerade `SparklineGroup`. För en linje-sparkline kan du ange linjefärgen via `group.line.color` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken och aktivera markörer för högsta/lägsta punkt.
6. Spara arbetsboken.

Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till och med E1 och lägger till en linje-sparkline i cell F1 som följer dessa värden. Det anpassar också linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

```javascript
const AsposeCells = require("aspose.cells");

// Steg 1: Skapa en Workbook och hämta det första kalkylbladet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Steg 3: Bygg en CellArea som pekar på målcell F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // kolumn F (0-indexerad)
dest.setEndColumn(5);
dest.setStartRow(0);      // rad 1 (0-indexerad)
dest.setEndRow(0);

// Steg 4: Lägg till en linje-sparkline från A1:E1 till F1
// SparklineGroups.Add returnerar indexet för den nyligen tillagda gruppen
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);

// Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjefärgen
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Steg 6: Aktivera markörer för hög- och lågpunkt
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Steg 7: Spara arbetsboken
workbook.save("output_line.xlsx");
```

## **Kolumn-sparklines**

En kolumn-sparkline renderar varje datapunkt som ett vertikalt stapeldiagram. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.Column` till metoden `sparklineGroups.add`.

Proceduren speglar exemplet med linje-sparkline:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll i samma källintervall (A1:E1) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Valfritt: anpassa den resulterande `SparklineGroup` — till exempel genom att sätta `group.type` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken till en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.

Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumn-sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att urskilja positiva och negativa bidrag med en blick.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Steg 2: Skriv exempelvärden i A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Steg 3: Bygg en CellArea som pekar på F1 (kolumnindex 5, radindex 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Steg 4: Lägg till en Column-sparkline i destinationscellen
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Steg 5: Bekräfta sparkline-typen genom att läsa group.Type
console.log("Sparkline Type added: " + group.getType());

// Steg 6: Spara arbetsboken
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Vinster/Förluster-sparklines**

En vinst/förlust-sparkline är en speciell variant av kolumn-sparkline som är utformad för att visa endast två utfall: ett positivt värde ritas som en "upp"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "ner"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat eller andra binära utfall över tid.

I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.Stacked` till metoden `sparklineGroups.add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-renderingen.)

Proceduren är densamma som för de andra två typerna:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll i källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar storleken på värdet ingen roll — bara dess tecken. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Valfritt: anpassa den returnerade `SparklineGroup`, till exempel genom att ange accentfärger för vinst- och förluststaplar.
6. Spara arbetsboken under ett unikt filnamn så att alla tre exempel kan samexistera på disken.

Exemplet nedan använder samma indata som de två föregående avsnitten. Värdena 5, -3, 8, -2, 6 tolkas som vinst, förlust, vinst, förlust, vinst — och sparkline i F1 återspeglar exakt det mönstret.

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

// Steg 3: Bygg ett CellArea som pekar på F1 (kolumn 5, rad 0)
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
// Aktivera markörer för hög- och lågpunkt
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Sätt högpunktens färg till grön
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);

// Sätt lågpunktens färg till röd
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);

// Sätt negativa punkters färg till orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);

// Sätt standardfärg för serien (används för positiva staplar)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// Steg 6: Spara arbetsboken
workbook.save("output_winloss.xlsx");

console.log("Arbetsboken har sparats: output_winloss.xlsx");
```

## **Kombinera alla tre sparkline-typerna**

De tre föregående exemplen producerar var sin egen arbetsbok så att utdatafilerna är enkla att inspektera var för sig. I ett verkligt scenario vill man dock ofta jämföra flera dataserier sida vid sida. Det renaste sättet att göra det är att lägga mer än en sparkline-grupp i samma kalkylblad, där varje grupp renderar en annan stil.

Du kan lägga till flera `SparklineGroup`-objekt i samma `SparklineGroupCollection`, och varje grupp kan rikta in sig på en annan målcell eller ett annat intervall. Till exempel kan du placera en linje-sparkline i F1, en kolumn-sparkline i F2 och en vinst/förlust-sparkline i F3 — alla läser från samma källdata i rad 1 — så att läsaren kan se tre olika visuella behandlingar av samma siffror.

Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar på en gång.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Steg 2: Fylla i exempeldata i rad 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Steg 3: Lägg till en linje-sparkline-grupp vid F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Anpassa linje-sparkline-färgen via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// Steg 4: Lägg till en kolumn-sparkline-grupp vid F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Anpassa färgen för kolumn-sparkline-serien
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// Steg 5: Lägg till en Vinst/Förlust (Staplad) sparkline-grupp vid F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Anpassa färgen för vinst/förlust-sparkline-serien
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// Steg 6: Spara arbetsboken
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

När du kombinerar flera sparkline-grupper i ett enda kalkylblad är varje grupp oberoende. De kan dela samma källintervall eller använda olika källintervall, och de kan stilas oberoende av varandra. Detta gör det enkelt att bygga en liten "instrumentpanel" med visualiseringar i celler direkt inuti ett befintligt kalkylblad.

{{% /alert %}}

## **Anpassa sparkline-utseendet**

När en `SparklineGroup` har skapats och lagts till i `worksheet.sparklineGroups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De vanligaste egenskaperna att anpassa är:

- **`group.type`** — `SparklineType` (Line, Column eller Stacked). Den sätts när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.line.color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.createCellsColor()`. Detta är egenskapen att använda för streckfärg på linje-sparklines.
- **`group.line.weight`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Markörer för högsta/lägsta punkt** — flaggor som aktiverar små markörer på de högsta och lägsta datapunkterna, användbara för att betona extremvärden.
- **Markörer för första/sista/negativa punkt** — flaggor som växlar markörer för den första, sista respektive negativa datapunkten.

För att ändra en färg ska du alltid skapa en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte en `System.Drawing.Color` direkt till sparkline-färgegenskaper — de förväntar sig typen `CellsColor` från `Aspose.Cells.Drawing`. Själva metoden `sparklineGroups.add` returnerar ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.



{{< app/cells/assistant language="javascript" >}}