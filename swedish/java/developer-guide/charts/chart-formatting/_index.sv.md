---
title: Diagramformatering
type: docs
weight: 20
url: /sv/java/chart-formatting/
---

## **Ställa in diagramens utseende**

I [Diagramtyper](/cells/sv/java/chart-types), gav vi en kort introduktion till diagramtyperna och diagramobjekt som erbjuds av Aspose.Cells.

I den här artikeln diskuterar vi hur man anpassar utseendet på diagrammen genom att ställa in ett antal olika egenskaper:

- [Ställa in diagramområdet](/cells/sv/java/chart-formatting/#setting-chart-area).
- [Inställning av diagramlinjer](/cells/sv/java/diagramformattering/#inställning-av-diagramlinjer).
- [Tillämpning av teman](/cells/sv/java/diagramformattering/#tillämpa-microsoft-excel-20072010-teman-på-diagram).
- [Inställning av titlar för diagram och axlar](/cells/sv/java/diagramformattering/#inställning-av-titlar-för-diagram-eller-axlar).
- [Arbete med rutnät](/cells/sv/java/diagramformattering/#inställa-stora-rutnät).
- [Inställning av gränser för bak- och sidoväggar](/cells/sv/java/diagramformattering/#inställa-gränser-för-bak-och-sidoväggar).

### **Inställning av diagramområde**

Det finns olika typer av områden i ett diagram och Aspose.Cells tillhandahåller flexibiliteten att modifiera utseendet på varje område. Utvecklare kan tillämpa olika formateringsinställningar på ett område genom att ändra dess förgrundsfärg, bakgrundsfärg och fyllnad etc.

I det givna exemplet har vi tillämpat olika formateringsinställningar på olika typer av områden i ett diagram. Dessa områden inkluderar:

- Plotområde
- Diagramområde
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) område
- Området hos en enda punkt i en [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Efter att exempelkoden har exekverats kommer en kolumnutskrift att läggas till arbetsbladet enligt nedan:

**En kolumnutskrift med fyllda områden** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Inställning av diagramlinjer**

Utvecklare kan också tillämpa olika typer av stilar på linjerna eller datamarkörerna för [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) enligt exemplet nedan. Genom att exekvera exempelkoden läggs en kolumnutskrift till arbetsbladet enligt nedan:

**Kolumnutskrift efter tillämpning av linjestilar** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Tillämpning av Microsoft Excel 2007/2010 teman på diagram**

Utvecklare kan tillämpa olika Microsoft Excel-teman och färger på [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) eller andra diagramobjekt enligt exemplet nedan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Inställning av diagram- eller axeltitlar**

Du kan använda Microsoft Excel för att ställa in titlarna på ett diagram och dess axlar i en WYSIWYG-miljö enligt nedan.

**Inställning av titlar för ett diagram & dess axlar med hjälp av Microsoft Excel** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells tillåter också utvecklare att ställa in titlarna på ett diagram och dess axlar vid körning. Alla diagram och deras axlar innehåller en [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)-metod som kan användas för att ställa in deras titlar enligt exemplet nedan. Efter att exempelkoden har exekverats kommer en kolumnutskrift att läggas till arbetsbladet enligt nedan:

**Kolumnutskrift efter inställning av titlar** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Inställning av stora rutnät**

#### **Dölja stora rutnät**

Utvecklare kan kontrollera synligheten för stora rutnät genom att använda [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible)-metoden för [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)-objektet. Efter att ha dolt de stora rutnäten kommer en kolumnutskrift som lagts till arbetsbladet att se ut enligt följande:

**En kolumnutskrift med dolda stora rutnät** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Ändra inställningar för stora rutnät**

Utvecklare kan inte bara kontrollera synligheten för stora rutnät utan också andra egenskaper inklusive dess färg etc. Efter att ha ställt in färgen på stora rutnät kommer en kolumnutskrift som lades till arbetsbladet att se ut enligt nedan:

**Kolumnutskrift med färgade stora rutnät** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Inställning av ramar för bak- och sidoväggar**

Sedan utgivningen av Microsoft Excel 2007 har väggarna i en 3D-diagram delats in i två delar: sidovägg och bakvägg, så vi måste använda två [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) objekt för att representera dem separat och du kan komma åt dem genom att använda [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) och [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

Exemplet nedan visar hur man ställer in sidoväggens kant genom att använda olika attribut.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Ändra diagrammets position och storlek**

Ibland vill du ändra positionen eller storleken på det nya eller befintliga diagrammet i arbetsbladet. Aspose.Cells tillhandahåller [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject)-egenskapen för att uppnå detta. Du kan använda dess underegenskaper för att ändra diagrammet med ny **höjd** och **bredd** eller ompositionera det med nya **X** och **Y**-koordinater.

### **Ändra diagrammets position och storlek**

För att ändra diagrammets position (X, Y-koordinater) och storlek (höjd, bredd), använd dessa egenskaper:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

Följande exempel förklarar användningen av ovanstående egenskaper. Det laddar den befintliga arbetsboken som innehåller ett diagram i dess första arbetsblad. Sedan ändrar det storlek och position på diagrammet och sparar arbetsboken.

Innan körning av provkoden ser källfilen ut så här:

**Diagramstorlek och position före körning av provkoden** 

![todo:image_alt_text](chart-formatting_7.png)

Efter körning ser utdatafilen ut så här:

**Diagramstorlek och position efter körning av provkoden** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipulering av Designerdiagram**

Det finns stunder när du kanske behöver manipulera eller ändra diagrammen i dina designer mallfiler. Aspose.Cells stöder fullständigt att manipulera designerdiagram med dess innehåll och element. Data, diagraminnehåll, bakgrundsbild och formatering kan bevaras med precision.

### **Manipulera designerdiagram i mallfilerna**

För att manipulera designerdiagram i en mallfil, använd alla diagramrelaterade API-anrop. Använd till exempel [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts)-egenskapen för att hämta den befintliga diagramssamlingen i mallfilen.

#### **Skapa ett diagram**

Följande exempel visar hur man skapar ett cirkeldiagram. Vi kommer att manipulera detta diagram senare. Följande utdata genereras av koden.

**Det inmatade cirkeldiagrammet** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipulera diagrammet**

Följande exempel visar hur man manipulerar det befintliga diagrammet. I det här exemplet modifierar vi diagrammet som skapades ovan. Följande utdata genereras av koden. Observera att färgen på diagramtiteln har ändrats från blå till svart, och 'England 30000' har ändrats till 'United Kingdom, 30K'.

**Cirkeldiagrammet har ändrats** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipulera ett linjediagram i designmallen**

I det här exemplet kommer vi att manipulera ett linjediagram. Vi kommer att lägga till några data-serier i det befintliga diagrammet och ändra deras linjefärger.

Först, ta en titt på designlinjediagrammet.

**Det inmatade linjediagrammet** 

![todo:image_alt_text](chart-formatting_11.png)

Nu manipulerar vi linjediagrammet (som finns i filen **linechart.xls**) med följande kod. Följande utdata genereras av koden.

**Det manipulerade linjediagrammet** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Användning av sparklines**

Microsoft Excel 2010 kan analysera information på fler sätt än någonsin tidigare. Det låter användarna spåra och markera viktiga datatrender med nya verktyg för dataanalys och visualisering. Sparklines är minidiagram som du kan placera i celler så att du kan se data och diagram på samma tabell. När sparklines används på rätt sätt blir dataanalys snabbare och mer fokuserad. De ger också en enkel vy av information och undviker överfyllda arbetsblad med många upptagna diagram.

Aspose.Cells erbjuder en API för att manipulera sparklines i kalkylblad.

### **Sparklines i Microsoft Excel**

För att infoga sparklines i Microsoft Excel 2010:

1. Välj cellerna där du vill att sparklines ska visas. För att göra dem enkla att visa, välj celler bredvid datan.
1. Klicka på **Infoga** på menyn och välj sedan **kolumn** i **Sparklines** gruppen.

![todo:image_alt_text](chart-formatting_13.png)

1. Välj eller ange området med celler i arbetsbladet som innehåller källdatan.
   Diagrammen visas.

Sparklines hjälper dig att se trender, till exempel, eller vinst- eller förlustrekord för en softbolliga. Sparklines kan till och med summera hela säsongen för varje lag i ligan.

![todo:image_alt_text](chart-formatting_14.png)

### **Sparklines med användning av Aspose.Cells**

Utvecklare kan skapa, ta bort eller läsa sparklines (i mallfilen) med hjälp av API:et som tillhandahålls av Aspose.Cells. Genom att lägga till anpassade grafik för en given dataserie har utvecklare friheten att lägga till olika typer av små diagram i valda cellområden.

Exemplet nedan demonstrerar funktionen Sparklines. Exemplet visar hur man:

1. Öppna en enkel mallfil.
1. Läs sparklinesinformation för ett arbetsblad.
1. Lägg till nya gnistrande linjer för ett givet datintervall till ett cellområde.
1. Sparar Excel-filen på disken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Tillämpa 3D-format på diagram**

Du kan behöva 3D-diagramstilar så att du kan få just resultat för ditt scenario. Aspose.Cells API:er tillhandahåller relevant API för att tillämpa Microsoft Excel 2007 3D-formatering som demonstreras i den här artikeln.

### **Ange 3D-format på diagram**

Ett komplett exempel ges nedan för att demonstrera hur man skapar ett diagram och tillämpar Microsoft Excel 2007 3D-formatering. Efter att ovanstående exempelkod har utförts kommer ett kolumn diagram (med 3D-effekter) att läggas till i arbetsbladet som visas nedan.

**Ett kolumn diagram med 3D-formatering**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

För en fullständig lista över vilka 2D- och 3D-diagram som stöds, se [Stödda diagramtyper för rendering](/cells/sv/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Fortsatta ämnen**
- [Ange bild som bakgrundsfyllning i diagrammet.](/cells/sv/java/set-picture-as-background-fill-in-the-chart/)
