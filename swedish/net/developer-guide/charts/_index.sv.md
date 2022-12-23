---
title: Skapa och hantera diagram
linktitle: Diagram
type: docs
weight: 130
url: /sv/net/creating-charts/
description: Skapa ett diagram i CSharp för Excel och ODS-filer.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Det är möjligt att lägga till en mängd olika diagram till kalkylblad med Aspose.Cells. Aspose.Cells tillhandahåller många flexibla diagramobjekt. Det här ämnet diskuterar Aspose.Cells' diagramobjekt.

{{% /alert %}}

## **Skapa diagram**

### **Skapa helt enkelt ett diagram**
Det är enkelt att skapa ett diagram med Aspose.Cells med följande exempelkoder:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Saker att veta för att skapa ett diagram**

Innan du skapar diagram är det viktigt att förstå några grundläggande begrepp som är användbara när du skapar diagram med Aspose.Cells.

#### **Kartlägga objekt**

Aspose.Cells tillhandahåller en speciell uppsättning klasser i[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) namnutrymme som används för att skapa diagram som stöds av Aspose.Cells. Dessa klasser används för att skapa**kartlägga objekt**, som fungerar som diagrammets byggstenar. Kartobjekten listas nedan:

- Serier, en enda dataserie i ett diagram.
- Axis, ett diagrams axel.
- Diagram, ett enda Excel-diagram.
- ChartArea, diagramområdet i kalkylbladet.
- ChartDataTable, en diagramdatatabell.
- ChartFrame, ramobjektet i ett diagram.
- ChartPoint, en enda punkt i en serie i ett diagram.
- ChartPointCollection, en samling som innehåller alla poäng i en serie.
- Diagram, en samling diagramobjekt.
- DataLabels, en samling av alla DataLabel-objekt för den angivna serien.
- FillFormat, fyllningsformat för en form.
- Golv, golvet i ett 3D-diagram.
- Legend, sjökortslegenden.
- Linje, diagramlinjen.
- SeriesCollection, en samling av serieobjekt.
- TickLabels, bockmarkeringsetiketterna som är associerade med bockmärken på en diagramaxel.
- Titel, titeln på ett diagram eller en axel.
- Trendlinje, en trendlinje i ett diagram.
- TrendlineCollection, en samling av alla Trendline-objekt för den angivna dataserien.
- Väggar, väggarna i ett 3D-diagram.

#### **Använda diagramobjekt**

Som nämnts ovan är alla diagramobjekt instanser av sina respektive klasser och tillhandahåller specifika egenskaper och metoder för att utföra specifika uppgifter. Använd diagramobjekt för att skapa diagram.

