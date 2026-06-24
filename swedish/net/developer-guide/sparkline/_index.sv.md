---
title: Sparklines i Aspose.Cells for .NET
linktitle: Sparklines
description: Aspose.Cells är ett .NET-bibliotek för att arbeta med kalkylbladsfiler som stöder skapande av sparklines — miniatyrdiagram placerade inuti kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
keywords: Aspose.Cells, .NET-bibliotek, kalkylblad, sparklines, linje-sparkline, kolumn-sparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder skapande av sparklines inuti kalkylbladsceller. Sparklines är miniatyrdiagram som får plats i en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och varje typ kan anpassas avseende färg, linjetjocklek, högsta/lägsta punkter samt markörer.

{{% /alert %}}

## **Introduktion**

Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymmet av ett fullstort diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet via API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `Aspose.Cells.Charts`.

I Aspose.Cells skapas varje sparkline du lägger till genom `worksheet.SparklineGroups.Add(...)`, som returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ställa in sparkline-typen, dataintervallet, målcellen och visuella egenskaper såsom linjefärg, linjetjocklek, markörer samt indikatorer för högsta/lägsta punkt.

{{% alert color="primary" %}}

En enskild `SparklineGroup` kan innehålla en eller flera sparklines som delar samma stil. När du anropar `Add` och skickar en rad med data plus en enskild målcell får du en sparkline inuti den cellen. Om ditt målintervall är bredare än en cell ritas en separat sparkline i varje målcell, alla med samma stil och dataintervall.

{{% /alert %}}

Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**

En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.Line` till metoden `SparklineGroups.Add`.

Arbetsflödet är detsamma som för alla andra sparkline-typer:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumn A till och med E) med de värden du vill visualisera.
3. Skapa en `CellArea` som beskriver den målcell där sparklinen ska ritas.
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Det tredje argumentet — `false` — talar om för Aspose.Cells att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparkline kan du ställa in linjefärgen med `group.Line.Color` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken och aktivera markörer för högsta/lägsta punkt.
6. Spara arbetsboken.

Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till och med E1 och lägger till en linje-sparkline i cell F1 som spårar dessa värden. Det anpassar också linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // Steg 1: Skapa en Workbook och hämta det första kalkylbladet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;

            // Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);

            // Steg 3: Bygg en CellArea som pekar på målcellen F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // kolumn F (0-indexerad)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // rad 1 (0-indexerad)
            dest.EndRow = 0;

            // Steg 4: Lägg till en linje-sparkline från A1:E1 i F1
            // SparklineGroups.Add returnerar indexet för den nyligen tillagda gruppen
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjefärgen
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // Steg 6: Aktivera markörer för högsta och lägsta punkt
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;

            // Steg 7: Spara arbetsboken
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Kolumn-sparklines**

En kolumn-sparkline renderar varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.Column` till metoden `SparklineGroups.Add`.

Proceduren speglar exemplet med linje-sparkline:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll samma källintervall (A1:E1) med de värden du vill visualisera.
3. Skapa en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att sätta `group.Type` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken till en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.

Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumn-sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att urskilja positiva och negativa bidrag med en blick.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Steg 1: Skapa en Workbook och hämta det första kalkylbladet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];

            // Steg 2: Skriv exempelvärden i A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }

            // Steg 3: Bygg en CellArea som pekar på F1 (kolumnindex 5, radindex 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;

            // Steg 4: Lägg till en Column-sparkline i målcellen
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];

            // Steg 5: Bekräfta sparkline-typen genom att läsa group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);

            // Steg 6: Spara arbetsboken
            workbook.Save("output_column.xlsx");

            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Vinst/förlust-sparklines**

En vinst/förlust-sparkline är en specialvariant av kolumn-sparkline som är utformad för att endast visa två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat, eller andra binära utfall över tid.

I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.Stacked` till metoden `SparklineGroups.Add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-renderingen.)

Proceduren är densamma som för de andra två typerna:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets storlek ingen roll — bara dess tecken gör det. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Skapa en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett unikt filnamn så att alla tre exempel kan samexistera på disk.

