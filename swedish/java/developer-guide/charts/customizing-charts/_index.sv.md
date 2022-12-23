---
title: Anpassa diagram
type: docs
weight: 15
url: /sv/java/creating-and-customizing-charts/
---
## **Skapa diagram**

Det är möjligt att lägga till en mängd olika diagram till kalkylblad med Aspose.Cells. Aspose.Cells tillhandahåller många flexibla diagramobjekt. Det här ämnet diskuterar Aspose.Cells' diagramobjekt.

### **Skapa helt enkelt ett diagram**

Det är enkelt att skapa ett diagram med Aspose.Cells med följande exempelkoder:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Saker att veta för att skapa ett diagram**

Innan du skapar diagram är det viktigt att förstå några grundläggande begrepp som är användbara när du skapar diagram med Aspose.Cells.

#### **Kartlägga objekt**

 Aspose.Cells tillhandahåller en speciell uppsättning klasser som används för att skapa alla typer av diagram. Dessa klasser används för att skapa**kartlägga objekt**, som fungerar som diagrammets byggstenar. Kartobjekten listas nedan:

- [**Axel**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), ett diagrams axel.
- [**Diagram**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), ett enda Excel-diagram.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), diagramområdet i kalkylbladet.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), en diagramdatatabell.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), ramobjektet i ett diagram.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), en enda punkt i en serie i ett diagram.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), en samling som innehåller alla punkter i en serie.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , en samling av[**Diagram**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)föremål.
-  DataLabels, DataLabels för den angivna[**Serier**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendlinje**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), etc.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), fyllningsformat för en form.
- [**Golv**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), golvet i ett 3D-diagram.
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), sjökortsförklaringen.
- [**Linje**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), diagramlinjen.
- [**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , en samling av[**Serier**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)föremål.
- [**Serier**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), representerar en enskild dataserie i ett diagram.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), bockmarkeringsetiketterna som är associerade med bockmarkeringar på en diagramaxel.
- [**Titel**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), titeln på ett diagram eller en axel.
- [**Trendlinje**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), en trendlinje i ett diagram.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), en samling av alla Trendline-objekt för den angivna dataserien.
- [**Väggar**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), väggarna i ett 3D-diagram.

#### **Använda diagramobjekt**

Som nämnts ovan är alla diagramobjekt instanser av sina respektive klasser och tillhandahåller specifika egenskaper och metoder för att utföra specifika uppgifter. Använd diagramobjekt för att skapa diagram.

