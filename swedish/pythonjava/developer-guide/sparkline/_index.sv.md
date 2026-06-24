---
title: Sparklines i Aspose.Cells for Python via Java
linktitle: Sparklines
description: Aspose.Cells är ett Python via Java-bibliotek för att arbeta med kalkylbladsfiler som stöder skapande av sparklines — miniatyrdiagram placerade inuti kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylblad, sparklines, linje-sparkline, kolumn-sparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder skapande av sparklines inuti kalkylbladsceller. Sparklines är miniatyrdiagram som får plats inom en enskild cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och varje typ kan anpassas med avseende på färg, linjetjocklek, högsta/lägsta punkter samt markörer.

{{% /alert %}}

## **Introduktion**

Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymmet för ett helt diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet via `SparklineGroup`- och `SparklineGroupCollection`-API:erna som finns i namnrymden `Aspose.Cells.Charts`.

I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.getSparklineGroups().add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ställa in sparkline-typ, dataområde, målcell samt visuella egenskaper som linjefärg, linjetjocklek, markörer och indikatorer för högsta/lägsta punkt.

{{% alert color="primary" %}}

En enskild `SparklineGroup` kan innehålla en eller flera sparklines som delar samma stil. När du anropar `add` och skickar en datarad samt en enskild målcell får du en sparkline inuti den cellen. Om ditt målområde är bredare än en cell ritas en separat sparkline i varje målcell, alla med samma stil och dataområde.

{{% /alert %}}

Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**

En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.LINE` till `add`-metoden.

Arbetsflödet är detsamma som för alla andra sparkline-typer:

1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
2. Fyll i en rad med källdata (till exempel rad 1, kolumnerna A till och med E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen där sparkline ska ritas.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Det tredje argumentet — `false` — anger att dataområdet är horisontellt (en rad) och inte vertikalt (en kolumn).
5. Valfritt: anpassa den returnerade `SparklineGroup`. För en linje-sparkline kan du ställa in linjefärgen via `group.getLine().getColor()` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken och aktivera markörer för högsta/lägsta punkt.
6. Spara arbetsboken.

Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till och med E1 och lägger till en linje-sparkline i cell F1 som spårar dessa värden. Det anpassar också linjefärgen till röd och aktiverar markörer för de högsta och lägsta punkterna.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# Steg 1: Skapa en Workbook och hämta det första kalkylbladet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# Steg 3: Bygg en CellArea som pekar på målcellen F1
dest = CellArea()
dest.setStartColumn(5)  # kolumn F (0-indexerad)
dest.setEndColumn(5)
dest.setStartRow(0)     # rad 1 (0-indexerad)
dest.setEndRow(0)

# Steg 4: Lägg till en linje-sparkline från A1:E1 till F1
# SparklineGroups.add returnerar indexet för den nyligen tillagda gruppen
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjens färg
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# Steg 6: Aktivera markeringar för högsta och lägsta punkt
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# Steg 7: Spara arbetsboken
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **Kolumn-sparklines**

En kolumn-sparkline renderar varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.COLUMN` till `add`-metoden.

Proceduren speglar exemplet med linje-sparkline:

1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
2. Fyll i samma källområde (A1:E1) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Valfritt: anpassa den resulterande `SparklineGroup` — till exempel genom att ställa in `group.getType()` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken till en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.

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

# Steg 2: Skriv exempelvärden till A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# Steg 3: Bygg en CellArea som pekar mot F1 (kolumnindex 5, radindex 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# Steg 4: Lägg till en Column sparkline till destinationscellen
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

En vinst/förlust-sparkline är en specialvariant av kolumn-sparkline som är utformad för att endast visa två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat eller andra binära utfall över tid.

