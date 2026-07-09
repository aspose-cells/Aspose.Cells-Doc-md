---
title: Sparklinjer i Aspose.Cells for Node.js via Java
linktitle: Sparklines
description: Aspose.Cells är ett Node.js via Java-bibliotek för att arbeta med kalkylbladsfiler som stöder skapande av sparklinjer — miniatyrdiagram placerade i kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklinjer med Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylblad, sparklinjer, linjesparklinje, kolumnsparklinje, vinst/förlust-sparklinje, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder skapande av sparklinjer i kalkylbladsceller. Sparklinjer är miniatyrdiagram som får plats i en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklinjer, och varje typ kan anpassas med avseende på färg, linjetjocklek, högsta/lägsta punkter samt markörer.

{{% /alert %}}

## **Introduktion**

Sparklinjer är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymmet för ett helt diagram. Excel stöder tre typer av sparklinjer: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet genom API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `com.aspose.cells.Charts`.

I Aspose.Cells skapas varje sparklinje du lägger till via `worksheet.SparklineGroups.add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ange sparklinjetyp, dataintervall, målcell samt visuella egenskaper som linjefärg, linjetjocklek, markörer och indikatorer för högsta/lägsta punkt.

{{% alert color="primary" %}}

En enskild `SparklineGroup` kan innehålla en eller flera sparklinjer som delar samma stil. När du anropar `add` och skickar en datarad plus en enda målcell, får du en sparklinje i den cellen. Om ditt målintervall är bredare än en cell, ritas en separat sparklinje i varje målcell, alla med samma stil och dataintervall.

{{% /alert %}}

Den här artikeln går igenom var och en av de tre sparklinjetyper som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linjesparklinjer**

En linjesparklinje drar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det naturligaste valet för att visa trender över tid. I Aspose.Cells skapas en linjesparklinje genom att skicka `SparklineType.Line` till metoden `SparklineGroups.add`.

Arbetsflödet är detsamma som för alla andra sparklinjetyper:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumnerna A till och med E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen där sparklinjen ska ritas.
4. Anropa `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Det tredje argumentet — `false` — talar om för Aspose.Cells att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linjesparklinje kan du ange linjefärgen med `group.Line.Color` (som förväntar sig en `CellsColor` från `com.aspose.cells.Drawing`), justera linjetjockleken samt aktivera markörer för högsta och lägsta punkter.
6. Spara arbetsboken.

Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till och med E1, och lägger till en linjesparklinje i cell F1 som följer dessa värden. Den anpassar också linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

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

// Steg 4: Lägg till en linje-sparkline från A1:E1 till F1
// SparklineGroups.Add returnerar indexet för den nyligen tillagda gruppen
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjens färg
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Steg 6: Aktivera markeringar för högsta och lägsta punkt
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Steg 7: Spara arbetsboken
workbook.save("output_line.xlsx");
```

## **Kolumnsparklinjer**

En kolumnsparklinje renderar varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars magnitud är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumnsparklinje genom att skicka `SparklineType.Column` till metoden `SparklineGroups.add`.

Proceduren speglar exemplet med linjesparklinje:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll samma källintervall (A1:E1) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att sätta `group.Type` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken i en separat utdatafil så att den inte skriver över exemplet med linjesparklinje.

Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumnsparklinje i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att se positiva och negativa bidrag med en blick.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Steg 2: Skriv exempelvärden till A1:E1
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

// Steg 4: Lägg till en kolumn-sparkline i målcellen
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

En vinst/förlust-sparklinje är en specialvariant av kolumnsparklinjen som är utformad för att visa endast två utfall: ett positivt värde ritas som en "upp"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "ner"-stapel (en förlust). Vinst/förlust-sparklinjer används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat, eller andra binära utfall över tid.

I Aspose.Cells skapas en vinst/förlust-sparklinje genom att skicka `SparklineType.Stacked` till metoden `SparklineGroups.add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-renderingen.)

Proceduren är densamma som för de andra två typerna:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll källintervallet. Eftersom vinst/förlust-sparklinjer behandlar varje värde som antingen en vinst eller en förlust, spelar värdets magnitud ingen roll — bara dess tecken gör det. Positiva värden blir upp-staplar och icke-positiva värden blir ner-staplar.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att sätta accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett distinkt filnamn så att alla tre exemplen kan samexistera på disk.

Exemplet nedan använder samma indata som de två föregående avsnitten. Värdena 5, -3, 8, -2, 6 tolkas som vinst, förlust, vinst, förlust, vinst — och sparklinjen som ritas i F1 återspeglar exakt det mönstret.

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

// Steg 3: Skapa en CellArea som pekar på F1 (kolumn 5, rad 0)
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
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Steg 5: Anpassa sparkline-gruppen
// Aktivera markörer för hög- och lågpunkt
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Ställ in högpunktens färg till grön
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// Ställ in lågpunktens färg till röd
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// Ställ in negativa punkters färg till orange
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

## **Kombinera alla tre sparklinjetyper**

De tre föregående exemplen producerar var sin egen arbetsbok så att utdatafilerna är enkla att inspektera var för sig. I ett verkligt scenario vill man dock ofta jämföra flera dataserier sida vid sida. Det renaste sättet att göra det är att placera mer än en sparklinjegrupp i samma kalkylblad, där varje grupp renderar en annan stil.

Du kan lägga till flera `SparklineGroup`-objekt i samma `SparklineGroupCollection`, och varje grupp kan rikta sig mot en annan målcell eller ett annat intervall. Du kan till exempel placera en linjesparklinje i F1, en kolumnsparklinje i F2 och en vinst/förlust-sparklinje i F3 — alla läser från samma källdata i rad 1 — så att läsaren kan se tre olika visuella behandlingar av samma siffror.

Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6, och lägger sedan till tre sparklinjegrupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparklinjestilar på en gång.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Steg 3: Lägg till en linje sparkline-grupp i F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Anpassa linje sparkline-färgen via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Steg 4: Lägg till en kolumn sparkline-grupp i F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Anpassa kolumn sparkline-seriefärgen
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Steg 5: Lägg till en Vinst/Förlust (Staplad) sparkline-grupp i F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Anpassa vinst/förlust sparkline-seriefärgen
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Steg 6: Spara arbetsboken
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

När du kombinerar flera sparklinjegrupper i ett enda kalkylblad är varje grupp oberoende. De kan dela samma källintervall eller använda olika källintervall, och de kan stylas oberoende av varandra. Detta gör det enkelt att bygga en liten "instrumentpanel" av visualiseringar i celler direkt i ett befintligt kalkylblad.

{{% /alert %}}

## **Anpassa sparklinjernas utseende**

När en `SparklineGroup` har skapats och lagts till i `worksheet.SparklineGroups`, kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De vanligaste egenskaperna att anpassa är:

- **`group.Type`** — `SparklineType` (Line, Column eller Stacked). Den sätts när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.Line.Color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.createCellsColor()`. Detta är egenskapen att använda för streckfärgen på en linjesparklinje.
- **`group.Line.Weight`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Markörer för högsta/lägsta punkt** — flaggor som slår på små markörer på de högsta och lägsta datapunkterna, användbart för att betona extremvärden.
- **Markörer för första/sista/negativa punkt** — flaggor som växlar markörer på de första, sista och negativa datapunkterna.

För att ändra en färg, skapa alltid en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte en `java.awt.Color` direkt till sparklinjefärgegenskaper — de förväntar sig typen `CellsColor` från `com.aspose.cells.Drawing`. Metoden `SparklineGroups.add` returnerar i sig ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.



{{< app/cells/assistant language="javascript" >}}