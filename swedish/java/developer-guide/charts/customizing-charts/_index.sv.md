---
title: Anpassa diagram
type: docs
weight: 15
url: /sv/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **Skapa diagram**

Det är möjligt att lägga till en mängd olika diagram i kalkylblad med Aspose.Cells. Aspose.Cells tillhandahåller många flexibla diagramobjekt. Det här ämnet diskuterar Aspose.Cells diagramobjekt.

### **Enkelt skapa ett diagram**

Det är enkelt att skapa ett diagram med Aspose.Cells med följande exempelkoder:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Saker att veta för att skapa ett diagram**

Innan du skapar diagram är det viktigt att förstå några grundläggande begrepp som är till hjälp när du skapar diagram med Aspose.Cells.

#### **Diagramobjekt**

Aspose.Cells tillhandahåller en speciell uppsättning klasser som används för att skapa alla typer av diagram. Dessa klasser används för att skapa **diagramobjekt**, som fungerar som diagrambyggstenar. Diagramobjekten listas nedan:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), en diagramaxel.
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), ett enskilt Excel-diagram.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), diagramområdet i kalkylbladet.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), en diagramdatatabell.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), förramobjektet i ett diagram.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), en enda punkt i en serie i ett diagram.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), en samling som innehåller alla punkterna i en serie.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), en samling av [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objekt.
- Dataetiketter, dataetiketter för det angivna [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), osv.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), fyllformat för en form.
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), golvet i ett 3D-diagram.
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), diagramlegenden.
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), diagramlinjen.
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection), en samling av [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objekt.
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), representerar en enskild data serie i ett diagram.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), kryssmarkeringsetiketter associerade med kryssmarkeringar på en diagramaxel.
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), diagram- eller axeltiteln.
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), en trendlinje i ett diagram.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), en samling av alla trendlinjeobjekt för den angivna data serien.
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), väggarna i en 3D-diagram.

#### **Användning av diagramobjekt**

Som nämnts ovan är alla diagramobjekt instanser av sina respektive klasser och tillhandahåller specifika egenskaper och metoder för att utföra specifika uppgifter. Använd diagramobjekt för att skapa diagram.

Lägg till vilken typ av diagram som helst i en arbetsbok med hjälp av [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)-samlingen. Varje objekt i [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)-samlingen representerar ett [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)-objekt. Ett [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)-objekt inkapslar alla diagramobjekt som krävs för att anpassa diagrammets utseende. Nästa avsnitt visar hur man använder några grundläggande diagramobjekt för att skapa ett enkelt diagram.

### **Skapa ett enkelt diagram**

Det är möjligt att skapa många olika typer av diagram med Aspose.Cells. Alla standarddiagram som stöds av Aspose.Cells är fördefinierade i en uppräkning med namnet [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). De fördefinierade diagramtyperna är:

