---
title: Sparklines i Aspose.Cells för Aspose.Cells for Java
linktitle: Sparklines
description: Aspose.Cells är ett Java-bibliotek för att arbeta med kalkylbladsfiler som stöder skapande av sparklines — miniatyrdiagram placerade inuti kalkylbladsceller. Den här artikeln förklarar hur man lägger till och anpassar linje-, kolumn- och vinst/förlust-sparklines med hjälp av Aspose.Cells-biblioteket.
keywords: Aspose.Cells, Java library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /sv/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder skapande av sparklines inuti kalkylbladsceller. Sparklines är miniatyrdiagram som får plats i en enda cell och ger en snabb visuell representation av datatrender. Aspose.Cells stöder linje-, kolumn- och vinst/förlust-sparklines, och varje typ kan anpassas med avseende på färg, linjetjocklek, högsta/lägsta punkter samt markeringar.

{{% /alert %}}

## **Introduktion**

Sparklines är små diagram i celler som är användbara när du vill visa en snabb trend intill en rad eller kolumn med data utan att ta upp utrymmet för ett helt diagram. Excel stöder tre typer av sparklines: **linje**, **kolumn** och **vinst/förlust**. Aspose.Cells speglar denna funktionalitet genom API:erna `SparklineGroup` och `SparklineGroupCollection` som finns i namnrymden `Aspose.Cells.Charts`.

I Aspose.Cells skapas varje sparkline du lägger till via `worksheet.getSparklineGroups().add(...)`, vilket returnerar ett `SparklineGroup`-objekt. Du kan sedan använda det objektet för att ange sparkline-typ, dataintervall, målcell samt visuella egenskaper som linjefärg, linjetjocklek, markeringar och indikatorer för högsta/lägsta punkt.

{{% alert color="primary" %}}

En enskild `SparklineGroup` kan innehålla en eller flera sparklines som delar samma stil. När du anropar `add` och skickar en rad med data plus en enda målcell får du en sparkline inuti den cellen. Om ditt målintervall är bredare än en cell ritas en separat sparkline i varje målcell, alla med samma stil och dataintervall.

{{% /alert %}}

Den här artikeln går igenom var och en av de tre sparkline-typer som stöds av Aspose.Cells — **Linje**, **Kolumn** och **Vinst/Förlust** — och visar hur man lägger till dem, anpassar deras färger samt sparar den resulterande arbetsboken.

## **Linje-sparklines**

En linje-sparkline ritar en kontinuerlig linje genom datapunkterna i en serie, vilket gör den till det mest naturliga valet för att visa trender över tid. I Aspose.Cells skapas en linje-sparkline genom att skicka `SparklineType.LINE` till metoden `add`.

Arbetsflödet är detsamma som för andra sparkline-typer:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll en rad med källdata (till exempel rad 1, kolumn A till E) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver den målcell där sparkline ska ritas.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Det tredje argumentet — `false` — anger att dataintervallet är horisontellt (en rad), inte vertikalt (en kolumn).
5. Anpassa eventuellt den returnerade `SparklineGroup`. För en linje-sparkline kan du ställa in linjefärgen med `group.getLine().setColor(...)` (som förväntar sig en `CellsColor` från `Aspose.Cells.Drawing`), justera linjetjockleken samt aktivera markeringar för högsta/lägsta punkter.
6. Spara arbetsboken.

Följande exempel skapar en arbetsbok, skriver värdena 5, -3, 8, -2, 6 i cellerna A1 till E1, och lägger till en linje-sparkline i cell F1 som spårar dessa värden. Det anpassar också linjefärgen till röd och aktiverar markeringar för de högsta och lägsta punkterna.

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

            // Steg 3: Bygg en CellArea som pekar på målcellen F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // kolumn F (0-indexerad)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // rad 1 (0-indexerad)
            dest.EndRow = 0;

            // Steg 4: Lägg till en Line-sparkline från A1:E1 till F1
            // SparklineGroups.add returnerar indexet för den nyligen tillagda gruppen
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Steg 5: Skapa en röd CellsColor och tilldela den till sparkline-linjens färg
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Steg 6: Aktivera markeringar för hög- och lågpunkt
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

En kolumn-sparkline renderar varje datapunkt som en vertikal stapel. Detta gör den väl lämpad för data vars storlek är meningsfull — till exempel månatliga försäljningssiffror eller antal. I Aspose.Cells skapar du en kolumn-sparkline genom att skicka `SparklineType.COLUMN` till metoden `add`.

Proceduren speglar exemplet med linje-sparkline:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll samma källintervall (A1:E1) med de värden du vill visualisera.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Anpassa eventuellt den resulterande `SparklineGroup` — till exempel genom att sätta `group.getType()` för att bekräfta typen, eller genom att justera stapelfärgen.
6. Spara arbetsboken i en separat utdatafil så att den inte skriver över exemplet med linje-sparkline.

Exemplet nedan skriver värdena 5, -3, 8, -2, 6 i A1:E1 och renderar en kolumn-sparkline i F1. Negativa värden ritas som staplar som går nedåt och positiva värden som staplar som går uppåt, vilket gör det enkelt att snabbt se positiva och negativa bidrag.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Skriv exempelvärden i A1:E1
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

