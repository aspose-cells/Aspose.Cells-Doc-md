---
title: Diagrammdarstellung
linktitle: Zum Bild oder PDF
type: docs
weight: 45
url: /de/net/chart-rendering/
---
## **Diagramme rendern**

 Aspose.Cells APIs unterstützen die Konvertierung der Excel-Diagramme in Bilder und PDF-Formate, ohne dass zusätzliche Tools oder Anwendungen erforderlich sind. Um Rendering-Unterstützung bereitzustellen, wird die[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) Klasse hat ausgesetzt[**Vorstellen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**ZuPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)Methoden mit einer Vielzahl von Überladungen, um den Anwendungsanforderungen am besten zu entsprechen.

### **Rendern von Diagrammen in Bilder**

 Das[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**ZuPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) -Methode verfügt über eine Vielzahl von Überladungen, um sowohl einfaches als auch erweitertes Rendern zu unterstützen. Wenn die Anforderung der Anwendung darin besteht, das Diagramm in seinen Standardabmessungen zu rendern, empfehlen wir Ihnen, die zu verwenden[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)Methode wie folgt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Es ist auch möglich, die Diagramme mit erweiterten Einstellungen in Bilder zu rendern. Aspose.Cells APIs haben eine überladene Version von verfügbar gemacht[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) Methode, die eine Instanz von akzeptieren könnte[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), während Parameter wie Auflösung, Glättungsmodus, Bildformat usw. festgelegt werden können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **Diagramm in PDF rendern**

 Um das Diagramm in das PDF-Format zu rendern, haben die Aspose.Cells-APIs die bereitgestellt[**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)-Methode mit der Möglichkeit, das resultierende PDF im Disc-Pfad oder Stream zu speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Unterstützte Diagrammtypen für das Rendern**

 Es gibt einige Diagrammtypen, die derzeit nicht für das Rendern unterstützt werden. Solche Diagrammtypen enthalten** N** im**Spalte „Unterstützt**“ der folgenden Tabelle.

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
|**Aktie**|StockHighLowClose|**Y**|
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

## **Themen vorantreiben**
- [Diagramm in PDF mit gewünschter Seitengröße konvertieren](/cells/de/net/chart-to-pdf/)