Lägg till vilken typ av diagram som helst i ett kalkylblad med hjälp av[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) samling. Varje objekt i[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) samlingen representerar en[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objekt. A[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)objekt kapslar in alla andra diagramobjekt som krävs för att anpassa diagrammets utseende. Nästa avsnitt visar hur du använder några grundläggande diagramobjekt för att skapa ett enkelt diagram.

### **Skapa diagram med Aspose.Cells**

**Steg:**

1.  Lägg till några data till kalkylbladsceller med[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) föremål[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)metod.
 Detta kommer att användas som datakälla för diagrammet.
1.  Lägg till ett diagram i kalkylbladet genom att anropa[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) samlingens[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) metod, inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objekt.
1.  Ange typen av diagram med[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)uppräkning.
 Till exempel använder exemplet nedan[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)värde som diagramtyp.
1.  Få tillgång till det nya[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objekt från[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)samling genom att passera dess index.
1.  Använd något av kartobjekten som är inkapslade i[**Diagram**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)objekt för att hantera diagrammet.
 I exemplet nedan används[**Seriekollektion**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)diagramobjekt för att ange diagrammets datakälla.

När du lägger till källdata till diagrammet kan datakällan vara ett cellintervall (som "A1:C3") eller en sekvens av icke-sammanhängande celler (som "A1, A3, A5"), eller en sekvens av värden (som "1,2,3").

Dessa allmänna steg låter dig skapa vilken typ av diagram som helst. Använd olika diagramobjekt för att skapa olika diagram.

 Det är möjligt att skapa många olika typer av sjökort med Aspose.Cells. Alla standarddiagram som stöds av Aspose.Cells är fördefinierade i en uppräkning med namnet[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

De fördefinierade diagramtyperna är:

|**Diagramtyper**|**Beskrivning**|
|:- |:- |
|Kolumn|Representerar klustrade kolumndiagram|
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
|Sprida ut|Representerar spridningsdiagram|
|ScatterConnectedByCurvesWithDataMarker|Representerar spridningsdiagram kopplade av kurvor, med datamarkörer|
|ScatterConnectedByCurvesWithoutDataMarker|Representerar spridningsdiagram kopplade av kurvor, utan datamarkörer|
|ScatterConnectedByLinesWithDataMarker|Representerar spridningsdiagram anslutna med linjer, med datamarkörer|
|ScatterConnectedByLinesWithoutDataMarker|Representerar spridningsdiagram anslutna med linjer, utan datamarkörer|
|Område|Representerar områdesdiagram|
|AreaStacked|Representerar staplade ytdiagram|
|Area100PercentStacked|Representerar 100 % staplade ytdiagram|
|Area3D|Representerar 3D-områdesdiagram|
|Area3DStacked|Representerar 3D Stacked Area Chart|
|Area3D100PercentStacked|Representerar 3D 100 % staplade ytdiagram|
|Munk|Representerar munkdiagram|
|Doughnut Exploderade|Representerar Exploded Donut Chart|
|Radar|Representerar radardiagram|
|RadarWithDataMarkers|Representerar radardiagram med datamarkörer|
|Radarfylld|Representerar fyllt radardiagram|
|Surface3D|Representerar 3D-ytdiagram|
|SurfaceWireframe3D|Representerar Wireframe 3D Ytdiagram|
|Ytkontur|Representerar konturdiagram|
|SurfaceContourWireframe|Representerar Wireframe Contour Chart|
|Bubbla|Representerar bubbeldiagram|
|Bubble3D|Representerar 3D Bubble Chart|
|Cylinder|Representerar cylinderdiagram|
|CylinderStacked|Representerar diagram över staplade cylindrar|
|Cylinder100PercentStacked|Representerar 100 % staplade cylinderdiagram|
|Cylinderical Bar|Representerar cylindriskt stapeldiagram.|
|CylindericalBarStacked|Representerar staplade cylindriska stapeldiagram|
|CylindericalBar100PercentStacked|Representerar 100 % staplade cylindriska stapeldiagram|
|CylindericalColumn3D|Representerar 3D Cylindrical Column Chart|
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
|PyramidBar|Representerar pyramidstapeldiagram|
|PyramidBarStacked|Representerar staplad pyramidstapeldiagram|
|PyramidBar100PercentStacked|Representerar 100 % staplad pyramidstapeldiagram|
|PyramidColumn3D|Representerar 3D Pyramid Column Chart|
{{% alert color="primary" %}}

När du tilldelar ett cellintervall som datakälla kan du bara ställa in intervallet från övre vänster till nedre höger. Till exempel är "A1:C3" giltigt medan "C3:A1" är ogiltigt.

{{% /alert %}}

#### **Pyramiddiagram**

När exempelkoden exekveras läggs ett pyramiddiagram till i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Linjediagram**

 I exemplet ovan ändrar du helt enkelt[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) till*Linje*skapar ett linjediagram. Den fullständiga källan finns nedan. när koden exekveras läggs ett linjediagram till i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Bubbeldiagram**

 För att skapa ett bubbeldiagram,[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) måste ställas in på[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)och några extra egenskaper som BubbleSizes, Values & XValues måste ställas in därefter. När följande kod körs läggs ett bubbeldiagram till i kalkylbladet.

#### **Linje med datamarkördiagram**

 För att skapa en linje med datamarkeringsdiagrammet,[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)måste ställas in på*ChartType.LineWithDataMarkers*och några extra egenskaper som bakgrundsområde, seriemarkörer, värden och XValues måste ställas in därefter. När följande kod körs läggs en rad med datamarkörsdiagrammet till i kalkylbladet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Förhandsämnen**
- [Läs och manipulera Excel 2016-diagram](/cells/sv/net/read-and-manipulate-excel-2016-charts/)
- [Hantera axlar i Excel-diagram](/cells/sv/net/chart-axes/)
- [Ställa in diagrammets utseende](/cells/sv/net/setting-chart-appearance/)
- [Diagramtyper](/cells/sv/net/chart-types/)
- [Anpassa diagram](/cells/sv/net/customizing-charts/)
- [Ställ in datakälla för diagrammet](/cells/sv/net/data-formatting-in-charts/)
- [Hantera dataetiketter för Excel-diagram](/cells/sv/net/insert-datalabels-to-chart/)
- [Generera diagram genom att bearbeta smarta markörer](/cells/sv/net/generate-chart-by-processing-smart-markers/)
- [Skaffa arbetsblad av diagrammet](/cells/sv/net/get-worksheet-of-the-chart/)
- [Hantera Legend of Excel-diagram](/cells/sv/net/chart-legend/)
- [Manipulera positionsstorlek och designerdiagram](/cells/sv/net/manipulate-position-size-and-designer-chart/)
- [Skapa cirkeldiagram med ledarlinjer](/cells/sv/net/creating-pie-chart-with-leader-lines/)
- [Former i diagram](/cells/sv/net/controls-in-charts/)
- [Hantera titlar på Excel-diagram](/cells/sv/net/chart-and-axis-titles/)
- [Diagramrendering](/cells/sv/net/chart-rendering/)
- [Få ekvationstext för diagramtrendlinje](/cells/sv/net/get-equation-text-of-chart-trendline/)
