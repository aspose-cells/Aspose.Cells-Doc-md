---
title: Skapa och hantera diagram
description: Lär dig hur man använder Aspose.Cells for .NET för att skapa diagram i Microsoft Excel. Vår guide kommer att visa de olika typer av diagram som kan skapas, samt hur man anpassar deras utseende och formatering.
keywords: Aspose.Cells for .NET, Skapande av diagram, Microsoft Excel, Diagramtyper, Anpassning, Utseende, Formatering.
linktitle: Diagram
type: docs
weight: 130
url: /sv/net/creating-charts/
description: Skapa ett diagram i CSharp för Excel och ODS filer.
keywords: skapa ett diagram, göra en graf 
---

{{% alert color="primary" %}}

Det är möjligt att lägga till en mängd olika diagram i kalkylblad med Aspose.Cells. Aspose.Cells tillhandahåller många flexibla diagramobjekt. Det här ämnet diskuterar Aspose.Cells diagramobjekt.

{{% /alert %}}

## **Skapa diagram**

### **Enkelt skapa ett diagram**
Det är enkelt att skapa ett diagram med Aspose.Cells med följande exempelkod:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Saker att veta för att skapa ett diagram**

Innan du skapar diagram är det viktigt att förstå några grundläggande begrepp som är till hjälp när du skapar diagram med Aspose.Cells.

#### **Diagramobjekt**

Aspose.Cells tillhandahåller en särskild uppsättning klasser i [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)-rymden som används för att skapa de diagram som stöds av Aspose.Cells. Dessa klasser används för att skapa **diagramobjekt**, som fungerar som diagramets byggstenar. Diagramobjekten listas nedan:

- Serie, en enda dataserie i ett diagram.
- Axeln, ett diagramaxel.
- Diagram, ett enskilt Excel-diagram.
- Diagramområde, diagramområdet i arbetsbladet.
- ChartDataTable, en diagramdatatabell.
- ChartFrame, objektet ram i ett diagram.
- ChartPoint, enstaka punkt i en serie i ett diagram.
- ChartPointCollection, en samling som innehåller alla punkter i en serie.
- Charts, en samling av diagramobjekt.
- DataLabels, en samling av alla DataLabel-objekt för den angivna serien.
- FillFormat, fyllnadsformat för en form.
- Floor, golvet i ett 3D-diagram.
- Legend, diagrammets legend.
- Line, diagramlinjen.
- SeriesCollection, en samling av serieobjekt.
- TickLabels, de tickmarkeringsetiketter som är associerade med tickmarkeringar på en diagramaxel.
- Title, diagram- eller axeltiteln.
- Trendline, en trendlinje i ett diagram.
- TrendlineCollection, en samling av alla Trendline-objekt för den angivna dataserien.
- Walls, väggarna i ett 3D-diagram.

#### **Användning av diagramobjekt**

Som nämnts ovan är alla diagramobjekt instanser av sina respektive klasser och tillhandahåller specifika egenskaper och metoder för att utföra specifika uppgifter. Använd diagramobjekt för att skapa diagram.

Lägg till vilken typ av diagram som helst i ett kalkylblad genom att använda [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)-samlingen. Varje objekt i [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)-samlingen representerar ett [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)-objekt. Ett [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)-objekt inkluderar alla andra diagramobjekt som krävs för att anpassa diagrammets utseende. Nästa avsnitt visar hur du använder några grundläggande diagramobjekt för att skapa ett enkelt diagram.

### **Skapa diagram med Aspose.Cells**

**Steg:**

