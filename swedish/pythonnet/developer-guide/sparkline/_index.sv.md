---
title: Sparklines i Aspose.Cells for Python via .NET
linktitle: Sparklines i Aspose.Cells for Python via .NET
description: Aspose.Cells är ett Python-bibliotek för att arbeta med kalkylblad som stöder skapande av sparklines, miniatyrdiagram placerade i kalkylbladsceller. Den här artikeln förklarar hur du lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Python-bibliotek, kalkylblad, sparklines, linje-sparkline, kolumn-sparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder skapande av sparklines i kalkylbladsceller. Sparklines är miniatyrdiagram som får plats i en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och var och en kan anpassas med avseende på färg, linjevikt, högsta/lägsta punkter samt markörer.

## **Introduktion**
Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymmet för ett helt diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna möjlighet genom API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `aspose.cells.charts`.
I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.sparkline_groups.add(...)`, som returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ställa in sparkline-typen, dataintervallet, målcellen och visuella egenskaper som linjefärg, linjevikt, markörer samt indikatorer för högsta/lägsta punkt.
Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur du lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**
En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det naturligaste valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.Line` till metoden `sparkline_groups.add`.
1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumn A till och med E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen där sparkline ska ritas.
4. Anropa `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. Det tredje argumentet — `False` — talar om för Aspose.Cells att dataområdet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparkline kan du ställa in linjefärgen med `group.line.color` (som förväntar sig en `CellsColor` från `aspose.cells.drawing`), justera linjevikten och växla markörer för högsta/lägsta punkt.
6. Spara arbetsboken.
Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till och med E1 och lägger till en linje-sparkline i cell F1 som spårar dessa värden. Den anpassar också linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True
# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

## **Kolumn-sparklines**
En kolumn-sparkline renderar varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.Column` till metoden `sparkline_groups.add`.
Tillvägagångssättet speglar exemplet med linje-sparkline:
1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att ställa in `group.type` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken till en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.
Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumn-sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att se positiva och negativa bidrag med en blick.

```python
import aspose.cells as ac
# Steg 1: Skapa en arbetsbok och hämta det första kalkylbladet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Steg 2: Skriv exempelvärden i A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])
# Steg 3: Bygg en CellArea som pekar på F1 (kolumnindex 5, radindex 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0
# Steg 4: Lägg till en kolumnsparkline i destinationscellen
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# Steg 5: Bekräfta sparkline-typen genom att läsa group.Type
print("Sparkline Type added: " + str(group.type))
# Steg 6: Spara arbetsboken
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **Vinst/Förlust-sparklines**
En vinst/förlust-sparkline är en speciell variant av kolumn-sparkline som är utformad för att visa endast två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat eller andra binära utfall över tid.
I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.Stacked` till metoden `sparkline_groups.add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-renderingen.)
1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
2. Fyll källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets storlek ingen roll — bara dess tecken gör det. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett unikt filnamn så att alla tre exempel kan samexistera på disk.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

## **Kombinera alla tre sparkline-typer**
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen visar alla tre sparkline-stilar på en gång.

```python
import aspose.cells as ac
import System.Drawing
# Steg 1: Skapa en arbetsbok och hämta det första kalkylbladet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Steg 3: Lägg till en linje-sparkline-grupp i F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]
# Anpassa linje-sparkline-färgen via CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color
# Steg 4: Lägg till en kolumn-sparkline-grupp i F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]
# Anpassa kolumn-sparkline-serie-färgen
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color
# Steg 5: Lägg till en vinst/förlust (staplad) sparkline-grupp i F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]
# Anpassa vinst/förlust-sparkline-serie-färgen
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color
# Steg 6: Spara arbetsboken
workbook.save("output_all.xlsx")
```

## **Anpassa sparklines utseende**
När en `SparklineGroup` har skapats och lagts till i `worksheet.sparkline_groups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De egenskaper som oftast anpassas är:
- **`group.type`** — `SparklineType` (Line, Column eller Stacked). Den ställs in när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.line.color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.create_cells_color()`. Detta är egenskapen att använda för streckfärgen på linje-sparklines.
- **`group.line.weight`** — linjevikten i punkter. Högre värden ger tjockare linjer.
- **Markörer för högsta/lägsta punkt** — flaggor som slår på små markörer på de högsta och lägsta datapunkterna, användbara för att betona extremvärden.
- **Markörer för första/sista/negativa punkt** — flaggor som växlar markörer på den första, sista och negativa datapunkten.
För att ändra en färg ska du alltid skapa en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Sparkline-färgegenskaper förväntar sig typen `CellsColor` från `aspose.cells.drawing` — tilldela inte ett rått färgvärde direkt till dem. Metoden `sparkline_groups.add` returnerar i sig ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}