// Lägg till en kolumn-sparkline i målcellen
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// Bekräfta sparkline-typen genom att läsa group.Type
System.out.println("Sparkline Type added: " + group.getType());

// Spara arbetsboken
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **Vinst/förlust-sparklines**

En vinst/förlust-sparkline är en specialvariant av kolumn-sparkline som är utformad för att visa endast två utfall: ett positivt värde ritas som en "uppåt"-stapel (en vinst) och ett noll- eller negativt värde ritas som en "nedåt"-stapel (en förlust). Vinst/förlust-sparklines används ofta för att visualisera sekvenser av vinster och förluster, godkänt/underkänt-resultat eller andra binära utfall över tid.

I Aspose.Cells skapas en vinst/förlust-sparkline genom att skicka `SparklineType.STACKED` till metoden `add`. (Trots namnet är `SparklineType.STACKED` det enum-värde som används för att begära vinst/förlust-renderingen.)

Proceduren är densamma som för de andra två typerna:

1. Skapa en ny `Workbook` och hämta det första kalkylbladet.
2. Fyll källintervallet. Eftersom vinst/förlust-sparklines behandlar varje värde som antingen en vinst eller en förlust spelar värdets storlek ingen roll — bara dess tecken. Positiva värden blir uppåt-staplar och icke-positiva värden blir nedåt-staplar.
3. Bygg en `CellArea` som beskriver målcellen.
4. Anropa `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Anpassa eventuellt den returnerade `SparklineGroup`, till exempel genom att ange accentfärger för vinst- och förluststaplarna.
6. Spara arbetsboken under ett distinkt filnamn så att alla tre exempel kan samexistera på disk.

Exemplet nedan använder samma indata som de två föregående avsnitten. Värdena 5, -3, 8, -2, 6 tolkas som vinst, förlust, vinst, förlust, vinst — och sparkline som ritas i F1 återspeglar exakt det mönstret.

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

// Lägg till en vinst/förlust-sparkline (SparklineType.Stacked)
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

// Ställ in negativa punkters färg till orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// Ställ in standardfärgen för serien (används för positiva staplar)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // Ungefärlig SteelBlue
group.setSeriesColor(seriesColor);

// Spara arbetsboken
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Kombinera alla tre sparkline-typer**

De tre föregående exemplen producerar var sin egen arbetsbok så att utdatafilerna är enkla att inspektera var för sig. I ett verkligt scenario vill man dock ofta jämföra flera dataserier sida vid sida. Det renaste sättet att göra det är att placera mer än en sparkline-grupp i samma kalkylblad, där varje grupp renderar en annan stil.

Du kan lägga till flera `SparklineGroup`-objekt i samma `SparklineGroupCollection`, och varje grupp kan rikta sig mot en annan målcell eller ett annat intervall. Du kan till exempel placera en linje-sparkline i F1, en kolumn-sparkline i F2 och en vinst/förlust-sparkline i F3 — alla läser från samma källdata i rad 1 — så att läsaren kan se tre olika visuella behandlingar av samma siffror.

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

// Anpassa kolumn-sparkline-seriefärgen
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Steg 5: Lägg till en Win/Loss (staplad) sparkline-grupp vid F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Använd statisk fabriksmetod
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Anpassa win/loss-sparkline-seriefärgen
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Steg 6: Spara arbetsboken
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

När du kombinerar flera sparkline-grupper i ett enda kalkylblad är varje grupp oberoende. De kan dela samma källintervall eller använda olika källintervall, och de kan stylas oberoende av varandra. Detta gör det enkelt att bygga en liten "instrumentpanel" av visualiseringar i celler direkt inuti ett befintligt kalkylblad.

{{% /alert %}}

## **Anpassa sparklines utseende**

När en `SparklineGroup` har skapats och lagts till i `worksheet.getSparklineGroups()` kan du läsa eller ändra flera av dess visuella egenskaper innan du sparar arbetsboken. De egenskaper som oftast anpassas är:

- **`group.getType()`** — `SparklineType` (LINE, COLUMN eller STACKED). Den sätts när gruppen läggs till, men du kan läsa tillbaka den för att bekräfta.
- **`group.getLine().setColor(...)`** — linjefärgen, uttryckt som en `CellsColor` skapad via `workbook.createCellsColor()`. Detta är egenskapen som ska användas för linje-sparklines streckfärg.
- **`group.getLine().setWeight(...)`** — linjetjockleken i punkter. Högre värden ger tjockare linjer.
- **Markeringar för högsta/lägsta punkt** — flaggor som slår på små markeringar på den högsta och lägsta datapunkten, användbara för att betona extremer.
- **Markeringar för första/sista/negativa punkt** — flaggor som växlar markeringar på den första, sista och negativa datapunkten.

För att ändra en färg, skapa alltid en `CellsColor`-instans och tilldela den till den relevanta egenskapen. Tilldela inte en `java.awt.Color` direkt till sparkline-färgegenskaper — de förväntar sig typen `CellsColor` från `Aspose.Cells.Drawing`. Själva metoden `add` returnerar ett fullständigt typat `SparklineGroup`-objekt, så du kan kedja egenskapstilldelningar på returvärdet eller lagra det i en lokal variabel och anpassa det innan du sparar.



{{< app/cells/assistant language="java" >}}