|**Diagramtyper**|**Beskrivning**|
| :- | :- |
|Column|Representerar det staplade kolumnl-diagrammet|
|ColumnStacked|Representerar det staplade kolumnl-diagrammet|
|Column100PercentStacked|Representerar 100% staplat kolumnl-diagram|
|Column3DClustered|Representerar 3D-staplade kolumnl-diagram|
|Column3DStacked|Representerar 3D-staplade kolumnl-diagram|
|Column3D100PercentStacked|Representerar 3D 100% staplat kolumnl-diagram|
|Column3D|Representerar 3D-kolumnl-diagram|
|Bar|Representerar det staplade stapeldiagrammet|
|BarStacked|Representerar det staplade stapeldiagrammet|
|Bar100PercentStacked|Representerar 100% staplat stapeldiagram|
|Bar3DClustered|Representerar 3D-staplade stapeldiagram|
|Bar3DStacked|Representerar 3D-staplade stapeldiagram|
|Bar3D100PercentStacked|Representerar 3D 100% staplat stapeldiagram|
|Line|Representerar linjediagram|
|LineStacked|Representerar staplat linjediagram|
|Line100PercentStacked|Representerar 100% staplat linjediagram|
|LineWithDataMarkers|Representerar linjediagram med datamarkörer|
|LineStackedWithDataMarkers|Representerar staplat linjediagram med datamarkörer|
|Line100PercentStackedWithDataMarkers|Representerar 100% staplat linjediagram med datamarkörer|
|Line3D|Representerar 3D linjediagram|
|Pie|Representerar cirkeldiagram|
|Pie3D|Representerar 3D cirkeldiagram|
|PiePie|Representerar kaka av kaka-diagram|
|PieExploded|Representerar Exploderad Cirkeldiagram|
|Pie3DExploded|Representerar 3D Exploderad Cirkeldiagram|
|PieBar|Representerar stapel av cirkeldiagram|
|Scatter|Representerar spridningsdiagrammet|
|ScatterConnectedByCurvesWithDataMarker|Representerar spridningsdiagrammet ansluten av kurvor, med datamarkörer|
|ScatterConnectedByCurvesWithoutDataMarker|Representerar spridningsdiagrammet ansluten av kurvor, utan datamarkörer|
|ScatterConnectedByLinesWithDataMarker|Representerar spridningsdiagrammet ansluten av linjer, med datamarkörer|
|ScatterConnectedByLinesWithoutDataMarker|Representerar spridningsdiagrammet ansluten av linjer, utan datamarkörer|
|Area|Representerar områdesdiagrammet|
|AreaStacked|Representerar staplade områdesdiagrammet|
|Area100PercentStacked|Representerar 100% staplade områdesdiagrammet|
|Area3D|Representerar 3D områdesdiagrammet|
|Area3DStacked|Representerar 3D staplade områdesdiagrammet|
|Area3D100PercentStacked|Representerar 3D 100% staplade områdesdiagrammet|
|Doughnut|Representerar doughnut diagrammet|
|DoughnutExploded|Representerar Exploderat doughnut diagram|
|Radar|Representerar radardiagrammet|
|RadarWithDataMarkers|Representerar radardiagrammet med datamarkörer|
|RadarFilled|Representerar fyllt radardiagram|
|Surface3D|Representerar 3D ytdiagram|
|SurfaceWireframe3D|Representerar wireframe 3D ytdiagram|
|SurfaceContour|Representerar konturdiagram|
|SurfaceContourWireframe|Representerar wireframe konturdiagram|
|Bubble|Representerar boll diagrammet|
|Bubble3D|Representerar 3D boll diagrammet|
|Cylinder|Representerar cylinderdiagram|
|CylinderStacked|Representerar staplade cylinderdiagram|
|Cylinder100PercentStacked|Representerar 100% staplade cylinderdiagram|
|CylindricalBar|Representerar cylindrisk stapeldiagram|
|CylindricalBarStacked|Representerar staplade cylindriska stapeldiagram|
|CylindricalBar100PercentStacked|Representerar 100% Staplad Cylindrisk Staplad Stapeldiagram|
|CylindricalColumn3D|Representerar 3D Cylindrisk Kolumn Diagram|
|Cone|Representerar Konediagram|
|ConeStacked|Representerar Staplad Konediagram|
|Cone100PercentStacked|Representerar 100% Staplad Konediagram|
|ConicalBar|Representerar Konisk Stapeldiagram|
|ConicalBarStacked|Representerar Staplad Konisk stapeldiagram|
|ConicalBar100PercentStacked|Representerar 100% Staplad Konisk Stapeldiagram|
|ConicalColumn3D|Representerar 3D Konisk Kolumn Diagram|
|Pyramid|Representerar Pyramid Diagram|
|PyramidStacked|Representerar Staplad Pyramiddiagram|
|Pyramid100PercentStacked|Representerar 100% Staplad Pyramiddiagram|
|PyramidBar|Representerar Pyramid Stapeldiagram|
|PyramidBarStacked|Representerar Staplad Pyramid Stapeldiagram|
|PyramidBar100PercentStacked|Representerar 100% Staplad Pyramid Stapeldiagram|
|PyramidColumn3D|Representerar 3D Pyramid Kolumn Diagram|
För att skapa en diagram med Aspose.Cells:

1. Lägg till lite data i kalkylbladsceller med [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) objektets [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) metod.
   Detta kommer att användas som datakälla för diagrammet.
1. Lägg till ett diagram i kalkylbladet genom att anropa [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) samlingen [*lägg till*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int)) metod, kapslat i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objekt.
1. Ange diagramtypen med [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) uppräkningen.
   Till exempel använder exemplet [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) värdet som diagramtyp.
1. Få tillgång till det nya [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objektet från [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) samlingen genom att skicka dess index.
1. Använd något av de diagramobjekt som är kapslade i [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objekt för att hantera diagrammet.
   Exemplet nedan använder [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) diagramobjektet för att ange diagrammets datakälla.

När du lägger till källdata till diagrammet kan datakällan vara en rad celler (t.ex. "A1:C3"), eller en följd av icke-sammanhängande celler (t.ex. "A1, A3, A5"), eller en följd av värden (t.ex. "1,2,3").

{{% alert color="primary" %}}

När du tilldelar en rad celler som datakälla kan du bara ställa in området från övre vänstra till nedre högra. Till exempel är "A1:C3" giltigt medan "C3:A1" är ogiltig.

{{% /alert %}}

Dessa allmänna steg gör det möjligt för dig att skapa vilken typ av diagram som helst. Använd olika diagramobjekt för att skapa olika diagram.

När exempelkoden körs, läggs en pyramiddiagram till arbetsbladet som visas nedan.

**Pyramiddiagram med dess datakälla**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

För att skapa en bubbel-diagram, måste [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)  vara satt till [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)  och några extra egenskaper såsom BubbleSizes, Values & XValues behöver sättas därefter. Vid körning av följande kod läggs ett bubbel-diagram till i arbetsbladet enligt nedan.

**Bubbel-diagram med dess datakälla**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Linje med Datum Markör Diagram**

För att skapa en linje med ett data markör diagram, måste [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)  vara satt till [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) och några extra egenskaper såsom bakgrundsområde, Serie Markörer, Värden & XVärden  behöver sättas. Vid körning av följande kod läggs en linje med ett data markör diagram till arbetsbladet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Skapa Anpassade Diagram**

Hittills, när vi har diskuterat diagram, har vi tittat på standarddiagram som har sina standardformateringsinställningar. Vi definierar bara datakällan, sätter några egenskaper och diagrammet skapas med sina standardformateringsinställningar. Men Aspose.Cells stöder också skapande av anpassade diagram som möjliggör för utvecklare att skapa diagram med sina egna formateringsinställningar.

### **Skapa Anpassade Diagram**

Utvecklare kan skapa anpassade diagram vid körning med hjälp av Aspose.Cells enkla API.

Ett diagram består av en dataserie. Varje dataserie i Aspose.Cells representeras av en [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objekt där [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) objektet fungerar som en samling av [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objekt. När man skapar ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (samlade i en [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) objekt).

{{% alert color="primary" %}}

För närvarande stöder endast Aspose.Cells anpassade diagram som kombinerar cirkel-, linje-, kolumn- och stapeldiagram men fler diagram kommer att stödjas i kommande versioner. För en fullständig lista över standarddiagram som Aspose.Cells stöder, läs artikeln [Diagramtyper](/cells/sv/java/diagramtyper/).

{{% /alert %}}

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett stapeldiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett stapeldiagram, kombinerat med ett linjediagram, till arbetsbladet.

**Anpassat diagram som kombinerar stapel- och linjediagram**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Programmeringsexempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

För att se en lista över stödda diagramtyper, läs artikeln [Diagramtyper](/cells/sv/java/diagramtyper/).

{{% /alert %}}

