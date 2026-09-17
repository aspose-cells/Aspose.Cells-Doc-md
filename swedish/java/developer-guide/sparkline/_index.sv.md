---
title: Sparklines i Aspose.Cells for Java
linktitle: Sparklines i Aspose.Cells for Java
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
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Steg 1: Skapa en Workbook och hämta det första arbetsbladet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();
            // Steg 2: Skriv exempelvärdena 5, -3, 8, -2, 6 i cellerna A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);
            // Steg 3: Bygg en CellArea som pekar på destinationscellen F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // kolumn F (0-indexerad)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // rad 1 (0-indexerad)
            dest.EndRow = 0;
            // Steg 4: Lägg till en linje-sparkline från A1:E1 till F1
            // SparklineGroups.add returnerar indexet för den nyligen tillagda gruppen
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjefärgen
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);
            // Steg 6: Aktivera högpunkt- och lågpunktmarkeringar
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);
            // Steg 7: Spara arbetsboken
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
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
// Skriv exempelvärden till A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Bygg en CellArea som pekar på F1 (kolumnindex 5, radindex 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Lägg till en Column-sparkline till destinationscellen
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Bekräfta sparkline-typen genom att läsa group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Spara arbetsboken
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
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Fylla i exempeldata
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Bygg en CellArea som pekar på F1 (kolumn 5, rad 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Lägg till en Vinst/Förlust-sparkline (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Anpassa sparkline-gruppen
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Ställ in högpunktens färg till grön
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);
// Ställ in lågpunktens färg till röd
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);
// Ställ in den negativa punktens färg till orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);
// Ställ in standardfärgen för serien (används för positiva staplar)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // SteelBlue-approximation
group.setSeriesColor(seriesColor);
// Spara arbetsboken
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinera alla tre sparkline-typer**
Det kombinerade exemplet nedan skapar en enda arbetsbok, fyller rad 1 med värdena 5, -3, 8, -2, 6 och lägger sedan till tre sparkline-grupper i cellerna F1, F2 och F3 — en av varje typ — så att den resulterande filen demonstrerar alla tre sparkline-stilar på en gång.

```java
import com.aspose.cells.*;
// Steg 1: Skapa en Workbook och hämta det första kalkylbladet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Steg 2: Fyll i exempeldata i rad 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Steg 3: Lägg till en linje-sparkline-grupp vid F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Fix: Använd statisk fabriksmetod
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Anpassa linje-sparkline-färgen via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Steg 4: Lägg till en kolumn-sparkline-grupp vid F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Använd statisk fabriksmetod
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Anpassa kolumn-sparkline-seriets färg
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Steg 5: Lägg till en vinst/förlust (staplad) sparkline-grupp vid F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Använd statisk fabriksmetod
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Anpassa vinst/förlust-sparkline-seriets färg
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Steg 6: Spara arbetsboken
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
{{% /alert %}}

{{< app/cells/assistant language="java" >}}