---
title: Diagramformatering
type: docs
weight: 20
url: /sv/java/chart-formatting/
---
## **Ställa in diagrammets utseende**

 I[Diagramtyper](/cells/sv/java/chart-types/), gav vi en kort introduktion till de typer av diagram och kartobjekt som erbjuds av Aspose.Cells.

I den här artikeln diskuterar vi hur du anpassar diagrammets utseende genom att ställa in ett antal olika egenskaper:

- [Ställa in sjökortsområdet](/cells/sv/java/chart-formatting/#setting-chart-area).
- [Ställa in diagramlinjer](/cells/sv/java/chart-formatting/#setting-chart-lines).
- [Tillämpa teman](/cells/sv/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Ställa in titlar till diagram och axlar](/cells/sv/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Arbeta med rutnät](/cells/sv/java/chart-formatting/#setting-major-gridlines).
- [Inställning av bårder för bak- och sidoväggar](/cells/sv/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Inställning av sjökortsområde**

Det finns olika typer av områden i ett diagram och Aspose.Cells ger flexibiliteten att ändra utseendet på varje område. Utvecklare kan tillämpa olika formateringsinställningar på ett område genom att ändra dess förgrundsfärg, bakgrundsfärg och fyllningsformat etc.

I exemplet nedan har vi tillämpat olika formateringsinställningar på olika typer av områden i ett diagram. Dessa områden inkluderar:

- Tomtområde
- Kartområde
- [**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) område
- Arean av en enda punkt i en[**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Efter exekvering av exempelkoden kommer ett kolumndiagram att läggas till i kalkylbladet enligt nedan:

**Ett kolumndiagram med fyllda områden** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Ställa in sjökortslinjer**

 Utvecklare kan också tillämpa olika typer av stilar på linjerna eller datamarkörerna för[**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)som visas nedan i exemplet. Genom att köra exempelkoden läggs ett kolumndiagram till i kalkylbladet som visas nedan:

**Kolumndiagram efter applicering av linjeformat** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Tillämpa Microsoft Excel 2007/2010-teman på diagram**

 Utvecklare kan tillämpa olika Microsoft Excel-teman och färger på[**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)eller andra diagramobjekt som visas i exemplet nedan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Ställa in titlar på diagram eller axlar**

Du kan använda Microsoft Excel för att ställa in titlarna på ett diagram och dess axlar i en WYSIWYG-miljö som visas nedan.

**Ställa in titlar för ett diagram och dess axlar med Microsoft Excel** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells tillåter också utvecklare att ställa in titlarna på ett diagram och dess axlar under körning. Alla diagram och deras axlar innehåller en[**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)metod som kan användas för att ställa in deras titlar som visas nedan i ett exempel. Efter exekvering av exempelkoden kommer ett kolumndiagram att läggas till i kalkylbladet enligt nedan:

**Kolumndiagram efter inställning av titlar** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Ställa in stora rutnät**

#### **Döljer stora rutnät**

 Utvecklare kan kontrollera synligheten för större rutnät genom att använda[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) metod för[**Linje**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)objekt. Efter att ha gömt de stora rutnätslinjerna har ett kolumndiagram som lagts till i kalkylbladet följande utseende:

**Ett kolumndiagram med dolda större rutnät** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Ändra större rutnätsinställningar**

Utvecklare kan inte bara kontrollera synligheten för större rutnätslinjer utan även andra egenskaper inklusive dess färg etc. Efter att ha ställt in färgen på större rutnätslinjer kommer ett kolumndiagram som läggs till i kalkylbladet att se följande ut:

**Kolumndiagram med färgade stora rutnät** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Ställa in kanter för bak- och sidoväggar**

 Sedan Microsoft Excel 2007 släpptes har väggarna i ett 3D-diagram delats upp i två delar: sidovägg och bakvägg, så vi måste använda två[**Väggar**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) objekt för att representera dem separat och du kan komma åt dem genom att använda[**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) och[**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

Exemplet nedan visar hur man ställer in sidoväggens kant genom att använda olika attribut.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Ändra diagramposition och storlek**

 Ibland vill du ändra positionen eller storleken på det nya eller befintliga diagrammet i kalkylbladet. Aspose.Cells tillhandahåller[**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) egendom för att uppnå detta. Du kan använda dess underegenskaper för att ändra storlek på diagrammet med nytt**höjd** och**bredd** eller placera om den med ny** X** och**Y** koordinater.

### **Ändra diagrammets position och storlek**

För att ändra diagrammets position (X, Y-koordinater) och storlek (höjd, bredd), använd dessa egenskaper:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

Följande exempel förklarar användningen av ovanstående egenskaper. Den laddar den befintliga arbetsboken som innehåller ett diagram i sitt första kalkylblad. Sedan ändrar den storleken och placerar om diagrammet och sparar arbetsboken.

Innan exekveringen av exempelkoden ser källfilen ut så här:

**Diagramstorlek och position före exekvering av exempelkod** 

![todo:image_alt_text](chart-formatting_7.png)

Efter körningen ser utdatafilen ut så här:

**Diagramstorlek och position efter exekvering av exempelkod** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipulera designerdiagram**

Det finns en tid då du kan behöva manipulera eller modifiera diagrammen i dina designermallfiler. Aspose.Cells har fullt stöd för att manipulera designerdiagram med dess innehåll och element. Data, diagraminnehåll, bakgrundsbild och formatering kan bevaras med noggrannhet.

### **Manipulera designerdiagram i mallfilerna**

 För att manipulera designerdiagram i en mallfil, använd alla diagramrelaterade API-anrop. Använd till exempel[**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) egenskap för att få den befintliga diagramsamlingen i mallfilen.

#### **Skapa ett diagram**

Följande exempel visar hur man skapar ett cirkeldiagram. Vi kommer att manipulera detta diagram senare. Följande utdata genereras av koden.

**Ingångscirkeldiagrammet** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipulera diagrammet**

Följande exempel visar hur man manipulerar det befintliga diagrammet. I det här exemplet ändrar vi diagrammet som skapats ovan. Följande utdata genereras av koden. Observera att färgen på sjökortstiteln har ändrats från blå till svart och 'England 30000' har ändrats till 'United Kingdom, 30K'.

**Cirkeldiagrammet har ändrats** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipulera ett linjediagram i designermallen**

det här exemplet kommer vi att manipulera ett linjediagram. Vi kommer att lägga till några dataserier till det befintliga diagrammet och ändra deras linjefärger.

Ta först en titt på designerns linjediagram.

**Ingångslinjediagrammet** 

![todo:image_alt_text](chart-formatting_11.png)

 Nu manipulerar vi linjediagrammet (som finns i**linjediagram.xls** fil) med följande kod. Följande utdata genereras av koden.

**Det manipulerade linjediagrammet** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Använder Sparklines**

Microsoft Excel 2010 kan analysera information på fler sätt än någonsin tidigare. Det låter användare spåra och lyfta fram viktiga datatrender med nya verktyg för dataanalys och visualisering. Sparklines är minidiagram som du kan placera inuti celler så att du kan se data och diagram på samma tabell. När sparklines används på rätt sätt går dataanalysen snabbare och mer rakt på sak. De ger också en enkel bild av information, och undviker överfulla kalkylblad med många upptagna diagram.

Aspose.Cells tillhandahåller ett API för att manipulera sparklines i kalkylblad.

### **Sparklines i Microsoft Excel**

Så här infogar du sparklines i Microsoft Excel 2010:

1. Markera cellerna där du vill att gnistlinjerna ska visas. För att göra dem enkla att se, markera celler vid sidan av data.
1.  Klick**Föra in** på bandet och välj sedan**kolumn** i**Sparklines** grupp.

![todo:image_alt_text](chart-formatting_13.png)

1. Välj eller ange cellintervallet i kalkylbladet som innehåller källdata.
 Diagrammen visas.

Sparklines hjälper dig att se trender, till exempel, eller vinst- eller förlustrekordet för en softballliga. Sparklines kan till och med summera hela säsongen för varje lag i ligan.

![todo:image_alt_text](chart-formatting_14.png)

### **Sparklines med Aspose.Cells**

Utvecklare kan skapa, ta bort eller läsa sparklines (i mallfilen) med API:et som tillhandahålls av Aspose.Cells. Genom att lägga till anpassad grafik för ett givet dataintervall har utvecklarna friheten att lägga till olika typer av små diagram till utvalda cellområden.

Exemplet nedan visar Sparklines-funktionen. Exemplet visar hur man:

1. Öppna en enkel mallfil.
1. Läs sparklines-information för ett kalkylblad.
1. Lägg till nya sparklines för ett givet dataintervall till ett cellområde.
1. Sparar Excel-filen på disk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Tillämpa 3D-format på diagram**

Du kanske behöver 3D-diagramstilar så att du kan få precis resultaten för ditt scenario. Aspose.Cells API:er tillhandahåller relevant API för att tillämpa Microsoft Excel 2007 3D-formatering som visas i den här artikeln.

### **Ställa in 3D-format till diagram**

Ett komplett exempel ges nedan för att visa hur man skapar ett diagram och använder Microsoft Excel 2007 3D-formatering. Efter exekvering av ovanstående exempelkod kommer ett kolumndiagram (med 3D-effekter) att läggas till i kalkylbladet enligt nedan.

**Ett kolumndiagram med 3D-formatering**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

 För en fullständig lista över vilka 2D- och 3D-diagram som stöds, se[Diagramtyper som stöds för rendering](/cells/sv/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Förhandsämnen**
- [Ställ in bild som bakgrund Fyll i diagrammet](/cells/sv/java/set-picture-as-background-fill-in-the-chart/)