1. Lägg till lite data i kalkylbladsceller med [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objektets [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) metod.
   Detta kommer att användas som datakälla för diagrammet.
1. Lägg till ett diagram i kalkylbladet genom att anropa [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add)-metoden för [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)-samlingen, innesluten i [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-objektet.
1. Ange diagramtypen med [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) uppräkningen.
   Till exempel, exemplet nedan använder värdet [**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) som diagramtyp.
1. Få tillgång till det nya [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objektet från [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) samlingen genom att skicka dess index.
1. Använd något av de diagramobjekt som är kapslade i [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objekt för att hantera diagrammet.
   Exemplet nedan använder [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) diagramobjektet för att ange diagrammets datakälla.

När du lägger till källdata till diagrammet kan datakällan vara en rad celler (t.ex. "A1:C3"), eller en följd av icke-sammanhängande celler (t.ex. "A1, A3, A5"), eller en följd av värden (t.ex. "1,2,3").

Dessa allmänna steg gör det möjligt för dig att skapa vilken typ av diagram som helst. Använd olika diagramobjekt för att skapa olika diagram.

Det är möjligt att skapa många olika typer av diagram med Aspose.Cells. Alla standarddiagram som stöds av Aspose.Cells är fördefinierade i en uppräkning som heter [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Fördefinierade diagramtyper är:

|**Diagramtyper**|**Beskrivning**|
| :- | :- |
|Column|Representerar diagram över klustringsskikt|
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
|Scatter|Representerar spridningsdiagram|
|ScatterConnectedByCurvesWithDataMarker|Representerar spridningsdiagram anslutna med kurvor, med datamarkörer|
|ScatterConnectedByCurvesWithoutDataMarker|Representerar spridningsdiagram anslutna med kurvor, utan datamarkörer|
|ScatterConnectedByLinesWithDataMarker|Representerar spridningsdiagram anslutna med linjer, med datamarkörer|
|ScatterConnectedByLinesWithoutDataMarker|Representerar spridningsdiagram anslutna med linjer, utan datamarkörer|
|Area|Representerar områdesdiagrammet|
|AreaStacked|Representerar staplade områdesdiagrammet|
|Area100PercentStacked|Representerar 100% staplade områdesdiagrammet|
|Area3D|Representerar 3D områdesdiagrammet|
|Area3DStacked|Representerar 3D staplade områdesdiagrammet|
|Area3D100PercentStacked|Representerar 3D 100% staplade områdesdiagrammet|
|Doughnut|Representerar doughnut diagrammet|
|DoughnutExploded|Representerar Exploderat doughnut diagram|
|Radar|Representerar radardiagram|
|RadarWithDataMarkers|Representerar Radar-diagram med datamarkörer|
|RadarFilled|Representerar fyllt radardiagram|
|Surface3D|Representerar 3D ytdiagram|
|SurfaceWireframe3D|Representerar Wireframe 3D-yt-diagram|
|SurfaceContour|Representerar konturdiagram|
|SurfaceContourWireframe|Representerar wireframe konturdiagram|
|Bubble|Representerar boll diagrammet|
|Bubble3D|Representerar 3D boll diagrammet|
|Cylinder|Representerar cylinderdiagram|
|CylinderStacked|Representerar staplade cylinderdiagram|
|Cylinder100PercentStacked|Representerar 100% staplade cylinderdiagram|
|CylindericalBar|Representerar Cylindrisk stapeldiagram|
|CylindericalBarStacked|Representerar Stapeldiagram med cylindriska staplar|
|CylindericalBar100PercentStacked|Representerar 100% stapeldiagram med cylindriska staplar|
|CylindericalColumn3D|Representerar 3D cylindrisk stapeldiagram|
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
|PyramidBar|Representerar Pyramid stapeldiagram|
|PyramidBarStacked|Representerar Staplad Pyramid Stapeldiagram|
|PyramidBar100PercentStacked|Representerar 100% Staplad Pyramid Stapeldiagram|
|PyramidColumn3D|Representerar 3D Pyramid Kolumn Diagram|
{{% alert color="primary" %}}

När du tilldelar en cellintervall som datakälla kan du bara ställa in intervallet från övre vänstra till nedre högra. Till exempel är "A1:C3" giltigt medan "C3:A1" är ogiltigt.

{{% /alert %}}

#### **Pyramiddiagram**

När exempelkoden körs läggs ett pyramiddiagram till kalkylarket.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Linjediagram**

I det ovanstående exemplet skapar enkelt att ändra [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) till *Line* ett linjediagram. Hela källan är förutsatt nedan. när koden körs, läggs ett linjediagram till kalkylarket.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Bubbel-diagram**

För att skapa ett bubbeldiagram, måste [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) inställas på [**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) och några extra egenskaper såsom BubbleSizes, värden & X-värden bör ställas in. Genom att utföra följande kod läggs ett bubbel-diagram till kalkylarket.

#### **Linje med Datum Markör Diagram**

För att skapa ett linjediagram med datamarkör, [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) uppsättas till *ChartType.LineWithDataMarkers* och några extra egenskaper såsom bakgrundsområde, Seriemarkör, värden & X-värden bör ställas in. Genom att utföra följande kod läggs ett linjediagram med datamarkör till kalkylarket.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Fortsatta ämnen**
- [Läs och hantera Excel 2016-diagram](/cells/sv/net/read-and-manipulate-excel-2016-charts/)
- [Hantera axlarna för Excel-diagram](/cells/sv/net/chart-axes/)
- [Ställa in diagramens utseende](/cells/sv/net/setting-chart-appearance/)
- [Diagramtyper](/cells/sv/net/chart-types/)
- [Anpassa diagram](/cells/sv/net/customizing-charts/)
- [Ställ in datamängd för diagrammet](/cells/sv/net/data-formatting-in-charts/)
- [Hantera Dataetiketter för Excel-diagram](/cells/sv/net/insert-datalabels-to-chart/)
- [Generera diagram genom att bearbeta Smarta Markörer](/cells/sv/net/generate-chart-by-processing-smart-markers/)
- [Hämta kalkylarket för diagrammet](/cells/sv/net/get-worksheet-of-the-chart/)
- [Hantera legenden för Excel-diagram](/cells/sv/net/chart-legend/)
- [Manipulera Position Size och Designer-diagram](/cells/sv/net/manipulate-position-size-and-designer-chart/)
- [Skapa cirkeldiagram med ledarlinjer](/cells/sv/net/creating-pie-chart-with-leader-lines/)
- [Former i diagram](/cells/sv/net/controls-in-charts/)
- [Hantera titlar för Excel-diagram](/cells/sv/net/chart-and-axis-titles/)
- [Diagramrendering](/cells/sv/net/chart-rendering/)
- [Få ekvationstext av diagramtrendlinje](/cells/sv/net/get-equation-text-of-chart-trendline/)
