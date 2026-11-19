---
title: Sparklines i Aspose.Cells for Java
linktitle: Sparklines
description: Aspose.Cells är ett Java-bibliotek för att arbeta med kalkylbladsfiler som stöder skapande av sparklines — miniatyrdiagram placerade i kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Java-bibliotek, kalkylblad, sparklines, linje-sparkline, kolumn-sparkline, vinst/förlust-sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder skapande av sparklines i kalkylbladsceller. Sparklines är miniatyrdiagram som får plats i en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och varje typ kan anpassas med avseende på färg, linjetjocklek, högsta/lägsta punkter och markörer.
{{% /alert %}}

## **Introduktion**
Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymme för ett helt diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet via API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `Aspose.Cells.Charts`.
I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.getSparklineGroups().add(...)`, som returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ange sparkline-typ, dataområde, målcell samt visuella egenskaper som linjefärg, linjetjocklek, markörer och indikatorer för högsta/lägsta punkt.
Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger och sparar den resulterande arbetsboken.

## **Linje-sparklines**
En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.LINE` till metoden `add`.
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll i en rad med källdata (till exempel rad 1, kolumnerna A till E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen där sparkline ska ritas.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Det tredje argumentet — `false` — anger att dataområdet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparkline kan du ställa in linjefärgen med `group.getLine().setColor(...)` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken och växla markörer för högsta/lägsta punkt.
6. Spara arbetsboken.
Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till E1 och lägger till en linje-sparkline i cell F1 som följer dessa värden. Det anpassar också linjefärgen till röd och aktiverar markörer för högsta och lägsta punkter.

```java
import com.aspose.cells.*;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
CellArea dest = new CellArea();
dest.StartColumn = 5;   // column F (0-indexed)
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1 (0-indexed)
dest.EndRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.add returns the index of the newly added group
int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
CellsColor red = workbook.createCellsColor();
red.setColor(com.aspose.cells.Color.getRed());
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Kolumn-sparklines**
En kolumn-sparkline återger varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars magnitud är meningsfull — till exempel månadsförsäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.COLUMN` till metoden `add`.
Proceduren speglar exemplet med linje-sparkline:
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att ställa in `group.getType()` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken i en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.
Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumn-sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att se positiva och negativa bidrag med en blick.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write sample values into A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Build a CellArea pointing to F1 (column index 5, row index 0)
CellArea dest = new CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Add a Column sparkline to the destination cell
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Confirm the sparkline type by reading group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Save the workbook
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **Vinst/förlust-sparklines**
En vinst/förlust-sparkline är en speciell variant av kolumn-sparkline som är utformad för att endast visa två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat eller andra binära utfall över tid.
I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.STACKED` till metoden `add`. (Trots namnet är `SparklineType.STACKED` det enum-värde som används för att begära vinst/förlust-rendering.)
1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll i källområdet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets magnitud ingen roll — bara dess tecken. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att ställa in accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett eget filnamn så att alla tre exemplen kan samexistera på disk.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Populate sample data
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Build a CellArea pointing to F1 (column 5, row 0)
CellArea dest = new CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Add a Win/Loss sparkline (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Customize the sparkline group
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(Color.fromArgb(70, 130, 180)); // SteelBlue approximation
group.setSeriesColor(seriesColor);
// Save the workbook
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinera alla tre sparkline-typer**
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar på en gång.

```java
import com.aspose.cells.*;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Fix: Use static factory method
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Use static factory method
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Use static factory method
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Anpassa sparklines utseende**
När en `SparklineGroup` har skapats och lagts till i `worksheet.getSparklineGroups()` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De mest anpassade egenskaperna är:
- **`group.getType()`** — `SparklineType` (LINE, COLUMN eller STACKED). Den ställs in när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.getLine().setColor(...)`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.createCellsColor()`. Detta är egenskapen att använda för linjefärgen på en linje-sparkline.
- **`group.getLine().setWeight(...)`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Markörer för högsta/lägsta punkt** — flaggor som aktiverar små markörer på den högsta och lägsta datapunkten, användbara för att betona extremvärden.
- **Markörer för första/sista/negativa punkt** — flaggor som växlar markörer på den första, sista och negativa datapunkten.
För att ändra en färg ska du alltid skapa en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte en `java.awt.Color` direkt till sparkline-färgegenskaper — de förväntar sig `CellsColor`-typen från `Aspose.Cells.Drawing`. Metoden `add` returnerar själv ett fullt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.

{{< app/cells/assistant language="java" >}}