---
title: Diagrammdarstellung
type: docs
weight: 30
url: /de/cpp/chart-rendering/
---
## **Erstellen von Diagrammen**

Aspose.Cells API-Unterstützung zum Erstellen einer Vielzahl von Excel-Diagrammen, wie unter dem Thema beschrieben[Erstellen und Anpassen von Excel-Diagrammen](/cells/de/cpp/creating-and-customizing-charts/). Um die Verwendung von Aspose.Cells-APIs zum Rendern der Diagramme im Bild- und PDF-Format zu demonstrieren, erstellen wir ein Diagramm vom Typ Column gemäß dem folgenden Snippet.

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

## **Diagramme rendern**

Aspose.Cells APIs unterstützen die Konvertierung der Excel-Diagramme in Bilder und PDF-Formate, ohne dass zusätzliche Tools oder Anwendungen erforderlich sind. Um die Renderingunterstützung bereitzustellen, hat die Chart-Klasse ToImage- und ToPdf-Methoden mit einer Vielzahl von Überladungen verfügbar gemacht, um den Anwendungsanforderungen am besten zu entsprechen.

### **Rendern von Diagrammen in Bilder**

Die Chart.toImage-Methode verfügt über eine Reihe von Überladungen, um sowohl einfaches als auch erweitertes Rendern zu unterstützen. Wenn die Anforderung der Anwendung darin besteht, das Diagramm in seinen Standardabmessungen zu rendern, empfehlen wir Ihnen, die Chart.toImage-Methode wie folgt zu verwenden.

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **Diagramm in PDF rendern**

Um das Diagramm in das PDF-Format zu rendern, haben die Aspose.Cells-APIs die Chart.ToPdf-Methode mit der Fähigkeit verfügbar gemacht, das resultierende PDF im Disc-Pfad oder Stream zu speichern.

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **Unterstützte Diagrammtypen für das Rendern**

Es gibt einige Diagrammtypen, die derzeit nicht für das Rendern unterstützt werden. Solche Diagrammtypen enthalten**N** im**Unterstützte ** Spalte der folgenden Tabelle.

|**Diagramm Typ**|**Diagrammuntertyp**|**Unterstützt**|
|:- |:- |:- |
|**Spalte**|Spalte|**Y**|
||Spalte gestapelt|**Y**|
||Spalte 100 Prozent gestapelt|**Y**|
||Column3DClustered|**Y**|
||Column3DStacked|**Y**|
||Column3D100PercentStacked|**Y**|
||Spalte3D|**Y**|
|**Bar**|Bar|**Y**|
||BarStacked|**Y**|
||Balken 100 Prozent gestapelt|**Y**|
||Bar3DClustered|**Y**|
||Bar3DStacked|**Y**|
||Bar3D100PercentStacked|**Y**|
|**Linie**|Linie|**Y**|
||LineStacked|**Y**|
||Zeile 100 Prozent gestapelt|**Y**|
||LineWithDataMarkers|**Y**|
||LineStackedWithDataMarkers|**Y**|
||Line100PercentStackedWithDataMarkers|**Y**|
||Line3D|**Y**|
|**Kuchen**|Kuchen|**Y**|
||Pie3D|**Y**|
||PiePie|**Y**|
||Kuchenexplodiert|**Y**|
||Pie3D Explodiert|**Y**|
||PieBar|**Y**|
|**Streuen**|Streuen|**Y**|
||ScatterConnectedByCurvesWithDataMarker|**Y**|
||ScatterConnectedByCurvesWithoutDataMarker|**Y**|
||ScatterConnectedByLinesWithDataMarker|**Y**|
||ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Bereich**|Bereich|**Y**|
||BereichStacked|**Y**|
||Area100ProcentStacked|**Y**|
||Bereich3D|**Y**|
||Area3DStacked|**Y**|
||Area3D100ProzentStacked|**Y**|
|**Krapfen**|Krapfen|**Y**|
||Donut Explodiert|**Y**|
|**Radar**|Radar|**Y**|
||RadarWithDataMarkers|**Y**|
||Radargefüllt|**Y**|
|**Auftauchen**|Surface3D|N|
||SurfaceWireframe3D|N|
||Oberflächenkontur|N|
||SurfaceContourWireframe|N|
|**Blase**|Blase|**Y**|
||Bubble3D|N|
|Aktie|StockHighLowClose|**Y**|
||StockOpenHighLowClose|**Y**|
||StockVolumeHighLowClose|**Y**|
||StockVolumeOpenHighLowClose|**Y**|
|**Zylinder**|Zylinder|**Y**|
||Zylinder gestapelt|**Y**|
||Zylinder 100 Prozent gestapelt|**Y**|
||Zylindrischer Stab|**Y**|
||ZylindrischBarStacked|**Y**|
||ZylindrischBar100ProzentGestapelt|**Y**|
||ZylindrischeSäule3D|**Y**|
|**Kegel**|Kegel|**Y**|
||Kegelgestapelt|**Y**|
||Kegel 100 Prozent gestapelt|**Y**|
||Konische Stange|**Y**|
||ConicalBarStacked|**Y**|
||ConicalBar100ProcentStacked|**Y**|
||KonischeSäule3D|**Y**|
|**Pyramide**|Pyramide|**Y**|
||PyramidStacked|**Y**|
||Pyramid100Prozent gestapelt|**Y**|
||PyramidBar|**Y**|
||PyramidBarStacked|**Y**|
||PyramidBar100PercentStacked|**Y**|
||PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Trichter**|Trichter|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sonnendurchbruch**|Sonnendurchbruch|**Y**|
|**Baumkarte**|Baumkarte|**Y**|
|**Wasserfall**|Wasserfall|**Y**|
|**Histogramm**|Histogramm|Y|
|**Karte**|Karte|**N**|

{{% alert color="primary" %}}

Falls Sie versuchen, die nicht unterstützten Diagrammtypen als Bild oder PDF zu rendern, erhalten Sie möglicherweise Bilder der Größe 0 oder leere PDFs.

{{% /alert %}}