Lägg till vilken typ av diagram som helst i ett kalkylblad med hjälp av[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) samling. Varje objekt i[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) samlingen representerar en[**Diagram**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objekt. A[**Diagram**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)objekt kapslar in alla diagramobjekt som krävs för att anpassa diagrammets utseende. Nästa avsnitt visar hur du använder några grundläggande diagramobjekt för att skapa ett enkelt diagram.

### **Skapa ett enkelt diagram**

 Det är möjligt att skapa många olika typer av sjökort med Aspose.Cells. Alla standarddiagram som stöds av Aspose.Cells är fördefinierade i en uppräkning med namnet[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). De fördefinierade diagramtyperna är:

|**Diagramtyper**|**Beskrivning**|
|:- |:- |
|Kolumn|Representerar det klustrade kolumndiagrammet|
|KolumnStackad|Representerar staplade kolumndiagram|
|Kolumn100ProcentStackad|Representerar 100 % staplat kolumndiagram|
|Kolumn3DClustrerad|Representerar 3D-klustrade kolumndiagram|
|Kolumn3DStackad|Representerar 3D staplade kolumndiagram|
|Kolumn3D100PercentStacked|Representerar 3D 100 % staplade kolumndiagram|
|Kolumn 3D|Representerar 3D-kolumndiagram|
|Bar|Representerar klustrade stapeldiagram|
|BarStacked|Representerar staplade stapeldiagram|
|Bar100PercentStacked|Representerar 100 % staplat stapeldiagram|
|Bar3DClustered|Representerar 3D-klustrade stapeldiagram|
|Bar3DStacked|Representerar 3D staplade stapeldiagram|
|Bar3D100PercentStacked|Representerar 3D 100 % staplade stapeldiagram|
|Linje|Representerar linjediagram|
|LineStacked|Representerar staplade linjediagram|
|Line100PercentStacked|Representerar 100 % staplade linjediagram|
|LineWithDataMarkers|Representerar linjediagram med datamarkörer|
|LineStackedWithDataMarkers|Representerar staplade linjediagram med datamarkörer|
|Line100PercentStackedWithDataMarkers|Representerar 100 % staplade linjediagram med datamarkörer|
|Line3D|Representerar 3D-linjediagram|
|Paj|Representerar cirkeldiagram|
|Pie3D|Representerar 3D-cirkeldiagram|
|PiePie|Representerar cirkeldiagram|
|PieExploderade|Representerar exploderat cirkeldiagram|
|Pie3DE exploderade|Representerar 3D-exploderat cirkeldiagram|
|PieBar|Representerar Bar of Pie Chart|
|Sprida ut|Representerar spridningsdiagrammet|
|ScatterConnectedByCurvesWithDataMarker|Representerar spridningsdiagrammet kopplat av kurvor, med datamarkörer|
|ScatterConnectedByCurvesWithoutDataMarker|Representerar spridningsdiagrammet kopplat med kurvor, utan datamarkörer|
|ScatterConnectedByLinesWithDataMarker|Representerar spridningsdiagrammet kopplat med linjer, med datamarkörer|
|ScatterConnectedByLinesWithoutDataMarker|Representerar spridningsdiagrammet kopplat med linjer, utan datamarkörer|
|Område|Representerar områdesdiagram|
|AreaStacked|Representerar staplade ytdiagram|
|Area100PercentStacked|Representerar 100 % staplade ytdiagram|
|Area3D|Representerar 3D-områdesdiagram|
|Area3DStacked|Representerar 3D Stacked Area Chart|
|Area3D100PercentStacked|Representerar 3D 100 % staplade ytdiagram|
|Munk|Representerar munkdiagram|
|Doughnut Exploderade|Representerar Exploded Donut Chart|
|Radar|Representerar radardiagrammet|
|RadarWithDataMarkers|Representerar radardiagrammet med datamarkörer|
|Radarfylld|Representerar fyllt radardiagram|
|Surface3D|Representerar 3D-ytdiagram|
|SurfaceWireframe3D|Representerar Wireframe 3D-ytdiagrammet|
|Ytkontur|Representerar konturdiagram|
|SurfaceContourWireframe|Representerar Wireframe Contour Chart|
|Bubbla|Representerar bubbeldiagram|
|Bubble3D|Representerar 3D Bubble Chart|
|Cylinder|Representerar cylinderdiagram|
|CylinderStacked|Representerar diagram över staplade cylindrar|
|Cylinder100PercentStacked|Representerar 100 % staplade cylinderdiagram|
|Cylindrical Bar|Representerar cylindriskt stapeldiagram.|
|CylindricalBarStacked|Representerar staplade cylindriska stapeldiagram|
|CylindricalBar100PercentStacked|Representerar 100 % staplade cylindriska stapeldiagram|
|CylindricalColumn3D|Representerar 3D Cylindrical Column Chart|
|Kon|Representerar kondiagram|
|ConeStacked|Representerar Stacked Cone Chart|
|Cone100PercentStacked|Representerar 100 % staplade kondiagram|
|ConicalBar|Representerar koniskt stapeldiagram|
|ConicalBarStacked|Representerar staplade koniska stapeldiagram|
|ConicalBar100PercentStacked|Representerar 100 % staplade koniska stapeldiagram|
|Konisk kolumn3D|Representerar 3D koniskt kolumndiagram|
|Pyramid|Representerar pyramiddiagram|
|PyramidStackad|Representerar staplade pyramiddiagram|
|Pyramid100ProcentStacked|Representerar 100 % staplade pyramiddiagram|
|PyramidBar|Representerar pyramidstapeldiagrammet|
|PyramidBarStacked|Representerar staplad pyramidstapeldiagram|
|PyramidBar100PercentStacked|Representerar 100 % staplad pyramidstapeldiagram|
|PyramidColumn3D|Representerar 3D Pyramid Column Chart|
Så här skapar du ett diagram med Aspose.Cells:

1.  Lägg till några data till kalkylbladsceller med[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) föremål[**satt värde**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)metod.
 Detta kommer att användas som datakälla för diagrammet.
1.  Lägg till ett diagram i kalkylbladet genom att anropa[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) samlingens[*Lägg till*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ) metod, inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)objekt.
1.  Ange typen av diagram med[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)uppräkning.
 Till exempel använder exemplet[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)värde som diagramtyp.
