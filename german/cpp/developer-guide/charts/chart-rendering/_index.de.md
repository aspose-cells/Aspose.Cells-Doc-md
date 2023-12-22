---
title: Diagrammdarstellung
type: docs
weight: 30
url: /de/cpp/chart-rendering/
---
##  **Diagramme erstellen**

Aspose.Cells APIs unterstützen die Erstellung einer Vielzahl von Excel-Diagrammen, wie im Thema beschrieben[Erstellen und Anpassen von Excel-Diagrammen](/cells/de/cpp/creating-and-customizing-charts/). Um die Verwendung von Aspose.Cells-APIs zum Rendern der Diagramme im Bild- und PDF-Format zu demonstrieren, erstellen wir ein Diagramm vom Typ „Säule“ gemäß dem folgenden Snippet.

{{< highlight "cpp" >}}

Aspose::Cells::Startup();

// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");

// Create a new workbook
Workbook workbook;

// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);

// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

Aspose::Cells::Cleanup();

{{< /highlight >}}

##  **Rendering-Diagramme**

Aspose.Cells APIs unterstützen die Konvertierung von Excel-Diagrammen in Bilder und PDF Formate, ohne dass zusätzliche Tools oder Anwendungen erforderlich sind. Um die Rendering-Unterstützung bereitzustellen, hat die Chart-Klasse ToImage- und ToPdf-Methoden mit einer Vielzahl von Überladungen bereitgestellt, um den Anwendungsanforderungen optimal gerecht zu werden.

###  **Rendern von Diagrammen in Bilder**

Die Chart.toImage-Methode verfügt über eine Vielzahl von Überladungen, um sowohl einfaches als auch erweitertes Rendering zu unterstützen. Wenn die Anwendungsanforderung darin besteht, das Diagramm in seinen Standardabmessungen darzustellen, empfehlen wir Ihnen, die Chart.toImage-Methode wie folgt zu verwenden.

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **Rendering-Diagramm bis PDF**

Um das Diagramm im PDF-Format zu rendern, haben die Aspose.Cells-APIs die Chart.ToPdf-Methode mit der Möglichkeit bereitgestellt, das resultierende PDF im Datenträgerpfad oder Stream zu speichern.

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **Unterstützte Diagrammtypen für das Rendering**

Es gibt einige Diagrammtypen, deren Darstellung derzeit nicht unterstützt wird. Solche Diagrammtypen enthalten**N** in der Kategorie **Unterstützt**Spalte der folgenden Tabelle.

|**Diagramm Typ**|**Untertyp des Diagramms**|**Unterstützt**|
| :- | :- | :- |
|**Spalte**|Spalte|*J**|
| |ColumnStacked|*J**|
| |Column100PercentStacked|*J**|
| |Column3DClustered|*J**|
| |Column3DStacked|*J**|
| |Column3D100PercentStacked|*J**|
| |Column3D|*J**|
|**Bar**|Bar|*J**|
| |BarStacked|*J**|
| |Bar100PercentStacked|*J**|
| |Bar3DClustered|*J**|
| |Bar3DStacked|*J**|
| |Bar3D100PercentStacked|*J**|
|**Linie**|Linie|*J**|
| |LineStacked|*J**|
| |Line100PercentStacked|*J**|
| |LineWithDataMarkers|*J**|
| |LineStackedWithDataMarkers|*J**|
| |Line100PercentStackedWithDataMarkers|*J**|
| |Line3D|*J**|
|**Kuchen**|Kuchen|*J**|
| |Pie3D|*J**|
| |PiePie|*J**|
| |PieExploded|*J**|
| |Pie3DEExploded|*J**|
| |PieBar|*J**|
|**Streuen**|Streuen|*J**|
| |ScatterConnectedByCurvesWithDataMarker|*J**|
| |ScatterConnectedByCurvesWithoutDataMarker|*J**|
| |ScatterConnectedByLinesWithDataMarker|*J**|
| |ScatterConnectedByLinesWithoutDataMarker|*J**|
|**Bereich**|Bereich|*J**|
| |BereichGestapelt|*J**|
| |Fläche100PercentStacked|*J**|
| |Area3D|*J**|
| |Area3DStacked|*J**|
| |Area3D100PercentStacked|*J**|
|**Krapfen**|Krapfen|*J**|
| |DonutExplodiert|*J**|
|**Radar**|Radar|*J**|
| |RadarWithDataMarkers|*J**|
| |Radargefüllt|*J**|
|**Oberfläche**|Surface3D|N|
| |OberflächeWireframe3D|N|
| |Oberflächenkontur|N|
| |SurfaceContourWireframe|N|
|**Blase**|Blase|*J**|
| |Bubble3D|N|
|Aktie|StockHighLowClose|*J**|
| |StockOpenHighLowClose|*J**|
| |StockVolumeHighLowClose|*J**|
| |StockVolumeOpenHighLowClose|*J**|
|**Zylinder**|Zylinder|*J**|
| |Zylindergestapelt|*J**|
| |Zylinder100PercentStacked|*J**|
| |Zylindrischer Balken|*J**|
| |CylindricalBarStacked|*J**|
| |CylindricalBar100PercentStacked|*J**|
| |Zylindrische Spalte3D|*J**|
|**Kegel**|Kegel|*J**|
| |Kegelgestapelt|*J**|
| |Cone100PercentStacked|*J**|
| |ConicalBar|*J**|
| |ConicalBarStacked|*J**|
| |ConicalBar100PercentStacked|*J**|
| |ConicalColumn3D|*J**|
|**Pyramide**|Pyramide|*J**|
| |PyramidStacked|*J**|
| |Pyramid100PercentStacked|*J**|
| |PyramidBar|*J**|
| |PyramidBarStacked|*J**|
| |PyramidBar100PercentStacked|*J**|
| |PyramidColumn3D|*J**|
|**BoxWhisker**|BoxWhisker|Y|
|**Trichter**|Trichter|*J**|
|**ParetoLinie**|ParetoLinie|*J**|
|**Sonnendurchbruch**|Sonnendurchbruch|*J**|
|**Baumkarte**|Baumkarte|*J**|
|**Wasserfall**|Wasserfall|*J**|
|**Histogramm**|Histogramm|Y|
|**Karte**|Karte|*N**|

{{% alert color="primary" %}}

Wenn Sie versuchen, die nicht unterstützten Diagrammtypen als Bild oder PDF zu rendern, erhalten Sie möglicherweise Bilder der Größe 0 oder leere PDF.

{{% /alert %}}
