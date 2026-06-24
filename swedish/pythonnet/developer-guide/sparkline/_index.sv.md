---
title: Sparklines i Aspose.Cells for Python via .NET
linktitle: Sparklines
description: Aspose.Cells är ett Python-bibliotek för att arbeta med kalkylarksfiler som stöder skapande av sparklines — miniatyrdiagram placerade i kalkylbladsceller. Denna artikel förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Python library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder skapande av sparklines i kalkylbladsceller. Sparklines är miniatyrdiagram som passar i en enskild cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och varje typ kan anpassas med avseende på färg, linjetjocklek, hög/låg-punkter och markörer.

{{% /alert %}}

## **Introduktion**

Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymmet av ett helt diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet genom `SparklineGroup`- och `SparklineGroupCollection`-API:erna som finns i namnrymden `aspose.cells.charts`.

I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.sparkline_groups.add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ange sparkline-typ, dataintervall, målcell och visuella egenskaper såsom linjefärg, linjetjocklek, markörer samt indikatorer för högsta/lägsta punkt.

{{% alert color="primary" %}}

En enskild `SparklineGroup` kan innehålla en eller flera sparklines som delar samma stil. När du anropar `add` och skickar en rad data samt en enskild målcell får du en sparkline i den cellen. Om ditt målintervall är bredare än en cell ritas en separat sparkline i varje målcell, alla med samma stil och dataintervall.

{{% /alert %}}

Denna artikel går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **linje**, **kolumn** och **vinst/förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**

En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.Line` till metoden `sparkline_groups.add`.

Arbetsflödet är detsamma som för alla andra sparkline-typer:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumn A till E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen där sparklinen ska ritas.
4. Anropa `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. Det tredje argumentet — `False` — anger att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparkline kan du ange linjefärgen med `group.line.color` (som förväntar sig en `CellsColor` från `aspose.cells.drawing`), justera linjetjockleken och växla markörer för högsta/lägsta punkt.
6. Spara arbetsboken.

Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till E1 och lägger till en linje-sparkline i cell F1 som följer dessa värden. Det anpassar också linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

```python
import aspose.cells as ac
import System.Drawing

# Steg 1: Skapa en Workbook och hämta det första kalkylbladet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Steg 3: Bygg en CellArea som pekar på destinationscellen F1
dest = ac.CellArea()
dest.start_column = 5   # kolumn F (0-indexerad)
dest.end_column = 5
dest.start_row = 0      # rad 1 (0-indexerad)
dest.end_row = 0

# Steg 4: Lägg till en linje-sparkline från A1:E1 i F1
# SparklineGroups.Add returnerar indexet för den nyligen tillagda gruppen
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjefärgen
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Steg 6: Aktivera markörer för hög- och lågpunkt
group.show_high_point = True
group.show_low_point = True

# Steg 7: Spara arbetsboken
workbook.save("output_line.xlsx")
```

## **Kolumn-sparklines**

En kolumn-sparkline visar varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.Column` till metoden `sparkline_groups.add`.

Proceduren speglar exemplet med linje-sparkline:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll samma källintervall (A1:E1) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att sätta `group.type` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken i en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.

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

# Steg 3: Bygg ett CellArea som pekar på F1 (kolumnindex 5, radindex 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# Steg 4: Lägg till en kolumn-sparkline i destinationscellen
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# Steg 5: Bekräfta sparkline-typen genom att läsa group.Type
print("Sparkline Type added: " + str(group.type))

# Steg 6: Spara arbetsboken
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **Vinst/förlust-sparklines**

En vinst/förlust-sparkline är en speciell variant av kolumn-sparkline som är utformad för att visa endast två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat eller andra binära utfall över tid.

I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.Stacked` till metoden `sparkline_groups.add`. (Trots namnet är `SparklineType.Stacked` det enum-värde som används för att begära vinst/förlust-rendering.)

