---
title: Sparklines i Aspose.Cells for .NET
linktitle: Sparklines
description: Aspose.Cells är ett .NET‑bibliotek för att arbeta med kalkylbladfiler som stödjer att skapa sparklines — miniatyrdiagram placerade i kalkylbladceller. Denna artikel förklarar hur man lägger till och anpassar linje‑, kolumn‑ och vinst/förlust‑sparklines med hjälp av Aspose.Cells‑biblioteket.
keywords: Aspose.Cells, .NET‑bibliotek, kalkylblad, sparklines, linje sparkline, kolumn sparkline, vinst/förlust sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder att skapa sparklines i kalkylblads‑celler. Sparklines är miniatyrdiagram som får plats i en enda cell och ger en snabb visuell representation av datapunkternas trender. Aspose.Cells stöder linje‑, kolumn‑ och vinst/förlust‑sparklines, och var och en kan anpassas avseende färg, linjebredd, högsta/lägsta punkter och markörer.
{{% /alert %}}

## **Introduktion**
Sparklines är små diagram i cellerna som är användbara när du vill visa en snabb trend bredvid en rad eller kolumn med data utan att ta upp utrymmet för ett fullständigt diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet via API:erna `SparklineGroup` och `SparklineGroupCollection` i `Aspose.Cells.Charts`‑namnrymden.  
I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.SparklineGroups.Add(...)` i kalkylbladet, vilket returnerar ett `SparklineGroup`‑objekt. Du kan sedan använda det objektet för att ange sparkline‑typen, dataintervallet, mål‑cellen samt visuella egenskaper som linjefärg, linjebredd, markörer och högsta/lägsta‑punktsindikatorer.  
Denna artikel går igenom de tre sparkline‑typer som stöds av Aspose.Cells — **Line**, **Column** och **Win/Loss** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje‑sparklines**
En linje‑sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje‑sparkline genom att skicka `SparklineType.Line` till metoden `SparklineGroups.Add`.

1. Skapa en ny `Workbook` och öppna det första kalkylbladet.  
2. Fyll i en rad med källdata (till exempel rad 1, kolumnerna A till E) med de värden du vill visualisera.  
3. Skapa ett `CellArea` som beskriver mål‑cellen där sparkline‑en ska ritas.  
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Det tredje argumentet — `false` — talar om för Aspose.Cells att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).  
5. Eventuellt kan du anpassa det returnerade `SparklineGroup`. För en linje‑sparkline kan du ange linjefärgen med `group.Line.Color` (som förväntar sig ett `CellsColor` från `Aspose.Cells.Drawing`), justera linjebredden och växla markörer för högsta/lägsta punkter.  
6. Spara arbetsboken.

Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till E1 och lägger till en linje‑sparkline i cell F1 som följer dessa värden. Det anpassar även linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;
            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.Add returns the index of the newly added group
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Step 6: Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Step 7: Save the workbook
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Kolumn‑sparklines**
En kolumn‑sparkline återger varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data där storleken är meningsfull — exempelvis månatliga försäljningsfigurer eller antal. I Aspose.Cells skapar du en kolumn‑sparkline genom att skicka `SparklineType.Column` till metoden `SparklineGroups.Add`.

Proceduren speglar linje‑sparkline‑exemplet:
1. Skapa en ny `Workbook` och öppna det första kalkylbladet.  
2. Fyll i en rad med källdata (till exempel rad 1, kolumnerna A till E) med de värden du vill visualisera.  
3. Skapa ett `CellArea` som beskriver mål‑cellen.  
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.  
5. Eventuellt kan du anpassa det resulterande `SparklineGroup` — till exempel genom att sätta `group.Type` för att bekräfta typen, eller genom att justera stapelfärgen.  
6. Spara arbetsboken till en separat utdatafil så att den inte skriv över linje‑sparkline‑exemplet.

Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och återger en kolumn‑sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att på ett ögonblick se positiva och negativa bidrag.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Step 2: Write sample values into A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Step 4: Add a Column sparkline to the destination cell
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Step 5: Confirm the sparkline type by reading group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Step 6: Save the workbook
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Vinst/Förlust‑sparklines**
En vinst/förlust‑sparkline är en speciell variant av kolumn‑sparkline som är avsedd att visa endast två utfall: ett positivt värde ritas som en ”uppåt”‑stapel (en vinst) och ett noll‑ eller negativt värde ritas som en ”nedåt”‑stapel (en förlust). Vinst/förlust‑sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkända/underkända resultat eller något binärt utfall över tid.

I Aspose.Cells skapas en vinst/förlust‑sparkline genom att skicka `SparklineType.Stacked` till metoden `SparklineGroups.Add`. (Trots namnet är `SparklineType.Stacked` det enum‑värde som begär vinst/förlust‑återgivning.)

1. Skapa en ny `Workbook` och öppna det första kalkylbladet.  
2. Fyll i källintervallet. Eftersom vinst/förlust‑sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets magnitud ingen roll — endast tecknet gör det. Positiva värden blir upp‑staplar och icke‑positiva värden blir ner‑staplar.  
3. Skapa ett `CellArea` som beskriver mål‑cellen.  
4. Anropa `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.  
5. Eventuellt kan du anpassa det returnerade `SparklineGroup`, till exempel genom att ange accentfärger för vinst‑ och förluststaplarna.  
6. Spara arbetsboken under ett separat filnamn så att alla tre exempel kan samexistera på disk.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1
            dest.EndRow = 0;
            // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Step 5: Customize the sparkline group
            // Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Set the high-point color to green
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Set the low-point color to red
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Set the negative-point color to orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Set the default series color (used for positive bars)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Step 6: Save the workbook
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Kombinera alla tre sparkline‑typer**
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline‑grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen visar alla tre sparkline‑stilar samtidigt.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Customize the column sparkline series color
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Step 6: Save the workbook
workbook.Save("output_all.xlsx");
```

## **Anpassa sparkline‑utseende**
När ett `SparklineGroup` har skapats och lagts till i `worksheet.SparklineGroups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De mest vanliga anpassade egenskaperna är:
- **`group.Type`** — `SparklineType` (Line, Column eller Stacked). Den sätts när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.  
- **`group.Line.Color`** — linjefärgen, uttryckt som ett `CellsColor` skapat via `workbook.CreateCellsColor()`. Detta är egenskapen att använda för linje‑sparkline‑strokefärg.  
- **`group.Line.Weight`** — linjebredden i punkter. Högre värden ger tjockare linjer.  
- Högsta/lägsta‑punktsmarkörer — flaggor som aktiverar små markörer på de högsta och lägsta datapunkterna, användbara för att framhäva extremvärden.  
- Första/sista/negativa‑punktsmarkörer — flaggor som växlar markörer på den första, sista och negativa datapunkterna.

För att ändra en färg, skapa alltid en `CellsColor`‑instans och tilldela den till den relevanta egenskapen. Tilldela inte en `System.Drawing.Color` direkt till sparkline‑färg‑egenskaper — de förväntar sig typen `CellsColor` från `Aspose.Cells.Drawing`. Metoden `SparklineGroups.Add` returnerar själv ett fullt typat `SparklineGroup`‑objekt, så du kan kedja egenskaps‑tilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.

## Related Articles
- [Konvertera Sparkline till bild och HTML i Aspose.Cells for .NET](/cells/sv/net/convert-sparkline-to-image-and-html/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for .NET](/cells/sv/net/add-page-field-in-pivot-table/)
- [Applicera stilar på pivottabeller i Aspose.Cells for .NET](/cells/sv/net/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/net/change-page-field-layout/)
- [Konvertera Excel till OFD-format](/cells/sv/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}