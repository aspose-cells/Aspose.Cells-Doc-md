---
title: Vom Diagramm zum Bild
linktitle: Vom Diagramm zum Bild
type: docs
weight: 46
url: /de/net/chart-to-image/
---
##  **Rendering-Diagramme**

 Aspose.Cells APIs unterstützen die Konvertierung von Excel-Diagrammen in Bildformate, ohne dass zusätzliche Tools oder Anwendungen erforderlich sind. Um Rendering-Unterstützung bereitzustellen, muss die[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) Klasse hat ausgesetzt[**Vorstellen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) Methoden mit einer Vielzahl von Überladungen, um den Anwendungsanforderungen am besten gerecht zu werden.

###  **Rendern von Diagrammen in Bilder**

 Der[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) Die Methode verfügt über eine Vielzahl von Überladungen, um sowohl einfaches als auch erweitertes Rendering zu unterstützen. Wenn die Anwendungsanforderung darin besteht, das Diagramm in seinen Standardabmessungen darzustellen, empfehlen wir die Verwendung von[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)Methode wie folgt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Es ist auch möglich, die Diagramme mit erweiterten Einstellungen in Bilder zu rendern. Aspose.Cells APIs haben eine Überlastungsversion von aufgedeckt[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) Methode, die eine Instanz von akzeptieren könnte[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), wobei Parameter wie Auflösung, Glättungsmodus, Bildformat usw. angegeben werden können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **Unterstützte Diagrammtypen für das Rendering**

 Es gibt einige Diagrammtypen, deren Darstellung derzeit nicht unterstützt wird. Solche Diagrammtypen enthalten**N** in der Kategorie **Unterstützt** Spalte der folgenden Tabelle.

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
|**Aktie**|StockHighLowClose|*J**|
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

##  **Vorabthemen**
- [Konvertieren Sie das Diagramm in PDF](/cells/de/net/chart-to-pdf/)
