---
title: Sparklines i Aspose.Cells for Python via Java
description: Aspose.Cells är ett Python via Java-bibliotek för arbete med kalkylbladsfiler som stöder att skapa sparklines — miniatyrdiagram placerade i kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med Aspose.Cells-biblioteket.
linktitle: Sparklines
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylblad, sparklines, linje-sparkline, kolumn-sparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder att skapa sparklines i kalkylbladsceller. Sparklines är miniatyrdiagram som får plats i en enskild cell och ger en snabb visuell representation av datatrender. Aspose.Cells stödjer linje-, kolumn- och vinst/förlust-sparklines, och var och en kan anpassas vad gäller färg, linjetjocklek, högsta/lägsta punkter samt markeringar.

## **Introduktion**
Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymmet av ett fullständigt diagram. Excel stödjer tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet via API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `Aspose.Cells.Charts`.
I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.getSparklineGroups().add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ange sparkline-typ, dataintervall, målcell samt visuella egenskaper som linjefärg, linjetjocklek, markeringar och indikatorer för högsta/lägsta punkt.
Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**
En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.LINE` till `add`-metoden.
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll i en rad med källdata (till exempel rad 1, kolumner A till och med E) med de värden du vill visualisera.
3. Skapa en `CellArea` som beskriver målcellen där sparkline ska ritas.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Det tredje argumentet — `false` — talar om för Aspose.Cells att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparkline kan du ställa in linjefärgen med `group.getLine().getColor()` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken och aktivera/avaktivera markeringar för högsta/lägsta punkt.
6. Spara arbetsboken.
Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till och med E1, och lägger till en linje-sparkline i cell F1 som spårar dessa värden. Det anpassar också linjefärgen till röd och aktiverar markeringar för de högsta och lägsta punkterna.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)
# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)
# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)
# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)
# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
jpype.shutdownJVM()
```

## **Kolumn-sparklines**
En kolumn-sparkline renderar varje datapunkt som ett vertikalt streck. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.COLUMN` till `add`-metoden.
Proceduren speglar exemplet med linje-sparkline:
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Skapa en `CellArea` som beskriver målcellen.
3. Anropa `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
4. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att anropa `group.getType()` för att bekräfta typen, eller genom att justera stapelfärgen.
5. Spara arbetsboken till en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.
Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumn-sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att snabbt se positiva och negativa bidrag.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType
# Steg 1: Skapa en Workbook och hämta det första kalkylbladet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Steg 2: Skriv exempelvärden i A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])
# Steg 3: Bygg en CellArea som pekar mot F1 (kolumnindex 5, radindex 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)
# Steg 4: Lägg till en Column-sparkline i destinationscellen
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)
# Steg 5: Bekräfta sparkline-typen genom att läsa group.Type
print("Sparkline Type added: " + str(group.getType()))
# Steg 6: Spara arbetsboken
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
jpype.shutdownJVM()
```

## **Vinst/förlust-sparklines**
En vinst/förlust-sparkline är en speciell variant av kolumn-sparkline som är utformad för att endast visa två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat eller andra binära utfall över tid.
I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.STACKED` till `add`-metoden. (Trots namnet är `SparklineType.STACKED` det enum-värde som används för att begära vinst/förlust-renderingen.)
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll i källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust har värdets storlek ingen betydelse — bara dess tecken. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Skapa en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett unikt filnamn så att alla tre exempel kan samexistera på disk.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)
# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
jpype.shutdownJVM()
```

## **Kombinera alla tre sparkline-typer**
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6, och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar på en gång.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color
# Steg 1: Skapa en Workbook och hämta det första kalkylbladet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Steg 3: Lägg till en linje-sparkline-grupp vid F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)
# Anpassa linje-sparkline-färgen via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)
# Steg 4: Lägg till en kolumn-sparkline-grupp vid F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)
# Anpassa kolumn-sparkline-serie-färgen
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)
# Steg 5: Lägg till en Win/Loss (staplad) sparkline-grupp vid F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)
# Anpassa win/loss-sparkline-serie-färgen
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)
# Steg 6: Spara arbetsboken
workbook.save("output_all.xlsx")
jpype.shutdownJVM()
```

## **Anpassa sparkline-utseende**
När en `SparklineGroup` har skapats och lagts till i `worksheet.getSparklineGroups()` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De mest anpassade egenskaperna är:
- **`group.getType()`** — `SparklineType` (LINE, COLUMN eller STACKED). Den anges när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.getLine().getColor()`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.createCellsColor()`. Detta är egenskapen att använda för linje-sparklinens streckfärg.
- **`group.getLine().getWeight()`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Markeringar för högsta/lägsta punkt** — flaggor som slår på små markeringar på de högsta och lägsta datapunkterna, användbara för att betona extremer.
- **Markeringar för första/sista/negativa punkter** — flaggor som växlar markeringar på den första, sista och negativa datapunkten.
För att ändra en färg, skapa alltid en `CellsColor`-instans och tilldela den till relevant egenskap. Tilldela inte en `java.awt.Color` direkt till sparkline-färgegenskaper — de förväntar sig typen `CellsColor` från `Aspose.Cells.Drawing`. Själva `add`-metoden returnerar ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}