Proceduren är densamma som för de andra två typerna:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets storlek ingen roll — endast dess tecken. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att sätta accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett unikt filnamn så att alla tre exempel kan samexistera på disk.

Exemplet nedan använder samma indata som de två föregående avsnitten. Värdena 5, -3, 8, -2, 6 tolkas som vinst, förlust, vinst, förlust, vinst — och sparklinen som ritas i F1 återspeglar exakt det mönstret.

```python
import aspose.cells as ac
import System.Drawing

# Steg 1: Skapa en Workbook och hämta det första arbetsbladet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Steg 2: Fylla i exempeldata i rad 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Steg 3: Bygg en CellArea som pekar på F1 (kolumn 5, rad 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # rad 1
dest.end_row = 0

# Steg 4: Lägg till en Win/Loss-sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Steg 5: Anpassa sparkline-gruppen
# Aktivera markörer för hög- och lågpunkt
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Sätt högpunktens färg till grön
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Sätt lågpunktens färg till röd
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Sätt negativa punkters färg till orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Sätt standardfärg för serien (används för positiva staplar)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Steg 6: Spara arbetsboken
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **Kombinera alla tre sparkline-typer**

De tre föregående exemplen producerar var sin egen arbetsbok så att utdatafilerna är enkla att inspektera var för sig. I ett verkligt scenario vill du dock ofta jämföra flera dataserier sida vid sida. Det renaste sättet att göra det är att lägga mer än en sparkline-grupp i samma kalkylblad, där varje grupp renderar en annan stil.

Du kan lägga till flera `SparklineGroup`-objekt i samma `SparklineGroupCollection`, och varje grupp kan rikta sig mot en annan målcell eller ett annat intervall. Till exempel kan du placera en linje-sparkline i F1, en kolumn-sparkline i F2 och en vinst/förlust-sparkline i F3 — alla läser från samma källdata i rad 1 — så att läsaren kan se tre olika visuella behandlingar av samma siffror.

Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar på en gång.

```python
import aspose.cells as ac
import System.Drawing

# Steg 1: Skapa en Workbook och hämta det första kalkylbladet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Steg 3: Lägg till en linje-sparkline-grupp vid F1
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

# Steg 4: Lägg till en kolumn-sparkline-grupp vid F2
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

# Steg 5: Lägg till en Win/Loss (staplad) sparkline-grupp vid F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Anpassa win/loss-sparkline-serie-färgen
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Steg 6: Spara arbetsboken
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

När du kombinerar flera sparkline-grupper i ett enda kalkylblad är varje grupp oberoende. De kan dela samma källintervall eller använda olika källintervall, och de kan stylas oberoende av varandra. Detta gör det enkelt att bygga en liten "instrumentpanel" av visualiseringar i celler direkt i ett befintligt kalkylblad.

{{% /alert %}}

## **Anpassa sparkline-utseende**

När en `SparklineGroup` har skapats och lagts till i `worksheet.sparkline_groups` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De mest anpassade egenskaperna är:

- **`group.type`** — `SparklineType` (linje, kolumn eller Stacked). Den sätts när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.line.color`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.create_cells_color()`. Detta är egenskapen att använda för linjefärgen på en linje-sparkline.
- **`group.line.weight`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Markörer för högsta/lägsta punkt** — flaggor som slår på små markörer på de högsta och lägsta datapunkterna, användbart för att betona extremvärden.
- **Markörer för första/sista/negativa punkt** — flaggor som växlar markörer på de första, sista och negativa datapunkterna.

För att ändra en färg ska du alltid skapa en `CellsColor`-instans och tilldela den till relevant egenskap. Sparkline-färgegenskaper förväntar sig typen `CellsColor` från `aspose.cells.drawing` — tilldela inte ett rått färgvärde direkt till dem. Metoden `sparkline_groups.add` returnerar själv ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.



{{< app/cells/assistant language="python" >}}