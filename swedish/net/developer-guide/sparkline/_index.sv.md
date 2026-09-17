---
title: Sparklines i Aspose.Cells for .NET
description: Aspose.Cells är ett .NET-bibliotek för arbete med kalkylbladsfiler som stöder skapande av sparklines — miniatyrdiagram placerade inuti kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
linktitle: Sparklines
keywords: Aspose.Cells, .NET-bibliotek, kalkylblad, sparklines, linje-sparkline, kolumn-sparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder skapande av sparklines inuti kalkylbladsceller. Sparklines är miniatyrdiagram som passar inom en enskild cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och var och en kan anpassas vad gäller färg, linjetjocklek, högsta/lägsta punkter och markörer.

## **Introduktion**
Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend bredvid en rad eller kolumn med data utan att ta upp utrymmet för ett fullstort diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktion via API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `Aspose.Cells.Charts`.
I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.SparklineGroups.Add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ställa in sparkline-typen, dataintervallet, målcellen och visuella egenskaper som linjefärg, linjetjocklek, markörer och indikatorer för högsta/lägsta punkter.
Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**
En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.Line` till metoden `SparklineGroups.Add`.
1. Skapa en ny `Workbook` och få tillgång till det första kalkylbladet.
2. Fyll i en rad med källdata (till exempel rad 1, kolumner A till och med E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen där sparklinen ska ritas.
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Det tredje argumentet — `false` — talar om för Aspose.Cells att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparkline kan du ställa in linjefärgen med hjälp av `group.Line.Color` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken och växla markörer för högsta/lägsta punkter.
6. Spara arbetsboken.
Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till och med E1, och lägger till en linje-sparkline i cell F1 som spårar dessa värden. Den anpassar också linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

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
            // Steg 1: Skapa en arbetsbok och hämta det första kalkylbladet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Steg 3: Bygg en CellArea som pekar på destinationscell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // kolumn F (0-indexerad)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // rad 1 (0-indexerad)
            dest.EndRow = 0;
            // Steg 4: Lägg till en linje-sparkline från A1:E1 till F1
            // SparklineGroups.Add returnerar indexet för den nyligen tillagda gruppen
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjefärgen
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Steg 6: Aktivera högpunkt- och lågpunktmarkörer
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Steg 7: Spara arbetsboken
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Kolumn-sparklines**
En kolumn-sparkline visar varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.Column` till metoden `SparklineGroups.Add`.
Proceduren speglar exemplet med linje-sparkline:
1. Skapa en ny `Workbook` och få tillgång till det första kalkylbladet.
2. Bygg en `CellArea` som beskriver målcellen.
3. Anropa `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
4. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att ställa in `group.Type` för att bekräfta typen, eller genom att justera stapelfärgen.
5. Spara arbetsboken i en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.
Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och visar en kolumn-sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör positiva och negativa bidrag enkla att se vid en första anblick.

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
            // Steg 3: Bygg en CellArea som pekar mot F1 (kolumnindex 5, radindex 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Steg 4: Lägg till en Column-sparkline i destinationscellen
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
En vinst/förlust-sparkline är en specialvariant av kolumn-sparkline utformad för att visa endast två utfall: ett positivt värde ritas som en "upp"-stapel (en vinst) och ett noll eller negativt värde ritas som en "ned"-stapel (en förlust). Vinst/förlust-sparklines används vanligtvis för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat, eller vilket binärt utfall som helst över tid.
I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.Stacked` till metoden `SparklineGroups.Add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-renderingen.)
1. Skapa en ny `Workbook` och få tillgång till det första kalkylbladet.
2. Fyll i källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets storlek ingen roll — bara dess tecken gör det. Positiva värden blir upp-staplar och icke-positiva värden blir ned-staplar.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förluststaplar.
6. Spara arbetsboken under ett distinkt filnamn så att alla tre exemplen kan samexistera på disk.

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
            // Ställ in färgen för högpunkten till grön
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Ställ in färgen för lågpunkten till röd
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Ställ in färgen för negativa punkter till orange
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
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6, och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen visar alla tre sparkline-stilar på en gång.

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
// Steg 3: Lägg till en linje-sparklinegrupp i F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Anpassa linje-sparklinefärgen via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Steg 4: Lägg till en kolumn-sparklinegrupp i F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Anpassa seriefärgen för kolumn-sparkline
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Steg 5: Lägg till en vinst/förlust (staplad) sparklinegrupp i F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Anpassa seriefärgen för vinst/förlust-sparkline
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Steg 6: Spara arbetsboken
workbook.Save("output_all.xlsx");
```

## **Anpassa sparkline-utseende**
När en `SparklineGroup` har skapats och lagts till i `worksheet.SparklineGroups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De vanligaste anpassade egenskaperna är:
- **`group.Type`** — `SparklineType` (Linje, Kolumn eller Stacked). Den ställs in när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.Line.Color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.CreateCellsColor()`. Detta är egenskapen som ska användas för linje-sparkline-streckfärg.
- **`group.Line.Weight`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Högsta/lägsta punktmarkörer** — flaggor som slår på små markörer på de högsta och lägsta datapunkterna, användbara för att betona extremer.
- **Första/sista/negativa punktmarkörer** — flaggor som växlar markörer på de första, sista och negativa datapunkterna.
För att ändra en färg, skapa alltid en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte en `System.Drawing.Color` direkt till sparkline-färgegenskaper — de förväntar sig typen `CellsColor` från `Aspose.Cells.Drawing`. Metoden `SparklineGroups.Add` returnerar själv ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.
{{% /alert %}}

## Relaterade artiklar
- [Konvertera sparkline till bild och HTML i Aspose.Cells for .NET](/cells/sv/net/convert-sparkline-to-image-and-html/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for .NET](/cells/sv/net/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for .NET](/cells/sv/net/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/net/change-page-field-layout/)
- [Konvertera Excel till OFD-format](/cells/sv/net/converting-excel-to-ofd-format/)csharp

{{< app/cells/assistant language="csharp" >}}