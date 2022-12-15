---
title: Diagramrendering
type: docs
weight: 30
url: /sv/cpp/chart-rendering/
---
## **Skapa diagram**

Aspose.Cells API:er stöder för att skapa en mängd Excel-diagram som beskrivs under ämnet[Skapa och anpassa Excel-diagram](/cells/sv/cpp/creating-and-customizing-charts/). För att demonstrera användningen av Aspose.Cells API:er för att rendera diagrammen i bild- och PDF-format, kommer vi att skapa ett diagram av typen Kolumn enligt följande utdrag.

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **Återgivning av diagram**

Aspose.Cells API:er stöder för att konvertera Excel-diagram till bilder och PDF-format utan att behöva några ytterligare verktyg eller applikationer. För att ge stöd för renderingen har klassen Chart exponerat ToImage & ToPdf-metoder med en mängd överbelastningar för att bäst passa applikationskraven.

### **Återge diagram till bilder**

Chart.toImage-metoden har en viss överbelastning för att stödja enkel såväl som avancerad rendering. Om applikationskravet är att återge diagrammet i dess standarddimensioner, föreslår vi att du använder Chart.toImage-metoden enligt följande.

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **Återge diagram till PDF**

För att rendera diagrammet till PDF-format har API:erna Aspose.Cells exponerat Chart.ToPdf-metoden med möjlighet att lagra den resulterande PDF-filen på skivväg eller Stream.

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **Sjökortstyper som stöds för rendering**

Det finns några diagramtyper som för närvarande inte stöds för rendering. Sådana diagramtyper innehåller**N** i**Stöds** kolumn i tabellen nedan.

|**Diagramtyp**|**Diagram undertyp**|**Stöds**|
|:- |:- |:- |
|**Kolumn**|Kolumn|**Y**|
||KolumnStackad|**Y**|
||Kolumn100ProcentStackad|**Y**|
||Kolumn3DClustrerad|**Y**|
||Kolumn3DStackad|**Y**|
||Kolumn3D100PercentStacked|**Y**|
||Kolumn 3D|**Y**|
|**Bar**|Bar|**Y**|
||BarStacked|**Y**|
||Bar100PercentStacked|**Y**|
||Bar3DClustered|**Y**|
||Bar3DStacked|**Y**|
||Bar3D100PercentStacked|**Y**|
|**Linje**|Linje|**Y**|
||LineStacked|**Y**|
||Line100PercentStacked|**Y**|
||LineWithDataMarkers|**Y**|
||LineStackedWithDataMarkers|**Y**|
||Line100PercentStackedWithDataMarkers|**Y**|
||Line3D|**Y**|
|**Paj**|Paj|**Y**|
||Pie3D|**Y**|
||PiePie|**Y**|
||PieExploderade|**Y**|
||Pie3DE exploderade|**Y**|
||PieBar|**Y**|
|**Sprida ut**|Sprida ut|**Y**|
||ScatterConnectedByCurvesWithDataMarker|**Y**|
||ScatterConnectedByCurvesWithoutDataMarker|**Y**|
||ScatterConnectedByLinesWithDataMarker|**Y**|
||ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Område**|Område|**Y**|
||AreaStacked|**Y**|
||Area100PercentStacked|**Y**|
||Area3D|**Y**|
||Area3DStacked|**Y**|
||Area3D100PercentStacked|**Y**|
|**Munk**|Munk|**Y**|
||Doughnut Exploderade|**Y**|
|**Radar**|Radar|**Y**|
||RadarWithDataMarkers|**Y**|
||Radarfylld|**Y**|
|**Yta**|Surface3D|N|
||SurfaceWireframe3D|N|
||Ytkontur|N|
||SurfaceContourWireframe|N|
|**Bubbla**|Bubbla|**Y**|
||Bubble3D|N|
|Stock|StockHighLowClose|**Y**|
||LagerÖppnaHögLågStäng|**Y**|
||LagervolymHögLågStäng|**Y**|
||Lagervolym ÖppenHögLågStäng|**Y**|
|**Cylinder**|Cylinder|**Y**|
||CylinderStacked|**Y**|
||Cylinder100PercentStacked|**Y**|
||Cylindrical Bar|**Y**|
||CylindricalBarStacked|**Y**|
||CylindricalBar100PercentStacked|**Y**|
||CylindricalColumn3D|**Y**|
|**Kon**|Kon|**Y**|
||ConeStacked|**Y**|
||Cone100PercentStacked|**Y**|
||ConicalBar|**Y**|
||ConicalBarStacked|**Y**|
||ConicalBar100PercentStacked|**Y**|
||Konisk kolumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
||PyramidStackad|**Y**|
||Pyramid100ProcentStacked|**Y**|
||PyramidBar|**Y**|
||PyramidBarStacked|**Y**|
||PyramidBar100PercentStacked|**Y**|
||PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Tratt**|Tratt|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Trädkarta**|Trädkarta|**Y**|
|**Vattenfall**|Vattenfall|**Y**|
|**Histogram**|Histogram|Y|
|**Karta**|Karta|**N**|

{{% alert color="primary" %}}

Om du försöker rendera diagramtyperna som inte stöds till bild eller PDF, kan du sluta med 0-stora bilder eller tom PDF.

{{% /alert %}}
