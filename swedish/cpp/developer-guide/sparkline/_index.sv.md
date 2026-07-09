---
title: Sparklines i Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells är ett C++-bibliotek för att arbeta med kalkylbladsfiler som stöder skapande av sparklines — miniatyrdiagram placerade inuti kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, sparklines, linje-sparkline, kolumn-sparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder skapande av sparklines inuti kalkylbladsceller. Sparklines är miniatyrdiagram som passar inom en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och varje typ kan anpassas med avseende på färg, linjetjocklek, högsta/lägsta punkter samt markörer.

{{% /alert %}}

## **Introduktion**

Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend bredvid en rad eller kolumn med data utan att ta upp utrymmet för ett helt diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet genom API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `Aspose.Cells.Charts`.

I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.SparklineGroups.Add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ställa in sparkline-typen, dataintervallet, destinationscellen och visuella egenskaper som linjefärg, linjetjocklek, markörer samt indikatorer för högsta/lägsta punkt.

{{% alert color="primary" %}}

En enskild `SparklineGroup` kan innehålla en eller flera sparklines som delar samma stil. När du anropar `Add` och skickar en rad med data plus en enda destinationscell får du en sparkline inuti den cellen. Om ditt destinationsintervall är bredare än en cell ritas en separat sparkline i varje destinationscell, alla med samma stil och dataintervall.

{{% /alert %}}

Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**

En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör det till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.Line` till metoden `SparklineGroups.Add`.

Arbetsflödet är detsamma som för alla andra sparkline-typer:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumnerna A till och med E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver destinationscellen där sparkline ska ritas.
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Det tredje argumentet — `false` — anger för Aspose.Cells att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparkline kan du ställa in linjefärgen med hjälp av `group.Line.Color` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken och aktivera markörer för högsta och lägsta punkt.
6. Spara arbetsboken.

Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till och med E1, och lägger till en linje-sparkline i cell F1 som spårar dessa värden. Det anpassar också linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Steg 1: Skapa en Workbook och hämta det första arbetsbladet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // Steg 3: Bygg en CellArea som pekar på destinationscellen F1
    CellArea dest;
    dest.StartColumn = 5;   // kolumn F (0-indexerad)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // rad 1 (0-indexerad)
    dest.EndRow = 0;

    // Steg 4: Lägg till en linje-snabbdiagram från A1:E1 till F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // Steg 5: Skapa en röd CellsColor och tilldela den till snabbdiagrammets linjefärg
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // Steg 6: Aktivera markeringar för högsta och lägsta punkt
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // Steg 7: Spara arbetsboken
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Kolumn-sparklines**

En kolumn-sparkline återger varje datapunkt som ett vertikalt streck. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.Column` till metoden `SparklineGroups.Add`.

Proceduren speglar exemplet med linje-sparkline:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll samma källintervall (A1:E1) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver destinationscellen.
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att ställa in `group.Type` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken till en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.

Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumn-sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att snabbt urskilja positiva och negativa bidrag.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Steg 1: Skapa en Workbook och hämta det första arbetsbladet
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Steg 2: Skriv exempelvärden till A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // Steg 3: Bygg en CellArea som pekar mot F1 (kolumnindex 5, radindex 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // Steg 4: Lägg till en Column-sparkline i målcellen
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // Steg 5: Bekräfta sparkline-typen genom att läsa group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // Steg 6: Spara arbetsboken
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Vinst/förlust-sparklines**

En vinst/förlust-sparkline är en speciell variant av kolumn-sparkline som är utformad för att endast visa två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat, eller andra binära utfall över tid.

I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.Stacked` till metoden `SparklineGroups.Add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-renderingen.)

Proceduren är densamma som för de andra två typerna:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets storlek ingen roll — bara dess tecken. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Bygg en `CellArea` som beskriver destinationscellen.
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett unikt filnamn så att alla tre exempel kan samexistera på disk.

Exemplet nedan använder samma indata som de två föregående avsnitten. Värdena 5, -3, 8, -2, 6 tolkas som vinst, förlust, vinst, förlust, vinst — och sparkline som ritas i F1 återspeglar exakt det mönstret.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Steg 1: Skapa en Workbook och hämta det första arbetsbladet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // Steg 2: Fyll i exempeldata i rad 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Steg 3: Bygg en CellArea som pekar mot F1 (kolumn 5, rad 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // rad 1
    dest.EndRow = 0;

    // Steg 4: Lägg till en Vinst/Förlust-sparkline (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Steg 5: Anpassa sparkline-gruppen
    // Aktivera markörer för hög- och lågpunkt
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // Sätt färgen för högpunkten till grön
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // Sätt färgen för lågpunkten till röd
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // Sätt färgen för negativa punkter till orange
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // Sätt standardfärgen för serien (används för positiva staplar)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Steg 6: Spara arbetsboken
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Kombinera alla tre sparkline-typer**

De föregående tre exemplen producerar var sin egen arbetsbok så att utdatafilerna är enkla att inspektera var för sig. I ett verkligt scenario vill man dock ofta jämföra flera dataserier sida vid sida. Det renaste sättet att göra det är att placera mer än en sparkline-grupp i samma kalkylblad, där varje grupp renderar en annan stil.

Du kan lägga till flera `SparklineGroup`-objekt i samma `SparklineGroupCollection`, och varje grupp kan rikta sig mot en annan destinationscell eller ett annat intervall. Du kan till exempel placera en linje-sparkline i F1, en kolumn-sparkline i F2 och en vinst/förlust-sparkline i F3 — alla läser från samma källdata i rad 1 — så att läsaren kan se tre olika visuella behandlingar av samma siffror.

Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6, och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar på en gång.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Steg 1: Skapa en Workbook och hämta det första arbetsbladet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Steg 3: Lägg till en linje-sparkline-grupp i F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // Anpassa färgen på linje-sparkline via CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // Steg 4: Lägg till en kolumn-sparkline-grupp i F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // Anpassa färgen på kolumn-sparkline-serien
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // Steg 5: Lägg till en Win/Loss (staplad) sparkline-grupp i F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // Anpassa färgen på win/loss-sparkline-serien
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // Steg 6: Spara arbetsboken
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

När du kombinerar flera sparkline-grupper i ett enda kalkylblad är varje grupp oberoende. De kan dela samma källintervall eller använda olika källintervall, och de kan stiliseras oberoende av varandra. Detta gör det enkelt att bygga en liten "instrumentpanel" av visualiseringar i celler direkt inuti ett befintligt kalkylblad.

{{% /alert %}}

## **Anpassa sparkline-utseende**

När en `SparklineGroup` har skapats och lagts till i `worksheet.SparklineGroups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De egenskaper som oftast anpassas är:

- **`group.Type`** — `SparklineType` (Line, Column eller Stacked). Den ställs in när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.Line.Color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.CreateCellsColor()`. Detta är egenskapen att använda för linje-sparkline-färgen.
- **`group.Line.Weight`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Högsta/lägsta punktmarkörer** — flaggor som aktiverar små markörer på de högsta och lägsta datapunkterna, användbara för att betona extremvärden.
- **Första/sista/negativa punktmarkörer** — flaggor som växlar markörer på de första, sista och negativa datapunkterna.

För att ändra en färg, skapa alltid en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte ett rått färgvärde direkt till sparkline-färgegenskaper — de förväntar sig typen `CellsColor` från `Aspose.Cells.Drawing`. Metoden `SparklineGroups.Add` returnerar i sig ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.



{{< app/cells/assistant language="cpp" >}}