I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.STACKED` till `add`-metoden. (Trots namnet är `SparklineType.STACKED` det enum-värde som används för att begära vinst/förlust-renderingen.)

Proceduren är densamma som för de andra två typerna:

1. Skapa en ny `Workbook` och öppna det första kalkylbladet.
2. Fyll i källområdet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets storlek ingen roll — endast dess tecken gör det. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Valfritt: anpassa den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett distinkt filnamn så att alla tre exemplen kan samexistera på disk.

Exemplet nedan använder samma indata som de två föregående avsnitten. Värdena 5, -3, 8, -2, 6 tolkas som vinst, förlust, vinst, förlust, vinst — och sparkline som ritas i F1 återspeglar exakt det mönstret.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# Steg 1: Skapa en Workbook och hämta det första kalkylbladet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# Steg 2: Fyll i exempeldata i rad 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Steg 3: Bygg en CellArea som pekar på F1 (kolumn 5, rad 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # rad 1
dest.setEndRow(0)

# Steg 4: Lägg till en Win/Loss-sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# Steg 5: Anpassa sparkline-gruppen
# Aktivera högpunkt- och lågpunktmarkeringar
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# Ställ in högpunktens färg till grön
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# Ställ in lågpunktens färg till röd
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# Ställ in den negativa punktens färg till orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# Ställ in standardfärgen för serien (används för positiva staplar)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# Steg 6: Spara arbetsboken
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **Kombinera alla tre sparkline-typer**

De tre föregående exemplen producerar var sin egen arbetsbok så att utdatafilerna är enkla att inspektera var för sig. I ett verkligt scenario vill man dock ofta jämföra flera dataserier sida vid sida. Det renaste sättet att göra det är att placera mer än en sparkline-grupp i samma kalkylblad, där varje grupp renderar en annan stil.

Du kan lägga till flera `SparklineGroup`-objekt i samma `SparklineGroupCollection`, och varje grupp kan rikta sig till en annan målcell eller ett annat intervall. Du kan till exempel placera en linje-sparkline i F1, en kolumn-sparkline i F2 och en vinst/förlust-sparkline i F3 — alla läser från samma källdata i rad 1 — så att läsaren kan se tre olika visuella behandlingar av samma siffror.

Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar på en gång.

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

# Steg 3: Lägg till en linje-sparkline-grupp i F1
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

# Steg 4: Lägg till en kolumn-sparkline-grupp i F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# Anpassa kolumn-sparkline-seriens färg
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# Steg 5: Lägg till en vinst/förlust (staplad) sparkline-grupp i F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# Anpassa vinst/förlust-sparkline-seriens färg
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # MörkOrange
stackedGroup.setSeriesColor(stackedColor)

# Steg 6: Spara arbetsboken
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

När du kombinerar flera sparkline-grupper i ett enda kalkylblad är varje grupp oberoende. De kan dela samma källområde eller använda olika källområden, och de kan stylas oberoende av varandra. Detta gör det enkelt att bygga en liten "instrumentpanel" med visualiseringar i celler direkt inuti ett befintligt kalkylblad.

{{% /alert %}}

## **Anpassa sparkline-utseende**

När en `SparklineGroup` har skapats och lagts till i `worksheet.getSparklineGroups()` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De vanligaste egenskaperna att anpassa är:

- **`group.getType()`** — `SparklineType` (LINE, COLUMN eller STACKED). Den sätts när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.getLine().getColor()`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.createCellsColor()`. Detta är egenskapen att använda för linje-sparklines streckfärg.
- **`group.getLine().getWeight()`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Markörer för högsta/lägsta punkt** — flaggor som aktiverar små markörer på den högsta och lägsta datapunkten, användbara för att framhäva extremvärden.
- **Markörer för första/sista/negativa punkt** — flaggor som växlar markörer för den första, sista och negativa datapunkten.

För att ändra en färg ska du alltid skapa en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte en `java.awt.Color` direkt till sparkline-färgegenskaper — de förväntar sig `CellsColor`-typen från `Aspose.Cells.Drawing`. Själva `add`-metoden returnerar ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.



{{< app/cells/assistant language="python" >}}