Exemplet nedan använder samma indata som de två föregående avsnitten. Värdena 5, -3, 8, -2, 6 tolkas som vinst, förlust, vinst, förlust, vinst — och sparklinen som ritas i F1 återspeglar exakt det mönstret.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Steg 1: Skapa en Workbook och hämta det första kalkylbladet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";

            // Steg 2: Fyll i exempeldata i rad 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);

            // Steg 3: Bygg en CellArea som pekar på F1 (kolumn 5, rad 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // rad 1
            dest.EndRow = 0;

            // Steg 4: Lägg till en Win/Loss-sparkline (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];

            // Steg 5: Anpassa sparkline-gruppen
            // Aktivera markörer för hög- och lågpunkt
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;

            // Ställ in högpunktens färg till grön
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;

            // Ställ in lågpunktens färg till röd
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;

            // Ställ in den negativa punktens färg till orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;

            // Ställ in standardfärgen för serien (används för positiva staplar)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;

            // Steg 6: Spara arbetsboken
            workbook.Save("output_winloss.xlsx");

            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Kombinera alla tre sparkline-typer**

De tre föregående exemplen producerar var sin egen arbetsbok så att utdatafilerna är enkla att inspektera var för sig. I ett verkligt scenario vill man dock ofta jämföra flera dataserier sida vid sida. Det renaste sättet att göra det är att placera mer än en sparkline-grupp i samma kalkylblad, där varje grupp renderar en annan stil.

Du kan lägga till flera `SparklineGroup`-objekt i samma `SparklineGroupCollection`, och varje grupp kan rikta sig mot en annan målcell eller ett annat intervall. Du kan till exempel placera en linje-sparkline i F1, en kolumn-sparkline i F2 och en vinst/förlust-sparkline i F3 — alla som läser från samma källdata i rad 1 — så att läsaren kan se tre olika visuella behandlingar av samma siffror.

Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar på en gång.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// Steg 1: Skapa en Workbook och hämta det första kalkylbladet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Steg 3: Lägg till en linje-sparkline-grupp vid F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];

// Anpassa linje-sparkline-färgen via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;

// Steg 4: Lägg till en kolumn-sparkline-grupp vid F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];

// Anpassa kolumn-sparkline-seriens färg
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;

// Steg 5: Lägg till en vinst/förlust (staplad) sparkline-grupp vid F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];

// Anpassa vinst/förlust-sparkline-seriens färg
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;

// Steg 6: Spara arbetsboken
workbook.Save("output_all.xlsx");
```

{{% alert color="primary" %}}

När du kombinerar flera sparkline-grupper i ett enda kalkylblad är varje grupp oberoende. De kan dela samma källintervall eller använda olika källintervall, och de kan stylas oberoende av varandra. Detta gör det enkelt att bygga en liten "instrumentpanel" med visualiseringar i celler direkt inuti ett befintligt kalkylblad.

{{% /alert %}}

## **Anpassa sparkline-utseende**

När en `SparklineGroup` har skapats och lagts till i `worksheet.SparklineGroups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De mest vanligt anpassade egenskaperna är:

- **`group.Type`** — `SparklineType` (Line, Column eller Stacked). Den sätts när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.Line.Color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.CreateCellsColor()`. Detta är egenskapen att använda för streckfärgen på linje-sparklines.
- **`group.Line.Weight`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Högsta/lägsta punktmarkörer** — flaggor som aktiverar små markörer på de högsta och lägsta datapunkterna, användbara för att framhäva extremvärden.
- **Första/sista/negativa punktmarkörer** — flaggor som växlar markörer på den första, sista och negativa datapunkten.

För att ändra en färg, skapa alltid en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte en `System.Drawing.Color` direkt till sparkline-färgegenskaper — de förväntar sig typen `CellsColor` från `Aspose.Cells.Drawing`. Metoden `SparklineGroups.Add` returnerar i sig ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.

## **Relaterade artiklar**

- [Komma åt celler i ett kalkylblad](/cells/sv/net/accessing-cells-of-a-worksheet/)
- [Formatera kalkylbladsceller i en arbetsbok](/cells/sv/net/format-worksheet-cells-in-a-workbook/)
- [Anpassa diagram](/cells/sv/net/customizing-charts/)
- [Skapa dynamiska diagram](/cells/sv/net/create-dynamic-charts/)
- [Hantera data i Excel-filer](/cells/sv/net/cells-data/)

{{< app/cells/assistant language="csharp" >}}