1.  Få tillgång till det nya[**Diagram**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objekt från[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)samling genom att passera dess index.
1.  Använd något av kartobjekten som är inkapslade i[**Diagram**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)objekt för att hantera diagrammet.
 I exemplet nedan används[**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)diagramobjekt för att ange diagrammets datakälla.

När du lägger till källdata till diagrammet kan datakällan vara ett cellintervall (som "A1:C3") eller en sekvens av icke-sammanhängande celler (som "A1, A3, A5"), eller en sekvens av värden (som "1,2,3").

{{% alert color="primary" %}}

När du tilldelar ett cellintervall som en datakälla kan du bara ställa in intervallet från övre vänster till nedre höger. Till exempel är "A1:C3" giltigt medan "C3:A1" är ogiltigt.

{{% /alert %}}

Dessa allmänna steg låter dig skapa vilken typ av diagram som helst. Använd olika diagramobjekt för att skapa olika diagram.

När exempelkoden exekveras läggs ett pyramiddiagram till i kalkylbladet som visas nedan.

**Pyramiddiagram med dess datakälla**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 För att skapa ett bubbeldiagram,[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)måste ställas in på[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)och några extra egenskaper som BubbleSizes, Values & XValues måste ställas in därefter. När följande kod körs läggs ett bubbeldiagram till i kalkylbladet som visas nedan.

**Bubbeldiagram med dess datakälla**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Linje med datamarkördiagram**

För att skapa en linje med ett datamarkeringsdiagram,[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)måste ställas in på[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) och några extra egenskaper som bakgrundsområde, seriemarkörer , värden & XValues måste ställas in i enlighet därmed. När följande kod körs läggs en rad med ett datamarkeringsdiagram till i kalkylbladet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Skapa anpassade diagram**

Hittills, när vi har diskuterat diagram, har vi tittat på standarddiagram som har sina standardformateringsinställningar. Vi definierar bara datakällan, ställer in några få egenskaper och diagrammet skapas med dess standardformatinställningar. Men Aspose.Cells stöder också att skapa anpassade diagram som gör det möjligt för utvecklare att skapa diagram med sina egna formatinställningar.

### **Skapa anpassade diagram**

Utvecklare kan skapa anpassade diagram vid körning med Aspose.Cells enkel API.

 Ett diagram är sammansatt av en dataserie. Varje dataserie i Aspose.Cells representeras av en[**Serier**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objekt medan[**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) objekt fungerar som en samling av[**Serier**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)föremål. När du skapar ett anpassat diagram har utvecklare friheten att använda olika typer av diagram för olika dataserier (samlade i en[**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)objekt).

{{% alert color="primary" %}}

 För närvarande stöder Aspose.Cells endast anpassade diagram som kombinerar cirkel-, linje-, kolumn- och kolumndiagram men fler diagram kommer att stödjas i framtida utgåvor. För en fullständig lista över standarddiagram som Aspose.Cells stöder, läs[Diagramtyper](/cells/sv/java/chart-types/) artikel.

{{% /alert %}}

Exempelkoden nedan visar hur man skapar anpassade diagram. I det här exemplet kommer vi att använda ett kolumndiagram för den första dataserien och ett linjediagram för den andra serien. Resultatet är att vi lägger till ett kolumndiagram, kombinerat med ett linjediagram, till kalkylbladet.

**Anpassat diagram som kombinerar kolumn- och linjediagram**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Programmeringsexempel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

För att se en lista över diagramtyper som stöds, läs[Diagramtyper](/cells/sv/java/chart-types/) artikel.

{{% /alert %}}

