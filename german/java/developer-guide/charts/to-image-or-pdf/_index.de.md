---
title: Diagrammdarstellung
linktitle: Zum Bild oder PDF
type: docs
weight: 40
url: /de/java/chart-rendering/
---
## **Erstellen von Diagrammen**

 Aspose.Cells API-Unterstützung zum Erstellen einer Vielzahl von Excel-Diagrammen, wie unter dem Thema beschrieben[Erstellen und Anpassen von Excel-Diagrammen](/cells/de/java/creating-and-customizing-charts/). Um die Verwendung von Aspose.Cells-APIs zum Rendern der Diagramme im Bild- und PDF-Format zu demonstrieren, erstellen wir ein Diagramm vom Typ Column gemäß dem folgenden Snippet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Diagramme rendern**

 Aspose.Cells-APIs unterstützen die Konvertierung der Excel-Diagramme in Bilder und PDF-Formate, ohne dass zusätzliche Tools oder Anwendungen erforderlich sind. Um Rendering-Unterstützung bereitzustellen, wird die[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)Klasse hat ausgesetzt[**vorstellen**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**zuPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) Methoden mit einer Vielzahl von Überladungen, um den Anwendungsanforderungen am besten zu entsprechen.

### **Rendern von Diagrammen in Bilder**

 Das[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))-Methode verfügt über eine Vielzahl von Überladungen, um sowohl einfaches als auch erweitertes Rendern zu unterstützen. Wenn die Anforderung der Anwendung darin besteht, das Diagramm in seinen Standardabmessungen zu rendern, empfehlen wir Ihnen, die zu verwenden[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) Methode wie folgt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Es ist auch möglich, die Diagramme mit erweiterten Einstellungen in Bilder zu rendern. Aspose.Cells APIs haben eine überladene Version von verfügbar gemacht[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) )-Methode, die eine Instanz von akzeptieren könnte[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)während es erlaubt, Parameter wie Auflösung, Rendering-Hinweise, Bildformat und so weiter anzugeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Rendering-Diagramm bis PDF**

 Um das Diagramm in das PDF-Format zu rendern, haben die Aspose.Cells-APIs die[**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream))-Methode mit der Möglichkeit, das Ergebnis PDF auf dem Datenträgerpfad oder einer Instanz von OutputStream zu speichern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Unterstützte Diagrammtypen für das Rendern**

 Es gibt einige Diagrammtypen, die derzeit nicht für das Rendern unterstützt werden. Solche Diagrammtypen enthalten** N** im**Unterstützte ** Spalte der folgenden Tabelle.

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
|**Oberfläche**|Surface3D|N|
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

Falls Sie versuchen, die nicht unterstützten Diagrammtypen als Bild oder PDF zu rendern, erhalten Sie möglicherweise Bilder der Größe 0 oder leere PDF.

{{% /alert %}}


## **Themen vorantreiben**
- [Konvertieren des Diagramms in ein Bild im Format SVG](/cells/de/java/converting-chart-to-image-in-svg-format/)
- [Diagramm PDF mit gewünschter Seitengröße erstellen](/cells/de/java/create-chart-pdf-with-desired-page-size/)
- [Diagramm nach SVG mit viewBox-Attribut exportieren](/cells/de/java/export-chart-to-svg-with-viewbox-attribute/)
